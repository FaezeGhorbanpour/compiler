# Generated from MyGrammar.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammarParser import MyGrammarParser
else:
    from MyGrammarParser import MyGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammarParser.

class MyGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammarParser#program.
    def visitProgram(self, ctx:MyGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#lowercasenumber.
    def visitLowercasenumber(self, ctx:MyGrammarParser.LowercasenumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#name.
    def visitName(self, ctx:MyGrammarParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#method.
    def visitMethod(self, ctx:MyGrammarParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#funcall.
    def visitFuncall(self, ctx:MyGrammarParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#assign.
    def visitAssign(self, ctx:MyGrammarParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#kind.
    def visitKind(self, ctx:MyGrammarParser.KindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#operands.
    def visitOperands(self, ctx:MyGrammarParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#deffunc.
    def visitDeffunc(self, ctx:MyGrammarParser.DeffuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#integer.
    def visitInteger(self, ctx:MyGrammarParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#doub.
    def visitDoub(self, ctx:MyGrammarParser.DoubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#dat.
    def visitDat(self, ctx:MyGrammarParser.DatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#arg.
    def visitArg(self, ctx:MyGrammarParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#expr.
    def visitExpr(self, ctx:MyGrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#plusexpr.
    def visitPlusexpr(self, ctx:MyGrammarParser.PlusexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#multexpr.
    def visitMultexpr(self, ctx:MyGrammarParser.MultexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#expression.
    def visitExpression(self, ctx:MyGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#args.
    def visitArgs(self, ctx:MyGrammarParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammarParser#functions.
    def visitFunctions(self, ctx:MyGrammarParser.FunctionsContext):
        return self.visitChildren(ctx)



del MyGrammarParser