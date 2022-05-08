from inspect import Parameter
from prompt_toolkit import PromptSession
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.sql import SqlLexer

# highlight sql statements
# use pygments library for coloring 
# lexer Parameter lets us to set the syntax  lexer 
# sqlLexer for highlighting 

def main():
    session = PromptSession(lexer=PygmentsLexer(SqlLexer))

    while True:
        try:
            text = session.prompt('> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            print('You entered: ', text)
        print('Goodbye!')

main()