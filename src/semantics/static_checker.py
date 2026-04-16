"""
Static Semantic Checker for TyC Programming Language

This module implements a comprehensive static semantic checker using visitor pattern
for the TyC procedural programming language. It performs type checking,
scope management, type inference, and detects all semantic errors as
specified in the TyC language specification.
"""

from functools import reduce
from typing import (
    Dict,
    List,
    Set,
    Optional,
    Any,
    Tuple,
    NamedTuple,
    Union,
    TYPE_CHECKING,
)
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode,
    Program,
    StructDecl,
    MemberDecl,
    FuncDecl,
    Param,
    VarDecl,
    IfStmt,
    WhileStmt,
    ForStmt,
    BreakStmt,
    ContinueStmt,
    ReturnStmt,
    BlockStmt,
    SwitchStmt,
    CaseStmt,
    DefaultStmt,
    Type,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    BinaryOp,
    PrefixOp,
    PostfixOp,
    AssignExpr,
    MemberAccess,
    FuncCall,
    Identifier,
    StructLiteral,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    ExprStmt,
    Expr,
    Stmt,
    Decl,
)

# Type aliases for better type hints
TyCType = Union[IntType, FloatType, StringType, VoidType, StructType]
from .static_error import (
    StaticError,
    Redeclared,
    UndeclaredIdentifier,
    UndeclaredFunction,
    UndeclaredStruct,
    TypeCannotBeInferred,
    TypeMismatchInStatement,
    TypeMismatchInExpression,
    MustInLoop,
)

class Symbol():
    def __init__(self, name: str, typ):
        self.name = name
        self.typ = typ
    
    def __str__(self):
        return f"{self.name}({str(self.typ)})"
    
    def __repr__(self):
        return self.__str__()

    def __format__(self, format_spec):
        if format_spec == "":
            return str(self)
        else:
            # result = format_spec
            max_size = 20 - 1
            # print(len(str(self.name)))
            name_len = len(str(self.name))
            typ_len = len(str(self.typ))

            spaces = max_size - name_len - typ_len

            result = format_spec.replace("%n", str(self.name) + "".join([" " for i in range(spaces)]))

            result = result.replace("%t", str(self.typ))
            result = result.replace("%%", "%")
            return result.format()

class StaticChecker(ASTVisitor):
    def get_global_scope(self, scope):
        return scope[len(scope) - 1]

    def get_struct_namespace(self, scope):
        return self.get_global_scope(scope)[0]

    def get_func_namespace(self, scope):
        return self.get_global_scope(scope)[1]

    def get_next_scope(self, scope):
        return scope[0]

    def add_new_scope(self, scope):
        return [] + [scope]

    def add_new_struct(self, name, scope):
        size = len(scope)

        return scope[0:size-1] + [[[Symbol(name, "StructDecl")] + self.get_struct_namespace(scope)] + [self.get_func_namespace(scope)]]

    def add_new_func(self, name, scope):
        size = len(scope)

        return scope[0:size-1] + [[[self.get_struct_namespace(scope)] + [Symbol(name, "FuncDecl")] + self.get_func_namespace(scope)]]

    def add_name(self, name, scope):
        size = len(scope)

        return scope[0:size-1] + scope[1:]

    def add_new_var(self, name, typ, scope):
        next_scope = get_next_scope(scope)
        next_scope += [Symbol(name, typ)]

        return next_scope + scope[1:]

    def remove_next_scope(self, scope):
        return scope[1:]

    def print_scope(self, scope):
        local_scopes = scope[0:len(scope)-1]
        global_scope = scope[len(scope)-1]
        struct_scope = global_scope[0]
        func_scope = global_scope[1]

        big_scope_seperator = "=================================="
        small_scope_seperator = "========================"

        print(big_scope_seperator)
        txt = "=={:^30}=="
        print(txt.format("LOCAL SCOPES"))
        print(big_scope_seperator)

        list(map(lambda x: self.print_local_scope(x), local_scopes))

        print()
        print(big_scope_seperator)
        txt = "=={:^30}=="
        print(txt.format("GLOBAL SCOPES"))
        print(big_scope_seperator)

        list(map(lambda x: self.print_local_scope(x), global_scope))

    def print_local_scope(self, scope):
        centering = "{:^34}"

        txt = "=={:%n %t}=="

        small_scope_seperator = centering.format("========================")
        print()
        print(small_scope_seperator)
        list(map(lambda x: print(centering.format(txt.format(x))), scope))
        print(small_scope_seperator)

    def check_program(self, ast):
        return self.visit(ast)

    def check_redeclared(self, kind, name, local_scope):
        if(any([True for nm in local_scope if name == nm])):
            raise Redeclared(kind, name)

    def visit_program(self, node: "Program", o: Any = None):
        o = reduce(lambda y, x: self.visit(x, y), node.decls, [[[],[]]])

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        self.check_redeclared("Struct", node.name, o)
        o = self.add_new_struct(node.name, o)
        # self.print_scope(o)

        o = self.add_new_scope(o)
        o = reduce(lambda y, x: self.visit(x, y), node.members, o)
        o = self.remove_next_scope(o)

        return o

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        self.check_redeclared("Member", node.name, self.get_next_scope(o))
        o = add_new_var(node.name, "MemberStruct", o)

        return o

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        self.check_redeclared("Function", node.name, self.get_func_namespace(o))

        o = self.add_new_func(node.name, o)
        # self.print_scope(o)

        o = self.add_new_scope(o)
        o = reduce(lambda y, x: self.visit(x, y), node.param, o)
        o = self.visit(node.body, o)

        o = self.remove_next_scope(o)

        return o

    def visit_param(self, node: "Param", o: Any = None):
        self.check_redeclared("Parameter", node.name, self.get_next_scope(o))

        o = add_new_var(node.name, node.param_type, o)

        return o

    # Type system
    def visit_int_type(self, node: "IntType", o: Any = None):
        return node

    def visit_float_type(self, node: "FloatType", o: Any = None):
        return node

    def visit_string_type(self, node: "StringType", o: Any = None):
        return node

    def visit_void_type(self, node: "VoidType", o: Any = None):
        return node

    def visit_struct_type(self, node: "StructType", o: Any = None):
        return node

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        o = reduce(lambda y, x: self.visit(x, y), node.statements, o)

        return o

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        self.check_redeclared("Variable", node.name, self.get_next_scope(o))

        o = self.add_new_var(node.name, node.var_type, o)

        return o

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        o = self.visit(node.condition, o)
        o = self.visit(node.then_stmt, o)
        o = self.visit(node.else_stmt, o) if node.else_stmt

        return o

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        o = self.visit(node.condition, o)

        o = self.add_new_scope(o)
        o = self.add_new_var("While", None, o)
        o = self.visit(node.body, o)

        return o

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        o = self.visit(node.init, o) if node.init
        o = self.visit(node.condition, o)
        o = self.visit(node.update, o) if node.update
        o = self.add_new_scope(o)
        o = self.add_name("For", None, o)
        o = self.visit(node.body, o)

        return o

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        o = self.add_new_scope(o)
        o = self.add_name("Switch", None, o)
        o = self.visit(node.expr)
        o = reduce(lambda y, x: self.visit(x, y), node.cases, o)
        o = self.visit(node.default_case) if node.default_case

        return o

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        o = self.visit(node.expr)
        o = reduce(lambda y, x: self.visit(x, y), node.statements, o)

        return o

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        o = reduce(lambda y, x: self.visit(x, y), node.statements, o)

        return o

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        local_scope = get_next_scope(o)

        if local_scope[0] not in ["Switch", "For", "While"]:
            raise MustInLoop("break")

        return o

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        local_scope = get_next_scope(o)

        if local_scope[0] not in ["Switch", "For", "While"]:
            raise MustInLoop("continue")

        return o

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        return o

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        return self.visit(node.expr, o)

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        pass

    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        pass

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        pass

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        pass

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        pass

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        pass

    def visit_identifier(self, node: "Identifier", o: Any = None):
        pass

    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        pass

    # Literals
    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return node

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return node

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return node
