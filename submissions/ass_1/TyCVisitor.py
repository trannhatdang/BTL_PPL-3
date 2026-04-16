# Generated from D:/DH/HK252/BTL_PPL 3/src/grammar/TyC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete generic visitor for a parse tree produced by TyCParser.

class TyCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TyCParser#program.
    def visitProgram(self, ctx:TyCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#prog_stat_list.
    def visitProg_stat_list(self, ctx:TyCParser.Prog_stat_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#prog_stat.
    def visitProg_stat(self, ctx:TyCParser.Prog_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#func_decl.
    def visitFunc_decl(self, ctx:TyCParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#param_list.
    def visitParam_list(self, ctx:TyCParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#param.
    def visitParam(self, ctx:TyCParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#param_type.
    def visitParam_type(self, ctx:TyCParser.Param_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#return_type.
    def visitReturn_type(self, ctx:TyCParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_decl.
    def visitStruct_decl(self, ctx:TyCParser.Struct_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_var_decl_list.
    def visitStruct_var_decl_list(self, ctx:TyCParser.Struct_var_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_var_decl_stat.
    def visitStruct_var_decl_stat(self, ctx:TyCParser.Struct_var_decl_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_var_type.
    def visitStruct_var_type(self, ctx:TyCParser.Struct_var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#struct_lit.
    def visitStruct_lit(self, ctx:TyCParser.Struct_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#stat_list.
    def visitStat_list(self, ctx:TyCParser.Stat_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#stat.
    def visitStat(self, ctx:TyCParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#var_decl_list.
    def visitVar_decl_list(self, ctx:TyCParser.Var_decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#var_decl_stat.
    def visitVar_decl_stat(self, ctx:TyCParser.Var_decl_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#var_decl_expr.
    def visitVar_decl_expr(self, ctx:TyCParser.Var_decl_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#var_type.
    def visitVar_type(self, ctx:TyCParser.Var_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#block_stat.
    def visitBlock_stat(self, ctx:TyCParser.Block_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#if_stat.
    def visitIf_stat(self, ctx:TyCParser.If_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#main_if_stat.
    def visitMain_if_stat(self, ctx:TyCParser.Main_if_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#else_if_stat.
    def visitElse_if_stat(self, ctx:TyCParser.Else_if_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#while_stat.
    def visitWhile_stat(self, ctx:TyCParser.While_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_stat.
    def visitFor_stat(self, ctx:TyCParser.For_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_init_stat.
    def visitFor_init_stat(self, ctx:TyCParser.For_init_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_cond_stat.
    def visitFor_cond_stat(self, ctx:TyCParser.For_cond_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#for_update_stat.
    def visitFor_update_stat(self, ctx:TyCParser.For_update_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#switch_stat.
    def visitSwitch_stat(self, ctx:TyCParser.Switch_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#case_expr_list.
    def visitCase_expr_list(self, ctx:TyCParser.Case_expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#case_expr.
    def visitCase_expr(self, ctx:TyCParser.Case_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#default_case_expr.
    def visitDefault_case_expr(self, ctx:TyCParser.Default_case_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#break_stat.
    def visitBreak_stat(self, ctx:TyCParser.Break_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#continue_stat.
    def visitContinue_stat(self, ctx:TyCParser.Continue_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#return_stat.
    def visitReturn_stat(self, ctx:TyCParser.Return_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_stat.
    def visitExpr_stat(self, ctx:TyCParser.Expr_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#lvalue.
    def visitLvalue(self, ctx:TyCParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr_list.
    def visitExpr_list(self, ctx:TyCParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#expr.
    def visitExpr(self, ctx:TyCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#assign_expr.
    def visitAssign_expr(self, ctx:TyCParser.Assign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#assigned_expr.
    def visitAssigned_expr(self, ctx:TyCParser.Assigned_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#arg_list.
    def visitArg_list(self, ctx:TyCParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#arg.
    def visitArg(self, ctx:TyCParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#un_op.
    def visitUn_op(self, ctx:TyCParser.Un_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#pre_op.
    def visitPre_op(self, ctx:TyCParser.Pre_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TyCParser#post_op.
    def visitPost_op(self, ctx:TyCParser.Post_opContext):
        return self.visitChildren(ctx)



del TyCParser