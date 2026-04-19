"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator


def test_ast_gen_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = """void main() {
}"""
    expected = "Program([FuncDecl(VoidType(), main, [], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_placeholder_1():
    source = """
        struct Point {
            int x;
            int y;
        };
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_placeholder_2():
    source = """
        int add(int x, int y) {
            return x + y;
        }
    """
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), x), Param(IntType(), y)], [ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_placeholder_3():
    source = """
        add(int x, int y) {
            return x + y;
        }
    """
    expected = "Program([FuncDecl(auto, add, [Param(IntType(), x), Param(IntType(), y)], [ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_gen_placeholder_4():
    source = """
        void main() {
            auto x = 10;
        }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, x = IntLiteral(10))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_1():
    source = "void main() { a = b + c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_2():
    source = "void main() { a = b - c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), -, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_3():
    source = "void main() { b = a * c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(b) = BinaryOp(Identifier(a), *, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_4():
    source = "void main() { a = b / c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), /, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_5():
    source = "void main() { a = b % c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), %, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_6():
    source = "void main() { a = b || c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), ||, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_7():
    source = "void main() { a = b && c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), &&, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_8():
    source = "void main() { a = b == c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), ==, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_9():
    source = "void main() { a = b != c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), !=, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_10():
    source = "void main() { a = b < c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), <, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_11():
    source = "void main() { a = b <= c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), <=, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_12():
    source = "void main() { a = b > c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), >, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_13():
    source = "void main() { a = b >= c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), >=, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_14():
    source = "void main() { a = !b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = PrefixOp(!Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_15():
    source = "void main() { a = -b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = PrefixOp(-Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_16():
    source = "void main() { a = +b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = PrefixOp(+Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_17():
    source = "void main() { a = ++b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = PrefixOp(++Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_18():
    source = "void main() { a = b++; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = PostfixOp(Identifier(b)++)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_19():
    source = "void main() { a = --b; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = PrefixOp(--Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_20():
    source = "void main() { a = b--; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = PostfixOp(Identifier(b)--)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_21():
    source = "void main() { a = b(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = FuncCall(b, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_22():
    source = "void main() { a = b.a; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = MemberAccess(Identifier(b).a)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_23():
    source = "void main() { a = (a + b); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), +, Identifier(b))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_24():
    source = "void main() { a = (a + b) * c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_25():
    source = "void main() { a = (a + b) * c / 5; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c)), /, IntLiteral(5))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_26():
    source = "void main() { a = (a + (b - 3) / 5 % 20 * 10) * (c / 5); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(b), -, IntLiteral(3)), /, IntLiteral(5)), %, IntLiteral(20)), *, IntLiteral(10))), *, BinaryOp(Identifier(c), /, IntLiteral(5)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_27():
    source = "void main() { a = (a + (b - 3) / 5 % 20 * 10) * (c / 5) * -25 + b++ * 25; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(b), -, IntLiteral(3)), /, IntLiteral(5)), %, IntLiteral(20)), *, IntLiteral(10))), *, BinaryOp(Identifier(c), /, IntLiteral(5))), *, IntLiteral(-25)), +, BinaryOp(PostfixOp(Identifier(b)++), *, IntLiteral(25)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_28():
    source = "void main() { a = (a.b + (!b - 3) / 5 || 20 == 10) * (c / 5) * -25 + b++ * 25; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(BinaryOp(BinaryOp(MemberAccess(Identifier(a).b), +, BinaryOp(BinaryOp(PrefixOp(!Identifier(b)), -, IntLiteral(3)), /, IntLiteral(5))), ||, BinaryOp(IntLiteral(20), ==, IntLiteral(10))), *, BinaryOp(Identifier(c), /, IntLiteral(5))), *, IntLiteral(-25)), +, BinaryOp(PostfixOp(Identifier(b)++), *, IntLiteral(25)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_29():
    source = "void main() { a = a || b && c;}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), ||, BinaryOp(Identifier(b), &&, Identifier(c)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_30():
    source = "void fun() {} void main() { a = f() * (3 * 3); }"
    expected = "Program([FuncDecl(VoidType(), fun, [], []), FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(f, []), *, BinaryOp(IntLiteral(3), *, IntLiteral(3)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_31():
    source = "void fun() {} void main() { a = (f() + 3) * 3; }"
    expected = "Program([FuncDecl(VoidType(), fun, [], []), FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(FuncCall(f, []), +, IntLiteral(3)), *, IntLiteral(3))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_32():
    source = "void fun() {} void main() { a = f() + 3 * 3; }"
    expected = "Program([FuncDecl(VoidType(), fun, [], []), FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(FuncCall(f, []), +, BinaryOp(IntLiteral(3), *, IntLiteral(3)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_1():
    source = "void fun() {} void main() { fun(); }"
    expected = "Program([FuncDecl(VoidType(), fun, [], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(fun, []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_2():
    source = "void _fun() {} void main() { _fun(); }"
    expected = "Program([FuncDecl(VoidType(), _fun, [], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(_fun, []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_3():
    source = "void _fun() { int c = 5; int b = 3; int a = b + c; int e = 3 * 5; return a;} void main() { int d = 3 *_fun(); }"
    expected = "Program([FuncDecl(VoidType(), _fun, [], [VarDecl(IntType(), c = IntLiteral(5)), VarDecl(IntType(), b = IntLiteral(3)), VarDecl(IntType(), a = BinaryOp(Identifier(b), +, Identifier(c))), VarDecl(IntType(), e = BinaryOp(IntLiteral(3), *, IntLiteral(5))), ReturnStmt(return Identifier(a))]), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), d = BinaryOp(IntLiteral(3), *, FuncCall(_fun, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_4():
    source = "void fn() { int c = 5; int b = 3; int a = b + c; int e = 3 * 5; return a;} void main() { int d = 3 *_fun(); }"
    expected = "Program([FuncDecl(VoidType(), fn, [], [VarDecl(IntType(), c = IntLiteral(5)), VarDecl(IntType(), b = IntLiteral(3)), VarDecl(IntType(), a = BinaryOp(Identifier(b), +, Identifier(c))), VarDecl(IntType(), e = BinaryOp(IntLiteral(3), *, IntLiteral(5))), ReturnStmt(return Identifier(a))]), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), d = BinaryOp(IntLiteral(3), *, FuncCall(_fun, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_5():
    source = "void main() { fun(2, 5, fun(), 3 + 5, fun.mandy, fun.mandy + 4 * 21); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(fun, [IntLiteral(2), IntLiteral(5), FuncCall(fun, []), BinaryOp(IntLiteral(3), +, IntLiteral(5)), MemberAccess(Identifier(fun).mandy), BinaryOp(MemberAccess(Identifier(fun).mandy), +, BinaryOp(IntLiteral(4), *, IntLiteral(21)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_6():
    source = "void main() { fun(clock, ++3, 3++, f++, --g, g--, smearing_bunny); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(fun, [Identifier(clock), PrefixOp(++IntLiteral(3)), PostfixOp(IntLiteral(3)++), PostfixOp(Identifier(f)++), PrefixOp(--Identifier(g)), PostfixOp(Identifier(g)--), Identifier(smearing_bunny)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_7():
    source = "struct hammond {int a; float b; string c; }; int lmao() {} void fun() {} void main() { fun(); }"
    expected = "Program([StructDecl(hammond, [MemberDecl(IntType(), a), MemberDecl(FloatType(), b), MemberDecl(StringType(), c)]), FuncDecl(IntType(), lmao, [], []), FuncDecl(VoidType(), fun, [], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(fun, []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_8():
    source = "struct hammond {int a; float b; string c; }; int lmao() {} void fun() {} void main() { fun(); }"
    expected = "Program([StructDecl(hammond, [MemberDecl(IntType(), a), MemberDecl(FloatType(), b), MemberDecl(StringType(), c)]), FuncDecl(IntType(), lmao, [], []), FuncDecl(VoidType(), fun, [], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(fun, []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_func_9():
    source = "struct hammond {int a; float b; string c; }; int lmao() {} void fun() {} void main() { fun(); } float lmao2() {} string lmao3() {}"
    expected = "Program([StructDecl(hammond, [MemberDecl(IntType(), a), MemberDecl(FloatType(), b), MemberDecl(StringType(), c)]), FuncDecl(IntType(), lmao, [], []), FuncDecl(VoidType(), fun, [], []), FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(fun, []))]), FuncDecl(FloatType(), lmao2, [], []), FuncDecl(StringType(), lmao3, [], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_struct_1():
    source = "struct Drive; struct Tribe; struct New; struct World;"
    expected = "Program([StructDecl(Drive, []), StructDecl(Tribe, []), StructDecl(New, []), StructDecl(World, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_struct_2():
    source = "void main() { lm = {_abc.ld, b+c(), {3, 5}}; bernie bern = {{{{3}}}}; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(lm) = StructLiteral({MemberAccess(Identifier(_abc).ld), BinaryOp(Identifier(b), +, FuncCall(c, [])), StructLiteral({IntLiteral(3), IntLiteral(5)})}))), VarDecl(StructType(bernie), bern = StructLiteral({StructLiteral({StructLiteral({StructLiteral({IntLiteral(3)})})})}))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_struct_3():
    source = "void main() { lm = {_abc.ld, b+c(), {3, 5}}; bernie bern = {{{{3}}}}; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(lm) = StructLiteral({MemberAccess(Identifier(_abc).ld), BinaryOp(Identifier(b), +, FuncCall(c, [])), StructLiteral({IntLiteral(3), IntLiteral(5)})}))), VarDecl(StructType(bernie), bern = StructLiteral({StructLiteral({StructLiteral({StructLiteral({IntLiteral(3)})})})}))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_struct_4():
    source = "void main() { int a = abc().d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a = MemberAccess(FuncCall(abc, []).d))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_struct_5():
    source = "void main() { a.x = 5; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(a).x) = IntLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_1():
    source = "void main() {if(pong_tin) { lmao(); }}"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(pong_tin) then BlockStmt([ExprStmt(FuncCall(lmao, []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_2():
    source = "void main() {if(pong_tin) lmao();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(pong_tin) then ExprStmt(FuncCall(lmao, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_3():
    source = "void main() {if(pong_tin) { lmao(); } else { porsche(); } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(pong_tin) then BlockStmt([ExprStmt(FuncCall(lmao, []))]), else BlockStmt([ExprStmt(FuncCall(porsche, []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_4():
    source = "void main() {if(pong_tin) lmao(); else stone_henge();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(pong_tin) then ExprStmt(FuncCall(lmao, [])), else ExprStmt(FuncCall(stone_henge, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_5():
    source = "void main() {if(pong_tin) { lmao(); } else spot_of_lunch(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(pong_tin) then BlockStmt([ExprStmt(FuncCall(lmao, []))]), else ExprStmt(FuncCall(spot_of_lunch, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_6():
    source = "void main() {if(pong_tin && on_paper ) { lmao(); } else spot_of_lunch(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(Identifier(pong_tin), &&, Identifier(on_paper)) then BlockStmt([ExprStmt(FuncCall(lmao, []))]), else ExprStmt(FuncCall(spot_of_lunch, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_7():
    source = "void main() {if(pong_tin && on_paper || (pretending * wahoo)) { lmao(); } else spot_of_lunch(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(BinaryOp(Identifier(pong_tin), &&, Identifier(on_paper)), ||, BinaryOp(Identifier(pretending), *, Identifier(wahoo))) then BlockStmt([ExprStmt(FuncCall(lmao, []))]), else ExprStmt(FuncCall(spot_of_lunch, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_8():
    source = "void main() {if(ahk || pong_tin && on_paper + 35 || (pretending * wahoo())) { lmao(); } else spot_of_lunch(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(BinaryOp(Identifier(ahk), ||, BinaryOp(Identifier(pong_tin), &&, BinaryOp(Identifier(on_paper), +, IntLiteral(35)))), ||, BinaryOp(Identifier(pretending), *, FuncCall(wahoo, []))) then BlockStmt([ExprStmt(FuncCall(lmao, []))]), else ExprStmt(FuncCall(spot_of_lunch, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_if_9():
    source = "void main() {if(pong_tin) { lmao(); a = 3 + 7; int s = 35;} else if(lmao) {lmao(); lmao();} else peaked();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(pong_tin) then BlockStmt([ExprStmt(FuncCall(lmao, [])), ExprStmt(AssignExpr(Identifier(a) = BinaryOp(IntLiteral(3), +, IntLiteral(7)))), VarDecl(IntType(), s = IntLiteral(35))]), else IfStmt(if Identifier(lmao) then BlockStmt([ExprStmt(FuncCall(lmao, [])), ExprStmt(FuncCall(lmao, []))]), else ExprStmt(FuncCall(peaked, []))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_block_statement_1():
    source = "void main() { {a = b + c;} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, Identifier(c))))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_block_statement_2():
    source = "void main() { {int a; int b = fun(); int c = b * a + 3 - fun();} }"
    expected = "Program([FuncDecl(VoidType(), main, [], [BlockStmt([VarDecl(IntType(), a), VarDecl(IntType(), b = FuncCall(fun, [])), VarDecl(IntType(), c = BinaryOp(BinaryOp(BinaryOp(Identifier(b), *, Identifier(a)), +, IntLiteral(3)), -, FuncCall(fun, [])))])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_block_statement_3():
    source = "void main() { { { { a = b + c; } } } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [BlockStmt([BlockStmt([BlockStmt([ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, Identifier(c))))])])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_while_1():
    source = "void main() {while(hammond) {boat();}}"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(hammond) do BlockStmt([ExprStmt(FuncCall(boat, []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_while_2():
    source = "void main() {while(hammond) boat();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(hammond) do ExprStmt(FuncCall(boat, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_while_3():
    source = "void main() {while(hammond) { boat(); a = b + c; box(); }}"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while Identifier(hammond) do BlockStmt([ExprStmt(FuncCall(boat, [])), ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, Identifier(c)))), ExprStmt(FuncCall(box, []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_while_4():
    source = "void main() {while(hammond || propeller + c) { boat(); a = b + c; box(); }}"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while BinaryOp(Identifier(hammond), ||, BinaryOp(Identifier(propeller), +, Identifier(c))) do BlockStmt([ExprStmt(FuncCall(boat, [])), ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, Identifier(c)))), ExprStmt(FuncCall(box, []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_while_5():
    source = "void main() {while(8 * hammond || propeller + c) { boat(); a = b + c; box(); }}"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while BinaryOp(BinaryOp(IntLiteral(8), *, Identifier(hammond)), ||, BinaryOp(Identifier(propeller), +, Identifier(c))) do BlockStmt([ExprStmt(FuncCall(boat, [])), ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(b), +, Identifier(c)))), ExprStmt(FuncCall(box, []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_1():
    source = "void main() {for(int i = 0; i < 10; ++i) {korean_crane_carrier();}}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(++Identifier(i)) do BlockStmt([ExprStmt(FuncCall(korean_crane_carrier, []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_2():
    source = "void main() {for(int i = 0; i < 10; ++i) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(++Identifier(i)) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_3():
    source = "void main() {for(int i = 0; i < 10; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_4():
    source = "void main() {for(int i = 0; ; ++i) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; PrefixOp(++Identifier(i)) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_5():
    source = "void main() {for(int i = 0; ; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_6():
    source = "void main() {for(; i < 10; ++i) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(++Identifier(i)) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_7():
    source = "void main() {for(; i < 10; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_8():
    source = "void main() {for(; ; ++i) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; PrefixOp(++Identifier(i)) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_9():
    source = "void main() {for(int i = 0; i < 10; i++) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_10():
    source = "void main() {for(int i = 0; i < 10; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_11():
    source = "void main() {for(int i = 0; ; i++) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; PostfixOp(Identifier(i)++) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_12():
    source = "void main() {for(int i = 0; ; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_13():
    source = "void main() {for(; i < 10; i++) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)++) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_14():
    source = "void main() {for(; i < 10; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_15():
    source = "void main() {for(; ; i++) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; PostfixOp(Identifier(i)++) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_16():
    source = "void main() {for(; ; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_17():
    source = "void main() {for(int i = 0; i < 10; --i) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(--Identifier(i)) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_18():
    source = "void main() {for(int i = 0; i < 10; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_19():
    source = "void main() {for(int i = 0; ; --i) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; PrefixOp(--Identifier(i)) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_20():
    source = "void main() {for(int i = 0; ; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_21():
    source = "void main() {for(; i < 10; --i) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(--Identifier(i)) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_22():
    source = "void main() {for(; i < 10; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected
    
def test_for_23():
    source = "void main() {for(; ; --i) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; PrefixOp(--Identifier(i)) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_24():
    source = "void main() {for(; ; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_25():
    source = "void main() {for(int i = 0; i < 10; i--) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)--) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_26():
    source = "void main() {for(int i = 0; i < 10; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_27():
    source = "void main() {for(int i = 0; ; i--) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; PostfixOp(Identifier(i)--) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_28():
    source = "void main() {for(int i = 0; ; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); None; None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_29():
    source = "void main() {for(; i < 10; i--) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); PostfixOp(Identifier(i)--) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_30():
    source = "void main() {for(; i < 10; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; BinaryOp(Identifier(i), <, IntLiteral(10)); None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_31():
    source = "void main() {for(; ; i--) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; PostfixOp(Identifier(i)--) do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_32():
    source = "void main() {for(; ; ) korean_crane_carrier();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do ExprStmt(FuncCall(korean_crane_carrier, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_33():
    source = "void main() {for(int i = 0; i < 10; ++i) pete();}"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); PrefixOp(++Identifier(i)) do ExprStmt(FuncCall(pete, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_34():
    source = "void main() { a = (a + b) * c / 5; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c)), /, IntLiteral(5))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_35():
    source = "void main() { a = (a + (b - 3) / 5 % 20 * 10) * (c / 5); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(b), -, IntLiteral(3)), /, IntLiteral(5)), %, IntLiteral(20)), *, IntLiteral(10))), *, BinaryOp(Identifier(c), /, IntLiteral(5)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_36():
    source = "void main() { a = (a + (b - 3) / 5 % 20 * 10) * (c / 5) * -25 + b++ * 25; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(BinaryOp(BinaryOp(BinaryOp(Identifier(b), -, IntLiteral(3)), /, IntLiteral(5)), %, IntLiteral(20)), *, IntLiteral(10))), *, BinaryOp(Identifier(c), /, IntLiteral(5))), *, IntLiteral(-25)), +, BinaryOp(PostfixOp(Identifier(b)++), *, IntLiteral(25)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_37():
    source = "void main() { a = (a.b + (!b - 3) / 5 || 20 == 10) * (c / 5) * -25 + b++ * 25; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(BinaryOp(BinaryOp(BinaryOp(MemberAccess(Identifier(a).b), +, BinaryOp(BinaryOp(PrefixOp(!Identifier(b)), -, IntLiteral(3)), /, IntLiteral(5))), ||, BinaryOp(IntLiteral(20), ==, IntLiteral(10))), *, BinaryOp(Identifier(c), /, IntLiteral(5))), *, IntLiteral(-25)), +, BinaryOp(PostfixOp(Identifier(b)++), *, IntLiteral(25)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_stat_1():
    source = "void main() {switch (day) { case 1: printInt(1); break; case 2: case 3: printInt(3); break; default: printInt(0);}}"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(day) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(printInt, [IntLiteral(1)])), BreakStmt()]), CaseStmt(case IntLiteral(2): []), CaseStmt(case IntLiteral(3): [ExprStmt(FuncCall(printInt, [IntLiteral(3)])), BreakStmt()])], default DefaultStmt(default: [ExprStmt(FuncCall(printInt, [IntLiteral(0)]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_stat_2():
    source = "void main() {switch (day) { }}"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(day) cases [], default DefaultStmt(default: []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_stat_3():
    source = "void main() {switch (day) { case 1 + 2: printInt(3); break; case (4): printInt(4); break; case +5: printInt(5); break; case -6: printInt(6); break; }}"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(day) cases [CaseStmt(case BinaryOp(IntLiteral(1), +, IntLiteral(2)): [ExprStmt(FuncCall(printInt, [IntLiteral(3)])), BreakStmt()]), CaseStmt(case IntLiteral(4): [ExprStmt(FuncCall(printInt, [IntLiteral(4)])), BreakStmt()]), CaseStmt(case PrefixOp(+IntLiteral(5)): [ExprStmt(FuncCall(printInt, [IntLiteral(5)])), BreakStmt()]), CaseStmt(case IntLiteral(-6): [ExprStmt(FuncCall(printInt, [IntLiteral(6)])), BreakStmt()])], default DefaultStmt(default: []))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_exp_38():
    source = "void main() { a = b + c * d - e / f; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(b), +, BinaryOp(Identifier(c), *, Identifier(d))), -, BinaryOp(Identifier(e), /, Identifier(f)))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_exp_39():
    source = "void main() { a = !--foo(); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = PrefixOp(!PrefixOp(--FuncCall(foo, [])))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_exp_40():
    source = "void main() { a = baz().x + 1; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(MemberAccess(FuncCall(baz, []).x), +, IntLiteral(1))))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_exp_41():
    source = "void main() { obj.field = 42; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(MemberAccess(Identifier(obj).field) = IntLiteral(42)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_exp_42():
    source = "void main() { a = {1, 2, {3, 4}}; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = StructLiteral({IntLiteral(1), IntLiteral(2), StructLiteral({IntLiteral(3), IntLiteral(4)})})))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_43():
    source = "void main() { a = (a + b) * c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_44():
    source = "void main() { a = a * (b + c); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(Identifier(a), *, BinaryOp(Identifier(b), +, Identifier(c)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_45():
    source = "void main() { a = a + b + c; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), +, Identifier(c))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_46():
    source = "void main() { a = a + b * c + d; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(a), +, BinaryOp(Identifier(b), *, Identifier(c))), +, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_47():
    source = "void main() { a = (a + b) * (c + d); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(a), +, Identifier(b)), *, BinaryOp(Identifier(c), +, Identifier(d)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_exp_48():
    source = "void main() { a = (a || b) && (c || d); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = BinaryOp(BinaryOp(Identifier(a), ||, Identifier(b)), &&, BinaryOp(Identifier(c), ||, Identifier(d)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_stmt_1():
    source = "void main() { return; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ReturnStmt(return)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_stmt_2():
    source = "void main() { while (i < 10) { if (i == 5) break; continue; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(10)) do BlockStmt([IfStmt(if BinaryOp(Identifier(i), ==, IntLiteral(5)) then BreakStmt()), ContinueStmt()]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_stmt_3():
    source = "void main() { for (;; ) { x = x + 1; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for None; None; None do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_stmt_4():
    source = "void main() { switch (x) { default: x = 0; } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [SwitchStmt(switch Identifier(x) cases [], default DefaultStmt(default: [ExprStmt(AssignExpr(Identifier(x) = IntLiteral(0)))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_stmt_5():
    source = "void main() { { int a = 1; { int b = a + 2; } } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [BlockStmt([VarDecl(IntType(), a = IntLiteral(1)), BlockStmt([VarDecl(IntType(), b = BinaryOp(Identifier(a), +, IntLiteral(2)))])])])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_decl_1():
    source = "add(int x, int y) { return x + y; }"
    expected = "Program([FuncDecl(auto, add, [Param(IntType(), x), Param(IntType(), y)], [ReturnStmt(return BinaryOp(Identifier(x), +, Identifier(y)))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_decl_2():
    source = "struct S; struct T { int x; };"
    expected = "Program([StructDecl(S, []), StructDecl(T, [MemberDecl(IntType(), x)])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_decl_3():
    source = "void main() { auto x; int y = 2; string s = \"hi\"; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(auto, x), VarDecl(IntType(), y = IntLiteral(2)), VarDecl(StringType(), s = StringLiteral('hi'))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_decl_4():
    source = "void main() { Point p = {1,2}; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)}))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_integration_1():
    source = '''
        struct Point {
            int x;
            int y;
        };
        int dist(Point p) {
            return p.x + p.y;
        }
        void main() {
            Point a = {1,2};
            int d = dist(a);
        }
    '''
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), FuncDecl(IntType(), dist, [Param(StructType(Point), p)], [ReturnStmt(return BinaryOp(MemberAccess(Identifier(p).x), +, MemberAccess(Identifier(p).y)))]), FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), a = StructLiteral({IntLiteral(1), IntLiteral(2)})), VarDecl(IntType(), d = FuncCall(dist, [Identifier(a)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_integration_2():
    source = "void main() { if (a) for (int i = 0; i < 2; i++) { switch (i) { case 0: a = 1; break; default: a = 2; } } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if Identifier(a) then ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(2)); PostfixOp(Identifier(i)++) do BlockStmt([SwitchStmt(switch Identifier(i) cases [CaseStmt(case IntLiteral(0): [ExprStmt(AssignExpr(Identifier(a) = IntLiteral(1))), BreakStmt()])], default DefaultStmt(default: [ExprStmt(AssignExpr(Identifier(a) = IntLiteral(2)))]))])))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_integration_3():
    source = "void f() {} int g(int x) { return x * 2; } void main() { int y = g(f(), 1); }"
    expected = "Program([FuncDecl(VoidType(), f, [], []), FuncDecl(IntType(), g, [Param(IntType(), x)], [ReturnStmt(return BinaryOp(Identifier(x), *, IntLiteral(2)))]), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), y = FuncCall(g, [FuncCall(f, []), IntLiteral(1)]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_stress_1():
    source = "void main() { a = {{{{1}}}}; }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(a) = StructLiteral({StructLiteral({StructLiteral({StructLiteral({IntLiteral(1)})})})})))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_stress_2():
    source = "void main() { if (a && (b || c)) { for (int i = 0; i < 3; i++) { while (x < y) { switch (x) { case 1: x++; break; default: x = x + 1; } } } } }"
    expected = "Program([FuncDecl(VoidType(), main, [], [IfStmt(if BinaryOp(Identifier(a), &&, BinaryOp(Identifier(b), ||, Identifier(c))) then BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(3)); PostfixOp(Identifier(i)++) do BlockStmt([WhileStmt(while BinaryOp(Identifier(x), <, Identifier(y)) do BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(PostfixOp(Identifier(x)++)), BreakStmt()])], default DefaultStmt(default: [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected


def test_stress_3():
    source = "void main() { result = (a.b + foo(c, d.e)) * -(x - y); }"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(result) = BinaryOp(BinaryOp(MemberAccess(Identifier(a).b), +, FuncCall(foo, [Identifier(c), MemberAccess(Identifier(d).e)])), *, PrefixOp(-BinaryOp(Identifier(x), -, Identifier(y))))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_stress_4():
    source = "void main() { result = x; } struct Point { int x; int y; };"
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(AssignExpr(Identifier(result) = Identifier(x)))]), StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected
