"""
Test cases for TyC Static Semantic Checker

This module contains test cases for the static semantic checker.
100 test cases covering all error types and comprehensive scenarios.
"""

from tests.utils import Checker
from src.utils.nodes import (
    Program,
    FuncDecl,
    BlockStmt,
    VarDecl,
    AssignExpr,
    ExprStmt,
    IntType,
    FloatType,
    StringType,
    VoidType,
    StructType,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    Identifier,
    BinaryOp,
    MemberAccess,
    FuncCall,
    StructDecl,
    MemberDecl,
    Param,
    ReturnStmt,
)


# ============================================================================
# Valid Programs (test_001 - test_010)
# ============================================================================


def test_001():
    """Test a valid program that should pass all checks"""
    source = """
void main() {
    int x = 5;
    int y = x + 1;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_002():
    """Test valid program with auto type inference"""
    source = """
void main() {
    auto x = 10;
    auto y = 3.14;
    auto z = x + y;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_003():
    """Test valid program with functions"""
    source = """
int add(int x, int y) {
    return x + y;
}
void main() {
    int sum = add(5, 3);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_004():
    """Test valid program with struct"""
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected


def test_005():
    """Test valid program with nested blocks"""
    source = """
void main() {
    int x = 10;
    {
        int y = 20;
        int z = x + y;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_006():
    """Test valid program with struct"""
    source = """
struct Point {
    int x;
    int y;
};

struct Vector2 {
    int x;
    int y;
};
void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_007():
    source = """
void main() {
    auto x;
    x = 3;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_008():
    source = """
void main() {
    auto x;
    {
        auto x;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_009():
    source = """
void main() {
    for(int i = 0; i < 10; ++i)
    {
        //int i;

    }

    i = i + 1;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_010():
    source = """
void main() {
    int i = readInt();
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_011():
    source = """
void main() {
    return;
}

int add(int x, int y) {
    if (x < 0) {
        return 0;
    }

    return add(y - 1, x);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_012():
    source = """
void main() {
    auto x;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

#############EXAMPLES##################
def ex_test_001():
    source = """
void main() {
    auto x;
    auto y;
    auto z = x + y;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def ex_test_002():
    source = """
void main() {
    int sum = unknown(5, 3);
}
"""
    expected = "UndeclaredFunction(unknown)"
    assert Checker(source).check_from_source() == expected

def ex_test_003():
    source = """
struct Point {
    int x;
    int y;
}

void main() {
    Point p;
    p.x = 10;
    p.y = 20;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

#############REDECLARED################
def test_redeclared_member_001():
    source = """
struct Point {
    int x;
    int x;
};

void main() {
    int x;
}
"""
    expected = "Redeclared(Member, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_001():
    source = """
struct Point {
    int x;
};

void main() {
    Point x;
    Point x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_002():
    source = """
struct Point {
    int x;
};

void main() {
    Point x;
    int x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_003():
    source = """
void main() {
    string x;
    int x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_004():
    source = """
void add(int x) {
    int x;
}

void main() {
    int x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_005():
    source = """
void main() {
    int x;
}

void add(int x, int y) {
    int x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_006():
    source = """
void main() {
    int x;
}

void add(int x, int y) {
    float x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_func_001():
    source = """
void main() {
    float x;
}

void main() {
    int x;
}
"""
    expected = "Redeclared(Function, main)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_func_002():
    source = """
void main() {
    float x;
}

void add(int x, int y) {
    return;
}

void add(float x, float y) {
    return;
}
"""
    expected = "Redeclared(Function, add)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_func_003():
    source = """
void main() {
    float x;
}

void readInt(int x, float x) {
    return;
}
"""
    expected = "Redeclared(Function, readInt)"
    assert Checker(source).check_from_source() == expected


def test_redeclared_parameter_001():
    source = """
void main() {
    float x;
}

void add(int x, int x) {
    return;
}
"""
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_parameter_002():
    source = """
void main() {
    float x;
}

void add(int x, float x) {
    return;
}
"""
    expected = "Redeclared(Parameter, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_struct_001():
    source = """
struct Point {
    int x;
    int x;
};

struct Point {
    int x;
};
"""
    expected = "Redeclared(Member, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_struct_002():
    source = """
struct Point {
    int x;
};

struct Point {
    float x;
};
"""
    expected = "Redeclared(Struct, Point)"
    assert Checker(source).check_from_source() == expected

#############UNDECLARED################
def test_undeclared_001():
    source = """
void main() {
    float x = a;
    int a;
}
"""
    expected = "UndeclaredIdentifier(a)"
    assert Checker(source).check_from_source() == expected

def test_undeclared_002():
    source = """
void main() {
    float x = x + 1;
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_undeclared_003():
    source = """
void main() {
    {
        int x;
    }
    x = x + 1;
}
"""
    expected = "UndeclaredIdentifier(x)"
    assert Checker(source).check_from_source() == expected

def test_undeclared_004():
    source = """
void main() {
    int x = add(5, 3);
}
"""
    expected = "UndeclaredFunction(add)"
    assert Checker(source).check_from_source() == expected

def test_undeclared_005():
    source = """
void main() {
    Point x;
}

struct Point {
    int x;
    int y;
};
"""
    expected = "UndeclaredStruct(Point)"
    assert Checker(source).check_from_source() == expected

def test_undeclared_006():
    source = """
struct Point {
    int x;
    Point y;
};

void main() {
    Point x;
}

"""
    expected = "UndeclaredStruct(Point)"
    assert Checker(source).check_from_source() == expected

#############MISMATCH################

def test_mismatch_001():
    source = """
void main() {
    auto x;
    x = x + 3.4 * x - 2.1;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(FloatLiteral(3.4), *, Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_002():
    source = """
void main() {
    auto x;
    auto y;
    auto z;
    x = (x && y) > (False || (z > 3));
    z = x;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), &&, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

# def test_mismatch_003():
#     source = """
# void main() {
#     auto x;
#     x = False;
# }
# """
#     expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(z = x)))"
#     assert Checker(source).check_from_source() == expected

#############INFER################

def test_infer_001():
    source = """
void main() {
    auto x;
    auto y;
    x = y;
}
"""
    expected = "TypeCannotBeInferred(ExprStmt(AssignExpr(Identifier(x) = Identifier(y))))"
    assert Checker(source).check_from_source() == expected

def test_infer_002():
    source = """
void main() {
    auto x;
    auto y;
    int result = x < y;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), <, Identifier(y)))"

def test_infer_003():
    source = """
void main() {
    auto x;
    auto y;

    x = (x && y) > (False || (z > 3));
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), &&, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_infer_004():
    source = """
void main() {
    auto x;
    auto y;

    x = y;
}
"""
    expected = "TypeCannotBeInferred(ExprStmt(AssignExpr(Identifier(x) = Identifier(y))))"
    assert Checker(source).check_from_source() == expected

def test_infer_005():
    source = """
void main() {
    auto x = 10;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_006():
    source = """
void main() {
    auto x = 10.5;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_007():
    source = """
void main() {
    auto x = "hi";
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_008():
    source = """
void main() {
    auto x;
    x = 5;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_009():
    source = """
void main() {
    auto x;
    printInt(x);
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_010():
    source = """
void main() {
    auto x;
    10 + x;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_011():
    source = """
void main() {
    auto x;
    x + 1.0;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, FloatLiteral(1.0)))"
    assert Checker(source).check_from_source() == expected

def test_infer_012():
    source = """
int add(int x, int y) {
    auto res;

    return res;
}

void main() {

}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_013():
    source = """
int add(int x, int y) {
    auto res;

    if(x > y) {
        return res;
    }

    if(res) {
        return x;
    }
}

void main() {

}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_014():
    source = """
int add(int x, int y) {
    auto res;

    if(x > y) {
        return res;
    }

    res = 1.0;
}

void main() {

}
"""
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(res) = FloatLiteral(1.0))))"
    assert Checker(source).check_from_source() == expected

def test_infer_015():
    source = """
void main() {
    auto x;
    x.member = 1;

}
"""
    expected = "TypeCannotBeInferred(MemberAccess(Identifier(x).member))"
    assert Checker(source).check_from_source() == expected

def test_infer_016():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    auto x = {1, 2};
}
"""
    expected = "TypeCannotBeInferred(VarDecl(auto, x = StructLiteral({IntLiteral(1), IntLiteral(2)})))"
    assert Checker(source).check_from_source() == expected

def test_infer_017():
    source = """
add(int x, float y) {
    if(x > y)
    {
        return x;
    }
    else
    {
        return y;
    }
}

void main() {

}
"""
    expected = "TypeMismatchInExpression(ReturnStmt(return Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_infer_018():
    source = """
void main() {
    auto x;
    while(x) {

    }
}
"""
    expected = "TypeMismatchInStatement(WhileStmt(while Identifier(x) do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_infer_019():
    source = """
void main() {
    auto x;
    for(int i = 0; i < x; ++i) {

    }
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(i), <, Identifier(x)))"
    assert Checker(source).check_from_source() == expected

def test_infer_020():
    source = """
void main() {
    auto x;
    x = readInt();
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_infer_021():
    source = """
void main() {
    auto x;
    float y;
    x + y;
    
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

def test_infer_021():
    source = """
void main() {
    auto x;
    float y;
    x + y;
}
"""
    expected = "TypeCannotBeInferred(BinaryOp(Identifier(x), +, Identifier(y)))"
    assert Checker(source).check_from_source() == expected

#############MISMATCH(STATEMENT)################

def test_mismatch_statement_001():
    source = """
void main() {
    if(readFloat())
    {

    }
}
"""
    expected = "TypeMismatchInStatement(IfStmt(if FuncCall(readFloat, []) then BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_002():
    source = """
void main() {
    if(readString())
    {

    }
}
"""
    expected = "TypeMismatchInStatement(IfStmt(if FuncCall(readString, []) then BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_003():
    source = """
void main() {
    while(readString())
    {

    }
}
"""
    expected = "TypeMismatchInStatement(WhileStmt(while FuncCall(readString, []) do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_004():
    source = """
void main() {
    for(; readString(); )
    {

    }
}
"""
    expected = "TypeMismatchInStatement(ForStmt(for None; FuncCall(readString, []); None do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_005():
    source = """
void main() {
    for(; readFloat(); )
    {

    }
}
"""
    expected = "TypeMismatchInStatement(ForStmt(for None; FuncCall(readFloat, []); None do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_006():
    source = """
void main() {
    float x = 5;
}
"""
    expected = "TypeMismatchInStatement"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_007():
    source = """
void main() {
    int x = 5.0;
}
"""
    expected = "TypeMismatchInStatement"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_008():
    source = """
void main() {
    int x = "hi";
}
"""
    expected = "TypeMismatchInStatement"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_009():
    source = """
void main() {
    string x = 5;
}
"""
    expected = "TypeMismatchInStatement"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_010():
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point x = 5;
}
"""
    expected = "TypeMismatchInStatement"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_011():
    source = """
struct Point {
    int x;
    int y;
};
void main() {
    Point x = {5, 5};
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_012():
    source = """
struct Point {
    int x;
    float y;
};

void main() {
    Point x = {5, 5.0};
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_013():
    source = """
struct Point {
    int x;
    string y;
};

void main() {
    Point x = {5, 5};
}
"""
    expected = "TypeMismatchInStatement(VarDecl(StructType(Point), x = StructLiteral({IntLiteral(5), IntLiteral(5)})))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_014():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    Point x = {5, 5};

    if(x)
    {

    }
}
"""
    expected = "TypeMismatchInStatement(VarDecl(StructType(Point), x = StructLiteral({IntLiteral(5), IntLiteral(5)})))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_015():
    source = """
void add() {
    return 5;
}

void main() {
    Point x = {5, 5};
}
"""
    expected = "TypeMismatchInExpression(ReturnStmt(return IntLiteral(5)))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_016():
    source = """
int add() {
    return;
}

void main() {
    Point x = {5, 5};
}
"""
    expected = "TypeMismatchInStatement(ReturnStmt(return))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_017():
    source = """
void main() {
    int x;
    float y;
    x = y = 1.0;
}
"""
    expected = "TypeMismatchInExpression(AssignExpr(Identifier(y) = FloatLiteral(1.0)))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_018():
    source = """
int add(int x, int y)
{
    if(x > y)
    {
        return x;
    }

    return;
}

void main() {

}
"""
    expected = "TypeMismatchInStatement(ReturnStmt(return))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_019():
    source = """
void main() {
    switch(5.0)
    {
        default:
            break;
    }

}
"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch FloatLiteral(5.0) cases [], default DefaultStmt(default: [BreakStmt()])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_020():
    source = """
void main() {
    switch("hi")
    {
        default:
            break;
    }

}
"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch StringLiteral('hi') cases [], default DefaultStmt(default: [BreakStmt()])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_021():
    source = """
void main() {
    float x;
    switch(x)
    {
        default:
            break;
    }

}
"""
    expected = "TypeMismatchInStatement(SwitchStmt(switch Identifier(x) cases [], default DefaultStmt(default: [BreakStmt()])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_statement_022():
    source = """
void main() {
    {
        return 5;
    }
}
"""
    expected = "TypeMismatchInExpression(ReturnStmt(return IntLiteral(5)))"
    assert Checker(source).check_from_source() == expected

#############MISMATCH(EXPR)################

def test_mismatch_expr_001():
    source = """
void main() {
    "a" + "b";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(StringLiteral('a'), +, StringLiteral('b')))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_002():
    source = """
void main() {
    1.5 % 2;
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(FloatLiteral(1.5), %, IntLiteral(2)))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_003():
    source = """
void main() {
    !"hi";
}
"""
    expected = "TypeMismatchInExpression(PrefixOp(!StringLiteral('hi')))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_004():
    source = """
void main() {
    float f;
    f++;
}
"""
    expected = "TypeMismatchInExpression(PostfixOp(Identifier(f)++))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_005():
    source = """
void main() {
    10++;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_006():
    source = """
void main() {
    "a" < "b";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(StringLiteral('a'), <, StringLiteral('b')))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_007():
    source = """
void main() {
    int a;
    a + "string";
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(a), +, StringLiteral('string')))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_008():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    Point a;
    Point b;
    a + b;
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(Identifier(a), +, Identifier(b)))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_008():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    {1, 2} + {2, 1};
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(StructLiteral({IntLiteral(1), IntLiteral(2)}), +, StructLiteral({IntLiteral(2), IntLiteral(1)})))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_009():
    source = """
void main() {
    printInt(5.0);
}
"""
    expected = "TypeMismatchInExpression(FuncCall(printInt, [FloatLiteral(5.0)]))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_010():
    source = """
void main() {
    printFloat(1);
}
"""
    expected = "TypeMismatchInExpression(FuncCall(printFloat, [IntLiteral(1)]))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_011():
    source = """
void main() {
    printString(5);
}
"""
    expected = "TypeMismatchInExpression(FuncCall(printString, [IntLiteral(5)]))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_012():
    source = """
void main() {
    readInt() + 1.5;
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_013():
    source = """
void main() {
    readFloat() && readFloat();
}
"""
    expected = "TypeMismatchInExpression(BinaryOp(FuncCall(readFloat, []), &&, FuncCall(readFloat, [])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_014():
    source = """
void main() {
    ++"hi";
}
"""
    expected = "TypeMismatchInExpression(PrefixOp(++StringLiteral('hi')))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_015():
    source = """
void main() {
    while("hi")
    {

    }
}
"""
    expected = "TypeMismatchInStatement(WhileStmt(while StringLiteral('hi') do BlockStmt([])))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_016():
    source = """
void main() {
    int x;
    x.x;
}
"""
    expected = "TypeMismatchInExpression(MemberAccess(Identifier(x).x))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_016():
    source = """
void main() {
    int x;
    float y;
    x = y;
}
"""
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(x) = Identifier(y))))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_expr_017():
    source = """
void main() {
    int x;
    float y;
    x = "hi";
}
"""
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(Identifier(x) = StringLiteral('hi))))"
    assert Checker(source).check_from_source() == expected

#############MUSTINLOOP################

def test_must_in_loop_001():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    continue;
}
"""
    expected = "MustInLoop(continue)"
    assert Checker(source).check_from_source() == expected

def test_must_in_loop_002():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    break;
}
"""
    expected = "MustInLoop(break)"
    assert Checker(source).check_from_source() == expected

def test_must_in_loop_002():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    switch(1)
    {
        default:
            continue;
    }
}
"""
    expected = "MustInLoop(continue)"
    assert Checker(source).check_from_source() == expected

def test_must_in_loop_003():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    switch(1)
    {
        default:
            continue;
    }
}
"""
    expected = "MustInLoop(continue)"
    assert Checker(source).check_from_source() == expected

def test_must_in_loop_004():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    while(1){
        if(0){
            continue;
        }
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_must_in_loop_005():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    while(1){
        continue;
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected

def test_must_in_loop_006():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    continue;
}
"""
    expected = "MustInLoop(continue)"
    assert Checker(source).check_from_source() == expected

def test_must_in_loop_007():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    switch(1)
    {
        default:
            continue;
    }
}
"""
    expected = "MustInLoop(continue)"
    assert Checker(source).check_from_source() == expected
    
def test_must_in_loop_008():
    source = """
struct Point {
    int x;
    int y;
};

void main() {
    while(1)
    {
        switch(1)
        {
            default:
                continue;
        }
    }
}
"""
    expected = "Static checking passed"
    assert Checker(source).check_from_source() == expected
