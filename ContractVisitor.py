# Generated from Contract.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ContractParser import ContractParser
else:
    from ContractParser import ContractParser

# This class defines a complete generic visitor for a parse tree produced by ContractParser.

class ContractVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ContractParser#program.
    def visitProgram(self, ctx:ContractParser.ProgramContext):
        return self.visitChildren(ctx)



del ContractParser