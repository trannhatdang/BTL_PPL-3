"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser

###############Must Pass#################
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"

###############Empty#################

def test_empty_1():
    source = ""
    assert Parser(source).parse() == "success"

def test_empty_2():
    source = "void fun() {}"
    assert Parser(source).parse() == "success"

def test_empty_3():
    source = "struct strong {};"
    assert Parser(source).parse() == "success"

def test_empty_4():
    source = "struct strong;"
    assert Parser(source).parse() == "success"

def test_empty_err_1():
    source = "void fun() {;}"
    assert Parser(source).parse() == "Error on line 1 col 12: ;"

def test_empty_err_2():
    source = "void fun() {;;;;;;}"
    assert Parser(source).parse() == "Error on line 1 col 12: ;"

###############Comments#################

def test_comments_1():
    source = "//this is a comment"
    assert Parser(source).parse() == "success"

###############Functions#################

def test_func_1():
    source = "void fun() {} void main() { }"
    assert Parser(source).parse() == "success"

def test_func_2():
    source = "void fun() {} void main() { fun(); }"
    assert Parser(source).parse() == "success"

def test_func_3():
    source = "void _fun() {} void main() { _fun(); }"
    assert Parser(source).parse() == "success"

def test_func_4():
    source = "void _fun() { int c = 5; int b = 3; int a = b + c; int e = 3 * 5; return a;} void main() { int d = 3 *_fun(); }"
    assert Parser(source).parse() == "success"

def test_func_5():
    source = "void fn() { int c = 5; int b = 3; int a = b + c; int e = 3 * 5; return a;} void main() { int d = 3 *_fun(); }"
    assert Parser(source).parse() == "success"

def test_func_6():
    source = "void main() { fun(2, 5, fun(), 3 + 5, fun.mandy, fun.mandy + 4 * 21); }"
    assert Parser(source).parse() == "success"

def test_func_7():
    source = "void main() { fun(clock, ++3, 3++, f++, --g, g--, smearing_bunny); }"
    assert Parser(source).parse() == "success"

def test_func_8():
    source = "void fun() { return; }"
    assert Parser(source).parse() == "success"

def test_func_9():
    source = "void fun() { return x + y; }"
    assert Parser(source).parse() == "success"

def test_func_10():
    source = "void fun(int a, int b, float d, string g, Point p) { return x + y; }"
    assert Parser(source).parse() == "success"

def test_func_11():
    source = "void fun(float c, float d, string g, Point p) { return x + y; }"
    assert Parser(source).parse() == "success"

def test_func_12():
    source = "fun(int a, int b, float d, string g, Point p) { return x + y; }"
    assert Parser(source).parse() == "success"

def test_func_13():
    source = "fun(float b, float d, string g, Point p) { return; }"
    assert Parser(source).parse() == "success"

def test_func_14():
    source = "fun(Point a, float d, string g, Point p) { return x + y; }\n void main() {fun({a, b}, {c, d}, \"lmao\", {d, g});}"
    assert Parser(source).parse() == "success"

def test_func_15():
    source = "void main() {fun({{a, b, {c, d}}, d, {d, g}});}"
    assert Parser(source).parse() == "success"

def test_func_16():
    source = "_f_u63n(float b, float d, string g, Point p) { return; }"
    assert Parser(source).parse() == "success"

def test_func_err_1():
    source = "void main() { fun(four wheel drive); }"
    assert Parser(source).parse() == "Error on line 1 col 23: wheel"

def test_func_err_2():
    source = "void fun(struct a, auto b) { return x + y; }"
    assert Parser(source).parse() == "Error on line 1 col 9: struct"

def test_func_err_3():
    source = "void fun(int a, float b { return x + y; }"
    assert Parser(source).parse() == "Error on line 1 col 24: {"

def test_func_err_4():
    source = "void fun int a, float b) { return x + y; }"
    assert Parser(source).parse() == "Error on line 1 col 9: int"

def test_func_err_5():
    source = "void fun(int a float b) { return x + y; }"
    assert Parser(source).parse() == "Error on line 1 col 15: float"

def test_func_err_6():
    source = "void fun(int a, float b) { return x + y }"
    assert Parser(source).parse() == "Error on line 1 col 40: }"

def test_func_err_7():
    source = "void fun(int a, float b) { return x + y;"
    assert Parser(source).parse() == "Error on line 1 col 40: <EOF>"

def test_func_err_8():
    source = "void fun(int a, float b) return x + y; }"
    assert Parser(source).parse() == "Error on line 1 col 25: return"

def test_func_err_9():
    source = "69fun(int a, float b) { return x + y }"
    assert Parser(source).parse() == "Error on line 1 col 0: 69"

def test_func_err_10():
    source = "void fun(in t a, float b) { return x + y }"
    assert Parser(source).parse() == "Error on line 1 col 14: a"

def test_func_err_11():
    source = "void f_u_(sdg)n(int a, float b) { return x + y }"
    assert Parser(source).parse() == "Error on line 1 col 13: )"

def test_func_err_12():
    source = "void (f_u_(sdg)n)(int a, float b) { return x + y }"
    assert Parser(source).parse() == "Error on line 1 col 5: ("

def test_func_err_13():
    source = "void fun(int a, float b) { return return x + y }"
    assert Parser(source).parse() == "Error on line 1 col 34: return"

###############Structs#################

def test_struct_1():
    source = "struct Drive; struct Tribe; struct New; struct World;"
    assert Parser(source).parse() == "success"

def test_struct_2():
    source = "struct Drive; void main() { Drive drive; }"
    assert Parser(source).parse() == "success"

def test_struct_3():
    source = "struct Drive {int c; int b; };"
    assert Parser(source).parse() == "success"

def test_struct_4():
    source = "struct Drive { Drive b; string bugatti; };"
    assert Parser(source).parse() == "success"

def test_struct_5():
    source = "struct Drive { Drive b; string gatti; }; void main() { Drive drive = {{}, \"veyron\"};}"
    assert Parser(source).parse() == "success"

def test_struct_6():
    source = "struct Drive;"
    assert Parser(source).parse() == "success"

def test_struct_7():
    source = "struct Drive { int b; };"
    assert Parser(source).parse() == "success"

def test_struct_8():
    source = "struct Drive {Drive b; string gatti; }; void main() { Drive specials; }"
    assert Parser(source).parse() == "success"

def test_struct_9():
    source = "struct Drive {Drive b; string gatti; }; void main() { Drive oh_cock; }"
    assert Parser(source).parse() == "success"

def test_struct_10():
    source = "struct lmao {int a;int b;};"
    assert Parser(source).parse() == "success"

def test_struct_11():
    source = "void main() { lmao lm = {a, b}; }"
    assert Parser(source).parse() == "success"

def test_struct_12():
    source = "void main() { lm = {a, b}; }"
    assert Parser(source).parse() == "success"

def test_struct_12():
    source = "void main() { lm = {a(), b+c}; }"
    assert Parser(source).parse() == "success"

def test_struct_13():
    source = "void main() { lm = {_abc.ld, b+c()}; }"
    assert Parser(source).parse() == "success"

def test_struct_14():
    source = "void main() { lm = {_abc.ld, b+c(), {3, 5}}; }"
    assert Parser(source).parse() == "success"

def test_struct_15():
    source = "void main() { lm = {_abc.ld, b+c(), {3, 5}}; bernie bern = {{{{3}}}}; }"
    assert Parser(source).parse() == "success"

def test_struct_16():
    source = "void main() { lm = {_abc.ld, b+c(), {3, 5}}; bernie bern = {{{{3}}}; }"
    assert Parser(source).parse() == "Error on line 1 col 67: ;"

def test_struct_17():
    source = "void main() { int a = abc().d; }"
    assert Parser(source).parse() == "success"

def test_struct_err_1():
    source = "struct hammond { struct mandy {int a; int b; };};"
    assert Parser(source).parse() == "Error on line 1 col 17: struct"

def test_struct_err_2():
    source = "struct hammond { auto b;};"
    assert Parser(source).parse() == "Error on line 1 col 17: auto"

def test_struct_err_3():
    source = "struct hammond { auto a; int b};"
    assert Parser(source).parse() == "Error on line 1 col 17: auto"

def test_struct_err_4():
    source = "struct lmao {int a;int b;}"
    assert Parser(source).parse() == "Error on line 1 col 26: <EOF>"

def test_struct_err_5():
    source = "struct lmao = {int a;int b;};"
    assert Parser(source).parse() == "Error on line 1 col 12: ="

def test_struct_err_6():
    source = "struct (36) {int a;int b;};"
    assert Parser(source).parse() == "Error on line 1 col 7: ("

def test_struct_err_7():
    source = "struct lmao ({int a;int b;});"
    assert Parser(source).parse() == "Error on line 1 col 12: ("

def test_struct_err_8():
    source = "struct lmao {{int a;int b;}};"
    assert Parser(source).parse() == "Error on line 1 col 13: {"

def test_struct_err_9():
    source = "struct lmao {int a;int b; struct lmao {int a; int b;};};"
    assert Parser(source).parse() == "Error on line 1 col 26: struct"

def test_struct_err_10():
    source = "struct lmao {int a = 34;int b = g; Point p = {dsg};};"
    assert Parser(source).parse() == "Error on line 1 col 19: ="

def test_struct_err_11():
    source = "struct lmao {int (60)a;int 39b;};"
    assert Parser(source).parse() == "Error on line 1 col 17: ("

###############Block Statement#################
def test_block_statement_1():
    source = "void main() { {a = b + c;} }"
    assert Parser(source).parse() == "success"

def test_block_statement_2():
    source = "void main() { {int a; int b = fun(); int c = b * a + 3 - fun();} }"
    assert Parser(source).parse() == "success"

def test_block_statement_3():
    source = "void main() { { { { a = b + c; } } } }"
    assert Parser(source).parse() == "success"

def test_block_statement_4():
    source = "void main() { int a; fun(); { hammond(); int a = james(); } }"
    assert Parser(source).parse() == "success"

def test_block_statement_5():
    source = "void main() { int a; fun(); { hammond(); {james();} } }"
    assert Parser(source).parse() == "success"

def test_block_statement_err_1():
    source = "void main() { int a; fun(); { hammond(); {james();} }"
    assert Parser(source).parse() == "Error on line 1 col 53: <EOF>"

def test_block_statement_err_2():
    source = "void main() { int a; fun(); { hammond(); {{james();} }"
    assert Parser(source).parse() == "Error on line 1 col 54: <EOF>"

###############If Else#################
def test_if_1():
    source = "void main() {if(pong_tin) { lmao(); }}"
    assert Parser(source).parse() == "success"

def test_if_2():
    source = "void main() {if(pong_tin) lmao();}"
    assert Parser(source).parse() == "success"

def test_if_3():
    source = "void main() {if(pong_tin) { lmao(); } else { porsche(); } }"
    assert Parser(source).parse() == "success"

def test_if_4():
    source = "void main() {if(pong_tin) lmao(); else stone_henge();}"
    assert Parser(source).parse() == "success"

def test_if_5():
    source = "void main() {if(pong_tin) { lmao(); } else spot_of_lunch(); }"
    assert Parser(source).parse() == "success"

def test_if_6():
    source = "void main() {if(pong_tin && on_paper ) { lmao(); } else spot_of_lunch(); }"
    assert Parser(source).parse() == "success"

def test_if_7():
    source = "void main() {if(pong_tin && on_paper || (pretending * wahoo)) { lmao(); } else spot_of_lunch(); }"
    assert Parser(source).parse() == "success"

def test_if_8():
    source = "void main() {if(ahk || pong_tin && on_paper + 35 || (pretending * wahoo())) { lmao(); } else spot_of_lunch(); }"
    assert Parser(source).parse() == "success"

def test_if_9():
    source = "void main() {if(pong_tin) { lmao(); a = 3 + 7; int s = 35;} else if(lmao) {lmao(); lmao();} else peaked();}"
    assert Parser(source).parse() == "success"

def test_if_err_1():
    source = "void main() {if(pong_tin) { lmao(); }; else spot_of_lunch(); }"
    assert Parser(source).parse() == "Error on line 1 col 37: ;"

def test_if_err_2():
    source = "void main() {if(pong_tin) { lmao(); } else chips }"
    assert Parser(source).parse() == "Error on line 1 col 49: }"

def test_if_err_3():
    source = "void main() {if(pong_tin) { lmao(); } else { }"
    assert Parser(source).parse() == "Error on line 1 col 46: <EOF>"

def test_if_err_4():
    source = "void main() {if(pong_tin) { lmao(); } else; { }"
    assert Parser(source).parse() == "Error on line 1 col 42: ;"

def test_if_err_5():
    source = "void main() {if(pong_tin); { lmao(); } else;}"
    assert Parser(source).parse() == "Error on line 1 col 25: ;"

def test_if_err_6():
    source = "void main() {if(pong_tin); { lmao(); } else if;}"
    assert Parser(source).parse() == "Error on line 1 col 25: ;"

def test_if_err_7():
    source = "void main() {if }"
    assert Parser(source).parse() == "Error on line 1 col 16: }"

def test_if_err_8():
    source = "void main() {if {lmao(); }}"
    assert Parser(source).parse() == "Error on line 1 col 16: {"
    
def test_if_err_9():
    source = "void main() {if {lmao(); }}"
    assert Parser(source).parse() == "Error on line 1 col 16: {"

def test_if_err_10():
    source = "void main() {if(pong_tin) { lmao(); a = 3 + 7; int s = 35;} else;}"
    assert Parser(source).parse() == "Error on line 1 col 64: ;"
###############Variable Declarations#################
def test_while_1():
    source = "void main() {while(hammond) {boat();}}"
    assert Parser(source).parse() == "success"

def test_while_2():
    source = "void main() {while(hammond) boat();}"
    assert Parser(source).parse() == "success"

def test_while_3():
    source = "void main() {while(hammond) { boat(); a = b + c; box(); }}"
    assert Parser(source).parse() == "success"

def test_while_4():
    source = "void main() {while(hammond || propeller + c) { boat(); a = b + c; box(); }}"
    assert Parser(source).parse() == "success"

def test_while_5():
    source = "void main() {while(8 * hammond || propeller + c) { boat(); a = b + c; box(); }}"
    assert Parser(source).parse() == "success"

def test_while_6():
    source = "void main() {while(titianic(phone)) { boat(); a = b + c; box(); }}"
    assert Parser(source).parse() == "success"

def test_while_7():
    source = "void main() { while({3, 5}) { boat(); a = b + c; box();} }"
    assert Parser(source).parse() == "success"

def test_while_err_1():
    source = "void main() {while(titianic(phone)) { boat(); a = b + c; box(); }"
    assert Parser(source).parse() == "Error on line 1 col 65: <EOF>"

def test_while_err_2():
    source = "void main() {while(titianic(phone) { boat(); a = b + c; box();} }"
    assert Parser(source).parse() == "Error on line 1 col 35: {"

def test_while_err_3():
    source = "void main() {while titianic(phone) { boat(); a = b + c; box();} }"
    assert Parser(source).parse() == "Error on line 1 col 19: titianic"

def test_while_err_4():
    source = "void main() {while hone) { boat(); a = b + c; box();} }"
    assert Parser(source).parse() == "Error on line 1 col 19: hone"

def test_while_err_5():
    source = "void main() {while uk { boat(); a = b + c; box();} }"
    assert Parser(source).parse() == "Error on line 1 col 19: uk"

###############For Statement#################
def test_for_1():
    source = "void main() {for(int i = 0; i < 10; ++i) {korean_crane_carrier();}}"
    assert Parser(source).parse() == "success"

def test_for_2():
    source = "void main() {for(int i = 0; i < 10; ++i) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_3():
    source = "void main() {for(int i = 0; i < 10; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_4():
    source = "void main() {for(int i = 0; ; ++i) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_5():
    source = "void main() {for(int i = 0; ; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_6():
    source = "void main() {for(; i < 10; ++i) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_7():
    source = "void main() {for(; i < 10; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"
    
def test_for_8():
    source = "void main() {for(; ; ++i) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_9():
    source = "void main() {for(int i = 0; i < 10; i++) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_10():
    source = "void main() {for(int i = 0; i < 10; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_11():
    source = "void main() {for(int i = 0; ; i++) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_12():
    source = "void main() {for(int i = 0; ; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_13():
    source = "void main() {for(; i < 10; i++) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_14():
    source = "void main() {for(; i < 10; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_15():
    source = "void main() {for(; ; i++) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_16():
    source = "void main() {for(; ; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_17():
    source = "void main() {for(int i = 0; i < 10; --i) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_18():
    source = "void main() {for(int i = 0; i < 10; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_19():
    source = "void main() {for(int i = 0; ; --i) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_20():
    source = "void main() {for(int i = 0; ; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_21():
    source = "void main() {for(; i < 10; --i) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_22():
    source = "void main() {for(; i < 10; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_23():
    source = "void main() {for(; ; --i) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_24():
    source = "void main() {for(; ; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_25():
    source = "void main() {for(int i = 0; i < 10; i--) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_26():
    source = "void main() {for(int i = 0; i < 10; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_27():
    source = "void main() {for(int i = 0; ; i--) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_28():
    source = "void main() {for(int i = 0; ; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_29():
    source = "void main() {for(; i < 10; i--) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_30():
    source = "void main() {for(; i < 10; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"
    
def test_for_31():
    source = "void main() {for(; ; i--) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_32():
    source = "void main() {for(; ; ) korean_crane_carrier();}"
    assert Parser(source).parse() == "success"

def test_for_33():
    source = "void main() {for(int i = 0; i < 10; ++i) pete();}"
    assert Parser(source).parse() == "success"

def test_for_err_1():
    source = "void main() {for(int i = 0; i < 10; ++i) ;;;}"
    assert Parser(source).parse() == "Error on line 1 col 41: ;"

###############Variable Declarations#################
def test_var_decl_1():
    source = "void main() {int a; }"
    assert Parser(source).parse() == "success"

def test_var_decl_2():
    source = "void main() {int a; int b; int c; int d; int d; int e; int g; int b; }"
    assert Parser(source).parse() == "success"

def test_var_decl_3():
    source = "void main() {float b;}"
    assert Parser(source).parse() == "success"

def test_var_decl_4():
    source = "void main() {float b;float b;float b;float b;}"
    assert Parser(source).parse() == "success"

def test_var_decl_5():
    source = "void main() {string sdg;}"
    assert Parser(source).parse() == "success"

def test_var_decl_6():
    source = "void main() {string sdg;string sdg;string sdg;string sdg;}"
    assert Parser(source).parse() == "success"

def test_var_decl_7():
    source = "void main() {auto gs;}"
    assert Parser(source).parse() == "success"

def test_var_decl_8():
    source = "void main() {auto gs;auto gs;auto gs;auto gs;}"
    assert Parser(source).parse() == "success"

def test_var_decl_9():
    source = "void main() {int a = 4; int d = 24; float g = 3.5; string gt = \"sdgdg\"; auto hammond = \"porsche\";}"
    assert Parser(source).parse() == "success"

def test_var_decl_10():
    source = "void main() {int a = d; int d = bs; float g = tgt; string gt = sdgag; auto hammond = porsche;}"
    assert Parser(source).parse() == "success"

def test_var_decl_err_1():
    source = "void main() {int int a; }"
    assert Parser(source).parse() == "Error on line 1 col 17: int"

def test_var_decl_err_2():
    source = "void main() {auto int a; }"
    assert Parser(source).parse() == "Error on line 1 col 18: int"

def test_var_decl_err_3():
    source = "void main() {float float bs; }"
    assert Parser(source).parse() == "Error on line 1 col 19: float"


###############Expressions#################

def test_exp_1():
    source = "void main() { a = b + c; }"
    assert Parser(source).parse() == "success"

def test_exp_2():
    source = "void main() { a = b - c; }"
    assert Parser(source).parse() == "success"

def test_exp_3():
    source = "void main() { b = a * c; }"
    assert Parser(source).parse() == "success"

def test_exp_4():
    source = "void main() { a = b / c; }"
    assert Parser(source).parse() == "success"

def test_exp_5():
    source = "void main() { a = b % c; }"
    assert Parser(source).parse() == "success"

def test_exp_6():
    source = "void main() { a = b || c; }"
    assert Parser(source).parse() == "success"

def test_exp_7():
    source = "void main() { a = b && c; }"
    assert Parser(source).parse() == "success"

def test_exp_8():
    source = "void main() { a = b == c; }"
    assert Parser(source).parse() == "success"

def test_exp_9():
    source = "void main() { a = b != c; }"
    assert Parser(source).parse() == "success"

def test_exp_10():
    source = "void main() { a = b < c; }"
    assert Parser(source).parse() == "success"

def test_exp_11():
    source = "void main() { a = b <= c; }"
    assert Parser(source).parse() == "success"

def test_exp_12():
    source = "void main() { a = b > c; }"
    assert Parser(source).parse() == "success"
    
def test_exp_13():
    source = "void main() { a = b >= c; }"
    assert Parser(source).parse() == "success"

def test_exp_14():
    source = "void main() { a = !b; }"
    assert Parser(source).parse() == "success"

def test_exp_15():
    source = "void main() { a = -b; }"
    assert Parser(source).parse() == "success"

def test_exp_16():
    source = "void main() { a = +b; }"
    assert Parser(source).parse() == "success"

def test_exp_17():
    source = "void main() { a = ++b; }"
    assert Parser(source).parse() == "success"

def test_exp_18():
    source = "void main() { a = b++; }"
    assert Parser(source).parse() == "success"

def test_exp_19():
    source = "void main() { a = --b; }"
    assert Parser(source).parse() == "success"

def test_exp_20():
    source = "void main() { a = b--; }"
    assert Parser(source).parse() == "success"

def test_exp_21():
    source = "void main() { a = b(); }"
    assert Parser(source).parse() == "success"

def test_exp_22():
    source = "void main() { a = b.a; }"
    assert Parser(source).parse() == "success"

def test_exp_23():
    source = "void main() { a = (a + b); }"
    assert Parser(source).parse() == "success"

def test_exp_24():
    source = "void main() { a = (a + b) * c; }"
    assert Parser(source).parse() == "success"

def test_exp_25():
    source = "void main() { a = (a + b) * c / 5; }"
    assert Parser(source).parse() == "success"

def test_exp_26():
    source = "void main() { a = (a + (b - 3) / 5 % 20 * 10) * (c / 5); }"
    assert Parser(source).parse() == "success"

def test_exp_27():
    source = "void main() { a = (a + (b - 3) / 5 % 20 * 10) * (c / 5) * -25 + b++ * 25; }"
    assert Parser(source).parse() == "success"

def test_exp_28():
    source = "void main() { a = (a.b + (!b - 3) / 5 || 20 == 10) * (c / 5) * -25 + b++ * 25; }"
    assert Parser(source).parse() == "success"

def test_exp_29():
    source = "void main() { a = a || b && c;}"
    assert Parser(source).parse() == "success"

def test_exp_err_1():
    source = "void main() { a + b = c }"
    assert Parser(source).parse() == "Error on line 1 col 20: ="

def test_exp_err_2():
    source = "void main() { a + b + c = c }"
    assert Parser(source).parse() == "Error on line 1 col 24: ="

def test_exp_err_3():
    source = "void main() { ((a + b) = c }"
    assert Parser(source).parse() == "Error on line 1 col 23: ="

def test_exp_err_4():
    source = "void main() { (a + b)) = c }"
    assert Parser(source).parse() == "Error on line 1 col 21: )"

def test_exp_err_5():
    source = "void main() { a + (b || ) * c = c }"
    assert Parser(source).parse() == "Error on line 1 col 24: )"

def test_exp_err_6():
    source = "void main() { a +  }"
    assert Parser(source).parse() == "Error on line 1 col 19: }"

def test_exp_err_7():
    source = "void main() { a + b }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_8():
    source = "void main() { a + (b *) }"
    assert Parser(source).parse() == "Error on line 1 col 22: )"

def test_exp_err_9():
    source = "void main() { a *  }"
    assert Parser(source).parse() == "Error on line 1 col 19: }"

def test_exp_err_10():
    source = "void main() { a -  }"
    assert Parser(source).parse() == "Error on line 1 col 19: }"

def test_exp_err_11():
    source = "void main() { a -+  }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_12():
    source = "void main() { a +-  }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_13():
    source = "void main() { a +=  }"
    assert Parser(source).parse() == "Error on line 1 col 17: ="

def test_exp_err_14():
    source = "void main() { a =+  }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_15():
    source = "void main() { a /  }"
    assert Parser(source).parse() == "Error on line 1 col 19: }"

def test_exp_err_16():
    source = "void main() { a &&  }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_17():
    source = "void main() { a %  }"
    assert Parser(source).parse() == "Error on line 1 col 19: }"

def test_exp_err_18():
    source = "void main() { a <  }"
    assert Parser(source).parse() == "Error on line 1 col 19: }"

def test_exp_err_19():
    source = "void main() { a <=  }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_20():
    source = "void main() { a >  }"
    assert Parser(source).parse() == "Error on line 1 col 19: }"

def test_exp_err_21():
    source = "void main() { a >=  }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_22():
    source = "void main() { a.  }"
    assert Parser(source).parse() == "Error on line 1 col 18: }"

def test_exp_err_23():
    source = "void main() { a!   }"
    assert Parser(source).parse() == "Error on line 1 col 15: !"

def test_exp_err_24():
    source = "void main() { a ==  }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_25():
    source = "void main() { a !=  }"
    assert Parser(source).parse() == "Error on line 1 col 20: }"

def test_exp_err_26():
    source = "void main() { *a }"
    assert Parser(source).parse() == "Error on line 1 col 14: *"

def test_exp_err_27():
    source = "void main() { =a  }"
    assert Parser(source).parse() == "Error on line 1 col 14: ="

def test_exp_err_28():
    source = "void main() { /a  }"
    assert Parser(source).parse() == "Error on line 1 col 14: /"

def test_exp_err_29():
    source = "void main() { && a  }"
    assert Parser(source).parse() == "Error on line 1 col 14: &&"

def test_exp_err_30():
    source = "void main() { || a  }"
    assert Parser(source).parse() == "Error on line 1 col 14: ||"

def test_exp_err_31():
    source = "void main() { % a  }"
    assert Parser(source).parse() == "Error on line 1 col 14: %"

def test_exp_err_32():
    source = "void main() { < a }"
    assert Parser(source).parse() == "Error on line 1 col 14: <"

def test_exp_err_33():
    source = "void main() { <= a }"
    assert Parser(source).parse() == "Error on line 1 col 14: <="

def test_exp_err_34():
    source = "void main() { > a }"
    assert Parser(source).parse() == "Error on line 1 col 14: >"

def test_exp_err_35():
    source = "void main() { >= a  }"
    assert Parser(source).parse() == "Error on line 1 col 14: >="

def test_exp_err_36():
    source = "void main() { .a  }"
    assert Parser(source).parse() == "Error on line 1 col 14: ."

def test_exp_err_37():
    source = "void main() { == a   }"
    assert Parser(source).parse() == "Error on line 1 col 14: =="

def test_exp_err_38():
    source = "void main() { != a  }"
    assert Parser(source).parse() == "Error on line 1 col 14: !="
###############In Spec (Must Pass)#################

def test_spec_fun_decl_1():
    source = "int add(int x, int y) {\n return x + y;\n}"
    assert Parser(source).parse() == "success"

def test_spec_fun_decl_2():
    source = "void main() {\n auto result = add(3, 5); printInt(result);\n}"
    assert Parser(source).parse() == "success"

def test_spec_fun_decl_3():
    source = "add(int x, int y) {\n return x + y;\n}\n //Return type inferred as float\n multiply(float a, float b) {\n return a * b;\n}"
    assert Parser(source).parse() == "success"

def test_spec_fun_decl_4():
    source = "greet(string name) {\nprintString(\"Hello, \");printString(name);\n}\nvoid main() {\nauto sum = add(3, 5);\nauto product = multiply(2.5, 3.0);\ngreet(\"World\");\n}"
    assert Parser(source).parse() == "success"

def test_spec_lexical_struct_1():
    source = "/* This is a block comment, that\n may span in many lines*/ void main() {auto x = 5;// what the hell is this\n}"
    assert Parser(source).parse() == "success"

def test_spec_lexical_struct_2():
    source = "/* This is a block comment // has no meaning here */ //This is a line comment so /* has no meaning here"
    assert Parser(source).parse() == "success"

def test_spec_struct_1():
    source = "struct Empty {};"
    assert Parser(source).parse() == "success"

def test_spec_struct_2():
    source = "struct Point {int x; int y;};"
    assert Parser(source).parse() == "success"

def test_spec_truct_3():
    source = "struct Point {string name; int age; float height;};"
    assert Parser(source).parse() == "success"

def test_spec_truct_init():
    source = "void main() {Point p1; Point p2 = {10, 20}; Person person1; Person person2 = {\"John\", 25, 1.75};}"
    assert Parser(source).parse() == "success"

def test_spec_truct_mem_acc():
    source = "void main() {Point p = {10, 20}; p.x = 30; auto x_coord = p.x; printInt(p.x); p.x++;}"
    assert Parser(source).parse() == "success"

def test_spec_var_decl_1():
    source = "void main() {auto x = 10; auto y = 3.14; auto msg = \"hello\"; auto sum = x + y;}"
    assert Parser(source).parse() == "success"

def test_spec_var_decl_2():
    source = "void main() {auto a; a = 10; auto b; b = 3.14; auto c; c = readInt();}"
    assert Parser(source).parse() == "success"

def test_spec_var_decl_3():
    source = "void main() {int x = 10; float d = 3.14; string s = \"hello\"; int result = x+5;}"
    assert Parser(source).parse() == "success"

def test_spec_var_decl_4():
    source = "void main() {int e; float f; string t; e = 10; f = 3.14;}"
    assert Parser(source).parse() == "success"

def test_spec_block_stat_1():
    source = "void main() {{auto x = 10; auto y = 20; auto sum = x + y; printInt(sum);}}"
    assert Parser(source).parse() == "success"

def test_spec_if_stat():
    source = "void main() {if(flag) { printInt(1); } else {printInt(0);}}"
    assert Parser(source).parse() == "success"

def test_spec_while_stat():
    source = "void main() {auto i = 0; while (i < 10) {printInt(i); ++i;}}"
    assert Parser(source).parse() == "success"

def test_spec_for_stat():
    source = "void main() {for(auto i = 0; i < 10; ++i) {printInt(i);}}"
    assert Parser(source).parse() == "success"

def test_spec_switch_stat_1():
    source = "void main() {switch (day) { case 1: printInt(1); break; case 2: case 3: printInt(3); break; default: printInt(0);}}"
    assert Parser(source).parse() == "success"

def test_spec_switch_stat_2():
    source = "void main() {switch (day) { }}"
    assert Parser(source).parse() == "success"

def test_spec_switch_stat_3():
    source = "void main() {switch (day) { case 1 + 2: printInt(3); break; case (4): printInt(4); break; case +5: printInt(5); break; case -6: printInt(6); break; }}"
    assert Parser(source).parse() == "success"
