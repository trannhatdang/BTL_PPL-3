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
def test_redeclared_var_001():
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

def test_redeclared_var_002():
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

def test_redeclared_var_003():
    source = """
void main() {
    Point x;
    int x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_004():
    source = """
void main() {
    string x;
    int x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_005():
    source = """
void main() {
    float x;
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
    int x;
}
"""
    expected = "Redeclared(Variable, x)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_var_007():
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
    expected = "Redeclared(Variable, add)"
    assert Checker(source).check_from_source() == expected

def test_redeclared_func_001():
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

def test_redeclared_func_003():
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

def test_redeclared_struct_mem_001():
    source = """
struct Point {
    int x;
    int x;
};
"""
    expected = "Redeclared(Member, x)"
    assert Checker(source).check_from_source() == expected


#############UNDECLARED################
def test_undeclared_001():
    source = """
void main() {
    float x = a;
}
"""
    expected = "UndeclaredIdentifier(a)"
    assert Checker(source).check_from_source() == expected

#############MISMATCH################

def test_mismatch_001():
    source = """
void main() {
    auto x;
    x = x + 3.4 * x - 2.1;
}
"""
    expected = "Type Mismatch In Expression: BinaryOp(Identifier(x) + FloatLit(2.1))"
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
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(z = x)))"
    assert Checker(source).check_from_source() == expected

def test_mismatch_004():
    source = """
void main() {
    auto x;
    x = False;
}
"""
    expected = "TypeMismatchInStatement(ExprStmt(AssignExpr(z = x)))"
    assert Checker(source).check_from_source() == expected

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

