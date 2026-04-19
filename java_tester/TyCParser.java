// Generated from java_tester/TyC.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class TyCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		AUTO=1, BREAK=2, CASE=3, CONTINUE=4, DEFAULT=5, ELSE=6, FOR=7, IF=8, RETURN=9, 
		STRUCT=10, SWITCH=11, WHILE=12, INT_TYPE=13, FLOAT_TYPE=14, STRING_TYPE=15, 
		VOID_TYPE=16, ADD_OP=17, MIN_OP=18, MULT_OP=19, DIV_OP=20, MOD_OP=21, 
		EQ_OP=22, NEQ_OP=23, LESS_OP=24, GREAT_OP=25, LEQ_OP=26, GEQ_OP=27, OR_OP=28, 
		AND_OP=29, NOT_OP=30, INC_OP=31, DEC_OP=32, ASS_OP=33, MEMACC_OP=34, LROUND_BRACK=35, 
		RROUND_BRACK=36, LSQUARE_BRACK=37, RSQUARE_BRACK=38, LCURLY_BRACK=39, 
		RCURLY_BRACK=40, SEMICOLON=41, COMMA=42, COLON=43, ID=44, INT=45, FLOAT=46, 
		STRING=47, NEWLINE=48, WS=49, COMMENT=50, LINE_COMMENT=51, ILLEGAL_ESCAPE=52, 
		UNCLOSE_STRING=53, ERROR_CHAR=54;
	public static final int
		RULE_program = 0, RULE_prog_stat_list = 1, RULE_prog_stat = 2, RULE_func_decl = 3, 
		RULE_param_list = 4, RULE_param = 5, RULE_param_type = 6, RULE_return_type = 7, 
		RULE_struct_decl = 8, RULE_struct_var_decl_list = 9, RULE_struct_var_decl_stat = 10, 
		RULE_struct_var_type = 11, RULE_struct_lit = 12, RULE_stat_list = 13, 
		RULE_stat = 14, RULE_var_decl_list = 15, RULE_var_decl_stat = 16, RULE_var_decl_expr = 17, 
		RULE_var_type = 18, RULE_block_stat = 19, RULE_if_stat = 20, RULE_main_if_stat = 21, 
		RULE_else_if_stat = 22, RULE_while_stat = 23, RULE_for_stat = 24, RULE_for_init_stat = 25, 
		RULE_for_cond_stat = 26, RULE_for_update_stat = 27, RULE_switch_stat = 28, 
		RULE_case_expr_list = 29, RULE_case_expr = 30, RULE_default_case_expr = 31, 
		RULE_break_stat = 32, RULE_continue_stat = 33, RULE_return_stat = 34, 
		RULE_expr_stat = 35, RULE_lvalue = 36, RULE_expr_list = 37, RULE_expr = 38, 
		RULE_assign_expr = 39, RULE_assigned_expr = 40, RULE_arg_list = 41, RULE_arg = 42, 
		RULE_un_op = 43, RULE_pre_op = 44, RULE_post_op = 45;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "prog_stat_list", "prog_stat", "func_decl", "param_list", 
			"param", "param_type", "return_type", "struct_decl", "struct_var_decl_list", 
			"struct_var_decl_stat", "struct_var_type", "struct_lit", "stat_list", 
			"stat", "var_decl_list", "var_decl_stat", "var_decl_expr", "var_type", 
			"block_stat", "if_stat", "main_if_stat", "else_if_stat", "while_stat", 
			"for_stat", "for_init_stat", "for_cond_stat", "for_update_stat", "switch_stat", 
			"case_expr_list", "case_expr", "default_case_expr", "break_stat", "continue_stat", 
			"return_stat", "expr_stat", "lvalue", "expr_list", "expr", "assign_expr", 
			"assigned_expr", "arg_list", "arg", "un_op", "pre_op", "post_op"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'auto'", "'break'", "'case'", "'continue'", "'default'", "'else'", 
			"'for'", "'if'", "'return'", "'struct'", "'switch'", "'while'", "'int'", 
			"'float'", "'string'", "'void'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
			"'!='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", "'++'", 
			"'--'", "'='", "'.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", 
			"','", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", "FOR", 
			"IF", "RETURN", "STRUCT", "SWITCH", "WHILE", "INT_TYPE", "FLOAT_TYPE", 
			"STRING_TYPE", "VOID_TYPE", "ADD_OP", "MIN_OP", "MULT_OP", "DIV_OP", 
			"MOD_OP", "EQ_OP", "NEQ_OP", "LESS_OP", "GREAT_OP", "LEQ_OP", "GEQ_OP", 
			"OR_OP", "AND_OP", "NOT_OP", "INC_OP", "DEC_OP", "ASS_OP", "MEMACC_OP", 
			"LROUND_BRACK", "RROUND_BRACK", "LSQUARE_BRACK", "RSQUARE_BRACK", "LCURLY_BRACK", 
			"RCURLY_BRACK", "SEMICOLON", "COMMA", "COLON", "ID", "INT", "FLOAT", 
			"STRING", "NEWLINE", "WS", "COMMENT", "LINE_COMMENT", "ILLEGAL_ESCAPE", 
			"UNCLOSE_STRING", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "TyC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TyCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public Prog_stat_listContext prog_stat_list() {
			return getRuleContext(Prog_stat_listContext.class,0);
		}
		public TerminalNode EOF() { return getToken(TyCParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			prog_stat_list();
			setState(93);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Prog_stat_listContext extends ParserRuleContext {
		public Prog_statContext prog_stat() {
			return getRuleContext(Prog_statContext.class,0);
		}
		public Prog_stat_listContext prog_stat_list() {
			return getRuleContext(Prog_stat_listContext.class,0);
		}
		public Prog_stat_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog_stat_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterProg_stat_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitProg_stat_list(this);
		}
	}

	public final Prog_stat_listContext prog_stat_list() throws RecognitionException {
		Prog_stat_listContext _localctx = new Prog_stat_listContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_prog_stat_list);
		try {
			setState(99);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRUCT:
			case INT_TYPE:
			case FLOAT_TYPE:
			case STRING_TYPE:
			case VOID_TYPE:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(95);
				prog_stat();
				setState(96);
				prog_stat_list();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Prog_statContext extends ParserRuleContext {
		public Func_declContext func_decl() {
			return getRuleContext(Func_declContext.class,0);
		}
		public Struct_declContext struct_decl() {
			return getRuleContext(Struct_declContext.class,0);
		}
		public Prog_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterProg_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitProg_stat(this);
		}
	}

	public final Prog_statContext prog_stat() throws RecognitionException {
		Prog_statContext _localctx = new Prog_statContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_prog_stat);
		try {
			setState(103);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
			case FLOAT_TYPE:
			case STRING_TYPE:
			case VOID_TYPE:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(101);
				func_decl();
				}
				break;
			case STRUCT:
				enterOuterAlt(_localctx, 2);
				{
				setState(102);
				struct_decl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Func_declContext extends ParserRuleContext {
		public Return_typeContext return_type() {
			return getRuleContext(Return_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public TerminalNode LROUND_BRACK() { return getToken(TyCParser.LROUND_BRACK, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode RROUND_BRACK() { return getToken(TyCParser.RROUND_BRACK, 0); }
		public Block_statContext block_stat() {
			return getRuleContext(Block_statContext.class,0);
		}
		public Func_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterFunc_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitFunc_decl(this);
		}
	}

	public final Func_declContext func_decl() throws RecognitionException {
		Func_declContext _localctx = new Func_declContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_func_decl);
		try {
			setState(118);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(105);
				return_type();
				setState(106);
				match(ID);
				setState(107);
				match(LROUND_BRACK);
				setState(108);
				param_list();
				setState(109);
				match(RROUND_BRACK);
				setState(110);
				block_stat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(112);
				match(ID);
				setState(113);
				match(LROUND_BRACK);
				setState(114);
				param_list();
				setState(115);
				match(RROUND_BRACK);
				setState(116);
				block_stat();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Param_listContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(TyCParser.COMMA, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public Param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterParam_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitParam_list(this);
		}
	}

	public final Param_listContext param_list() throws RecognitionException {
		Param_listContext _localctx = new Param_listContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_param_list);
		try {
			setState(126);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				param();
				setState(121);
				match(COMMA);
				setState(122);
				param_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(124);
				param();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public Param_typeContext param_type() {
			return getRuleContext(Param_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitParam(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			param_type();
			setState(129);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Param_typeContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(TyCParser.INT_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(TyCParser.STRING_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(TyCParser.FLOAT_TYPE, 0); }
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public Param_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterParam_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitParam_type(this);
		}
	}

	public final Param_typeContext param_type() throws RecognitionException {
		Param_typeContext _localctx = new Param_typeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_param_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 17592186101760L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Return_typeContext extends ParserRuleContext {
		public Param_typeContext param_type() {
			return getRuleContext(Param_typeContext.class,0);
		}
		public TerminalNode VOID_TYPE() { return getToken(TyCParser.VOID_TYPE, 0); }
		public Return_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterReturn_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitReturn_type(this);
		}
	}

	public final Return_typeContext return_type() throws RecognitionException {
		Return_typeContext _localctx = new Return_typeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_return_type);
		try {
			setState(135);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
			case FLOAT_TYPE:
			case STRING_TYPE:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(133);
				param_type();
				}
				break;
			case VOID_TYPE:
				enterOuterAlt(_localctx, 2);
				{
				setState(134);
				match(VOID_TYPE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Struct_declContext extends ParserRuleContext {
		public TerminalNode STRUCT() { return getToken(TyCParser.STRUCT, 0); }
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(TyCParser.SEMICOLON, 0); }
		public TerminalNode LCURLY_BRACK() { return getToken(TyCParser.LCURLY_BRACK, 0); }
		public Struct_var_decl_listContext struct_var_decl_list() {
			return getRuleContext(Struct_var_decl_listContext.class,0);
		}
		public TerminalNode RCURLY_BRACK() { return getToken(TyCParser.RCURLY_BRACK, 0); }
		public Struct_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_decl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterStruct_decl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitStruct_decl(this);
		}
	}

	public final Struct_declContext struct_decl() throws RecognitionException {
		Struct_declContext _localctx = new Struct_declContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_struct_decl);
		try {
			setState(147);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				match(STRUCT);
				setState(138);
				match(ID);
				setState(139);
				match(SEMICOLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				match(STRUCT);
				setState(141);
				match(ID);
				setState(142);
				match(LCURLY_BRACK);
				setState(143);
				struct_var_decl_list();
				setState(144);
				match(RCURLY_BRACK);
				setState(145);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Struct_var_decl_listContext extends ParserRuleContext {
		public Struct_var_decl_statContext struct_var_decl_stat() {
			return getRuleContext(Struct_var_decl_statContext.class,0);
		}
		public Struct_var_decl_listContext struct_var_decl_list() {
			return getRuleContext(Struct_var_decl_listContext.class,0);
		}
		public Struct_var_decl_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_var_decl_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterStruct_var_decl_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitStruct_var_decl_list(this);
		}
	}

	public final Struct_var_decl_listContext struct_var_decl_list() throws RecognitionException {
		Struct_var_decl_listContext _localctx = new Struct_var_decl_listContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_struct_var_decl_list);
		try {
			setState(153);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_TYPE:
			case FLOAT_TYPE:
			case STRING_TYPE:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(149);
				struct_var_decl_stat();
				setState(150);
				struct_var_decl_list();
				}
				break;
			case RCURLY_BRACK:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Struct_var_decl_statContext extends ParserRuleContext {
		public Struct_var_typeContext struct_var_type() {
			return getRuleContext(Struct_var_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(TyCParser.SEMICOLON, 0); }
		public Struct_var_decl_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_var_decl_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterStruct_var_decl_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitStruct_var_decl_stat(this);
		}
	}

	public final Struct_var_decl_statContext struct_var_decl_stat() throws RecognitionException {
		Struct_var_decl_statContext _localctx = new Struct_var_decl_statContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_struct_var_decl_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			struct_var_type();
			setState(156);
			match(ID);
			setState(157);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Struct_var_typeContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(TyCParser.INT_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(TyCParser.STRING_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(TyCParser.FLOAT_TYPE, 0); }
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public Struct_var_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_var_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterStruct_var_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitStruct_var_type(this);
		}
	}

	public final Struct_var_typeContext struct_var_type() throws RecognitionException {
		Struct_var_typeContext _localctx = new Struct_var_typeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_struct_var_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(159);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 17592186101760L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Struct_litContext extends ParserRuleContext {
		public TerminalNode LCURLY_BRACK() { return getToken(TyCParser.LCURLY_BRACK, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public TerminalNode RCURLY_BRACK() { return getToken(TyCParser.RCURLY_BRACK, 0); }
		public Struct_litContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_struct_lit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterStruct_lit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitStruct_lit(this);
		}
	}

	public final Struct_litContext struct_lit() throws RecognitionException {
		Struct_litContext _localctx = new Struct_litContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_struct_lit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(LCURLY_BRACK);
			setState(162);
			expr_list();
			setState(163);
			match(RCURLY_BRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Stat_listContext extends ParserRuleContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public Stat_listContext stat_list() {
			return getRuleContext(Stat_listContext.class,0);
		}
		public Stat_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterStat_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitStat_list(this);
		}
	}

	public final Stat_listContext stat_list() throws RecognitionException {
		Stat_listContext _localctx = new Stat_listContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_stat_list);
		try {
			setState(169);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AUTO:
			case BREAK:
			case CONTINUE:
			case FOR:
			case IF:
			case RETURN:
			case SWITCH:
			case WHILE:
			case INT_TYPE:
			case FLOAT_TYPE:
			case STRING_TYPE:
			case ADD_OP:
			case MIN_OP:
			case NOT_OP:
			case INC_OP:
			case DEC_OP:
			case LROUND_BRACK:
			case LCURLY_BRACK:
			case ID:
			case INT:
			case FLOAT:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(165);
				stat();
				setState(166);
				stat_list();
				}
				break;
			case CASE:
			case DEFAULT:
			case RCURLY_BRACK:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public Var_decl_statContext var_decl_stat() {
			return getRuleContext(Var_decl_statContext.class,0);
		}
		public Block_statContext block_stat() {
			return getRuleContext(Block_statContext.class,0);
		}
		public If_statContext if_stat() {
			return getRuleContext(If_statContext.class,0);
		}
		public While_statContext while_stat() {
			return getRuleContext(While_statContext.class,0);
		}
		public For_statContext for_stat() {
			return getRuleContext(For_statContext.class,0);
		}
		public Switch_statContext switch_stat() {
			return getRuleContext(Switch_statContext.class,0);
		}
		public Break_statContext break_stat() {
			return getRuleContext(Break_statContext.class,0);
		}
		public Continue_statContext continue_stat() {
			return getRuleContext(Continue_statContext.class,0);
		}
		public Return_statContext return_stat() {
			return getRuleContext(Return_statContext.class,0);
		}
		public Expr_statContext expr_stat() {
			return getRuleContext(Expr_statContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitStat(this);
		}
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_stat);
		try {
			setState(181);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				var_decl_stat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(172);
				block_stat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(173);
				if_stat();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(174);
				while_stat();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(175);
				for_stat();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(176);
				switch_stat();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(177);
				break_stat();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(178);
				continue_stat();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(179);
				return_stat();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(180);
				expr_stat();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_decl_listContext extends ParserRuleContext {
		public Var_decl_statContext var_decl_stat() {
			return getRuleContext(Var_decl_statContext.class,0);
		}
		public Var_decl_listContext var_decl_list() {
			return getRuleContext(Var_decl_listContext.class,0);
		}
		public Var_decl_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterVar_decl_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitVar_decl_list(this);
		}
	}

	public final Var_decl_listContext var_decl_list() throws RecognitionException {
		Var_decl_listContext _localctx = new Var_decl_listContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_var_decl_list);
		try {
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				var_decl_stat();
				setState(184);
				var_decl_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_decl_statContext extends ParserRuleContext {
		public Var_decl_exprContext var_decl_expr() {
			return getRuleContext(Var_decl_exprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(TyCParser.SEMICOLON, 0); }
		public Var_decl_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterVar_decl_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitVar_decl_stat(this);
		}
	}

	public final Var_decl_statContext var_decl_stat() throws RecognitionException {
		Var_decl_statContext _localctx = new Var_decl_statContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_var_decl_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(189);
			var_decl_expr();
			setState(190);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_decl_exprContext extends ParserRuleContext {
		public Var_typeContext var_type() {
			return getRuleContext(Var_typeContext.class,0);
		}
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public TerminalNode ASS_OP() { return getToken(TyCParser.ASS_OP, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Var_decl_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_decl_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterVar_decl_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitVar_decl_expr(this);
		}
	}

	public final Var_decl_exprContext var_decl_expr() throws RecognitionException {
		Var_decl_exprContext _localctx = new Var_decl_exprContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_var_decl_expr);
		try {
			setState(200);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(192);
				var_type();
				setState(193);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(195);
				var_type();
				setState(196);
				match(ID);
				setState(197);
				match(ASS_OP);
				setState(198);
				expr(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Var_typeContext extends ParserRuleContext {
		public TerminalNode INT_TYPE() { return getToken(TyCParser.INT_TYPE, 0); }
		public TerminalNode STRING_TYPE() { return getToken(TyCParser.STRING_TYPE, 0); }
		public TerminalNode FLOAT_TYPE() { return getToken(TyCParser.FLOAT_TYPE, 0); }
		public TerminalNode AUTO() { return getToken(TyCParser.AUTO, 0); }
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public Var_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterVar_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitVar_type(this);
		}
	}

	public final Var_typeContext var_type() throws RecognitionException {
		Var_typeContext _localctx = new Var_typeContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_var_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 17592186101762L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Block_statContext extends ParserRuleContext {
		public TerminalNode LCURLY_BRACK() { return getToken(TyCParser.LCURLY_BRACK, 0); }
		public Stat_listContext stat_list() {
			return getRuleContext(Stat_listContext.class,0);
		}
		public TerminalNode RCURLY_BRACK() { return getToken(TyCParser.RCURLY_BRACK, 0); }
		public Block_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterBlock_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitBlock_stat(this);
		}
	}

	public final Block_statContext block_stat() throws RecognitionException {
		Block_statContext _localctx = new Block_statContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_block_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			match(LCURLY_BRACK);
			setState(205);
			stat_list();
			setState(206);
			match(RCURLY_BRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class If_statContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(TyCParser.IF, 0); }
		public TerminalNode LROUND_BRACK() { return getToken(TyCParser.LROUND_BRACK, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RROUND_BRACK() { return getToken(TyCParser.RROUND_BRACK, 0); }
		public Main_if_statContext main_if_stat() {
			return getRuleContext(Main_if_statContext.class,0);
		}
		public TerminalNode ELSE() { return getToken(TyCParser.ELSE, 0); }
		public Else_if_statContext else_if_stat() {
			return getRuleContext(Else_if_statContext.class,0);
		}
		public If_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterIf_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitIf_stat(this);
		}
	}

	public final If_statContext if_stat() throws RecognitionException {
		If_statContext _localctx = new If_statContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_if_stat);
		try {
			setState(222);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(208);
				match(IF);
				setState(209);
				match(LROUND_BRACK);
				setState(210);
				expr(0);
				setState(211);
				match(RROUND_BRACK);
				setState(212);
				main_if_stat();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(214);
				match(IF);
				setState(215);
				match(LROUND_BRACK);
				setState(216);
				expr(0);
				setState(217);
				match(RROUND_BRACK);
				setState(218);
				main_if_stat();
				setState(219);
				match(ELSE);
				setState(220);
				else_if_stat();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Main_if_statContext extends ParserRuleContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public Main_if_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main_if_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterMain_if_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitMain_if_stat(this);
		}
	}

	public final Main_if_statContext main_if_stat() throws RecognitionException {
		Main_if_statContext _localctx = new Main_if_statContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_main_if_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			stat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Else_if_statContext extends ParserRuleContext {
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public Else_if_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_if_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterElse_if_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitElse_if_stat(this);
		}
	}

	public final Else_if_statContext else_if_stat() throws RecognitionException {
		Else_if_statContext _localctx = new Else_if_statContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_else_if_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			stat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class While_statContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(TyCParser.WHILE, 0); }
		public TerminalNode LROUND_BRACK() { return getToken(TyCParser.LROUND_BRACK, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RROUND_BRACK() { return getToken(TyCParser.RROUND_BRACK, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public While_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterWhile_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitWhile_stat(this);
		}
	}

	public final While_statContext while_stat() throws RecognitionException {
		While_statContext _localctx = new While_statContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_while_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(WHILE);
			setState(229);
			match(LROUND_BRACK);
			setState(230);
			expr(0);
			setState(231);
			match(RROUND_BRACK);
			setState(232);
			stat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_statContext extends ParserRuleContext {
		public TerminalNode FOR() { return getToken(TyCParser.FOR, 0); }
		public TerminalNode LROUND_BRACK() { return getToken(TyCParser.LROUND_BRACK, 0); }
		public For_init_statContext for_init_stat() {
			return getRuleContext(For_init_statContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(TyCParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(TyCParser.SEMICOLON, i);
		}
		public For_cond_statContext for_cond_stat() {
			return getRuleContext(For_cond_statContext.class,0);
		}
		public For_update_statContext for_update_stat() {
			return getRuleContext(For_update_statContext.class,0);
		}
		public TerminalNode RROUND_BRACK() { return getToken(TyCParser.RROUND_BRACK, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public For_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterFor_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitFor_stat(this);
		}
	}

	public final For_statContext for_stat() throws RecognitionException {
		For_statContext _localctx = new For_statContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_for_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			match(FOR);
			setState(235);
			match(LROUND_BRACK);
			setState(236);
			for_init_stat();
			setState(237);
			match(SEMICOLON);
			setState(238);
			for_cond_stat();
			setState(239);
			match(SEMICOLON);
			setState(240);
			for_update_stat();
			setState(241);
			match(RROUND_BRACK);
			setState(242);
			stat();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_init_statContext extends ParserRuleContext {
		public Var_decl_exprContext var_decl_expr() {
			return getRuleContext(Var_decl_exprContext.class,0);
		}
		public Expr_statContext expr_stat() {
			return getRuleContext(Expr_statContext.class,0);
		}
		public For_init_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_init_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterFor_init_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitFor_init_stat(this);
		}
	}

	public final For_init_statContext for_init_stat() throws RecognitionException {
		For_init_statContext _localctx = new For_init_statContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_for_init_stat);
		try {
			setState(247);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(244);
				var_decl_expr();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(245);
				expr_stat();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_cond_statContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public For_cond_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_cond_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterFor_cond_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitFor_cond_stat(this);
		}
	}

	public final For_cond_statContext for_cond_stat() throws RecognitionException {
		For_cond_statContext _localctx = new For_cond_statContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_for_cond_stat);
		try {
			setState(251);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD_OP:
			case MIN_OP:
			case NOT_OP:
			case INC_OP:
			case DEC_OP:
			case LROUND_BRACK:
			case LCURLY_BRACK:
			case ID:
			case INT:
			case FLOAT:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(249);
				expr(0);
				}
				break;
			case SEMICOLON:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class For_update_statContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public For_update_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_update_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterFor_update_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitFor_update_stat(this);
		}
	}

	public final For_update_statContext for_update_stat() throws RecognitionException {
		For_update_statContext _localctx = new For_update_statContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_for_update_stat);
		try {
			setState(255);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ADD_OP:
			case MIN_OP:
			case NOT_OP:
			case INC_OP:
			case DEC_OP:
			case LROUND_BRACK:
			case LCURLY_BRACK:
			case ID:
			case INT:
			case FLOAT:
			case STRING:
				enterOuterAlt(_localctx, 1);
				{
				setState(253);
				expr(0);
				}
				break;
			case RROUND_BRACK:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Switch_statContext extends ParserRuleContext {
		public TerminalNode SWITCH() { return getToken(TyCParser.SWITCH, 0); }
		public TerminalNode LROUND_BRACK() { return getToken(TyCParser.LROUND_BRACK, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RROUND_BRACK() { return getToken(TyCParser.RROUND_BRACK, 0); }
		public TerminalNode LCURLY_BRACK() { return getToken(TyCParser.LCURLY_BRACK, 0); }
		public Case_expr_listContext case_expr_list() {
			return getRuleContext(Case_expr_listContext.class,0);
		}
		public Default_case_exprContext default_case_expr() {
			return getRuleContext(Default_case_exprContext.class,0);
		}
		public TerminalNode RCURLY_BRACK() { return getToken(TyCParser.RCURLY_BRACK, 0); }
		public Switch_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switch_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterSwitch_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitSwitch_stat(this);
		}
	}

	public final Switch_statContext switch_stat() throws RecognitionException {
		Switch_statContext _localctx = new Switch_statContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_switch_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(SWITCH);
			setState(258);
			match(LROUND_BRACK);
			setState(259);
			expr(0);
			setState(260);
			match(RROUND_BRACK);
			setState(261);
			match(LCURLY_BRACK);
			setState(262);
			case_expr_list();
			setState(263);
			default_case_expr();
			setState(264);
			match(RCURLY_BRACK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Case_expr_listContext extends ParserRuleContext {
		public Case_exprContext case_expr() {
			return getRuleContext(Case_exprContext.class,0);
		}
		public Case_expr_listContext case_expr_list() {
			return getRuleContext(Case_expr_listContext.class,0);
		}
		public Case_expr_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case_expr_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterCase_expr_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitCase_expr_list(this);
		}
	}

	public final Case_expr_listContext case_expr_list() throws RecognitionException {
		Case_expr_listContext _localctx = new Case_expr_listContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_case_expr_list);
		try {
			setState(270);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CASE:
				enterOuterAlt(_localctx, 1);
				{
				setState(266);
				case_expr();
				setState(267);
				case_expr_list();
				}
				break;
			case DEFAULT:
			case RCURLY_BRACK:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Case_exprContext extends ParserRuleContext {
		public TerminalNode CASE() { return getToken(TyCParser.CASE, 0); }
		public TerminalNode LROUND_BRACK() { return getToken(TyCParser.LROUND_BRACK, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RROUND_BRACK() { return getToken(TyCParser.RROUND_BRACK, 0); }
		public TerminalNode COLON() { return getToken(TyCParser.COLON, 0); }
		public Stat_listContext stat_list() {
			return getRuleContext(Stat_listContext.class,0);
		}
		public Case_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_case_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterCase_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitCase_expr(this);
		}
	}

	public final Case_exprContext case_expr() throws RecognitionException {
		Case_exprContext _localctx = new Case_exprContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_case_expr);
		try {
			setState(284);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(272);
				match(CASE);
				setState(273);
				match(LROUND_BRACK);
				setState(274);
				expr(0);
				setState(275);
				match(RROUND_BRACK);
				setState(276);
				match(COLON);
				setState(277);
				stat_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(279);
				match(CASE);
				setState(280);
				expr(0);
				setState(281);
				match(COLON);
				setState(282);
				stat_list();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Default_case_exprContext extends ParserRuleContext {
		public TerminalNode DEFAULT() { return getToken(TyCParser.DEFAULT, 0); }
		public TerminalNode COLON() { return getToken(TyCParser.COLON, 0); }
		public Stat_listContext stat_list() {
			return getRuleContext(Stat_listContext.class,0);
		}
		public Default_case_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_default_case_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterDefault_case_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitDefault_case_expr(this);
		}
	}

	public final Default_case_exprContext default_case_expr() throws RecognitionException {
		Default_case_exprContext _localctx = new Default_case_exprContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_default_case_expr);
		try {
			setState(290);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DEFAULT:
				enterOuterAlt(_localctx, 1);
				{
				setState(286);
				match(DEFAULT);
				setState(287);
				match(COLON);
				setState(288);
				stat_list();
				}
				break;
			case RCURLY_BRACK:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Break_statContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(TyCParser.BREAK, 0); }
		public TerminalNode SEMICOLON() { return getToken(TyCParser.SEMICOLON, 0); }
		public Break_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterBreak_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitBreak_stat(this);
		}
	}

	public final Break_statContext break_stat() throws RecognitionException {
		Break_statContext _localctx = new Break_statContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_break_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(292);
			match(BREAK);
			setState(293);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Continue_statContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(TyCParser.CONTINUE, 0); }
		public TerminalNode SEMICOLON() { return getToken(TyCParser.SEMICOLON, 0); }
		public Continue_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterContinue_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitContinue_stat(this);
		}
	}

	public final Continue_statContext continue_stat() throws RecognitionException {
		Continue_statContext _localctx = new Continue_statContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_continue_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(295);
			match(CONTINUE);
			setState(296);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Return_statContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(TyCParser.RETURN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(TyCParser.SEMICOLON, 0); }
		public Return_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterReturn_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitReturn_stat(this);
		}
	}

	public final Return_statContext return_stat() throws RecognitionException {
		Return_statContext _localctx = new Return_statContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_return_stat);
		try {
			setState(304);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(298);
				match(RETURN);
				setState(299);
				expr(0);
				setState(300);
				match(SEMICOLON);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(302);
				match(RETURN);
				setState(303);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_statContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(TyCParser.SEMICOLON, 0); }
		public Expr_statContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterExpr_stat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitExpr_stat(this);
		}
	}

	public final Expr_statContext expr_stat() throws RecognitionException {
		Expr_statContext _localctx = new Expr_statContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_expr_stat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(306);
			expr(0);
			setState(307);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LvalueContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public TerminalNode INT() { return getToken(TyCParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(TyCParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(TyCParser.STRING, 0); }
		public Struct_litContext struct_lit() {
			return getRuleContext(Struct_litContext.class,0);
		}
		public LvalueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lvalue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterLvalue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitLvalue(this);
		}
	}

	public final LvalueContext lvalue() throws RecognitionException {
		LvalueContext _localctx = new LvalueContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_lvalue);
		try {
			setState(314);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(309);
				match(ID);
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(310);
				match(INT);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 3);
				{
				setState(311);
				match(FLOAT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(312);
				match(STRING);
				}
				break;
			case LCURLY_BRACK:
				enterOuterAlt(_localctx, 5);
				{
				setState(313);
				struct_lit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr_listContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(TyCParser.COMMA, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Expr_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterExpr_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitExpr_list(this);
		}
	}

	public final Expr_listContext expr_list() throws RecognitionException {
		Expr_listContext _localctx = new Expr_listContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_expr_list);
		try {
			setState(322);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(316);
				expr(0);
				setState(317);
				match(COMMA);
				setState(318);
				expr_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(320);
				expr(0);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode LROUND_BRACK() { return getToken(TyCParser.LROUND_BRACK, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RROUND_BRACK() { return getToken(TyCParser.RROUND_BRACK, 0); }
		public LvalueContext lvalue() {
			return getRuleContext(LvalueContext.class,0);
		}
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public Arg_listContext arg_list() {
			return getRuleContext(Arg_listContext.class,0);
		}
		public Pre_opContext pre_op() {
			return getRuleContext(Pre_opContext.class,0);
		}
		public Un_opContext un_op() {
			return getRuleContext(Un_opContext.class,0);
		}
		public TerminalNode MULT_OP() { return getToken(TyCParser.MULT_OP, 0); }
		public TerminalNode DIV_OP() { return getToken(TyCParser.DIV_OP, 0); }
		public TerminalNode MOD_OP() { return getToken(TyCParser.MOD_OP, 0); }
		public TerminalNode ADD_OP() { return getToken(TyCParser.ADD_OP, 0); }
		public TerminalNode MIN_OP() { return getToken(TyCParser.MIN_OP, 0); }
		public TerminalNode LESS_OP() { return getToken(TyCParser.LESS_OP, 0); }
		public TerminalNode LEQ_OP() { return getToken(TyCParser.LEQ_OP, 0); }
		public TerminalNode GREAT_OP() { return getToken(TyCParser.GREAT_OP, 0); }
		public TerminalNode GEQ_OP() { return getToken(TyCParser.GEQ_OP, 0); }
		public TerminalNode EQ_OP() { return getToken(TyCParser.EQ_OP, 0); }
		public TerminalNode NEQ_OP() { return getToken(TyCParser.NEQ_OP, 0); }
		public TerminalNode AND_OP() { return getToken(TyCParser.AND_OP, 0); }
		public TerminalNode OR_OP() { return getToken(TyCParser.OR_OP, 0); }
		public TerminalNode ASS_OP() { return getToken(TyCParser.ASS_OP, 0); }
		public TerminalNode MEMACC_OP() { return getToken(TyCParser.MEMACC_OP, 0); }
		public Post_opContext post_op() {
			return getRuleContext(Post_opContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 76;
		enterRecursionRule(_localctx, 76, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(341);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(325);
				match(LROUND_BRACK);
				setState(326);
				expr(0);
				setState(327);
				match(RROUND_BRACK);
				}
				break;
			case 2:
				{
				setState(329);
				lvalue();
				}
				break;
			case 3:
				{
				setState(330);
				match(ID);
				setState(331);
				match(LROUND_BRACK);
				setState(332);
				arg_list();
				setState(333);
				match(RROUND_BRACK);
				}
				break;
			case 4:
				{
				setState(335);
				pre_op();
				setState(336);
				expr(9);
				}
				break;
			case 5:
				{
				setState(338);
				un_op();
				setState(339);
				expr(8);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(371);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(369);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(343);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(344);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(345);
						expr(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(346);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(347);
						_la = _input.LA(1);
						if ( !(_la==ADD_OP || _la==MIN_OP) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(348);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(349);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(350);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 251658240L) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(351);
						expr(6);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(352);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(353);
						_la = _input.LA(1);
						if ( !(_la==EQ_OP || _la==NEQ_OP) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(354);
						expr(5);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(355);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						{
						setState(356);
						match(AND_OP);
						}
						setState(357);
						expr(4);
						}
						break;
					case 6:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(358);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						{
						setState(359);
						match(OR_OP);
						}
						setState(360);
						expr(3);
						}
						break;
					case 7:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(361);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(362);
						match(ASS_OP);
						setState(363);
						expr(1);
						}
						break;
					case 8:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(364);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(365);
						match(MEMACC_OP);
						setState(366);
						match(ID);
						}
						break;
					case 9:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(367);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(368);
						post_op();
						}
						break;
					}
					} 
				}
				setState(373);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assign_exprContext extends ParserRuleContext {
		public TerminalNode ASS_OP() { return getToken(TyCParser.ASS_OP, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ID() { return getToken(TyCParser.ID, 0); }
		public Assigned_exprContext assigned_expr() {
			return getRuleContext(Assigned_exprContext.class,0);
		}
		public TerminalNode MEMACC_OP() { return getToken(TyCParser.MEMACC_OP, 0); }
		public Assign_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterAssign_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitAssign_expr(this);
		}
	}

	public final Assign_exprContext assign_expr() throws RecognitionException {
		Assign_exprContext _localctx = new Assign_exprContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_assign_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(379);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(374);
				match(ID);
				}
				break;
			case 2:
				{
				setState(375);
				assigned_expr();
				setState(376);
				match(MEMACC_OP);
				setState(377);
				match(ID);
				}
				break;
			}
			setState(381);
			match(ASS_OP);
			setState(382);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Assigned_exprContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Assigned_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assigned_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterAssigned_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitAssigned_expr(this);
		}
	}

	public final Assigned_exprContext assigned_expr() throws RecognitionException {
		Assigned_exprContext _localctx = new Assigned_exprContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_assigned_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Arg_listContext extends ParserRuleContext {
		public ArgContext arg() {
			return getRuleContext(ArgContext.class,0);
		}
		public TerminalNode COMMA() { return getToken(TyCParser.COMMA, 0); }
		public Arg_listContext arg_list() {
			return getRuleContext(Arg_listContext.class,0);
		}
		public Arg_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterArg_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitArg_list(this);
		}
	}

	public final Arg_listContext arg_list() throws RecognitionException {
		Arg_listContext _localctx = new Arg_listContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_arg_list);
		try {
			setState(392);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,25,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(386);
				arg();
				setState(387);
				match(COMMA);
				setState(388);
				arg_list();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(390);
				arg();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ArgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterArg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitArg(this);
		}
	}

	public final ArgContext arg() throws RecognitionException {
		ArgContext _localctx = new ArgContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_arg);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(394);
			expr(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Un_opContext extends ParserRuleContext {
		public TerminalNode NOT_OP() { return getToken(TyCParser.NOT_OP, 0); }
		public TerminalNode MIN_OP() { return getToken(TyCParser.MIN_OP, 0); }
		public TerminalNode ADD_OP() { return getToken(TyCParser.ADD_OP, 0); }
		public Un_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_un_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterUn_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitUn_op(this);
		}
	}

	public final Un_opContext un_op() throws RecognitionException {
		Un_opContext _localctx = new Un_opContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_un_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(396);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1074135040L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Pre_opContext extends ParserRuleContext {
		public TerminalNode INC_OP() { return getToken(TyCParser.INC_OP, 0); }
		public TerminalNode DEC_OP() { return getToken(TyCParser.DEC_OP, 0); }
		public Pre_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pre_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterPre_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitPre_op(this);
		}
	}

	public final Pre_opContext pre_op() throws RecognitionException {
		Pre_opContext _localctx = new Pre_opContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_pre_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(398);
			_la = _input.LA(1);
			if ( !(_la==INC_OP || _la==DEC_OP) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Post_opContext extends ParserRuleContext {
		public TerminalNode INC_OP() { return getToken(TyCParser.INC_OP, 0); }
		public TerminalNode DEC_OP() { return getToken(TyCParser.DEC_OP, 0); }
		public Post_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_post_op; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).enterPost_op(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TyCListener ) ((TyCListener)listener).exitPost_op(this);
		}
	}

	public final Post_opContext post_op() throws RecognitionException {
		Post_opContext _localctx = new Post_opContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_post_op);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(400);
			_la = _input.LA(1);
			if ( !(_la==INC_OP || _la==DEC_OP) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 38:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		case 3:
			return precpred(_ctx, 4);
		case 4:
			return precpred(_ctx, 3);
		case 5:
			return precpred(_ctx, 2);
		case 6:
			return precpred(_ctx, 1);
		case 7:
			return precpred(_ctx, 11);
		case 8:
			return precpred(_ctx, 10);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00016\u0193\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007,\u0002"+
		"-\u0007-\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0003\u0001d\b\u0001\u0001\u0002\u0001\u0002\u0003"+
		"\u0002h\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u0003w\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u007f"+
		"\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0003\u0007\u0088\b\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u0094\b\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0003\t\u009a\b\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0003\r\u00aa\b\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0001\u000e\u0003\u000e\u00b6\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0003\u000f\u00bc\b\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0003\u0011\u00c9\b\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0003\u0014\u00df\b\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016"+
		"\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u0019\u0003\u0019\u00f8\b\u0019\u0001\u001a\u0001\u001a\u0003\u001a"+
		"\u00fc\b\u001a\u0001\u001b\u0001\u001b\u0003\u001b\u0100\b\u001b\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001"+
		"\u001d\u0003\u001d\u010f\b\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u011d\b\u001e\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0003\u001f\u0123\b\u001f\u0001 \u0001"+
		" \u0001 \u0001!\u0001!\u0001!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\""+
		"\u0001\"\u0003\"\u0131\b\"\u0001#\u0001#\u0001#\u0001$\u0001$\u0001$\u0001"+
		"$\u0001$\u0003$\u013b\b$\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0003"+
		"%\u0143\b%\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001"+
		"&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0003&\u0156"+
		"\b&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001"+
		"&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001"+
		"&\u0001&\u0001&\u0001&\u0001&\u0001&\u0001&\u0005&\u0172\b&\n&\f&\u0175"+
		"\t&\u0001\'\u0001\'\u0001\'\u0001\'\u0001\'\u0003\'\u017c\b\'\u0001\'"+
		"\u0001\'\u0001\'\u0001(\u0001(\u0001)\u0001)\u0001)\u0001)\u0001)\u0001"+
		")\u0003)\u0189\b)\u0001*\u0001*\u0001+\u0001+\u0001,\u0001,\u0001-\u0001"+
		"-\u0001-\u0000\u0001L.\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\u0000"+
		"\b\u0002\u0000\r\u000f,,\u0003\u0000\u0001\u0001\r\u000f,,\u0001\u0000"+
		"\u0013\u0015\u0001\u0000\u0011\u0012\u0001\u0000\u0018\u001b\u0001\u0000"+
		"\u0016\u0017\u0002\u0000\u0011\u0012\u001e\u001e\u0001\u0000\u001f \u0197"+
		"\u0000\\\u0001\u0000\u0000\u0000\u0002c\u0001\u0000\u0000\u0000\u0004"+
		"g\u0001\u0000\u0000\u0000\u0006v\u0001\u0000\u0000\u0000\b~\u0001\u0000"+
		"\u0000\u0000\n\u0080\u0001\u0000\u0000\u0000\f\u0083\u0001\u0000\u0000"+
		"\u0000\u000e\u0087\u0001\u0000\u0000\u0000\u0010\u0093\u0001\u0000\u0000"+
		"\u0000\u0012\u0099\u0001\u0000\u0000\u0000\u0014\u009b\u0001\u0000\u0000"+
		"\u0000\u0016\u009f\u0001\u0000\u0000\u0000\u0018\u00a1\u0001\u0000\u0000"+
		"\u0000\u001a\u00a9\u0001\u0000\u0000\u0000\u001c\u00b5\u0001\u0000\u0000"+
		"\u0000\u001e\u00bb\u0001\u0000\u0000\u0000 \u00bd\u0001\u0000\u0000\u0000"+
		"\"\u00c8\u0001\u0000\u0000\u0000$\u00ca\u0001\u0000\u0000\u0000&\u00cc"+
		"\u0001\u0000\u0000\u0000(\u00de\u0001\u0000\u0000\u0000*\u00e0\u0001\u0000"+
		"\u0000\u0000,\u00e2\u0001\u0000\u0000\u0000.\u00e4\u0001\u0000\u0000\u0000"+
		"0\u00ea\u0001\u0000\u0000\u00002\u00f7\u0001\u0000\u0000\u00004\u00fb"+
		"\u0001\u0000\u0000\u00006\u00ff\u0001\u0000\u0000\u00008\u0101\u0001\u0000"+
		"\u0000\u0000:\u010e\u0001\u0000\u0000\u0000<\u011c\u0001\u0000\u0000\u0000"+
		">\u0122\u0001\u0000\u0000\u0000@\u0124\u0001\u0000\u0000\u0000B\u0127"+
		"\u0001\u0000\u0000\u0000D\u0130\u0001\u0000\u0000\u0000F\u0132\u0001\u0000"+
		"\u0000\u0000H\u013a\u0001\u0000\u0000\u0000J\u0142\u0001\u0000\u0000\u0000"+
		"L\u0155\u0001\u0000\u0000\u0000N\u017b\u0001\u0000\u0000\u0000P\u0180"+
		"\u0001\u0000\u0000\u0000R\u0188\u0001\u0000\u0000\u0000T\u018a\u0001\u0000"+
		"\u0000\u0000V\u018c\u0001\u0000\u0000\u0000X\u018e\u0001\u0000\u0000\u0000"+
		"Z\u0190\u0001\u0000\u0000\u0000\\]\u0003\u0002\u0001\u0000]^\u0005\u0000"+
		"\u0000\u0001^\u0001\u0001\u0000\u0000\u0000_`\u0003\u0004\u0002\u0000"+
		"`a\u0003\u0002\u0001\u0000ad\u0001\u0000\u0000\u0000bd\u0001\u0000\u0000"+
		"\u0000c_\u0001\u0000\u0000\u0000cb\u0001\u0000\u0000\u0000d\u0003\u0001"+
		"\u0000\u0000\u0000eh\u0003\u0006\u0003\u0000fh\u0003\u0010\b\u0000ge\u0001"+
		"\u0000\u0000\u0000gf\u0001\u0000\u0000\u0000h\u0005\u0001\u0000\u0000"+
		"\u0000ij\u0003\u000e\u0007\u0000jk\u0005,\u0000\u0000kl\u0005#\u0000\u0000"+
		"lm\u0003\b\u0004\u0000mn\u0005$\u0000\u0000no\u0003&\u0013\u0000ow\u0001"+
		"\u0000\u0000\u0000pq\u0005,\u0000\u0000qr\u0005#\u0000\u0000rs\u0003\b"+
		"\u0004\u0000st\u0005$\u0000\u0000tu\u0003&\u0013\u0000uw\u0001\u0000\u0000"+
		"\u0000vi\u0001\u0000\u0000\u0000vp\u0001\u0000\u0000\u0000w\u0007\u0001"+
		"\u0000\u0000\u0000xy\u0003\n\u0005\u0000yz\u0005*\u0000\u0000z{\u0003"+
		"\b\u0004\u0000{\u007f\u0001\u0000\u0000\u0000|\u007f\u0003\n\u0005\u0000"+
		"}\u007f\u0001\u0000\u0000\u0000~x\u0001\u0000\u0000\u0000~|\u0001\u0000"+
		"\u0000\u0000~}\u0001\u0000\u0000\u0000\u007f\t\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0003\f\u0006\u0000\u0081\u0082\u0005,\u0000\u0000\u0082"+
		"\u000b\u0001\u0000\u0000\u0000\u0083\u0084\u0007\u0000\u0000\u0000\u0084"+
		"\r\u0001\u0000\u0000\u0000\u0085\u0088\u0003\f\u0006\u0000\u0086\u0088"+
		"\u0005\u0010\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0086"+
		"\u0001\u0000\u0000\u0000\u0088\u000f\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0005\n\u0000\u0000\u008a\u008b\u0005,\u0000\u0000\u008b\u0094\u0005"+
		")\u0000\u0000\u008c\u008d\u0005\n\u0000\u0000\u008d\u008e\u0005,\u0000"+
		"\u0000\u008e\u008f\u0005\'\u0000\u0000\u008f\u0090\u0003\u0012\t\u0000"+
		"\u0090\u0091\u0005(\u0000\u0000\u0091\u0092\u0005)\u0000\u0000\u0092\u0094"+
		"\u0001\u0000\u0000\u0000\u0093\u0089\u0001\u0000\u0000\u0000\u0093\u008c"+
		"\u0001\u0000\u0000\u0000\u0094\u0011\u0001\u0000\u0000\u0000\u0095\u0096"+
		"\u0003\u0014\n\u0000\u0096\u0097\u0003\u0012\t\u0000\u0097\u009a\u0001"+
		"\u0000\u0000\u0000\u0098\u009a\u0001\u0000\u0000\u0000\u0099\u0095\u0001"+
		"\u0000\u0000\u0000\u0099\u0098\u0001\u0000\u0000\u0000\u009a\u0013\u0001"+
		"\u0000\u0000\u0000\u009b\u009c\u0003\u0016\u000b\u0000\u009c\u009d\u0005"+
		",\u0000\u0000\u009d\u009e\u0005)\u0000\u0000\u009e\u0015\u0001\u0000\u0000"+
		"\u0000\u009f\u00a0\u0007\u0000\u0000\u0000\u00a0\u0017\u0001\u0000\u0000"+
		"\u0000\u00a1\u00a2\u0005\'\u0000\u0000\u00a2\u00a3\u0003J%\u0000\u00a3"+
		"\u00a4\u0005(\u0000\u0000\u00a4\u0019\u0001\u0000\u0000\u0000\u00a5\u00a6"+
		"\u0003\u001c\u000e\u0000\u00a6\u00a7\u0003\u001a\r\u0000\u00a7\u00aa\u0001"+
		"\u0000\u0000\u0000\u00a8\u00aa\u0001\u0000\u0000\u0000\u00a9\u00a5\u0001"+
		"\u0000\u0000\u0000\u00a9\u00a8\u0001\u0000\u0000\u0000\u00aa\u001b\u0001"+
		"\u0000\u0000\u0000\u00ab\u00b6\u0003 \u0010\u0000\u00ac\u00b6\u0003&\u0013"+
		"\u0000\u00ad\u00b6\u0003(\u0014\u0000\u00ae\u00b6\u0003.\u0017\u0000\u00af"+
		"\u00b6\u00030\u0018\u0000\u00b0\u00b6\u00038\u001c\u0000\u00b1\u00b6\u0003"+
		"@ \u0000\u00b2\u00b6\u0003B!\u0000\u00b3\u00b6\u0003D\"\u0000\u00b4\u00b6"+
		"\u0003F#\u0000\u00b5\u00ab\u0001\u0000\u0000\u0000\u00b5\u00ac\u0001\u0000"+
		"\u0000\u0000\u00b5\u00ad\u0001\u0000\u0000\u0000\u00b5\u00ae\u0001\u0000"+
		"\u0000\u0000\u00b5\u00af\u0001\u0000\u0000\u0000\u00b5\u00b0\u0001\u0000"+
		"\u0000\u0000\u00b5\u00b1\u0001\u0000\u0000\u0000\u00b5\u00b2\u0001\u0000"+
		"\u0000\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b5\u00b4\u0001\u0000"+
		"\u0000\u0000\u00b6\u001d\u0001\u0000\u0000\u0000\u00b7\u00b8\u0003 \u0010"+
		"\u0000\u00b8\u00b9\u0003\u001e\u000f\u0000\u00b9\u00bc\u0001\u0000\u0000"+
		"\u0000\u00ba\u00bc\u0001\u0000\u0000\u0000\u00bb\u00b7\u0001\u0000\u0000"+
		"\u0000\u00bb\u00ba\u0001\u0000\u0000\u0000\u00bc\u001f\u0001\u0000\u0000"+
		"\u0000\u00bd\u00be\u0003\"\u0011\u0000\u00be\u00bf\u0005)\u0000\u0000"+
		"\u00bf!\u0001\u0000\u0000\u0000\u00c0\u00c1\u0003$\u0012\u0000\u00c1\u00c2"+
		"\u0005,\u0000\u0000\u00c2\u00c9\u0001\u0000\u0000\u0000\u00c3\u00c4\u0003"+
		"$\u0012\u0000\u00c4\u00c5\u0005,\u0000\u0000\u00c5\u00c6\u0005!\u0000"+
		"\u0000\u00c6\u00c7\u0003L&\u0000\u00c7\u00c9\u0001\u0000\u0000\u0000\u00c8"+
		"\u00c0\u0001\u0000\u0000\u0000\u00c8\u00c3\u0001\u0000\u0000\u0000\u00c9"+
		"#\u0001\u0000\u0000\u0000\u00ca\u00cb\u0007\u0001\u0000\u0000\u00cb%\u0001"+
		"\u0000\u0000\u0000\u00cc\u00cd\u0005\'\u0000\u0000\u00cd\u00ce\u0003\u001a"+
		"\r\u0000\u00ce\u00cf\u0005(\u0000\u0000\u00cf\'\u0001\u0000\u0000\u0000"+
		"\u00d0\u00d1\u0005\b\u0000\u0000\u00d1\u00d2\u0005#\u0000\u0000\u00d2"+
		"\u00d3\u0003L&\u0000\u00d3\u00d4\u0005$\u0000\u0000\u00d4\u00d5\u0003"+
		"*\u0015\u0000\u00d5\u00df\u0001\u0000\u0000\u0000\u00d6\u00d7\u0005\b"+
		"\u0000\u0000\u00d7\u00d8\u0005#\u0000\u0000\u00d8\u00d9\u0003L&\u0000"+
		"\u00d9\u00da\u0005$\u0000\u0000\u00da\u00db\u0003*\u0015\u0000\u00db\u00dc"+
		"\u0005\u0006\u0000\u0000\u00dc\u00dd\u0003,\u0016\u0000\u00dd\u00df\u0001"+
		"\u0000\u0000\u0000\u00de\u00d0\u0001\u0000\u0000\u0000\u00de\u00d6\u0001"+
		"\u0000\u0000\u0000\u00df)\u0001\u0000\u0000\u0000\u00e0\u00e1\u0003\u001c"+
		"\u000e\u0000\u00e1+\u0001\u0000\u0000\u0000\u00e2\u00e3\u0003\u001c\u000e"+
		"\u0000\u00e3-\u0001\u0000\u0000\u0000\u00e4\u00e5\u0005\f\u0000\u0000"+
		"\u00e5\u00e6\u0005#\u0000\u0000\u00e6\u00e7\u0003L&\u0000\u00e7\u00e8"+
		"\u0005$\u0000\u0000\u00e8\u00e9\u0003\u001c\u000e\u0000\u00e9/\u0001\u0000"+
		"\u0000\u0000\u00ea\u00eb\u0005\u0007\u0000\u0000\u00eb\u00ec\u0005#\u0000"+
		"\u0000\u00ec\u00ed\u00032\u0019\u0000\u00ed\u00ee\u0005)\u0000\u0000\u00ee"+
		"\u00ef\u00034\u001a\u0000\u00ef\u00f0\u0005)\u0000\u0000\u00f0\u00f1\u0003"+
		"6\u001b\u0000\u00f1\u00f2\u0005$\u0000\u0000\u00f2\u00f3\u0003\u001c\u000e"+
		"\u0000\u00f31\u0001\u0000\u0000\u0000\u00f4\u00f8\u0003\"\u0011\u0000"+
		"\u00f5\u00f8\u0003F#\u0000\u00f6\u00f8\u0001\u0000\u0000\u0000\u00f7\u00f4"+
		"\u0001\u0000\u0000\u0000\u00f7\u00f5\u0001\u0000\u0000\u0000\u00f7\u00f6"+
		"\u0001\u0000\u0000\u0000\u00f83\u0001\u0000\u0000\u0000\u00f9\u00fc\u0003"+
		"L&\u0000\u00fa\u00fc\u0001\u0000\u0000\u0000\u00fb\u00f9\u0001\u0000\u0000"+
		"\u0000\u00fb\u00fa\u0001\u0000\u0000\u0000\u00fc5\u0001\u0000\u0000\u0000"+
		"\u00fd\u0100\u0003L&\u0000\u00fe\u0100\u0001\u0000\u0000\u0000\u00ff\u00fd"+
		"\u0001\u0000\u0000\u0000\u00ff\u00fe\u0001\u0000\u0000\u0000\u01007\u0001"+
		"\u0000\u0000\u0000\u0101\u0102\u0005\u000b\u0000\u0000\u0102\u0103\u0005"+
		"#\u0000\u0000\u0103\u0104\u0003L&\u0000\u0104\u0105\u0005$\u0000\u0000"+
		"\u0105\u0106\u0005\'\u0000\u0000\u0106\u0107\u0003:\u001d\u0000\u0107"+
		"\u0108\u0003>\u001f\u0000\u0108\u0109\u0005(\u0000\u0000\u01099\u0001"+
		"\u0000\u0000\u0000\u010a\u010b\u0003<\u001e\u0000\u010b\u010c\u0003:\u001d"+
		"\u0000\u010c\u010f\u0001\u0000\u0000\u0000\u010d\u010f\u0001\u0000\u0000"+
		"\u0000\u010e\u010a\u0001\u0000\u0000\u0000\u010e\u010d\u0001\u0000\u0000"+
		"\u0000\u010f;\u0001\u0000\u0000\u0000\u0110\u0111\u0005\u0003\u0000\u0000"+
		"\u0111\u0112\u0005#\u0000\u0000\u0112\u0113\u0003L&\u0000\u0113\u0114"+
		"\u0005$\u0000\u0000\u0114\u0115\u0005+\u0000\u0000\u0115\u0116\u0003\u001a"+
		"\r\u0000\u0116\u011d\u0001\u0000\u0000\u0000\u0117\u0118\u0005\u0003\u0000"+
		"\u0000\u0118\u0119\u0003L&\u0000\u0119\u011a\u0005+\u0000\u0000\u011a"+
		"\u011b\u0003\u001a\r\u0000\u011b\u011d\u0001\u0000\u0000\u0000\u011c\u0110"+
		"\u0001\u0000\u0000\u0000\u011c\u0117\u0001\u0000\u0000\u0000\u011d=\u0001"+
		"\u0000\u0000\u0000\u011e\u011f\u0005\u0005\u0000\u0000\u011f\u0120\u0005"+
		"+\u0000\u0000\u0120\u0123\u0003\u001a\r\u0000\u0121\u0123\u0001\u0000"+
		"\u0000\u0000\u0122\u011e\u0001\u0000\u0000\u0000\u0122\u0121\u0001\u0000"+
		"\u0000\u0000\u0123?\u0001\u0000\u0000\u0000\u0124\u0125\u0005\u0002\u0000"+
		"\u0000\u0125\u0126\u0005)\u0000\u0000\u0126A\u0001\u0000\u0000\u0000\u0127"+
		"\u0128\u0005\u0004\u0000\u0000\u0128\u0129\u0005)\u0000\u0000\u0129C\u0001"+
		"\u0000\u0000\u0000\u012a\u012b\u0005\t\u0000\u0000\u012b\u012c\u0003L"+
		"&\u0000\u012c\u012d\u0005)\u0000\u0000\u012d\u0131\u0001\u0000\u0000\u0000"+
		"\u012e\u012f\u0005\t\u0000\u0000\u012f\u0131\u0005)\u0000\u0000\u0130"+
		"\u012a\u0001\u0000\u0000\u0000\u0130\u012e\u0001\u0000\u0000\u0000\u0131"+
		"E\u0001\u0000\u0000\u0000\u0132\u0133\u0003L&\u0000\u0133\u0134\u0005"+
		")\u0000\u0000\u0134G\u0001\u0000\u0000\u0000\u0135\u013b\u0005,\u0000"+
		"\u0000\u0136\u013b\u0005-\u0000\u0000\u0137\u013b\u0005.\u0000\u0000\u0138"+
		"\u013b\u0005/\u0000\u0000\u0139\u013b\u0003\u0018\f\u0000\u013a\u0135"+
		"\u0001\u0000\u0000\u0000\u013a\u0136\u0001\u0000\u0000\u0000\u013a\u0137"+
		"\u0001\u0000\u0000\u0000\u013a\u0138\u0001\u0000\u0000\u0000\u013a\u0139"+
		"\u0001\u0000\u0000\u0000\u013bI\u0001\u0000\u0000\u0000\u013c\u013d\u0003"+
		"L&\u0000\u013d\u013e\u0005*\u0000\u0000\u013e\u013f\u0003J%\u0000\u013f"+
		"\u0143\u0001\u0000\u0000\u0000\u0140\u0143\u0003L&\u0000\u0141\u0143\u0001"+
		"\u0000\u0000\u0000\u0142\u013c\u0001\u0000\u0000\u0000\u0142\u0140\u0001"+
		"\u0000\u0000\u0000\u0142\u0141\u0001\u0000\u0000\u0000\u0143K\u0001\u0000"+
		"\u0000\u0000\u0144\u0145\u0006&\uffff\uffff\u0000\u0145\u0146\u0005#\u0000"+
		"\u0000\u0146\u0147\u0003L&\u0000\u0147\u0148\u0005$\u0000\u0000\u0148"+
		"\u0156\u0001\u0000\u0000\u0000\u0149\u0156\u0003H$\u0000\u014a\u014b\u0005"+
		",\u0000\u0000\u014b\u014c\u0005#\u0000\u0000\u014c\u014d\u0003R)\u0000"+
		"\u014d\u014e\u0005$\u0000\u0000\u014e\u0156\u0001\u0000\u0000\u0000\u014f"+
		"\u0150\u0003X,\u0000\u0150\u0151\u0003L&\t\u0151\u0156\u0001\u0000\u0000"+
		"\u0000\u0152\u0153\u0003V+\u0000\u0153\u0154\u0003L&\b\u0154\u0156\u0001"+
		"\u0000\u0000\u0000\u0155\u0144\u0001\u0000\u0000\u0000\u0155\u0149\u0001"+
		"\u0000\u0000\u0000\u0155\u014a\u0001\u0000\u0000\u0000\u0155\u014f\u0001"+
		"\u0000\u0000\u0000\u0155\u0152\u0001\u0000\u0000\u0000\u0156\u0173\u0001"+
		"\u0000\u0000\u0000\u0157\u0158\n\u0007\u0000\u0000\u0158\u0159\u0007\u0002"+
		"\u0000\u0000\u0159\u0172\u0003L&\b\u015a\u015b\n\u0006\u0000\u0000\u015b"+
		"\u015c\u0007\u0003\u0000\u0000\u015c\u0172\u0003L&\u0007\u015d\u015e\n"+
		"\u0005\u0000\u0000\u015e\u015f\u0007\u0004\u0000\u0000\u015f\u0172\u0003"+
		"L&\u0006\u0160\u0161\n\u0004\u0000\u0000\u0161\u0162\u0007\u0005\u0000"+
		"\u0000\u0162\u0172\u0003L&\u0005\u0163\u0164\n\u0003\u0000\u0000\u0164"+
		"\u0165\u0005\u001d\u0000\u0000\u0165\u0172\u0003L&\u0004\u0166\u0167\n"+
		"\u0002\u0000\u0000\u0167\u0168\u0005\u001c\u0000\u0000\u0168\u0172\u0003"+
		"L&\u0003\u0169\u016a\n\u0001\u0000\u0000\u016a\u016b\u0005!\u0000\u0000"+
		"\u016b\u0172\u0003L&\u0001\u016c\u016d\n\u000b\u0000\u0000\u016d\u016e"+
		"\u0005\"\u0000\u0000\u016e\u0172\u0005,\u0000\u0000\u016f\u0170\n\n\u0000"+
		"\u0000\u0170\u0172\u0003Z-\u0000\u0171\u0157\u0001\u0000\u0000\u0000\u0171"+
		"\u015a\u0001\u0000\u0000\u0000\u0171\u015d\u0001\u0000\u0000\u0000\u0171"+
		"\u0160\u0001\u0000\u0000\u0000\u0171\u0163\u0001\u0000\u0000\u0000\u0171"+
		"\u0166\u0001\u0000\u0000\u0000\u0171\u0169\u0001\u0000\u0000\u0000\u0171"+
		"\u016c\u0001\u0000\u0000\u0000\u0171\u016f\u0001\u0000\u0000\u0000\u0172"+
		"\u0175\u0001\u0000\u0000\u0000\u0173\u0171\u0001\u0000\u0000\u0000\u0173"+
		"\u0174\u0001\u0000\u0000\u0000\u0174M\u0001\u0000\u0000\u0000\u0175\u0173"+
		"\u0001\u0000\u0000\u0000\u0176\u017c\u0005,\u0000\u0000\u0177\u0178\u0003"+
		"P(\u0000\u0178\u0179\u0005\"\u0000\u0000\u0179\u017a\u0005,\u0000\u0000"+
		"\u017a\u017c\u0001\u0000\u0000\u0000\u017b\u0176\u0001\u0000\u0000\u0000"+
		"\u017b\u0177\u0001\u0000\u0000\u0000\u017c\u017d\u0001\u0000\u0000\u0000"+
		"\u017d\u017e\u0005!\u0000\u0000\u017e\u017f\u0003L&\u0000\u017fO\u0001"+
		"\u0000\u0000\u0000\u0180\u0181\u0003L&\u0000\u0181Q\u0001\u0000\u0000"+
		"\u0000\u0182\u0183\u0003T*\u0000\u0183\u0184\u0005*\u0000\u0000\u0184"+
		"\u0185\u0003R)\u0000\u0185\u0189\u0001\u0000\u0000\u0000\u0186\u0189\u0003"+
		"T*\u0000\u0187\u0189\u0001\u0000\u0000\u0000\u0188\u0182\u0001\u0000\u0000"+
		"\u0000\u0188\u0186\u0001\u0000\u0000\u0000\u0188\u0187\u0001\u0000\u0000"+
		"\u0000\u0189S\u0001\u0000\u0000\u0000\u018a\u018b\u0003L&\u0000\u018b"+
		"U\u0001\u0000\u0000\u0000\u018c\u018d\u0007\u0006\u0000\u0000\u018dW\u0001"+
		"\u0000\u0000\u0000\u018e\u018f\u0007\u0007\u0000\u0000\u018fY\u0001\u0000"+
		"\u0000\u0000\u0190\u0191\u0007\u0007\u0000\u0000\u0191[\u0001\u0000\u0000"+
		"\u0000\u001acgv~\u0087\u0093\u0099\u00a9\u00b5\u00bb\u00c8\u00de\u00f7"+
		"\u00fb\u00ff\u010e\u011c\u0122\u0130\u013a\u0142\u0155\u0171\u0173\u017b"+
		"\u0188";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}