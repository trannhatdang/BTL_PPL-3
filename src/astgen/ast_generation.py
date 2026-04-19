"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *

class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""
    # Visit a parse tree produced by TyCParser#program.

    def visitProgram(self, ctx:TyCParser.ProgramContext):
        prog_stat_list_ctx = ctx.prog_stat_list()

        decls = self.visit(prog_stat_list_ctx)
        prog = Program(decls)

        return prog

    # Visit a parse tree produced by TyCParser#prog_stat_list.
    def visitProg_stat_list(self, ctx:TyCParser.Prog_stat_listContext):
        prog_stat_list_ctx = ctx.prog_stat_list()
        prog_stat_ctx = ctx.prog_stat()

        next_prog_stat_list = self.visit(prog_stat_list_ctx) if prog_stat_list_ctx else None
        prog_stat = self.visit(prog_stat_ctx) if prog_stat_ctx else None

        decls = []

        if prog_stat:
            decls.append(prog_stat)

        if next_prog_stat_list:
            decls.extend(next_prog_stat_list)

        return decls

    # Visit a parse tree produced by TyCParser#prog_stat.
    def visitProg_stat(self, ctx:TyCParser.Prog_statContext):
        func_decl_ctx = ctx.func_decl()
        struct_decl_ctx = ctx.struct_decl()

        func_decl = self.visit(func_decl_ctx) if func_decl_ctx else None
        struct_decl = self.visit(struct_decl_ctx) if struct_decl_ctx else None

        stat = func_decl if func_decl else struct_decl

        return stat

    # Visit a parse tree produced by TyCParser#func_decl.
    def visitFunc_decl(self, ctx:TyCParser.Func_declContext):
        return_type_ctx = ctx.return_type()
        ID_ctx = ctx.ID().getText() if ctx.ID() else None
        param_list_ctx = ctx.param_list()
        block_stat_ctx = ctx.block_stat()

        return_type = self.visit(return_type_ctx) if return_type_ctx else None
        ID = ID_ctx
        param_list = self.visit(param_list_ctx)
        block_stat = self.visit(block_stat_ctx)

        ret = FuncDecl(return_type, ID, param_list, block_stat)

        return ret

    # Visit a parse tree produced by TyCParser#param_list.
    def visitParam_list(self, ctx:TyCParser.Param_listContext):
        param_list_ctx = ctx.param_list()
        param_ctx = ctx.param()

        param_list = self.visit(param_list_ctx) if param_list_ctx else None
        param = self.visit(param_ctx) if param_ctx else None

        ret = []

        if param:
            ret.append(param)

        if param_list:
            ret.extend(param_list)

        return ret

    # Visit a parse tree produced by TyCParser#param.
    def visitParam(self, ctx:TyCParser.ParamContext):
        param_type_ctx = ctx.param_type()
        ID_ctx = ctx.ID().getText() if ctx.ID() else None

        param_type = self.visit(param_type_ctx)
        ID = ID_ctx

        ret = Param(param_type, ID)

        return ret

    # Visit a parse tree produced by TyCParser#param_type.
    def visitParam_type(self, ctx:TyCParser.Param_typeContext):
        int_type_ctx = ctx.INT_TYPE()
        float_type_ctx = ctx.FLOAT_TYPE()
        string_type_ctx = ctx.STRING_TYPE()
        ID_type_ctx = ctx.ID().getText() if ctx.ID() else None

        if int_type_ctx:
            return IntType()
        elif float_type_ctx:
            return FloatType()
        elif string_type_ctx:
            return StringType()
        elif ID_type_ctx:
            return StructType(ID_type_ctx)

        return None

    # Visit a parse tree produced by TyCParser#return_type.
    def visitReturn_type(self, ctx:TyCParser.Return_typeContext):
        param_type_ctx = ctx.param_type()
        void_type_ctx = ctx.VOID_TYPE()

        if void_type_ctx is not None:
            return VoidType()
        elif param_type_ctx is not None:
            return self.visit(param_type_ctx)

        return None

    # Visit a parse tree produced by TyCParser#struct_decl.
    def visitStruct_decl(self, ctx:TyCParser.Struct_declContext):
        ID_ctx = ctx.ID().getText() if ctx.ID() else None
        struct_var_decl_list_ctx = ctx.struct_var_decl_list()

        ID = ID_ctx
        struct_var_decl_list = self.visit(struct_var_decl_list_ctx) if struct_var_decl_list_ctx else None

        ret = StructDecl(ID, struct_var_decl_list)

        return ret

    # Visit a parse tree produced by TyCParser#struct_var_decl_list.
    def visitStruct_var_decl_list(self, ctx:TyCParser.Struct_var_decl_listContext):
        struct_var_decl_stat_ctx = ctx.struct_var_decl_stat()
        struct_var_decl_list_ctx = ctx.struct_var_decl_list()

        struct_var_decl_stat = self.visit(struct_var_decl_stat_ctx) if struct_var_decl_stat_ctx else None
        struct_var_decl_list = self.visit(struct_var_decl_list_ctx) if struct_var_decl_list_ctx else None

        ret = []

        if struct_var_decl_stat:
            ret.append(struct_var_decl_stat)

        if struct_var_decl_list:
            ret.extend(struct_var_decl_list)

        return ret

    # Visit a parse tree produced by TyCParser#struct_var_decl_stat.
    def visitStruct_var_decl_stat(self, ctx:TyCParser.Struct_var_decl_statContext):
        struct_var_type_ctx = ctx.struct_var_type()
        ID_ctx = ctx.ID().getText() if ctx.ID() else None

        struct_var_type = self.visit(struct_var_type_ctx)
        ID = ID_ctx

        ret = MemberDecl(struct_var_type, ID)

        return ret

    # Visit a parse tree produced by TyCParser#struct_lit.
    def visitStruct_lit(self, ctx:TyCParser.Struct_litContext):
        expr_list_ctx = ctx.expr_list()

        expr_list = self.visit(expr_list_ctx)

        ret = StructLiteral(expr_list)

        return ret

    # Visit a parse tree produced by TyCParser#struct_var_type.
    def visitStruct_var_type(self, ctx:TyCParser.Struct_var_typeContext):
        int_type_ctx = ctx.INT_TYPE()
        float_type_ctx = ctx.FLOAT_TYPE()
        string_type_ctx = ctx.STRING_TYPE()
        ID_type_ctx = ctx.ID().getText() if ctx.ID() else None

        if int_type_ctx:
            ret = IntType()
        elif float_type_ctx:
            ret = FloatType()
        elif string_type_ctx:
            ret = StringType()
        else:
            ret = StructType(ID_type_ctx)

        return ret

    # Visit a parse tree produced by TyCParser#stat_list.
    def visitStat_list(self, ctx:TyCParser.Stat_listContext):
        stat_ctx = ctx.stat()
        stat_list_ctx = ctx.stat_list()

        stat = self.visit(stat_ctx) if stat_ctx else None
        stat_list = self.visit(stat_list_ctx) if stat_list_ctx else None

        ret = []

        if stat:
            ret.append(stat)

        if stat_list:
            ret.extend(stat_list)

        return ret

    # Visit a parse tree produced by TyCParser#stat.
    def visitStat(self, ctx:TyCParser.StatContext):
        var_decl_stat_ctx = ctx.var_decl_stat()
        block_stat_ctx = ctx.block_stat()
        if_stat_ctx = ctx.if_stat()
        while_stat_ctx = ctx.while_stat()
        for_stat_ctx = ctx.for_stat()
        switch_stat_ctx = ctx.switch_stat()
        break_stat_ctx = ctx.break_stat()
        continue_stat_ctx = ctx.continue_stat()
        return_stat_ctx = ctx.return_stat()
        expr_stat_ctx = ctx.expr_stat()

        if var_decl_stat_ctx:
            return self.visit(var_decl_stat_ctx)

        if block_stat_ctx:
            return self.visit(block_stat_ctx)

        if if_stat_ctx:
            return self.visit(if_stat_ctx)

        if while_stat_ctx:
            return self.visit(while_stat_ctx)

        if for_stat_ctx:
            return self.visit(for_stat_ctx)

        if switch_stat_ctx:
            return self.visit(switch_stat_ctx)

        if break_stat_ctx:
            return self.visit(break_stat_ctx)

        if continue_stat_ctx:
            return self.visit(continue_stat_ctx)

        if return_stat_ctx:
            return self.visit(return_stat_ctx)

        return self.visit(expr_stat_ctx)

    # Visit a parse tree produced by TyCParser#var_decl_list.
    def visitVar_decl_list(self, ctx:TyCParser.Var_decl_listContext):
        var_decl_stat_ctx = ctx.var_decl_stat()
        var_decl_list_ctx = ctx.var_decl_list()

        var_decl_stat = self.visit(var_decl_stat_ctx)
        var_decl_list = self.visit(var_decl_list_ctx)

        ret = []

        if var_decl_stat:
            ret.append(var_decl_stat)

        if var_decl_list:
            ret.extend(var_decl_list)

        return ret

    # Visit a parse tree produced by TyCParser#var_decl_stat.
    def visitVar_decl_stat(self, ctx:TyCParser.Var_decl_statContext):
        var_decl_expr_ctx = ctx.var_decl_expr()

        var_decl_expr = self.visit(var_decl_expr_ctx)
        return var_decl_expr

    # Visit a parse tree produced by TyCParser#var_decl_expr.
    def visitVar_decl_expr(self, ctx:TyCParser.Var_decl_exprContext):
        var_type_ctx = ctx.var_type()
        ID_ctx = ctx.ID().getText() if ctx.ID() else None
        expr_ctx = ctx.expr()

        var_type = self.visit(var_type_ctx)
        ID = ID_ctx
        expr = self.visit(expr_ctx) if expr_ctx else None

        ret = VarDecl(var_type, ID, expr)

        return ret

    # Visit a parse tree produced by TyCParser#var_type.
    def visitVar_type(self, ctx:TyCParser.Var_typeContext):
        int_type_ctx = ctx.INT_TYPE()
        float_type_ctx = ctx.FLOAT_TYPE()
        string_type_ctx = ctx.STRING_TYPE()
        auto_type_ctx = ctx.AUTO()
        ID_type_ctx = ctx.ID().getText() if ctx.ID() else None

        if int_type_ctx:
            ret = IntType()
        elif float_type_ctx:
            ret = FloatType()
        elif string_type_ctx:
            ret = StringType()
        elif ID_type_ctx:
            ret = StructType(ID_type_ctx)
        else:
            ret = None

        return ret

    # Visit a parse tree produced by TyCParser#block_stat.
    def visitBlock_stat(self, ctx:TyCParser.Block_statContext):
        stat_list_ctx = ctx.stat_list()

        stat_list = self.visit(stat_list_ctx) if stat_list_ctx else None

        ret = BlockStmt(stat_list)

        return ret

    # Visit a parse tree produced by TyCParser#if_stat.
    def visitIf_stat(self, ctx:TyCParser.If_statContext):
        expr_ctx = ctx.expr()
        main_if_stat_ctx = ctx.main_if_stat()
        else_if_stat_ctx = ctx.else_if_stat()

        expr = self.visit(expr_ctx)
        main_stmt = self.visit(main_if_stat_ctx)
        else_stmt = self.visit(else_if_stat_ctx) if else_if_stat_ctx else None

        ret = IfStmt(expr, main_stmt, else_stmt)

        return ret

    # Visit a parse tree produced by TyCParser#main_if_stat.
    def visitMain_if_stat(self, ctx:TyCParser.Main_if_statContext):
        stat_ctx = ctx.stat()

        stat = self.visit(stat_ctx) if stat_ctx else None

        return stat

    # Visit a parse tree produced by TyCParser#else_if_stat.
    def visitElse_if_stat(self, ctx:TyCParser.Else_if_statContext):
        stat_ctx = ctx.stat()

        stat = self.visit(stat_ctx) if stat_ctx else None

        return stat

    # Visit a parse tree produced by TyCParser#while_stat.
    def visitWhile_stat(self, ctx:TyCParser.While_statContext):
        expr_ctx = ctx.expr()
        stat_ctx = ctx.stat()

        expr = self.visit(expr_ctx)
        stat = self.visit(stat_ctx)

        ret = WhileStmt(expr, stat)

        return ret

    # Visit a parse tree produced by TyCParser#for_stat.
    def visitFor_stat(self, ctx:TyCParser.For_statContext):
        for_init_stat_ctx = ctx.for_init_stat()
        for_cond_stat_ctx = ctx.for_cond_stat()
        for_update_stat_ctx = ctx.for_update_stat()
        stat_ctx = ctx.stat()

        for_init_stat = self.visit(for_init_stat_ctx)
        for_cond_stat = self.visit(for_cond_stat_ctx)
        for_update_stat = self.visit(for_update_stat_ctx)
        stat = self.visit(stat_ctx)

        ret = ForStmt(for_init_stat, for_cond_stat, for_update_stat, stat)

        return ret

    # Visit a parse tree produced by TyCParser#for_init_stat.
    def visitFor_init_stat(self, ctx:TyCParser.For_init_statContext):
        var_decl_stat_ctx = ctx.var_decl_expr()
        expr_stat_ctx = ctx.expr_stat()

        var_decl_stat = self.visit(var_decl_stat_ctx) if var_decl_stat_ctx else None
        expr_stat = self.visit(expr_stat_ctx) if expr_stat_ctx else None

        ret = var_decl_stat if var_decl_stat else expr_stat

        return ret

    # Visit a parse tree produced by TyCParser#for_cond_stat.
    def visitFor_cond_stat(self, ctx:TyCParser.For_cond_statContext):
        expr_ctx = ctx.expr()

        expr = self.visit(expr_ctx) if expr_ctx else None

        return expr

    # Visit a parse tree produced by TyCParser#for_update_stat.
    def visitFor_update_stat(self, ctx:TyCParser.For_update_statContext):
        expr_ctx = ctx.expr()

        expr = self.visit(expr_ctx) if expr_ctx else None

        return expr

    # Visit a parse tree produced by TyCParser#switch_stat.
    def visitSwitch_stat(self, ctx:TyCParser.Switch_statContext):
        expr_ctx = ctx.expr()
        case_expr_list_ctx = ctx.case_expr_list()
        default_case_expr_ctx = ctx.default_case_expr()

        expr = self.visit(expr_ctx)
        case_expr_list = self.visit(case_expr_list_ctx)
        default_case_expr = self.visit(default_case_expr_ctx)

        ret = SwitchStmt(expr, case_expr_list, default_case_expr)

        return ret

    # Visit a parse tree produced by TyCParser#case_expr_list.
    def visitCase_expr_list(self, ctx:TyCParser.Case_expr_listContext):
        case_expr_ctx = ctx.case_expr()
        case_expr_list_ctx = ctx.case_expr_list()

        case_expr = self.visit(case_expr_ctx) if case_expr_ctx else None
        case_expr_list = self.visit(case_expr_list_ctx) if case_expr_list_ctx else None

        ret = []

        if case_expr:
            ret.append(case_expr)

        if case_expr_list:
            ret.extend(case_expr_list)

        return ret

    # Visit a parse tree produced by TyCParser#case_expr.
    def visitCase_expr(self, ctx:TyCParser.Case_exprContext):
        expr_ctx = ctx.expr()
        stat_list_ctx = ctx.stat_list()

        expr = self.visit(expr_ctx)
        stat_list = self.visit(stat_list_ctx)

        ret = CaseStmt(expr, stat_list)
        return ret

    # Visit a parse tree produced by TyCParser#default_case_expr.
    def visitDefault_case_expr(self, ctx:TyCParser.Default_case_exprContext):
        stat_list_ctx = ctx.stat_list()

        stat_list = self.visit(stat_list_ctx) if stat_list_ctx else None

        ret = DefaultStmt(stat_list)

        return ret

    # Visit a parse tree produced by TyCParser#break_stat.
    def visitBreak_stat(self, ctx:TyCParser.Break_statContext):
        return BreakStmt()

    # Visit a parse tree produced by TyCParser#continue_stat.
    def visitContinue_stat(self, ctx:TyCParser.Continue_statContext):
        return ContinueStmt()

    # Visit a parse tree produced by TyCParser#return_stat.
    def visitReturn_stat(self, ctx:TyCParser.Return_statContext):
        expr_ctx = ctx.expr()

        expr = self.visit(expr_ctx) if expr_ctx else None

        ret = ReturnStmt(expr)

        return ret

    # Visit a parse tree produced by TyCParser#expr_stat.
    def visitExpr_stat(self, ctx:TyCParser.Expr_statContext):
        expr_ctx = ctx.expr()

        if expr_ctx:
            expr = self.visit(expr_ctx)
            return ExprStmt(expr)

    # Visit a parse tree produced by TyCParser#lvalue.
    def visitLvalue(self, ctx:TyCParser.LvalueContext):
        int_lit = ctx.INT()
        float_lit = ctx.FLOAT()
        string_lit = ctx.STRING()
        id_lit = ctx.ID().getText() if ctx.ID() else None
        struct_lit = ctx.struct_lit()

        if int_lit:
            ret = IntLiteral(int_lit)
        elif float_lit:
            ret = FloatLiteral(float_lit)
        elif string_lit:
            ret = StringLiteral(f"{string_lit}")
        elif struct_lit:
            ret = self.visit(struct_lit)
        else:
            ret = Identifier(id_lit)

        return ret

    # Visit a parse tree produced by TyCParser#expr_list.
    def visitExpr_list(self, ctx:TyCParser.Expr_listContext):
        expr_ctx = ctx.expr()
        expr_list_ctx = ctx.expr_list()

        expr = self.visit(expr_ctx) if expr_ctx else None
        expr_list = self.visit(expr_list_ctx) if expr_list_ctx else None

        ret = []

        if expr:
            ret.append(expr)

        if expr_list:
            ret.extend(expr_list)

        return ret

    # Visit a parse tree produced by TyCParser#expr.
    def visitExpr(self, ctx:TyCParser.ExprContext):
        if ctx.arg_list() and ctx.LROUND_BRACK():
            arg_list_ctx = ctx.arg_list()
            arg_list = self.visit(arg_list_ctx) if arg_list_ctx else None
            LROUND_BRACK = ctx.LROUND_BRACK()

            ID = ctx.ID().getText() if ctx.ID() else None

            return FuncCall(ID, arg_list)

        expr_ctx = ctx.expr()

        if len(expr_ctx) == 2 and ctx.children[1].getText() != '=':
            bin_op = ctx.children[1].getText()
            l_expr = self.visit(expr_ctx[0])
            r_expr = self.visit(expr_ctx[1])
            # l_bin_expr = self.visit(ctx.l_bin_expr()):
            return BinaryOp(l_expr, bin_op, r_expr)
        elif len(expr_ctx) == 2:
            l_expr = self.visit(expr_ctx[0])

            if ctx.ID():
                l_expr = MemberAccess(l_expr, ctx.ID().getText())

            r_expr = self.visit(expr_ctx[1])
            return AssignExpr(l_expr, r_expr)

        if len(expr_ctx) == 0:
            lvalue_ctx = ctx.lvalue()

            return self.visit(lvalue_ctx)

        expr_ctx = expr_ctx[0]
        expr = self.visit(expr_ctx)

        if ctx.LROUND_BRACK():
            return self.visit(expr_ctx)

        MEMACC_OP = ctx.MEMACC_OP()

        if MEMACC_OP:
            ID = ctx.ID().getText() if ctx.ID() else None
            return MemberAccess(expr, ID)

        post_op_ctx = ctx.post_op()

        if post_op_ctx:
            post_op = self.visit(post_op_ctx)
            return PostfixOp(post_op, expr)

        pre_op_ctx = ctx.pre_op()

        if pre_op_ctx:
            pre_op = self.visit(pre_op_ctx)
            return PrefixOp(pre_op, expr)

        un_op_ctx = ctx.un_op()

        un_op = self.visit(un_op_ctx)
        return PrefixOp(un_op, expr)

    # Visit a parse tree produced by TyCParser#assign_expr.
    def visitAssign_expr(self, ctx:TyCParser.Assign_exprContext):
        ID = ctx.ID().getText() if ctx.ID() else None
        expr = self.visit(ctx.expr())
        assigned_expr_ctx = ctx.assigned_expr()

        if assigned_expr_ctx:
            assigned_expr = self.visit(assigned_expr_ctx)
            mem_acc = MemberAccess(assigned_expr, ID)

            return AssignExpr(mem_acc, expr)

        return AssignExpr(ID, expr)

    # Visit a parse tree produced by TyCParser#arg_list.
    def visitArg_list(self, ctx:TyCParser.Arg_listContext):
        arg_ctx = ctx.arg()
        arg_list_ctx = ctx.arg_list()

        arg = self.visit(arg_ctx) if arg_ctx else None
        arg_list = self.visit(arg_list_ctx) if arg_list_ctx else None

        ret = []

        if arg:
            ret.append(arg)

        if arg_list:
            ret.extend(arg_list)

        return ret

    # Visit a parse tree produced by TyCParser#arg.
    def visitArg(self, ctx:TyCParser.ArgContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by TyCParser#un_op.
    def visitUn_op(self, ctx:TyCParser.Un_opContext):
        return ctx.children[0]

    # Visit a parse tree produced by TyCParser#pre_op.
    def visitPre_op(self, ctx:TyCParser.Pre_opContext):
        return ctx.children[0]

    # Visit a parse tree produced by TyCParser#post_op.
    def visitPost_op(self, ctx:TyCParser.Post_opContext):
        return ctx.children[0]
