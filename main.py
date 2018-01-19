from antlr4 import *
from ContractLexer import ContractLexer
from ContractListener import ContractListener
from ContractParser import ContractParser
import sys


def handleExpression(expr, parser):
    print(expr.toStringTree(recog=parser))
    for child in expr.getChildren():
        print(child.getRuleIndex())
        print(child.toStringTree())
        print(child.children)

def print_tree(tree, lev):
    print(" " * lev) + "` " + str(tree)
    for c in tree.getChildren():
        print_tree(c, lev + 1)





def main(code):
    codeStream = InputStream(code)
    lexer = ContractLexer(codeStream)
    stream = CommonTokenStream(lexer)
    parser = ContractParser(stream)
    tree = parser.program()
    print_tree(parser.program().tree, 0)
    handleExpression(tree, parser)


if __name__ == '__main__':
    codes, code = '', input()
    try:
        while 'END' not in code:
            codes += code + '\n'
            code = input()
        main(codes[:-1])
    except:
        pass