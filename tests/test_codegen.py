"""
Test cases for TyC code generation.
"""

from src.utils.nodes import *
from tests.utils import CodeGenerator


def test_001():
    """Test 1: Hello World - print string"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printString", [StringLiteral("Hello World")]))
            ])
        )
    ])
    expected = "Hello World"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_002():
    """Test 2: Print integer"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [IntLiteral(42)]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_003():
    """Test 3: Print float"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printFloat", [FloatLiteral(3.14)]))
            ])
        )
    ])
    expected = "3.14"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_004():
    """Test 4: Variable declaration and assignment"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                ExprStmt(FuncCall("printInt", [Identifier("x")]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_005():
    """Test 5: Binary operation - addition"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(5), "+", IntLiteral(3))
                ]))
            ])
        )
    ])
    expected = "8"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_006():
    """Test 6: Binary operation - multiplication"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(IntLiteral(6), "*", IntLiteral(7))
                ]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_007():
    """Test 7: If statement"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                IfStmt(
                    BinaryOp(IntLiteral(1), "<", IntLiteral(2)),
                    ExprStmt(FuncCall("printString", [StringLiteral("yes")])),
                    ExprStmt(FuncCall("printString", [StringLiteral("no")]))
                )
            ])
        )
    ])
    expected = "yes"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_008():
    """Test 8: While loop"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "i", IntLiteral(0)),
                WhileStmt(
                    BinaryOp(Identifier("i"), "<", IntLiteral(3)),
                    BlockStmt([
                        ExprStmt(FuncCall("printInt", [Identifier("i")])),
                        ExprStmt(AssignExpr(
                            Identifier("i"),
                            BinaryOp(Identifier("i"), "+", IntLiteral(1))
                        ))
                    ])
                )
            ])
        )
    ])
    expected = "012"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_009():
    """Test 9: Function call with return value"""
    ast = Program([
        FuncDecl(
            IntType(),
            "add",
            [Param(IntType(), "a"), Param(IntType(), "b")],
            BlockStmt([
                ReturnStmt(BinaryOp(Identifier("a"), "+", Identifier("b")))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ExprStmt(FuncCall("printInt", [
                    FuncCall("add", [IntLiteral(20), IntLiteral(22)])
                ]))
            ])
        )
    ])
    expected = "42"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"


def test_010():
    """Test 10: Multiple statements - arithmetic operations"""
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(IntType(), "x", IntLiteral(10)),
                VarDecl(IntType(), "y", IntLiteral(20)),
                ExprStmt(FuncCall("printInt", [
                    BinaryOp(Identifier("x"), "+", Identifier("y"))
                ]))
            ])
        )
    ])
    expected = "30"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_for_01():
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                        BinaryOp(Identifier("i"), "<", IntLiteral(10)),
                        PostfixOp("++", Identifier("i")),
                        BlockStmt([
                            ExprStmt(FuncCall("printInt", [
                                Identifier("i")
                            ]))
                        ])
                )
            ])
        )
    ])
    expected = "0123456789"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_for_02():
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                        BinaryOp(Identifier("i"), "<", IntLiteral(10)),
                        PrefixOp("++", Identifier("i")),
                        BlockStmt([
                            ExprStmt(FuncCall("printInt", [
                                Identifier("i")
                            ]))
                        ])
                )
            ])
        )
    ])
    expected = "0123456789"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_for_03():
    ast = Program([
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                ForStmt(VarDecl(IntType(), "i", IntLiteral(0)),
                        BinaryOp(Identifier("i"), "<", IntLiteral(10)),
                        PrefixOp("++", Identifier("i")),
                        BlockStmt([
                            ExprStmt(FuncCall("printInt", [
                                Identifier("i")
                            ]))
                        ])
                )
            ])
        )
    ])
    expected = "0123456789"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_struct_decl_01():
    ast = Program([
        StructDecl("Test", [
                MemberDecl(IntType(), 'x'),
                MemberDecl(FloatType(), 'y')
            ]),
        StructDecl("Point", [
                MemberDecl(IntType(), 'x'),
                MemberDecl(IntType(), 'y')
            ]),
        StructDecl("Vector", [
                MemberDecl(FloatType(), 'x'),
                MemberDecl(FloatType(), 'y')
            ]),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StructType("Test"), "test"),
                VarDecl(StructType("Point"), "point"),
                VarDecl(StructType("Vector"), "vector"),
            ])
        )
    ])
    expected = ""
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_struct_decl_02():
    ast = Program([
        StructDecl("Test", [
                MemberDecl(IntType(), 'x'),
                MemberDecl(FloatType(), 'y')
            ]),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StructType("Test"), "test"),
                ExprStmt(MemberAccess(Identifier("test"), "x"))
            ])
        )
    ])
    expected = ""
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_struct_decl_03():
    ast = Program([
        StructDecl("Test", [
                MemberDecl(IntType(), 'x'),
                MemberDecl(FloatType(), 'y')
            ]),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StructType("Test"), "test"),
                ExprStmt(AssignExpr(MemberAccess(Identifier("test"), "x"), IntLiteral(10))),
                ExprStmt(FuncCall("printInt", [
                    MemberAccess(Identifier("test"), "x")
                ]))
            ])
        )
    ])
    expected = "10"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_struct_literal_01():
    ast = Program([
        StructDecl("Point", [
                MemberDecl(IntType(), 'x'),
                MemberDecl(IntType(), 'y')
            ]),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StructType("Point"), "test"),
                ExprStmt(AssignExpr(Identifier("test"), StructLiteral([IntLiteral(1), IntLiteral(1)]))),
                ExprStmt(FuncCall("printString", [
                    StringLiteral("(")
                ])),
                ExprStmt(FuncCall("printInt", [
                    MemberAccess(Identifier("test"), "x")
                ])),
                ExprStmt(FuncCall("printString", [
                    StringLiteral(", ")
                ])),
                ExprStmt(FuncCall("printInt", [
                    MemberAccess(Identifier("test"), "y")
                ])),
                ExprStmt(FuncCall("printString", [
                    StringLiteral(")")
                ]))
            ])
        )
    ])
    expected = "(1, 1)"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_struct_literal_02():
    ast = Program([
        StructDecl("Point", [
                MemberDecl(FloatType(), 'x'),
                MemberDecl(FloatType(), 'y')
            ]),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StructType("Point"), "test"),
                ExprStmt(AssignExpr(Identifier("test"), StructLiteral([FloatLiteral(-2.5), FloatLiteral(2.5)]))),
                ExprStmt(FuncCall("printString", [
                    StringLiteral("(")
                ])),
                ExprStmt(FuncCall("printFloat", [
                    MemberAccess(Identifier("test"), "x")
                ])),
                ExprStmt(FuncCall("printString", [
                    StringLiteral(", ")
                ])),
                ExprStmt(FuncCall("printFloat", [
                    MemberAccess(Identifier("test"), "y")
                ])),
                ExprStmt(FuncCall("printString", [
                    StringLiteral(")")
                ]))
            ])
        )
    ])
    expected = "(-2.5, 2.5)"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_struct_literal_03():
    ast = Program([
        StructDecl("Person", [
                MemberDecl(StringType(), 'name'),
                MemberDecl(IntType(), 'age'),
        ]),
        FuncDecl(
            VoidType(),
            "printPerson",
            [Param(StructType("Person"), "person")],
            BlockStmt([
                ExprStmt(FuncCall("printString", [
                    StringLiteral("\nName: ")
                ])),
                ExprStmt(FuncCall("printString", [
                    MemberAccess(Identifier("person"), "name")
                ])),
                ExprStmt(FuncCall("printString", [
                    StringLiteral("\nAge: ")
                ])),
                ExprStmt(FuncCall("printInt", [
                    MemberAccess(Identifier("person"), "age")
                ]))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StructType("Person"), "person"),
                ExprStmt(AssignExpr(Identifier("person"), StructLiteral([StringLiteral('deng'), IntLiteral(21)]))),
                ExprStmt(FuncCall("printPerson", [
                    Identifier("person")
                ]))
            ])
        )
    ])
    expected = "Name: deng\nAge: 21"
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"

def test_struct_literal_04():
    ast = Program([
        StructDecl("Person", [
                MemberDecl(StringType(), 'name'),
                MemberDecl(IntType(), 'age'),
        ]),
        FuncDecl(
            VoidType(),
            "printPerson",
            [Param(StructType("Person"), "person")],
            BlockStmt([
                ExprStmt(FuncCall("printString", [
                    StringLiteral("\nName: ")
                ])),
                ExprStmt(FuncCall("printString", [
                    MemberAccess(Identifier("person"), "name")
                ])),
                ExprStmt(FuncCall("printString", [
                    StringLiteral("\nAge: ")
                ])),
                ExprStmt(FuncCall("printInt", [
                    MemberAccess(Identifier("person"), "age")
                ]))
            ])
        ),
        FuncDecl(
            VoidType(),
            "main",
            [],
            BlockStmt([
                VarDecl(StructType("Person"), "person", StructLiteral([StringLiteral('deng'), IntLiteral(21)])),
                ExprStmt(FuncCall("printPerson", [
                    Identifier("person")
                ]))
            ])
        )
    ])
    expected = """Name: deng\nAge: 21"""
    result = CodeGenerator().generate_and_run(ast)
    assert result == expected, f"Expected '{expected}', got '{result}'"
