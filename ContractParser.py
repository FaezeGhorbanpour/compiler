# Generated from Contract.g by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3&")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\5\2\4\3\2\2\2\4\5\7")
        buf.write("\26\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class ContractParser ( Parser ):

    grammarFileName = "Contract.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Double'", "'Int'", "'Date'", 
                     "'Contract'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'->'", "'::'", "'('", "')'", "'one'", "','", "'='", 
                     "'TimeFunct'", "'mkDate'", "'give'" ]

    symbolicNames = [ "<INVALID>", "LOWERCASE", "DOUBLE", "INT", "DATE", 
                      "CONTRACT", "NUMBERS", "OPERANDS", "FUNCTIONS", "TO", 
                      "ASSIGNMENT", "LPAREN", "RPAREN", "ONE", "COMMA", 
                      "EQUAL", "TIMEFUNCT", "MKDATE", "GIVE", "WS", "Prog", 
                      "TYPES", "Name", "Type", "Deffunc", "Defvar", "Def", 
                      "Assign", "Int", "Double", "Date", "Expr", "Felan", 
                      "Expression", "Args", "Arg", "Funccall" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    LOWERCASE=1
    DOUBLE=2
    INT=3
    DATE=4
    CONTRACT=5
    NUMBERS=6
    OPERANDS=7
    FUNCTIONS=8
    TO=9
    ASSIGNMENT=10
    LPAREN=11
    RPAREN=12
    ONE=13
    COMMA=14
    EQUAL=15
    TIMEFUNCT=16
    MKDATE=17
    GIVE=18
    WS=19
    Prog=20
    TYPES=21
    Name=22
    Type=23
    Deffunc=24
    Defvar=25
    Def=26
    Assign=27
    Int=28
    Double=29
    Date=30
    Expr=31
    Felan=32
    Expression=33
    Args=34
    Arg=35
    Funccall=36

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Prog(self):
            return self.getToken(ContractParser.Prog, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ContractParser.Prog)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





