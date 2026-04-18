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

class AssignStmt(Stmt):
    def __init__(self, expr : Expr):
        super().__init__()

    def accept(self, visitor, o):
        visitor.visit_assign_stmt(self, o)

    def __str__():
        return f"ExprStmt({self.expr})"



class Symbol():
    def __init__(self, name: str, typ, value, params = None):
        self.name = name
        self.typ = typ
        self.params = params

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
    def get_local_scopes(self, scope):
        size = len(scope)

        return scope[0:size-2]

    def get_struct_namespace(self, scope):
        return scope[len(scope)-2]

    def get_func_namespace(self, scope):
        return scope[len(scope)-1]

    def get_next_scope(self, scope):
        return scope[0]

    def get_next_struct(self, scope):
        return self.get_struct_namespace(scope)[0]

    def add_new_scope(self, scope):
        return [[]] + scope

    def add_new_struct(self, name, scope):
        size = len(scope)
        # print(scope[0:size-2] + [[[Symbol(name, "StructDecl")]] + scope[size-2]] + [scope[size-1]])

        return scope[0:size-2] + [[[Symbol(name, "StructDecl")]] + scope[size-2]] + [scope[size-1]]

    def add_new_func(self, name, typ, params, scope):
        size = len(scope)
        # print(scope[0:size-1] + [[Symbol(name, "FuncDecl")] + scope[size-1]])

        return scope[0:size-1] + [[Symbol(name, typ, params)] + scope[size-1]]

    def add_name(self, name, scope):
        return [scope[0] + [name]] + scope[1:]

    def add_new_var(self, name, typ, scope):
        next_scope = self.get_next_scope(scope)
        # print([next_scope + [Symbol(name, typ)]] + scope[1:])

        return [next_scope + [Symbol(name, typ)]] + scope[1:]

    def add_new_struct_mem(self, name, typ, scope):
        size = len(scope)
        # print(scope[0:size-2] + [[scope[size-2][0] + [Symbol(name, typ)]] + scope[size-2][1:]] + [scope[size-1]])

        return scope[0:size-2] + [[scope[size-2][0] + [Symbol(name, typ)]] + scope[size-2][1:]] + [scope[size-1]]

    def remove_next_scope(self, scope):
        return scope[1:]

    def infer_type(self, lhs, rhs):
        return

    def ass_type(self, lt, rt, local_scope_list):
        # ret = [sym for scope in local_scope_list for sym in scope if str(name) == str(sym.name)]))
        # ret = [sym for scope in local_scope_list for sym in scope if str(name) == str(sym.name)]))

        # if len(ret) > 0:

        if lt is None or rt is None:
            return False
        elif lt is None:
            lt = rt
        else:
            rt = lt

        return True

    # def get_type(self, name, local_scope_list, typ = None, err = None):
    #     ret = [sym for scope in local_scope_list for sym in scope if str(name) == str(sym.name)]))
    #
    #     if len(ret) < 0:
    #         return None
    #
    #     sym = ret[0]
    #
    #     if sym.typ is None and typ is not None:
    #         sym.typ = typ
    #         return typ
    #
    #     if sym.typ is not None and sym.typ is not typ:
    #         raise err
    #
    #     return sym.typ

    def get_func_type(self, name, func_scope):
        ret = [sym for sym in scope if str(name) == str(sym.name)]

        if len(ret) > 0:
            return ret[0].typ

    def print_scope(self, scope, action_name = "SOME ACTION"):

        local_scopes = scope[0:len(scope)-2]
        struct_scope = self.get_struct_namespace(scope)
        func_scope = self.get_func_namespace(scope)

        print_seperator = "========================================================================"
        big_scope_seperator = "=================================="
        small_scope_seperator = "========================"
        centering = "{:^34}"
        txt = "=={:^30}=="

        print()
        print(print_seperator)
        print(action_name)

        print()
        print(big_scope_seperator)
        print(txt.format("LOCAL SCOPES"))
        print(big_scope_seperator)
        list(map(lambda x: self.print_local_scope(x), local_scopes))
        print(big_scope_seperator)

        print()
        print(big_scope_seperator)
        print(txt.format("STRUCT SCOPE"))
        print(big_scope_seperator)
        list(map(lambda x: self.print_local_scope(x), struct_scope))
        print(big_scope_seperator)

        print()
        print(big_scope_seperator)
        print(txt.format("FUNC SCOPE"))
        node_format = "=={:%n %t}=="
        print(big_scope_seperator)
        list(map(lambda x: print(centering.format(node_format.format(x))), func_scope))
        print(big_scope_seperator)

        print(print_seperator)

    def print_scope_list(self, scope):
        list(map(lambda x: self.print_local_scope(x), scope))

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
        # if len(local_scope) > 0:
        #     test = [nm for nm in local_scope if str(name) == str(nm.name)]
        #     if(len(test) > 0):
        #         print(test[0].name)
        #         print(name)
        if(any([True for nm in local_scope if str(name) == str(nm.name)])):
            raise Redeclared(kind, name)

    def check_redeclared_struct(self, name, scope):
        struct_namespace = self.get_struct_namespace(scope)

        if(any([True for struct in struct_namespace if str(name) == str(struct[0].name)])):
            raise Redeclared("Struct", name)

    def check_redeclared_func(self, name, scope):
        func_namespace = self.get_func_namespace(scope)

        if(any([True for func in func_namespace if str(name) == str(func.name)])):
            raise Redeclared("Function", name)

    def check_redeclared_member(self, name, struct_scope):
        if(any([True for member in struct_scope[1:] if str(name) == str(member.name)])):
            raise Redeclared("Member", name)

    def check_struct(self, ls, rs):
        l_size = len(ls)
        r_size = len(rs)

        if(l_size != r_size):
            return False

        if(any([True for i in range(l_size) if type(ls[i].typ) is not type(rt[i].typ)])):
            return False

        return True

    def check_type(self, lt, rt):
        if type(lt) is list and type(rt) is not list or type(lt) is not list and type(rt) is list:
            return False

        if type(lt) is list:
            self.check_struct(lt, rt)

        if lt is None or rt is None:
            return True
        else:
            return type(lt) == type(rt)

    def check_same_type(self, lt, rt, typ):
        if type(lt) is typ and type(rt) is typ:
            return True

        return False

    def get_symbol(self, name, local_scope_list):
        ret = [True for scope in local_scope_list for nm in scope if str(name) == str(nm.name)]

        if(len(ret) <= 0):
            raise UndeclaredIdentifier(name)

        return ret[0]

    def get_struct(self, name, scope):
        struct_namespace = self.get_struct_namespace(scope)

        ret = [struct for struct in struct_namespace if str(name) == str(struct[0].name)]

        if(len(ret) <= 0):
            raise UndeclaredStruct(name)

        return ret[0]

    def get_func(self, name, scope):
        func_namespace = self.get_func_namespace(scope)

        ret = [sym for sym in func_namespace if str(name) == str(sym.name)]

        if(len(ret) <= 0):
            raise UndeclaredFunction(name)

        return ret[0]

    def get_struct_member_list(self, struct_name, struct_name_space):
        struct = next(iter([struct for struct in struct_namespace if str(struct[0].name) == str(struct_name)]))

        return struct[1:]

    def get_struct_member(self, struct_name, member_name, struct_namespace):
        struct = next(iter([struct for struct in struct_namespace if str(struct[0].name) == str(struct_name)]))

        return next(iter([member for member in struct if str(member.name) == (member_name)]))

    # def get_member(self, member_name, struct_name, scope):
    #     struct_namespace = self.get_struct_namespace(scope)
    #
    #     if(not any([True for struct in struct_namespace for member in struct if struct_name == struct[0].name and member.name == member_name])):
    #         raise Undeclared("Member", name)

    def visit_program(self, node: "Program", o: Any = None):
        o = reduce(lambda y, x: self.visit(x, y), node.decls, [[],[]])

    def visit_struct_decl(self, node: "StructDecl", o: Any = None):
        self.check_redeclared_struct(node.name, o)
        o = self.add_new_struct(node.name, o)

        o = reduce(lambda y, x: self.visit(x, y), node.members, o)

        return o

    def visit_member_decl(self, node: "MemberDecl", o: Any = None):
        self.check_redeclared_member(node.name, self.get_next_struct(o))

        if isinstance(node.member_type, StructType):
            self.get_struct(node.member_type.struct_name, o)

            current_struct_name = self.get_next_struct(o)[0].name
            if current_struct_name == node.member_type.struct_name:
                raise UndeclaredStruct(node.member_type.struct_name)

        # self.print_scope(o, "adding member decl")
        o = self.add_new_struct_mem(node.name, "MemberStruct", o)

        return o

    def visit_func_decl(self, node: "FuncDecl", o: Any = None):
        self.check_redeclared_func(node.name, o)
        params = [param.param_type for param in node.params]

        o = self.add_new_func(node.name, node.typ, params, o)

        o = self.add_new_scope(o)
        o = reduce(lambda y, x: self.visit(x, y), node.params, o)
        o = self.visit(node.body, o)

        o = self.remove_next_scope(o)

        return o

    def visit_param(self, node: "Param", o: Any = None):
        self.check_redeclared("Parameter", node.name, self.get_next_scope(o))

        o = self.add_new_var(node.name, node.param_type, o)

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
        return self.get_struct_member_list(node.struct_name)

    # Statements
    def visit_block_stmt(self, node: "BlockStmt", o: Any = None):
        o = reduce(lambda y, x: self.visit(x, y), node.statements, o)

        return o

    def visit_var_decl(self, node: "VarDecl", o: Any = None):
        self.check_redeclared("Variable", node.name, self.get_next_scope(o))
        name = node.name
        var_type = node.var_type
        init_value = self.visit(node.init_value) if node.init_value else None

        if var_type is None:
            # init_value
            pass
        elif var_type.typ is not init_value.typ:
            pass




        o = self.add_new_var(node.name, node.var_type, o)
        # self.print_scope(o, "adding new var")

        return o

    def visit_if_stmt(self, node: "IfStmt", o: Any = None):
        o = self.visit(node.condition, o)
        o = self.visit(node.then_stmt, o)
        o = self.visit(node.else_stmt, o) if node.else_stmt else o

        return o

    def visit_while_stmt(self, node: "WhileStmt", o: Any = None):
        o = self.visit(node.condition, o)

        o = self.add_new_scope(o)
        o = self.add_new_var("While", None, o)
        o = self.visit(node.body, o)

        return o

    def visit_for_stmt(self, node: "ForStmt", o: Any = None):
        o = self.visit(node.init, o) if node.init else o
        o = self.visit(node.condition, o)
        o = self.visit(node.update, o) if node.update else o
        o = self.add_new_scope(o)
        o = self.add_name("For", None, o)
        o = self.visit(node.body, o)

        return o

    def visit_switch_stmt(self, node: "SwitchStmt", o: Any = None):
        o = self.add_new_scope(o)
        o = self.add_name("Switch", None, o)
        o = self.visit(node.expr)
        o = reduce(lambda y, x: self.visit(x, y), node.cases, o)
        o = self.visit(node.default_case) if node.default_case else o

        return o

    def visit_case_stmt(self, node: "CaseStmt", o: Any = None):
        o = self.visit(node.expr)
        o = reduce(lambda y, x: self.visit(x, y), node.statements, o)

        return o

    def visit_default_stmt(self, node: "DefaultStmt", o: Any = None):
        o = reduce(lambda y, x: self.visit(x, y), node.statements, o)

        return o

    def visit_break_stmt(self, node: "BreakStmt", o: Any = None):
        local_scope = self.get_next_scope(o)

        if local_scope[0].name not in ["Switch", "For", "While"]:
            raise MustInLoop("break")

        return o

    def visit_continue_stmt(self, node: "ContinueStmt", o: Any = None):
        local_scope = self.get_next_scope(o)

        if local_scope[0].name not in ["Switch", "For", "While"]:
            raise MustInLoop("continue")

        return o

    def visit_return_stmt(self, node: "ReturnStmt", o: Any = None):
        return o

    def visit_expr_stmt(self, node: "ExprStmt", o: Any = None):
        if type(node.expr) is AssignExpr:
            return self.visit(AssignStmt(node.expr), o)

        return self.visit(node.expr, o)

    def visit_assign_stmt(self, node: "AssignStmt", o: Any = None):
        lt = self.visit(node.expr)
        rt = self.visit(node.expr)

        if not self.check_type(lt, rt):
            raise TypeMismatchInStatement(node)

        self.ass_type(lt, rt)

        return o

    # Expressions
    def visit_binary_op(self, node: "BinaryOp", o: Any = None):
        lt = self.visit(node.left, o)
        rt = self.visit(node.right, o)

        if type(lt) is StructType or type(rt) is StructType:
            raise TypeMismatchInExpression(node)

        if node.operator == '+' or node.operator == '-' or node.operator == '*' or node.operator == '/':
            if type(lt) is StringType or type(rt) is StringType:
                raise TypeMismatchInExpression(node)

            if self.check_same_type(lt, rt, IntType):
                return IntType()

            return FloatType()
        elif node.operator == '%':
            if type(lt) is not IntType or type(rt) is not IntType:
                raise TypeMismatchInExpression(node)

            return IntType()
        elif node.operator == '==' or node.operator == '!=' or node.operator == '<' or node.operator == '<=' or node.operator == '>' or node.operator == '>=':
            if type(lt) is StringType or type(rt) is StringType:
                raise TypeMismatchInExpression(node)

            if self.check_same_type(lt, rt, IntType):
                raise TypeMismatchInExpression(node)

            if self.check_same_type(lt, rt, FloatType):
                raise TypeMismatchInExpression(node)

            return IntType()
        else:
            if type(lt) is not IntType or type(rt) is not IntType:
                raise TypeMismatchInExpression(node)

            return IntType()


    def visit_prefix_op(self, node: "PrefixOp", o: Any = None):
        operand_typ = self.visit(node.operand, o)
        if operand_typ is not IntType:
            raise TypeMismatchInExpression(node)

        return IntType()

    def visit_postfix_op(self, node: "PostfixOp", o: Any = None):
        operand_typ = self.visit(node.operand, o)

        if operand_typ is not IntType:
            raise TypeMismatchInExpression(node)

        return IntType()

    def visit_assign_expr(self, node: "AssignExpr", o: Any = None):
        lt = self.visit(node.lhs, o)
        rt = self.visit(node.rhs, o)

        if not self.check_type(lt, rt):
            raise TypeMismatchInExpression(node)

        self.ass_type(lt, rt)

        return lhs_expr

    def visit_member_access(self, node: "MemberAccess", o: Any = None):
        obj = self.visit(node.obj, o)

        if(type(obj) is not StructType):
            raise TypeMismatchInExpression(node)

        struct_name = obj.typ.struct_name
        member = self.get_struct_member(struct_name, node.member, self.get_struct_namespace(o))

        return member.typ

    def visit_func_call(self, node: "FuncCall", o: Any = None):
        func = self.get_func(node.name, self.get_func_namespace(o))

        param_len = len(func.params)
        args_len = len(node.args)

        args_sym_list = [self.visit(arg, o) for arg in node.args]

        if param_len != args_len:
            raise TypeMismatchInExpression(node)

        if any([not self.check_type(args_sym_list[i].typ, func.params[i]) for i in range(param_len)]):
            raise TypeMismatchInExpression(node)

        [self.ass_type(args_sym_list[i].typ, func.params[i].typ, o) for i in range(param_len)]

        return func.typ

    def visit_identifier(self, node: "Identifier", o: Any = None):
        sym = self.get_symbol(node.name, self.get_local_scopes(o))

        return sym.typ

    # Literals
    def visit_struct_literal(self, node: "StructLiteral", o: Any = None):
        return [self.visit(val) for val in node.values]

    def visit_int_literal(self, node: "IntLiteral", o: Any = None):
        return IntType()

    def visit_float_literal(self, node: "FloatLiteral", o: Any = None):
        return FloatType()

    def visit_string_literal(self, node: "StringLiteral", o: Any = None):
        return StringType()
