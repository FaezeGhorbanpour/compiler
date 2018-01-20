# Generated from Contract.g4 by ANTLR 4.5.3
# encoding: utf-8
from io import StringIO

from antlr4 import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\60")
        buf.write("\n\4\2\t\2\3\2\6\2\6\n\2\r\2\16\2\7\3\2\2\2\3\2\2\3\4")
        buf.write("\2%&\60\60\t\2\5\3\2\2\2\4\6\t\2\2\2\5\4\3\2\2\2\6\7\3")
        buf.write("\2\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b\3\3\2\2\2\3\7")
        return buf.getvalue()


class ContractParser ( Parser ):
    grammarFileName = "Contract.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Double'", "'Int'", "'Date'",
                     "'Contract'", "<INVALID>", "<INVALID>", "'+'", "'-'",
                     "'*'", "'/'", "'and'", "'or'", "'then'", "'scalaX'",
                     "'scala'", "'truncate'", "'->'", "'::'", "'('", "')'",
                     "'one'", "','", "'.'", "'='", "'TimeFunct'", "'mkDate'",
                     "'give'"]

    symbolicNames = [ "<INVALID>", "LOWERCASE", "DOUBLE", "INT", "DATE",
                      "CONTRACT", "NUMBER", "LOWERCASE_NUMBER", "PLUS",
                      "MINUS", "TIMES", "DIV", "AND", "OR", "THEN", "SCALAX",
                      "SCALA", "TRUNCATE", "TO", "ASSIGNMENT", "LPAREN",
                      "RPAREN", "ONE", "COMMA", "DOT", "EQUAL", "TIMEFUNCT",
                      "MKDATE", "GIVE", "WS", "Name", "Type", "Operands",
                      "Deffunc", "Defvar", "Def", "Assign", "Int", "Double",
                      "Date", "Expr", "Felan", "Expression", "Args", "Arg",
                      "Functions", "Funccall"]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    LOWERCASE=1
    DOUBLE=2
    INT=3
    DATE=4
    CONTRACT=5
    NUMBER = 6
    LOWERCASE_NUMBER = 7
    PLUS = 8
    MINUS = 9
    TIMES = 10
    DIV = 11
    AND = 12
    OR = 13
    THEN = 14
    SCALAX = 15
    SCALA = 16
    TRUNCATE = 17
    TO = 18
    ASSIGNMENT = 19
    LPAREN = 20
    RPAREN = 21
    ONE = 22
    COMMA = 23
    DOT = 24
    EQUAL = 25
    TIMEFUNCT = 26
    MKDATE = 27
    GIVE = 28
    WS = 29
    Name = 30
    Type = 31
    Operands = 32
    Deffunc = 33
    Defvar = 34
    Def = 35
    Assign = 36
    Int = 37
    Double = 38
    Date = 39
    Expr = 40
    Felan = 41
    Expression = 42
    Args = 43
    Arg = 44
    Functions = 45
    Funccall = 46

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Assign(self, i: int = None):
            if i is None:
                return self.getTokens(ContractParser.Assign)
            else:
                return self.getToken(ContractParser.Assign, i)

        def Funccall(self, i: int = None):
            if i is None:
                return self.getTokens(ContractParser.Funccall)
            else:
                return self.getToken(ContractParser.Funccall, i)

        def Def(self, i: int = None):
            if i is None:
                return self.getTokens(ContractParser.Def)
            else:
                return self.getToken(ContractParser.Def, i)

        def getRuleIndex(self):
            return ContractParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ContractParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 3
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << ContractParser.Def) | (1 << ContractParser.Assign) | (
                    1 << ContractParser.Funccall))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 5
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << ContractParser.Def) | (1 << ContractParser.Assign) | (
                    1 << ContractParser.Funccall))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





