from lexer import Lexer
import io
from parserTB import Parser

<<<<<<< HEAD
text_input = """Division @ dasdsd,,
"""
||||||| merged common ancestors
text_input = """Division @
"""
=======

text_input = """Beginning;
Division@x{Ire@decrease;Ire@x;};End."""
>>>>>>> 37245ed03d7b298c88fe94307f8a591040e3fb3d
new_input=""""""
#for removing commented words
for y in text_input.splitlines():
    if("/-" in y):
        new_input = new_input+y[0:y.find("/-")+2]+"\n"
        #print(y[0:y.find("/-")+2])
    else:
        new_input = new_input + y + "\n"
lexer = Lexer().get_lexer()
line_no = 1
tokens = lexer.lex(new_input)
d ={1: ["Line No", "Lexeme","Return Token","Lexeme No in Line","Matchability"]}
i = 2
lexemer = 1
errors = 0

for y in new_input.splitlines():
    for token in lexer.lex(y):
        #tokens = lexer.lex(y)
        #print(lexer)
        if(token.gettokentype() != "ERROR"):
          d[i]=[line_no, token.getstr(),token.gettokentype(),lexemer,"Matchable"]

        else:
         d[i] = [line_no, token.getstr(), token.gettokentype(), lexemer, "Non Matchable"]
         errors = errors + 1
        i = i+1
        lexemer = lexemer +1
    line_no = line_no +1
    lexemer = 1

for k, v in d.items():
 line=v
 print ("{:<15} {:<20} {:<30} {:<35} {:<20}".format(line[0], line[1], line[2],line[3],line[4]))
print ("\nNUMBER OF ERROR ",errors)

<<<<<<< HEAD
# pg = Parser()
# pg.parse()
# parser = pg.get_parser()
# parser.parse(tokens)
||||||| merged common ancestors

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)
=======
pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()



>>>>>>> 37245ed03d7b298c88fe94307f8a591040e3fb3d
