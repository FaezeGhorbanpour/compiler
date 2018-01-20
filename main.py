from antlr4 import *

from ContractLexer import ContractLexer
from ContractParser import ContractParser


def print_tree(tree, lev):
    print((" " * lev) + "` " + str(tree))
    for c in tree.getChildren():
        print_tree(c, lev + 1)





def main(code):
    codeStream = InputStream(code)
    lexer = ContractLexer(codeStream)
    stream = CommonTokenStream(lexer)
    parser = ContractParser(stream)
    tree = parser.program()
    print_tree(tree, 0)
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    codes, code = '', input()
    try:
        while 'END' not in code:
            codes += code + '\n'
            code = input()
        main(codes[:-1])
    except:
        pass