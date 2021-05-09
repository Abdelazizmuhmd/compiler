from lexer import Lexer
import io
from parserTB import Parser



text_input = """Beginning;
Division@x{Ire@decrease;Ire@x;};End."""
new_input=""""""
#for removing commented words
for y in text_input.splitlines():
    if("/-" in y):
        new_input = new_input+y[0:y.find("/-")+2]+"\n"
        #print(y[0:y.find("/-")+2])
    #elif('/#' in y and '#/' in y):
     #   new_input = new_input+y[0:y.find("/#")+2]+y[(y.find("#/")):]+"\n"
    else:
        new_input = new_input + y + "\n"
if('/#' in new_input and '#/' in new_input):
    new_input = new_input.replace(new_input[(new_input.find("/#")+2):new_input.find("#/")],"")
print(new_input)

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
print ("\nNUMBER OF ERROR ",errors,"\n")

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens)



