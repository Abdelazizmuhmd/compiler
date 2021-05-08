from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('Class', r'Division')
        self.lexer.add('Inheritance', r'InferedFrom')
        self.lexer.add('Condition', r'WhetherDo')
        self.lexer.add('Condition', r'Else')
        self.lexer.add('Integer', r'Ire')
        self.lexer.add('Condition', r'Sire')
        self.lexer.add('Character', r'Clo')
        self.lexer.add('String', r'SetOfClo')
        self.lexer.add('Float', r'FBU')
        self.lexer.add('SFloat', r'SFBU')
        self.lexer.add('Void', r'NoneValue')
        self.lexer.add('Break', r'TerminateThisNow')
        self.lexer.add('Loop', r'RingWhen')
        self.lexer.add('Return', r'BackedValue')
        self.lexer.add('Struct', r'STT')
        self.lexer.add('Switch', r'Check')
        self.lexer.add('Switch', r'CaseOf')
        self.lexer.add('Start Statement', r'Beginning')
        self.lexer.add('End Statement', r'End')
        self.lexer.add('Comment', r'\/#')
        self.lexer.add('Comment', r'\#/')
        self.lexer.add('Comment', r'/-')
        self.lexer.add('Arithmetic Operation', r'[+*\/-]')
        self.lexer.add('Logic operators', r'\&&')
        self.lexer.add('Logic operators', r'\|{2}')
        self.lexer.add('Logic operators', r'\~')
        self.lexer.add('relational operators', r'\==')
        self.lexer.add('relational operators', r'<=')
        self.lexer.add('relational operators', r'>=')
        self.lexer.add('relational operators', r'\<')
        self.lexer.add('relational operators', r'\>')
        self.lexer.add('relational operators', r'\!=')
        # self.lexer.add('relational operators', r'^(<=)$')
        # self.lexer.add('relational operators', r'^(>=)$')
        self.lexer.add('Assignment operator', r'\=')
        self.lexer.add('Access operator', r'\.')
        self.lexer.add('Braces', r'\[')
        self.lexer.add('Braces', r'\]')
        self.lexer.add('Braces', r'\{')
        self.lexer.add('Braces', r'\}')
        self.lexer.add('Quotation Mark', r'\"')
        self.lexer.add('Inclusion', r'Using')
        self.lexer.add('Delimiter', r'\@')
        self.lexer.add('Delimiter', r'\;')
        self.lexer.add('Constant', r'\d+')
        #self.lexer.add('IDENTIFIER',r'^[a-zA-Z|_].([a-zA-Z-|_-|0-9])')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        # Operators
        #self.lexer.add('SUM', r'\+')
        #self.lexer.add('DIFF', r'\-')
        #self.lexer.add('TIMES', r'\*')
        #self.lexer.add('DIVIDE', r'\/')

        # Ignore spaces
        self.lexer.ignore('\s+')
        self.lexer.add('IDENTIFIER', r'[a-zA-Z|_].([a-zA-Z0-9|_])*')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()