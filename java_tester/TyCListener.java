// Generated from java_tester/TyC.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TyCParser}.
 */
public interface TyCListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TyCParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(TyCParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(TyCParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#prog_stat_list}.
	 * @param ctx the parse tree
	 */
	void enterProg_stat_list(TyCParser.Prog_stat_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#prog_stat_list}.
	 * @param ctx the parse tree
	 */
	void exitProg_stat_list(TyCParser.Prog_stat_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#prog_stat}.
	 * @param ctx the parse tree
	 */
	void enterProg_stat(TyCParser.Prog_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#prog_stat}.
	 * @param ctx the parse tree
	 */
	void exitProg_stat(TyCParser.Prog_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#func_decl}.
	 * @param ctx the parse tree
	 */
	void enterFunc_decl(TyCParser.Func_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#func_decl}.
	 * @param ctx the parse tree
	 */
	void exitFunc_decl(TyCParser.Func_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#param_list}.
	 * @param ctx the parse tree
	 */
	void enterParam_list(TyCParser.Param_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#param_list}.
	 * @param ctx the parse tree
	 */
	void exitParam_list(TyCParser.Param_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(TyCParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(TyCParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#param_type}.
	 * @param ctx the parse tree
	 */
	void enterParam_type(TyCParser.Param_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#param_type}.
	 * @param ctx the parse tree
	 */
	void exitParam_type(TyCParser.Param_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#return_type}.
	 * @param ctx the parse tree
	 */
	void enterReturn_type(TyCParser.Return_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#return_type}.
	 * @param ctx the parse tree
	 */
	void exitReturn_type(TyCParser.Return_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#struct_decl}.
	 * @param ctx the parse tree
	 */
	void enterStruct_decl(TyCParser.Struct_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#struct_decl}.
	 * @param ctx the parse tree
	 */
	void exitStruct_decl(TyCParser.Struct_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#struct_var_decl_list}.
	 * @param ctx the parse tree
	 */
	void enterStruct_var_decl_list(TyCParser.Struct_var_decl_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#struct_var_decl_list}.
	 * @param ctx the parse tree
	 */
	void exitStruct_var_decl_list(TyCParser.Struct_var_decl_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#struct_var_decl_stat}.
	 * @param ctx the parse tree
	 */
	void enterStruct_var_decl_stat(TyCParser.Struct_var_decl_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#struct_var_decl_stat}.
	 * @param ctx the parse tree
	 */
	void exitStruct_var_decl_stat(TyCParser.Struct_var_decl_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#struct_var_type}.
	 * @param ctx the parse tree
	 */
	void enterStruct_var_type(TyCParser.Struct_var_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#struct_var_type}.
	 * @param ctx the parse tree
	 */
	void exitStruct_var_type(TyCParser.Struct_var_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#struct_lit}.
	 * @param ctx the parse tree
	 */
	void enterStruct_lit(TyCParser.Struct_litContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#struct_lit}.
	 * @param ctx the parse tree
	 */
	void exitStruct_lit(TyCParser.Struct_litContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#stat_list}.
	 * @param ctx the parse tree
	 */
	void enterStat_list(TyCParser.Stat_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#stat_list}.
	 * @param ctx the parse tree
	 */
	void exitStat_list(TyCParser.Stat_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(TyCParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(TyCParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#var_decl_list}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl_list(TyCParser.Var_decl_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#var_decl_list}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl_list(TyCParser.Var_decl_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#var_decl_stat}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl_stat(TyCParser.Var_decl_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#var_decl_stat}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl_stat(TyCParser.Var_decl_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#var_decl_expr}.
	 * @param ctx the parse tree
	 */
	void enterVar_decl_expr(TyCParser.Var_decl_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#var_decl_expr}.
	 * @param ctx the parse tree
	 */
	void exitVar_decl_expr(TyCParser.Var_decl_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#var_type}.
	 * @param ctx the parse tree
	 */
	void enterVar_type(TyCParser.Var_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#var_type}.
	 * @param ctx the parse tree
	 */
	void exitVar_type(TyCParser.Var_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#block_stat}.
	 * @param ctx the parse tree
	 */
	void enterBlock_stat(TyCParser.Block_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#block_stat}.
	 * @param ctx the parse tree
	 */
	void exitBlock_stat(TyCParser.Block_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#if_stat}.
	 * @param ctx the parse tree
	 */
	void enterIf_stat(TyCParser.If_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#if_stat}.
	 * @param ctx the parse tree
	 */
	void exitIf_stat(TyCParser.If_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#main_if_stat}.
	 * @param ctx the parse tree
	 */
	void enterMain_if_stat(TyCParser.Main_if_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#main_if_stat}.
	 * @param ctx the parse tree
	 */
	void exitMain_if_stat(TyCParser.Main_if_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#else_if_stat}.
	 * @param ctx the parse tree
	 */
	void enterElse_if_stat(TyCParser.Else_if_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#else_if_stat}.
	 * @param ctx the parse tree
	 */
	void exitElse_if_stat(TyCParser.Else_if_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#while_stat}.
	 * @param ctx the parse tree
	 */
	void enterWhile_stat(TyCParser.While_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#while_stat}.
	 * @param ctx the parse tree
	 */
	void exitWhile_stat(TyCParser.While_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#for_stat}.
	 * @param ctx the parse tree
	 */
	void enterFor_stat(TyCParser.For_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#for_stat}.
	 * @param ctx the parse tree
	 */
	void exitFor_stat(TyCParser.For_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#for_init_stat}.
	 * @param ctx the parse tree
	 */
	void enterFor_init_stat(TyCParser.For_init_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#for_init_stat}.
	 * @param ctx the parse tree
	 */
	void exitFor_init_stat(TyCParser.For_init_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#for_cond_stat}.
	 * @param ctx the parse tree
	 */
	void enterFor_cond_stat(TyCParser.For_cond_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#for_cond_stat}.
	 * @param ctx the parse tree
	 */
	void exitFor_cond_stat(TyCParser.For_cond_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#for_update_stat}.
	 * @param ctx the parse tree
	 */
	void enterFor_update_stat(TyCParser.For_update_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#for_update_stat}.
	 * @param ctx the parse tree
	 */
	void exitFor_update_stat(TyCParser.For_update_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#switch_stat}.
	 * @param ctx the parse tree
	 */
	void enterSwitch_stat(TyCParser.Switch_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#switch_stat}.
	 * @param ctx the parse tree
	 */
	void exitSwitch_stat(TyCParser.Switch_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#case_expr_list}.
	 * @param ctx the parse tree
	 */
	void enterCase_expr_list(TyCParser.Case_expr_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#case_expr_list}.
	 * @param ctx the parse tree
	 */
	void exitCase_expr_list(TyCParser.Case_expr_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#case_expr}.
	 * @param ctx the parse tree
	 */
	void enterCase_expr(TyCParser.Case_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#case_expr}.
	 * @param ctx the parse tree
	 */
	void exitCase_expr(TyCParser.Case_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#default_case_expr}.
	 * @param ctx the parse tree
	 */
	void enterDefault_case_expr(TyCParser.Default_case_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#default_case_expr}.
	 * @param ctx the parse tree
	 */
	void exitDefault_case_expr(TyCParser.Default_case_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#break_stat}.
	 * @param ctx the parse tree
	 */
	void enterBreak_stat(TyCParser.Break_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#break_stat}.
	 * @param ctx the parse tree
	 */
	void exitBreak_stat(TyCParser.Break_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#continue_stat}.
	 * @param ctx the parse tree
	 */
	void enterContinue_stat(TyCParser.Continue_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#continue_stat}.
	 * @param ctx the parse tree
	 */
	void exitContinue_stat(TyCParser.Continue_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#return_stat}.
	 * @param ctx the parse tree
	 */
	void enterReturn_stat(TyCParser.Return_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#return_stat}.
	 * @param ctx the parse tree
	 */
	void exitReturn_stat(TyCParser.Return_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#expr_stat}.
	 * @param ctx the parse tree
	 */
	void enterExpr_stat(TyCParser.Expr_statContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#expr_stat}.
	 * @param ctx the parse tree
	 */
	void exitExpr_stat(TyCParser.Expr_statContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#lvalue}.
	 * @param ctx the parse tree
	 */
	void enterLvalue(TyCParser.LvalueContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#lvalue}.
	 * @param ctx the parse tree
	 */
	void exitLvalue(TyCParser.LvalueContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#expr_list}.
	 * @param ctx the parse tree
	 */
	void enterExpr_list(TyCParser.Expr_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#expr_list}.
	 * @param ctx the parse tree
	 */
	void exitExpr_list(TyCParser.Expr_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(TyCParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(TyCParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#assign_expr}.
	 * @param ctx the parse tree
	 */
	void enterAssign_expr(TyCParser.Assign_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#assign_expr}.
	 * @param ctx the parse tree
	 */
	void exitAssign_expr(TyCParser.Assign_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#assigned_expr}.
	 * @param ctx the parse tree
	 */
	void enterAssigned_expr(TyCParser.Assigned_exprContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#assigned_expr}.
	 * @param ctx the parse tree
	 */
	void exitAssigned_expr(TyCParser.Assigned_exprContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#arg_list}.
	 * @param ctx the parse tree
	 */
	void enterArg_list(TyCParser.Arg_listContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#arg_list}.
	 * @param ctx the parse tree
	 */
	void exitArg_list(TyCParser.Arg_listContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#arg}.
	 * @param ctx the parse tree
	 */
	void enterArg(TyCParser.ArgContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#arg}.
	 * @param ctx the parse tree
	 */
	void exitArg(TyCParser.ArgContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#un_op}.
	 * @param ctx the parse tree
	 */
	void enterUn_op(TyCParser.Un_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#un_op}.
	 * @param ctx the parse tree
	 */
	void exitUn_op(TyCParser.Un_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#pre_op}.
	 * @param ctx the parse tree
	 */
	void enterPre_op(TyCParser.Pre_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#pre_op}.
	 * @param ctx the parse tree
	 */
	void exitPre_op(TyCParser.Pre_opContext ctx);
	/**
	 * Enter a parse tree produced by {@link TyCParser#post_op}.
	 * @param ctx the parse tree
	 */
	void enterPost_op(TyCParser.Post_opContext ctx);
	/**
	 * Exit a parse tree produced by {@link TyCParser#post_op}.
	 * @param ctx the parse tree
	 */
	void exitPost_op(TyCParser.Post_opContext ctx);
}