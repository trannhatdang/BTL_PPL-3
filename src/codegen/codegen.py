"""
Code generator for TyC.
"""

from typing import Any

from ..utils.nodes import *
from ..utils.visitor import BaseVisitor
from .emitter import *
from .frame import *
from .io import IO_SYMBOL_LIST
from .utils import *
import glob


class StringArrayType:
    """Marker type for JVM main(String[] args)."""
    pass


class CodeGenerator(BaseVisitor):
    """Minimal AST -> Jasmin code generator."""

    def __init__(self):
        self.emit = None
        self.functions = {}
        self.current_return_type = VoidType()
        self.class_name = "TyC"

    def _lookup_symbol(self, name: str, sym_list: list[Symbol]) -> Symbol:
        for sym in reversed(sym_list):
            if sym.name == name:
                return sym
        raise RuntimeError(f"Undeclared symbol: {name}")

    def _infer_struct(self, typ_list):
        len_check = [struct for struct in self.struct_list if (len(struct) - 1) == len(typ_list)]
        ret = [struct for struct in len_check if self._check_struct_match(struct[1:], typ_list)]
        # print(len_check)
        # print(ret)

        if len(ret) == 0:
            raise RuntimeError("No such struct")

        return ret[0]

    def _find_struct(self, struct_name):
        ret = [struct for struct in self.struct_list if struct[0] == struct_name]

        if len(ret) == 0:
            raise RuntimeError("No such struct")

        return ret[0]

    def _check_struct_match(self, struct, literal):
        struct_len = len(struct)
        literal_len = len(literal)

        if struct_len != literal_len:
            raise RuntimeError("Struct mismatch")

        res = [typ for i in range(struct_len) if type(struct[i][1]) is not type(literal[i])]

        if len(res) > 0:
            raise RuntimeError("Struct mismatch")

        return len(res) == 0

    def _infer_type(self, node: Expr, o: Access):
        if isinstance(node, IntLiteral):
            return IntType()
        if isinstance(node, FloatLiteral):
            return FloatType()
        if isinstance(node, StringLiteral):
            return StringType()
        if isinstance(node, Identifier):
            return self._lookup_symbol(node.name, o.sym).type
        if isinstance(node, MemberAccess):
            return StructType()
        if isinstance(node, AssignExpr):
            return self._infer_type(node.rhs, o)
        if isinstance(node, FuncCall):
            return self.functions[node.name].type.return_type
        if isinstance(node, BinaryOp):
            if node.operator in ["+", "-", "*", "/", "%"]:
                left_type = self._infer_type(node.left, o)
                right_type = self._infer_type(node.right, o)
                if is_float_type(left_type) or is_float_type(right_type):
                    return FloatType()
                return IntType()
            if node.operator in ["<", "<=", ">", ">=", "==", "!="]:
                return IntType()
        return IntType()

    def _check_struct(self, struct, expect_name, expect_member, arr):
        # print('check_struct: ')
        # print(struct)
        # print(expect_name)
        # print(struct[0])
        if struct[0] != expect_name:
            return

        # print('check_struct: ')
        # print(struct)

        struct_types = [typ for name, typ in struct[1:] if name == expect_member]

        if len(struct_types) > 0:
            arr.append(struct_types[0])

    def _get_member_typ(self, name, member):
        arr = []
        list(map(lambda x: self._check_struct(x, name, member, arr), self.struct_list))

        if(len(arr) == 0):
            raise RuntimeError("No such member")

        return arr[0]

    def _put_struct_field(self, lhs_name, lhs_type, lhs_member_name, lhs_member_type, lhs_idx, o):
        code = self.emit.emit_dup(o.frame)
        code += self.emit.emit_get_field(f'{lhs_type.struct_name}/{lhs_member_name}', lhs_member_type, o.frame)
        code += self.emit.emit_read_var(lhs_name, lhs_type, lhs_idx, o.frame)
        code += self.emit.emit_dup_x1(o.frame)
        code += self.emit.emit_pop(o.frame)
        code += self.emit.emit_put_field(f'{lhs_type.struct_name}/{lhs_member_name}', lhs_member_type, o.frame)
        return code

    def visit_program(self, node: Program, o: Any = None):
        self.emit = Emitter(f"{self.class_name}.j")
        self.emit.print_out(self.emit.emit_prolog(self.class_name))
        self.struct_list = []

        for io_sym in IO_SYMBOL_LIST:
            self.functions[io_sym.name] = io_sym

        for decl in node.decls:
            if isinstance(decl, FuncDecl):
                return_type = decl.return_type if decl.return_type else VoidType()
                param_types = [p.param_type for p in decl.params]
                self.functions[decl.name] = Symbol(
                    decl.name, FunctionType(param_types, return_type), CName(self.class_name)
                )

        for decl in node.decls:
            self.visit(decl, None)

        self.emit.emit_epilog()

    def visit_func_decl(self, node: FuncDecl, o: Any = None):
        self.current_return_type = node.return_type if node.return_type else VoidType()
        frame = Frame(node.name, self.current_return_type)
        frame.enter_scope(True)

        if node.name == "main":
            mtype = FunctionType([StringArrayType()], VoidType())
        else:
            mtype = FunctionType([p.param_type for p in node.params], self.current_return_type)

        self.emit.print_out(self.emit.emit_method(node.name, mtype, True))

        start_label = frame.get_start_label()
        end_label = frame.get_end_label()
        self.emit.print_out(self.emit.emit_label(start_label, frame))

        local_syms: list[Symbol] = []
        if node.name == "main":
            args_idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(
                    args_idx, "args", StringArrayType(), start_label, end_label
                )
            )

        for param in node.params:
            idx = frame.get_new_index()
            self.emit.print_out(
                self.emit.emit_var(idx, param.name, param.param_type, start_label, end_label)
            )
            local_syms.append(Symbol(param.name, param.param_type, Index(idx)))

        sub_body = SubBody(frame, local_syms)
        self.visit(node.body, sub_body)

        if is_void_type(self.current_return_type):
            self.emit.print_out(self.emit.emit_return(VoidType(), frame))

        self.emit.print_out(self.emit.emit_label(end_label, frame))
        frame.exit_scope()
        self.emit.print_out(self.emit.emit_end_method(frame))

    def visit_block_stmt(self, node: BlockStmt, o: SubBody = None):
        for stmt in node.statements:
            o = self.visit(stmt, o)
        return o

    def visit_var_decl(self, node: VarDecl, o: SubBody = None):
        frame = o.frame
        idx = frame.get_new_index()
        var_type = node.var_type if node.var_type else self._infer_type(node.init_value, Access(frame, o.sym))

        if isinstance(var_type, StructType) or type(var_type).__name__ == 'StructType':
            self.emit.print_out(
                self.emit.emit_new_instance(
                    var_type.struct_name, frame
                )
                + self.emit.emit_write_var(node.name, var_type, idx, frame)
            )
        else:
            self.emit.print_out(
                self.emit.emit_var(
                    idx, node.name, var_type, frame.get_start_label(), frame.get_end_label()
                )
            )

        if node.init_value is not None:
            rhs_code, _ = self.visit(node.init_value, Access(frame, o.sym))
            if isinstance(var_type, StructType) or type(var_type).__name__ == 'StructType':
                struct = self._find_struct(var_type.struct_name)
                code = rhs_code + ''.join([self._put_struct_field(node.name, var_type, struct[i][0], struct[i][1], idx, o) for i in range(1, len(struct))])
                self.emit.print_out(code)
            else:
                self.emit.print_out(rhs_code)
                self.emit.print_out(self.emit.emit_write_var(node.name, var_type, idx, frame))

        o.sym.append(Symbol(node.name, var_type, Index(idx)))
        return o

    def visit_expr_stmt(self, node: ExprStmt, o: SubBody = None):
        code, expr_type = self.visit(node.expr, Access(o.frame, o.sym))
        self.emit.print_out(code)
        if not is_void_type(expr_type):
            self.emit.print_out(self.emit.emit_pop(o.frame))
        return o

    def visit_if_stmt(self, node: IfStmt, o: SubBody = None):
        frame = o.frame
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        else_label = frame.get_new_label()
        end_label = frame.get_new_label()
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(else_label, frame))
        self.visit(node.then_stmt, o)
        self.emit.print_out(self.emit.emit_goto(end_label, frame))
        self.emit.print_out(self.emit.emit_label(else_label, frame))
        if node.else_stmt:
            self.visit(node.else_stmt, o)
        self.emit.print_out(self.emit.emit_label(end_label, frame))
        return o

    def visit_while_stmt(self, node: WhileStmt, o: SubBody = None):
        frame = o.frame
        start_label = frame.get_new_label()
        end_label = frame.get_new_label()
        self.emit.print_out(self.emit.emit_label(start_label, frame))
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(end_label, frame))
        self.visit(node.body, o)
        self.emit.print_out(self.emit.emit_goto(start_label, frame))
        self.emit.print_out(self.emit.emit_label(end_label, frame))
        return o

    def visit_return_stmt(self, node: ReturnStmt, o: SubBody = None):
        if node.expr is None:
            self.emit.print_out(self.emit.emit_return(VoidType(), o.frame))
            return o
        code, ret_type = self.visit(node.expr, Access(o.frame, o.sym))
        self.emit.print_out(code)
        self.emit.print_out(self.emit.emit_return(ret_type, o.frame))
        return o

    def visit_binary_op(self, node: BinaryOp, o: Access = None):
        left_code, left_type = self.visit(node.left, o)
        right_code, right_type = self.visit(node.right, o)
        frame = o.frame

        if node.operator in ["+", "-"]:
            result_type = FloatType() if is_float_type(left_type) or is_float_type(right_type) else IntType()
            return (
                left_code
                + right_code
                + self.emit.emit_add_op(node.operator, result_type, frame),
                result_type,
            )
        if node.operator in ["*", "/"]:
            result_type = FloatType() if is_float_type(left_type) or is_float_type(right_type) else IntType()
            return (
                left_code
                + right_code
                + self.emit.emit_mul_op(node.operator, result_type, frame),
                result_type,
            )
        if node.operator == "%":
            return left_code + right_code + self.emit.emit_mod(frame), IntType()
        if node.operator in ["<", "<=", ">", ">=", "==", "!="]:
            op_type = FloatType() if is_float_type(left_type) or is_float_type(right_type) else IntType()
            return left_code + right_code + self.emit.emit_re_op(node.operator, op_type, frame), IntType()
        raise RuntimeError(f"Unsupported operator: {node.operator}")

    def visit_assign_expr(self, node: AssignExpr, o: Access = None):
        if isinstance(node.lhs, Identifier):
            lhs_name = node.lhs.name
        elif isinstance(node.lhs, MemberAccess):
            lhs_name = node.lhs.obj.name
        else:
            raise RuntimeError("Minimal codegen only supports identifier assignment or member access")

        rhs_code, rhs_type = self.visit(node.rhs, o)
        lhs_sym = self._lookup_symbol(lhs_name, o.sym)
        idx = lhs_sym.value.value

        if isinstance(node.lhs, Identifier) and isinstance(node.rhs, StructLiteral):
            struct = self._find_struct(lhs_sym.type.struct_name)
            code = rhs_code + "".join([self._put_struct_field(lhs_name, lhs_sym.type, struct[i][0], struct[i][1], idx, o) for i in range(1, len(struct))])
        elif isinstance(node.lhs, Identifier):
            code = rhs_code + self.emit.emit_dup(o.frame) + self.emit.emit_write_var(lhs_name, lhs_sym.type, idx, o.frame)
        else:
            #member acc
            code = self.emit.emit_read_var(lhs_name, lhs_sym.type, idx, o.frame) + rhs_code + self.emit.emit_dup_x1(o.frame) + self.emit.emit_put_field(f'{lhs_sym.type.struct_name}/{node.lhs.member}', self._get_member_typ(lhs_sym.type.struct_name, node.lhs.member), o.frame)

        return code, rhs_type

    def visit_func_call(self, node: FuncCall, o: Access = None):
        frame = o.frame
        fn_sym = self.functions[node.name]
        fn_type = fn_sym.type
        code = ""
        for arg in node.args:
            arg_code, _ = self.visit(arg, o)
            code += arg_code
        code += self.emit.emit_invoke_static(f"{fn_sym.value.value}/{node.name}", fn_type, frame)
        return code, fn_type.return_type

    def visit_identifier(self, node: Identifier, o: Access = None):
        sym = self._lookup_symbol(node.name, o.sym)
        return self.emit.emit_read_var(node.name, sym.type, sym.value.value, o.frame), sym.type

    def visit_int_literal(self, node: IntLiteral, o: Access = None):
        return self.emit.emit_push_iconst(node.value, o.frame), IntType()

    def visit_float_literal(self, node: FloatLiteral, o: Access = None):
        return self.emit.emit_push_fconst(str(node.value), o.frame), FloatType()

    def visit_string_literal(self, node: StringLiteral, o: Access = None):
        return self.emit.emit_push_const(node.value, StringType(), o.frame), StringType()

    def visit_struct_decl(self, node: StructDecl, o: Any = None):
        self.struct_emit = Emitter(f"{node.name}.j")
        frame = Frame(node.name, None)

        self.struct_emit.print_out(self.struct_emit.emit_prolog(node.name))

        struct = [node.name]

        struct_members = list(map(lambda x: self.visit(x, Access(frame, [])), node.members))

        struct += struct_members

        self.struct_emit.print_out(self.struct_emit.emit_init_method())
        self.struct_emit.print_out(self.struct_emit.jvm.emitLIMITSTACK(1))
        self.struct_emit.print_out(self.struct_emit.jvm.emitLIMITLOCAL(1))
        self.struct_emit.print_out(self.struct_emit.emit_read_var(node.name, StructType(node.name), 0, frame))
        self.struct_emit.print_out(self.struct_emit.emit_new_object())
        self.struct_emit.print_out(self.struct_emit.emit_return(VoidType(), frame))
        self.struct_emit.print_out(self.struct_emit.jvm.emitENDMETHOD())

        self.struct_list.append(struct)
        #print(self.struct_list)

        self.struct_emit.emit_epilog()
        return None

    def visit_member_decl(self, node: MemberDecl, o: Any = None):
        frame = o.frame
        var_type = node.member_type

        self.struct_emit.print_out(
                self.struct_emit.emit_field(node.name, var_type)
        )

        return node.name, var_type

    def visit_param(self, node: Param, o: Any = None):
        return None

    def visit_int_type(self, node: IntType, o: Any = None):
        return node

    def visit_float_type(self, node: FloatType, o: Any = None):
        return node

    def visit_string_type(self, node: StringType, o: Any = None):
        return node

    def visit_void_type(self, node: VoidType, o: Any = None):
        return node

    def visit_struct_type(self, node: StructType, o: Any = None):
        return node

    def visit_for_stmt(self, node: ForStmt, o: Any = None):
        frame = o.frame
        start_label = frame.get_new_label()
        end_label = frame.get_new_label()
        # print('hi')
        self.visit(node.init, o)
        self.emit.print_out(self.emit.emit_label(start_label, frame))
        # print('hi')
        cond_code, _ = self.visit(node.condition, Access(frame, o.sym))
        self.emit.print_out(cond_code)
        self.emit.print_out(self.emit.emit_if_false(end_label, frame))
        self.visit(node.body, o)
        update_code, _ = self.visit(node.update, Access(frame, o.sym))
        self.emit.print_out(update_code)
        self.emit.print_out(self.emit.emit_pop(frame))
        self.emit.print_out(self.emit.emit_goto(start_label, frame))
        self.emit.print_out(self.emit.emit_label(end_label, frame))
        return o

    def visit_switch_stmt(self, node: SwitchStmt, o: Any = None):
        raise RuntimeError("SwitchStmt not supported in minimal codegen")

    def visit_case_stmt(self, node: CaseStmt, o: Any = None):
        raise RuntimeError("CaseStmt not supported in minimal codegen")

    def visit_default_stmt(self, node: DefaultStmt, o: Any = None):
        raise RuntimeError("DefaultStmt not supported in minimal codegen")

    def visit_break_stmt(self, node: BreakStmt, o: Any = None):
        raise RuntimeError("BreakStmt not supported in minimal codegen")

    def visit_continue_stmt(self, node: ContinueStmt, o: Any = None):
        raise RuntimeError("ContinueStmt not supported in minimal codegen")

    def visit_prefix_op(self, node: PrefixOp, o: Any = None):
        operand_val, operand_typ = self.visit(node.operand, o)

        if not isinstance(operand_typ, IntType):
            raise RuntimeError("Incorrect operand type for postfix op")

        frame = o.frame

        if node.operator in ["++", "--"]:
            name = node.operand.name if isinstance(node.operand, Identifier) else node.obj.name
            sym = self._lookup_symbol(name, o.sym)
            idx = sym.value.value
            result_type = IntType()

            one_code, _ = self.visit(IntLiteral(1), Access(o.frame, o.sym))

            if isinstance(node.operand, Identifier):
                code = operand_val
                code += one_code
                code += self.emit.emit_add_op(node.operator[0], result_type, o.frame)
                code += self.emit.emit_dup(frame)
                code += self.emit.emit_write_var(node.operand.name, sym.type, idx, o.frame)
            else:
                code = self.emit.emit_read_var(node.operand.obj, sym.type, idx, o.frame)
                code += operand_val
                code += one_code
                code += self.emit.emit_add_op(node.operator[0], result_type, o.frame)
                code += self.emit.emit_dup_x1(o.frame)
                code += self.emit.emit_put_field(f'{sym.type.name}/{node.operand.obj}', result_type, sym.typ, o.frame)

            return code, result_type

    def visit_postfix_op(self, node: PostfixOp, o: Any = None):
        operand_val, operand_typ = self.visit(node.operand, o)

        if not isinstance(operand_typ, IntType):
            raise RuntimeError("Incorrect operand type for postfix op")

        frame = o.frame

        if node.operator in ["++", "--"]:
            name = node.operand.name if isinstance(node.operand, Identifier) else node.obj.name
            sym = self._lookup_symbol(name, o.sym)
            idx = sym.value.value
            result_type = IntType()

            one_code, _ = self.visit(IntLiteral(1), Access(o.frame, o.sym))

            if isinstance(node.operand, Identifier):
                code = operand_val
                code += self.emit.emit_dup(frame)
                code += one_code
                code += self.emit.emit_add_op(node.operator[0], result_type, o.frame)
                code += self.emit.emit_write_var(node.operand.name, sym.type, idx, o.frame)
            else:
                code = self.emit.emit_read_var(node.operand.obj, sym.type, idx, o.frame)
                code += operand_val
                code += self.emit.dup_x1(o.frame)
                code += one_code
                code += self.emit.emit_add_op(node.operator[0], result_type, o.frame)
                code += self.emit.emit_put_field(f'{sym.type.name}/{node.operand.obj}', result_type, sym.typ, o.frame)

            return code, result_type

    def visit_member_access(self, node: MemberAccess, o: Any = None):
        name = node.obj.name
        member = node.member

        sym = self._lookup_symbol(name, o.sym)
        struct_name = sym.type.struct_name
        member_typ = self._get_member_typ(struct_name, member)

        code = self.emit.emit_read_var(name, sym.type, sym.value.value, o.frame) + self.emit.emit_get_field(f'{struct_name}/{member}', member_typ, o.frame)

        return code, sym.type

    def visit_struct_literal(self, node: StructLiteral, o: Any = None):
        expr_list = [self.visit(val, o) for val in node.values]

        expr_code_list = [code for code, typ in expr_list]
        typ_list = [typ for code, typ in expr_list]

        frame = o.frame
        struct = self._infer_struct(typ_list)
        code = self.emit.emit_new_instance(struct[0], frame) + ''.join([self.emit.emit_dup(frame) + expr_code_list[i] + self.emit.emit_put_field(f'{struct[0]}/{struct[i+1][0]}', struct[i+1][1], o.frame) for i in range(len(expr_code_list))])
        # print(code)

        return code, StructType(struct[0])
