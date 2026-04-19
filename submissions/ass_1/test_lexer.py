"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


'''
def test_lexer_placeholder():
    """Placeholder test - replace with actual test cases"""
    source = "// This is a placeholder test"
    tokenizer = Tokenizer(source)
    # TODO: Add actual test assertions
    assert tokenizer.get_tokens_as_string() == 'EOF'
'''
###############Must Pass#################

def test_keyword_auto():
    """1. Keyword"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"


def test_operator_assign():
    """2. Operator"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"


def test_separator_semi():
    """3. Separator"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"


def test_integer_single_digit():
    """4. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"


def test_float_decimal():
    """5. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"


def test_string_simple():
    """6. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"


def test_identifier_simple():
    """7. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"


def test_line_comment():
    """8. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"


def test_integer_in_expression():
    """9. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"

def test_complex_expression():
    """10. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

###############Empty#################

def test_empty_1():
    tokenizer = Tokenizer("")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_empty_2():
    tokenizer = Tokenizer("\t\t\t\t\t\t\t\t\t\t\t")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_empty_3():
    tokenizer = Tokenizer("\n\n\n\n\n\n\n\n\n\n\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_empty_4():
    tokenizer = Tokenizer("                                                         ")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

###############Whitespace#################

def test_whitespace_1():
    tokenizer = Tokenizer(" \t\f\r\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

###############Comments#################

def test_comments_1():
    tokenizer = Tokenizer("//this is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_comments_2():
    tokenizer = Tokenizer("//this should be all ignored \r\n\n\n\n\n\n")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comments_1():
    tokenizer = Tokenizer("/*this is a block comment \r\n\r\n\r\n*/")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comments_2():
    tokenizer = Tokenizer("/*lmao*/")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comments_3():
    tokenizer = Tokenizer("/*lmao")
    assert tokenizer.get_tokens_as_string() == "/,*,lmao,<EOF>"

def test_block_comments_4():
    tokenizer = Tokenizer("/*/*lmao*/*/")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

###############Identifiers#################

def test_ID_only_words_1():
    tokenizer = Tokenizer("a")
    assert tokenizer.get_tokens_as_string() == "a,<EOF>"

def test_ID_only_words_2():
    tokenizer = Tokenizer("asdgsdgsdgsdg")
    assert tokenizer.get_tokens_as_string() == "asdgsdgsdgsdg,<EOF>"

def test_ID_only_words_3():
    tokenizer = Tokenizer("A")
    assert tokenizer.get_tokens_as_string() == "A,<EOF>"

def test_ID_only_words_4():
    tokenizer = Tokenizer("AASDGLJSDLKJGIORWJEOIJW")
    assert tokenizer.get_tokens_as_string() == "AASDGLJSDLKJGIORWJEOIJW,<EOF>"

def test_ID_only_words_5():
    tokenizer = Tokenizer("AAsdgLJSwgfJGgsgJEOIJW")
    assert tokenizer.get_tokens_as_string() == "AAsdgLJSwgfJGgsgJEOIJW,<EOF>"

def test_ID_only_words_6():
    tokenizer = Tokenizer("sdgLJSwgfJGgsgJEOIJW")
    assert tokenizer.get_tokens_as_string() == "sdgLJSwgfJGgsgJEOIJW,<EOF>"

def test_ID_only_underscore_1():
    tokenizer = Tokenizer("_")
    assert tokenizer.get_tokens_as_string() == "_,<EOF>"

def test_ID_only_underscore_2():
    tokenizer = Tokenizer("__")
    assert tokenizer.get_tokens_as_string() == "__,<EOF>"

def test_ID_only_underscore_3():
    tokenizer = Tokenizer("____")
    assert tokenizer.get_tokens_as_string() == "____,<EOF>"

def test_ID_words_number_1():
    tokenizer = Tokenizer("asdg214")
    assert tokenizer.get_tokens_as_string() == "asdg214,<EOF>"

def test_ID_words_number_2():
    tokenizer = Tokenizer("asdg214sdg")
    assert tokenizer.get_tokens_as_string() == "asdg214sdg,<EOF>"

def test_ID_words_number_3():
    tokenizer = Tokenizer("asdg214sdg231")
    assert tokenizer.get_tokens_as_string() == "asdg214sdg231,<EOF>"

def test_ID_words_number_4():
    tokenizer = Tokenizer("asdg231")
    assert tokenizer.get_tokens_as_string() == "asdg231,<EOF>"

def test_ID_words_underscore_1():
    tokenizer = Tokenizer("a_sdg")
    assert tokenizer.get_tokens_as_string() == "a_sdg,<EOF>"

def test_ID_words_underscore_2():
    tokenizer = Tokenizer("_sdg")
    assert tokenizer.get_tokens_as_string() == "_sdg,<EOF>"

def test_ID_words_underscore_3():
    tokenizer = Tokenizer("sdg_")
    assert tokenizer.get_tokens_as_string() == "sdg_,<EOF>"

def test_ID_words_underscore_4():
    tokenizer = Tokenizer("_sdgh_")
    assert tokenizer.get_tokens_as_string() == "_sdgh_,<EOF>"

def test_ID_words_underscore_number_1():
    tokenizer = Tokenizer("a_1")
    assert tokenizer.get_tokens_as_string() == "a_1,<EOF>"

def test_ID_words_underscore_number_2():
    tokenizer = Tokenizer("a1_")
    assert tokenizer.get_tokens_as_string() == "a1_,<EOF>"

def test_ID_words_underscore_number_3():
    tokenizer = Tokenizer("_a1")
    assert tokenizer.get_tokens_as_string() == "_a1,<EOF>"

def test_ID_words_underscore_number_4():
    tokenizer = Tokenizer("_1a")
    assert tokenizer.get_tokens_as_string() == "_1a,<EOF>"

def test_ID_err_1():
    tokenizer = Tokenizer("\u00C8")
    assert tokenizer.get_tokens_as_string() == "Error Token \u00C8"

def test_ID_err_2():
    tokenizer = Tokenizer("¼")
    assert tokenizer.get_tokens_as_string() == "Error Token ¼"

###############Characters#################

def test_escape_chara_1():
    tokenizer = Tokenizer("\"\\n\"")
    assert tokenizer.get_tokens_as_string() == "\\n,<EOF>"

def test_escape_chara_2():
    tokenizer = Tokenizer("\"\\t\"")
    assert tokenizer.get_tokens_as_string() == "\\t,<EOF>"

def test_escape_chara_3():
    tokenizer = Tokenizer("\" \\\" \"")
    assert tokenizer.get_tokens_as_string() == " \\\" ,<EOF>"

def test_inside_extended_ascii():
    tokenizer = Tokenizer("\"Ç\"")
    assert tokenizer.get_tokens_as_string() == "Ç,<EOF>"

def test_inside_extended_ascii_2():
    tokenizer = Tokenizer("\"\u00A1\"")
    assert tokenizer.get_tokens_as_string() == "\u00A1,<EOF>"

def test_inside_extended_ascii_3():
    tokenizer = Tokenizer("\"\u007f\u00D1\"")
    assert tokenizer.get_tokens_as_string() == "\u007f\u00D1,<EOF>"

def test_inside_extended_ascii_4():
    tokenizer = Tokenizer("\"\u00FF\"")
    assert tokenizer.get_tokens_as_string() == "\u00FF,<EOF>"

def test_inside_extended_ascii_5():
    tokenizer = Tokenizer("\"\u0081\"")
    assert tokenizer.get_tokens_as_string() == "\u0081,<EOF>"

def test_outside_extended_ascii():
    tokenizer = Tokenizer("\"迷\"")
    assert tokenizer.get_tokens_as_string() == "Error Token \"迷\""

###############Literals#################

def test_floating_point_1():
    tokenizer = Tokenizer("1.0e35")
    assert tokenizer.get_tokens_as_string() == "1.0e35,<EOF>"

def test_floating_point_2():
    tokenizer = Tokenizer("1.0e-35")
    assert tokenizer.get_tokens_as_string() == "1.0e-35,<EOF>"

def test_floating_point_3():
    tokenizer = Tokenizer("-1.0e35")
    assert tokenizer.get_tokens_as_string() == "-1.0e35,<EOF>"

def test_floating_point_4():
    tokenizer = Tokenizer("-1.0e-35")
    assert tokenizer.get_tokens_as_string() == "-1.0e-35,<EOF>"

def test_floating_point_5():
    tokenizer = Tokenizer("1.0E35")
    assert tokenizer.get_tokens_as_string() == "1.0E35,<EOF>"

def test_floating_point_6():
    tokenizer = Tokenizer("1.0E-35")
    assert tokenizer.get_tokens_as_string() == "1.0E-35,<EOF>"

def test_floating_point_7():
    tokenizer = Tokenizer("-1.0E35")
    assert tokenizer.get_tokens_as_string() == "-1.0E35,<EOF>"

def test_floating_point_8():
    tokenizer = Tokenizer("-1.0E-35")
    assert tokenizer.get_tokens_as_string() == "-1.0E-35,<EOF>"

def test_floating_point_dot_1():
    tokenizer = Tokenizer("1.035")
    assert tokenizer.get_tokens_as_string() == "1.035,<EOF>"

def test_floating_point_dot_2():
    tokenizer = Tokenizer("-1.035")
    assert tokenizer.get_tokens_as_string() == "-1.035,<EOF>"

def test_floating_point_dot_3():
    tokenizer = Tokenizer(".035")
    assert tokenizer.get_tokens_as_string() == ".035,<EOF>"

def test_floating_point_dot_4():
    tokenizer = Tokenizer("-.035")
    assert tokenizer.get_tokens_as_string() == "-.035,<EOF>"

def test_floating_point_dot_5():
    tokenizer = Tokenizer("1.")
    assert tokenizer.get_tokens_as_string() == "1.,<EOF>"

def test_floating_point_dot_6():
    tokenizer = Tokenizer("-1.")
    assert tokenizer.get_tokens_as_string() == "-1.,<EOF>"

def test_floating_point_exp_1():
    tokenizer = Tokenizer("1e53")
    assert tokenizer.get_tokens_as_string() == "1e53,<EOF>"

def test_floating_point_exp_2():
    tokenizer = Tokenizer("1e-53")
    assert tokenizer.get_tokens_as_string() == "1e-53,<EOF>"

def test_floating_point_exp_3():
    tokenizer = Tokenizer("-1e53")
    assert tokenizer.get_tokens_as_string() == "-1e53,<EOF>"

def test_floating_point_exp_4():
    tokenizer = Tokenizer("-1e-53")
    assert tokenizer.get_tokens_as_string() == "-1e-53,<EOF>"

def test_floating_point_exp_5():
    tokenizer = Tokenizer("1E53")
    assert tokenizer.get_tokens_as_string() == "1E53,<EOF>"

def test_floating_point_exp_6():
    tokenizer = Tokenizer("1E-53")
    assert tokenizer.get_tokens_as_string() == "1E-53,<EOF>"

def test_floating_point_exp_7():
    tokenizer = Tokenizer("-1E53")
    assert tokenizer.get_tokens_as_string() == "-1E53,<EOF>"

def test_floating_point_exp_8():
    tokenizer = Tokenizer("-1E-53")
    assert tokenizer.get_tokens_as_string() == "-1E-53,<EOF>"

def test_floating_point_dot_exp_1():
    tokenizer = Tokenizer("1.e53")
    assert tokenizer.get_tokens_as_string() == "1.e53,<EOF>"

def test_floating_point_dot_exp_2():
    tokenizer = Tokenizer("1.e-35")
    assert tokenizer.get_tokens_as_string() == "1.e-35,<EOF>"

def test_floating_point_dot_exp_3():
    tokenizer = Tokenizer("-1.e53")
    assert tokenizer.get_tokens_as_string() == "-1.e53,<EOF>"

def test_floating_point_dot_exp_4():
    tokenizer = Tokenizer("-1.e-35")
    assert tokenizer.get_tokens_as_string() == "-1.e-35,<EOF>"

def test_floating_point_dot_exp_5():
    tokenizer = Tokenizer("1.E53")
    assert tokenizer.get_tokens_as_string() == "1.E53,<EOF>"

def test_floating_point_dot_exp_6():
    tokenizer = Tokenizer("1.E-53")
    assert tokenizer.get_tokens_as_string() == "1.E-53,<EOF>"

def test_floating_point_dot_exp_7():
    tokenizer = Tokenizer("-1.E53")
    assert tokenizer.get_tokens_as_string() == "-1.E53,<EOF>"

def test_floating_point_dot_exp_8():
    tokenizer = Tokenizer("-1.E-53")
    assert tokenizer.get_tokens_as_string() == "-1.E-53,<EOF>"

def test_floating_point_large_num_1():
    tokenizer = Tokenizer("111111111111111111111.111111111111111111111111111111111111")
    assert tokenizer.get_tokens_as_string() == "111111111111111111111.111111111111111111111111111111111111,<EOF>"

def test_floating_point_large_num_2():
    tokenizer = Tokenizer("60602351267102.e0262620")
    assert tokenizer.get_tokens_as_string() == "60602351267102.e0262620,<EOF>"

def test_floating_point_large_num_3():
    tokenizer = Tokenizer("000000000000000000000000060602351267102.e0262620")
    assert tokenizer.get_tokens_as_string() == "000000000000000000000000060602351267102.e0262620,<EOF>"

def test_floating_point_large_num_4():
    tokenizer = Tokenizer("000000000000000000000000060602351267102.")
    assert tokenizer.get_tokens_as_string() == "000000000000000000000000060602351267102.,<EOF>"

def test_err_floating_point_1():
    tokenizer = Tokenizer("E-53")
    assert tokenizer.get_tokens_as_string() == "E,-53,<EOF>"

def test_err_floating_point_2():
    tokenizer = Tokenizer(".-53")
    assert tokenizer.get_tokens_as_string() == ".,-53,<EOF>"

def test_err_floating_point_3():
    tokenizer = Tokenizer(".E53")
    assert tokenizer.get_tokens_as_string() == ".,E53,<EOF>"

def test_err_floating_point_4():
    tokenizer = Tokenizer("a.53")
    assert tokenizer.get_tokens_as_string() == "a,.53,<EOF>"

def test_err_floating_point_dot_exp_1():
    tokenizer = Tokenizer(".e53")
    assert tokenizer.get_tokens_as_string() == ".,e53,<EOF>"

def test_err_floating_point_dot_exp_2():
    tokenizer = Tokenizer(".e-35")
    assert tokenizer.get_tokens_as_string() == ".,e,-35,<EOF>"

def test_err_floating_point_dot_exp_3():
    tokenizer = Tokenizer("-.e53")
    assert tokenizer.get_tokens_as_string() == "-,.,e53,<EOF>"

def test_err_floating_point_dot_exp_4():
    tokenizer = Tokenizer("-.e-35")
    assert tokenizer.get_tokens_as_string() == "-,.,e,-35,<EOF>"

def test_err_floating_point_dot_exp_5():
    tokenizer = Tokenizer(".E53")
    assert tokenizer.get_tokens_as_string() == ".,E53,<EOF>"

def test_err_floating_point_dot_exp_6():
    tokenizer = Tokenizer(".E-53")
    assert tokenizer.get_tokens_as_string() == ".,E,-53,<EOF>"

def test_err_floating_point_dot_exp_7():
    tokenizer = Tokenizer("-.E53")
    assert tokenizer.get_tokens_as_string() == "-,.,E53,<EOF>"

def test_err_floating_point_dot_exp_8():
    tokenizer = Tokenizer("-.E-53")
    assert tokenizer.get_tokens_as_string() == "-,.,E,-53,<EOF>"

def test_integer_1():
    tokenizer = Tokenizer("10")
    assert tokenizer.get_tokens_as_string() == "10,<EOF>"

def test_integer_2():
    tokenizer = Tokenizer("035")
    assert tokenizer.get_tokens_as_string() == "035,<EOF>"

def test_integer_3():
    tokenizer = Tokenizer("350")
    assert tokenizer.get_tokens_as_string() == "350,<EOF>"

def test_integer_4():
    tokenizer = Tokenizer("000000000000000000025")
    assert tokenizer.get_tokens_as_string() == "000000000000000000025,<EOF>"

def test_integer_5():
    tokenizer = Tokenizer("250000000000000")
    assert tokenizer.get_tokens_as_string() == "250000000000000,<EOF>"

def test_integer_6():
    tokenizer = Tokenizer("2525252525252525")
    assert tokenizer.get_tokens_as_string() == "2525252525252525,<EOF>"

def test_integer_7():
    tokenizer = Tokenizer("0x35")
    assert tokenizer.get_tokens_as_string() == "0,x35,<EOF>"

def test_integer_8():
    tokenizer = Tokenizer("0b213521352")
    assert tokenizer.get_tokens_as_string() == "0,b213521352,<EOF>"

def test_integer_9():
    tokenizer = Tokenizer("00025000")
    assert tokenizer.get_tokens_as_string() == "00025000,<EOF>"

def test_integer_10():
    tokenizer = Tokenizer("0025000250025002500")
    assert tokenizer.get_tokens_as_string() == "0025000250025002500,<EOF>"

def test_integer_11():
    tokenizer = Tokenizer("0020530230620360230423")
    assert tokenizer.get_tokens_as_string() == "0020530230620360230423,<EOF>"

def test_integer_12():
    tokenizer = Tokenizer("0-3")
    assert tokenizer.get_tokens_as_string() == "0,-,3,<EOF>"

def test_string_1():
    tokenizer = Tokenizer("\"lmao\"")
    assert tokenizer.get_tokens_as_string() == "lmao,<EOF>"

def test_string_2():
    tokenizer = Tokenizer("\" \\0\\b\\t\\n\\f\\r \"")
    assert tokenizer.get_tokens_as_string() == " \\0\\b\\t\\n\\f\\r ,<EOF>"

def test_string_3():
    tokenizer = Tokenizer("\"lmao\" + \"hihi\"")
    assert tokenizer.get_tokens_as_string() == "lmao,+,hihi,<EOF>"

def test_string_4():
    tokenizer = Tokenizer("\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vel lorem urna. Sed pretium et leo vel lobortis. Quisque in neque vehicula, scelerisque nisi in, tempus nunc. Phasellus et leo dolor. Donec lacinia dictum turpis sit amet sodales. Nunc iaculis viverra dolor at mollis. Mauris id nisi ligula. Quisque nec rutrum neque. Quisque volutpat quam id nisl dignissim, vel finibus elit cursus. Aliquam volutpat, eros quis imperdiet facilisis, nunc turpis molestie libero, non suscipit orci nulla ut augue. Etiam id lorem sed odio rhoncus euismod. Pellentesque id ultricies lectus, et bibendum diam. Quisque vel dui quis libero ultrices blandit. Morbi in eros ultrices, fermentum arcu vel, ornare eros.\"")
    assert tokenizer.get_tokens_as_string() == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vel lorem urna. Sed pretium et leo vel lobortis. Quisque in neque vehicula, scelerisque nisi in, tempus nunc. Phasellus et leo dolor. Donec lacinia dictum turpis sit amet sodales. Nunc iaculis viverra dolor at mollis. Mauris id nisi ligula. Quisque nec rutrum neque. Quisque volutpat quam id nisl dignissim, vel finibus elit cursus. Aliquam volutpat, eros quis imperdiet facilisis, nunc turpis molestie libero, non suscipit orci nulla ut augue. Etiam id lorem sed odio rhoncus euismod. Pellentesque id ultricies lectus, et bibendum diam. Quisque vel dui quis libero ultrices blandit. Morbi in eros ultrices, fermentum arcu vel, ornare eros.,<EOF>"

def test_string_5():
    tokenizer = Tokenizer("\"this is a string containing tab\t\"")
    assert tokenizer.get_tokens_as_string() == "this is a string containing tab\t,<EOF>"

def test_string_6():
    tokenizer = Tokenizer("\"this is a string containing tab\\t\"")
    assert tokenizer.get_tokens_as_string() == "this is a string containing tab\\t,<EOF>"

def test_string_7():
    tokenizer = Tokenizer("\"He asked me: \\\"Where is John?\\\" \"")
    assert tokenizer.get_tokens_as_string() == "He asked me: \\\"Where is John?\\\" ,<EOF>"

def test_string_8():
    tokenizer = Tokenizer("\"Many people ask: Is Pyosik a god? \\t I find the question fascinating.\\n Let's redefine: What's a god? A god is one people believe in \t - \t someone who we can care for, cheer for \t - \t and many believe in Pyosik.\"")
    assert tokenizer.get_tokens_as_string() == "Many people ask: Is Pyosik a god? \\t I find the question fascinating.\\n Let's redefine: What's a god? A god is one people believe in \t - \t someone who we can care for, cheer for \t - \t and many believe in Pyosik.,<EOF>"

def test_string_9():
    tokenizer = Tokenizer("\"\fThis is a form feed. \\f This is also a form feed.\"")
    assert tokenizer.get_tokens_as_string() == "\fThis is a form feed. \\f This is also a form feed.,<EOF>"

def test_string_10():
    tokenizer = Tokenizer("\"\bThis is a backspace. \\b This is also a backspace.\"")
    assert tokenizer.get_tokens_as_string() == "\bThis is a backspace. \\b This is also a backspace.,<EOF>"

def test_string_11():
    tokenizer = Tokenizer("\"\\\\This is a backslash.\"")
    assert tokenizer.get_tokens_as_string() == "\\\\This is a backslash.,<EOF>"

def test_string_illegal_escape_1():
    tokenizer = Tokenizer("\"\\ \"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\ "

def test_string_illegal_escape_2():
    tokenizer = Tokenizer("\"\\g lmao\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\g"

def test_string_illegal_escape_3():
    tokenizer = Tokenizer("\"\\glmao\"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\g"

def test_string_illegal_escape_4():
    tokenizer = Tokenizer("\"asdgsdg \\a asdgasdg     \"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: asdgsdg \\a"

def test_string_illegal_escape_5():
    tokenizer = Tokenizer("\"\\x01 \"")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\x"

def test_string_unclosed_string_1():
    tokenizer = Tokenizer("\"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: "

def test_string_unclosed_string_2():
    tokenizer = Tokenizer("\"\"\"")
    assert tokenizer.get_tokens_as_string() == ",Unclosed String: "

def test_string_unclosed_string_3():
    tokenizer = Tokenizer("\"\"\"\"\"")
    assert tokenizer.get_tokens_as_string() == ",,Unclosed String: "

def test_string_unclosed_string_4():
    tokenizer = Tokenizer("\"lmao\"\"\"\"")
    assert tokenizer.get_tokens_as_string() == "lmao,,Unclosed String: "

def test_string_unclosed_string_5():
    tokenizer = Tokenizer("\"lmao\"\"\"\"   ")
    assert tokenizer.get_tokens_as_string() == "lmao,,Unclosed String:    "

def test_string_unclosed_string_6():
    tokenizer = Tokenizer("\" \r \"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String:  \r"

def test_string_unclosed_string_7():
    tokenizer = Tokenizer("\" \n \"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String:  \n"

def test_string_unclosed_string_8():
    tokenizer = Tokenizer("\" \r\n \"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String:  \r"

def test_string_unclosed_string_9():
    tokenizer = Tokenizer("\"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: "

def test_string_unclosed_string_10():
    tokenizer = Tokenizer("\" this is an unclosed string \n \"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String:  this is an unclosed string \n"

def test_string_unclosed_string_11():
    tokenizer = Tokenizer("\"employment is dead\r\"")
    assert tokenizer.get_tokens_as_string() == "Unclosed String: employment is dead\r"

def test_string_both_err_1():
    tokenizer = Tokenizer("\"\\g lmao   ")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String: \\g"

def test_string_both_err_2():
    tokenizer = Tokenizer("\" some text \\l")
    assert tokenizer.get_tokens_as_string() == "Illegal Escape In String:  some text \\l"

###############Expressions#################

def test_func_1():
    tokenizer = Tokenizer("lmao();")
    assert tokenizer.get_tokens_as_string() == "lmao,(,),;,<EOF>"

def test_func_2():
    tokenizer = Tokenizer("(a+lmao)();")
    assert tokenizer.get_tokens_as_string() == "(,a,+,lmao,),(,),;,<EOF>"

def test_func_3():
    tokenizer = Tokenizer("(a)();")
    assert tokenizer.get_tokens_as_string() == "(,a,),(,),;,<EOF>"

def test_func_4():
    tokenizer = Tokenizer("(a-lmao)();")
    assert tokenizer.get_tokens_as_string() == "(,a,-,lmao,),(,),;,<EOF>"

def test_func_5():
    tokenizer = Tokenizer("(a*lmao)();")
    assert tokenizer.get_tokens_as_string() == "(,a,*,lmao,),(,),;,<EOF>"

def test_func_6():
    tokenizer = Tokenizer("(_3535)();")
    assert tokenizer.get_tokens_as_string() == "(,_3535,),(,),;,<EOF>"

def test_func_7():
    tokenizer = Tokenizer("(_3535_)();")
    assert tokenizer.get_tokens_as_string() == "(,_3535_,),(,),;,<EOF>"

def test_func_8():
    tokenizer = Tokenizer("(_asg34)();")
    assert tokenizer.get_tokens_as_string() == "(,_asg34,),(,),;,<EOF>"

def test_func_9():
    tokenizer = Tokenizer("a+3();")
    assert tokenizer.get_tokens_as_string() == "a,+,3,(,),;,<EOF>"

def test_ass_1():
    tokenizer = Tokenizer("a=b=c;")
    assert tokenizer.get_tokens_as_string() == "a,=,b,=,c,;,<EOF>"

def test_ass_2():
    tokenizer = Tokenizer("a+b=c;")
    assert tokenizer.get_tokens_as_string() == "a,+,b,=,c,;,<EOF>"

def test_ass_3():
    tokenizer = Tokenizer("a=b=c=b=s=g=3=4;")
    assert tokenizer.get_tokens_as_string() == "a,=,b,=,c,=,b,=,s,=,g,=,3,=,4,;,<EOF>"

def test_ass_4():
    tokenizer = Tokenizer("a+b+d+f=4;")
    assert tokenizer.get_tokens_as_string() == "a,+,b,+,d,+,f,=,4,;,<EOF>"

def test_ass_5():
    tokenizer = Tokenizer("a+b+d+_sfdg=4;")
    assert tokenizer.get_tokens_as_string() == "a,+,b,+,d,+,_sfdg,=,4,;,<EOF>"

def test_ass_6():
    tokenizer = Tokenizer("a=4+35=sg;")
    assert tokenizer.get_tokens_as_string() == "a,=,4,+,35,=,sg,;,<EOF>"

def test_add_1():
    tokenizer = Tokenizer("3+5")
    assert tokenizer.get_tokens_as_string() == "3,+,5,<EOF>"

def test_add_2():
    tokenizer = Tokenizer("a+b")
    assert tokenizer.get_tokens_as_string() == "a,+,b,<EOF>"

def test_add_3():
    tokenizer = Tokenizer("a++b")
    assert tokenizer.get_tokens_as_string() == "a,++,b,<EOF>"

def test_add_4():
    tokenizer = Tokenizer("a+4")
    assert tokenizer.get_tokens_as_string() == "a,+,4,<EOF>"

def test_add_4():
    tokenizer = Tokenizer("a+4\t")
    assert tokenizer.get_tokens_as_string() == "a,+,4,<EOF>"

def test_min_1():
    tokenizer = Tokenizer("3-5")
    assert tokenizer.get_tokens_as_string() == "3,-5,<EOF>"

def test_min_2():
    tokenizer = Tokenizer("a=3-5")
    assert tokenizer.get_tokens_as_string() == "a,=,3,-5,<EOF>"

def test_mult():
    tokenizer = Tokenizer("3*5")
    assert tokenizer.get_tokens_as_string() == "3,*,5,<EOF>"

def test_div():
    tokenizer = Tokenizer("3/5")
    assert tokenizer.get_tokens_as_string() == "3,/,5,<EOF>"

def test_mod():
    tokenizer = Tokenizer("3%5")
    assert tokenizer.get_tokens_as_string() == "3,%,5,<EOF>"

def test_or():
    tokenizer = Tokenizer("3||5")
    assert tokenizer.get_tokens_as_string() == "3,||,5,<EOF>"

def test_and():
    tokenizer = Tokenizer("3&&5")
    assert tokenizer.get_tokens_as_string() == "3,&&,5,<EOF>"

def test_eq():
    tokenizer = Tokenizer("3==5")
    assert tokenizer.get_tokens_as_string() == "3,==,5,<EOF>"

def test_neq():
    tokenizer = Tokenizer("3!=5")
    assert tokenizer.get_tokens_as_string() == "3,!=,5,<EOF>"

def test_less():
    tokenizer = Tokenizer("3<5")
    assert tokenizer.get_tokens_as_string() == "3,<,5,<EOF>"

def test_leq():
    tokenizer = Tokenizer("3<=5")
    assert tokenizer.get_tokens_as_string() == "3,<=,5,<EOF>"

def test_great():
    tokenizer = Tokenizer("3>5")
    assert tokenizer.get_tokens_as_string() == "3,>,5,<EOF>"

def test_geq():
    tokenizer = Tokenizer("3>=5")
    assert tokenizer.get_tokens_as_string() == "3,>=,5,<EOF>"

def test_mem_acc():
    tokenizer = Tokenizer("mindy.high")
    assert tokenizer.get_tokens_as_string() == "mindy,.,high,<EOF>"

def test_inc_1():
    tokenizer = Tokenizer("++a")
    assert tokenizer.get_tokens_as_string() == "++,a,<EOF>"

def test_inc_2():
    tokenizer = Tokenizer("a++")
    assert tokenizer.get_tokens_as_string() == "a,++,<EOF>"

def test_dec_1():
    tokenizer = Tokenizer("--a")
    assert tokenizer.get_tokens_as_string() == "--,a,<EOF>"

def test_dec_2():
    tokenizer = Tokenizer("a--")
    assert tokenizer.get_tokens_as_string() == "a,--,<EOF>"

###############Seperators#################

def test_round_brack():
    tokenizer = Tokenizer("()")
    assert tokenizer.get_tokens_as_string() == "(,),<EOF>"

def test_square_brack():
    tokenizer = Tokenizer("[]")
    assert tokenizer.get_tokens_as_string() == "[,],<EOF>"

def test_curly_brack():
    tokenizer = Tokenizer("{}")
    assert tokenizer.get_tokens_as_string() == "{,},<EOF>"

def test_curly_brack_2():
    tokenizer = Tokenizer("Point p = {10, 20}")
    assert tokenizer.get_tokens_as_string() == "Point,p,=,{,10,,,20,},<EOF>"

def test_curly_brack_3():
    tokenizer = Tokenizer("Point p = {{{{{}}}}}")
    assert tokenizer.get_tokens_as_string() == "Point,p,=,{,{,{,{,{,},},},},},<EOF>"

def test_colon_semicolon_comma():
    tokenizer = Tokenizer(";,:")
    assert tokenizer.get_tokens_as_string() == ";,,,:,<EOF>"

###############Keywords#################

def test_keyword_1():
    tokenizer = Tokenizer("int a")
    assert tokenizer.get_tokens_as_string() == "int,a,<EOF>"

def test_keyword_2():
    tokenizer = Tokenizer("string b")
    assert tokenizer.get_tokens_as_string() == "string,b,<EOF>"

def test_keyword_3():
    tokenizer = Tokenizer("float c")
    assert tokenizer.get_tokens_as_string() == "float,c,<EOF>"

def test_keyword_4():
    tokenizer = Tokenizer("lmao d")
    assert tokenizer.get_tokens_as_string() == "lmao,d,<EOF>"

def test_keyword_5():
    tokenizer = Tokenizer("auto d = 3.5")
    assert tokenizer.get_tokens_as_string() == "auto,d,=,3.5,<EOF>"

def test_keyword_6():
    tokenizer = Tokenizer("break;")
    assert tokenizer.get_tokens_as_string() == "break,;,<EOF>"

def test_keyword_7():
    tokenizer = Tokenizer("case true:")
    assert tokenizer.get_tokens_as_string() == "case,true,:,<EOF>"

def test_keyword_8():
    tokenizer = Tokenizer("continue;")
    assert tokenizer.get_tokens_as_string() == "continue,;,<EOF>"

def test_keyword_9():
    tokenizer = Tokenizer("if(){}else{};")
    assert tokenizer.get_tokens_as_string() == "if,(,),{,},else,{,},;,<EOF>"

def test_keyword_10():
    tokenizer = Tokenizer("return;")
    assert tokenizer.get_tokens_as_string() == "return,;,<EOF>"

def test_keyword_11():
    tokenizer = Tokenizer("struct Point;")
    assert tokenizer.get_tokens_as_string() == "struct,Point,;,<EOF>"

def test_keyword_12():
    tokenizer = Tokenizer("switch();")
    assert tokenizer.get_tokens_as_string() == "switch,(,),;,<EOF>"

###############Error Char#################
def test_error_char_1():
    tokenizer = Tokenizer("\"がんばって\"")
    assert tokenizer.get_tokens_as_string() == "Error Token \"がんばって\""
















