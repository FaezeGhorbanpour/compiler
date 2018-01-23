from antlr4 import *

from MyGrammarLexer import MyGrammarLexer
from MyGrammarParser import MyGrammarParser


def print_tree(tree, lev):
    print((" " * lev) + "` " + str(tree))
    for c in tree.getChildren():
        print_tree(c, lev + 1)





def main(code):
    codeStream = InputStream(code)
    lexer = MyGrammarLexer(codeStream)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
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