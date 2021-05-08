from rply import ParserGenerator
from ast import Number, Sum, Print,Diff,Times,Div


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['Class', 'Inheritance', 'Condition', 'Integer',
             'Character', 'String', 'Float', 'SFloat', 'Void',
             'Break','Loop','Return','Struct','Switch','Start Statement',
             'End Statement','Comment','Arithmetic Operation','Logic operators',
             'relational operators','Assignment operator','Access operator','Braces'
             ,'Quotation Mark','Inclusion','Delimiter','Constant','IDENTIFIER']
        )

    @self.pg.production(':')
    def parse(self):
        #some rules and tokens share same name like conidition, what is the token for () ,  extra spaces for no reason ex 24 after expression and ;
        #1
        @self.pg.production('Program : Start Statement ClassDeclaration Delimiter End Statement Access Operator')
        @self.pg.production('Program : Comment Delimiter using_command')
        def Program(P):
            print("matched Program")

        #2
        # id -> what is id
        @self.pg.production('ClassDeclaration : Class Delimiter ID Braces Class_Implementation Braces')
        @self.pg.production('ClassDeclaration : Class Delimiter ID Delimiter Inheritance Braces Class_Implementation Braces')
        def ClassDeclaration(P):
            print("matched ClassDeclaration")

        #3
        @self.pg.production('Class_Implementation : VarDeclaration Class_Implementation')
        @self.pg.production('Class_Implementation : MethodDeclaration Class_Implementation')
        @self.pg.production('Class_Implementation : Comment Class_Implementation')
        @self.pg.production('Class_Implementation : Func _Call Class_Implementation')
        #empty idk what it is
        @self.pg.production('empty')
        def Class_Implementation(P):
            print("matched Class_Implementation")

        #4
        #extra space after decl
        @self.pg.production('MethodDeclaration : Func Decl Delimiter')
        @self.pg.production('MethodDeclaration : Func Decl Braces VarDeclaration Statements Braces')
        def MethodDeclaration(P):
            print("matched MethodDeclaration")

        #5
        #extra space after @
        @self.pg.production('Func Decl : Type Delimiter ID relational operators ParameterList relational operators')
        def FuncDecl(P):
            print("matched Func Decl")

        #6
        @self.pg.production('Type : Integer')
        @self.pg.production('Type : SInteger')
        @self.pg.production('Type : Clo')
        @self.pg.production('Type : SetOfClo')
        @self.pg.production('Type : FBU')
        @self.pg.production('Type : SFBU')
        @self.pg.production('Type : NoneValue')
        def Type(P):
            print("matched Type")

        #7
        #empty idk what it is
        @self.pg.production('ParameterList : empty')
        @self.pg.production('ParameterList : NoneValue')
        @self.pg.production('ParameterList : Non-Empty List')
        def ParameterList(P):
            print("matched ParameterList")

        #8
        #extra space after @
        @self.pg.production('Non-Empty List : Type Delimiter ID')
        #what is  ,
        @self.pg.production('Non-Empty List : Non-Empty List , Type Delimiter ID')
        def Non-EmptyList(P):
            print("matched Non-Empty List")

        #9
        #idk what is empty
        @self.pg.production('VarDeclaration : empty')
        @self.pg.production('VarDeclaration : Type Delimiter ID_List Delimiter VarDeclaration')
        def VarDeclaration(P):
            print("matched VarDeclaration")

        #10
        @self.pg.production('ID_List : ID')
        #what id ID and Comma
        @self.pg.production('ID_List : ID_List , ID')
        def ID_List(P):
            print("matched ID_List")

        #11
        #what is empty
        @self.pg.production('Statements : empty')
        @self.pg.production('Statements : Statement Statements')
        def Statements(P):
            print("matched Statements")

        #12
        #what is ID
        @self.pg.production('Statement : Assignment')
        @self.pg.production('Statement : WhetherDo_Statement')
        @self.pg.production('Statement : RingWhen_Statement')
        @self.pg.production('Statement : BackedValue_Statement')
        @self.pg.production('Statement : terminatethis _Statement')
        @self.pg.production('Statement : read Braces ID Braces Delimiter')
        @self.pg.production('Statement : write Braces Expression Braces Delimiter')
        def Statement(P):
             print("matched Statement")

        #13
        @self.pg.production('Assignment : VarDeclaration Assignment operator Expression Delimiter')
        def Assignment(P):
            print("matched Assignment")

        #14
        #what is ID
        @self.pg.production('Func _Call : ID Braces Argument_List Braces Delimiter')
        def Func_Call(P):
            print("matched Func _Call")

        #15
        @self.pg.production('Argument_List : empty')
        @self.pg.production('Argument_List : NonEmpty_Argument_List')
        def Argument_List(P):
            print("matched Argument_List")

        #16
        #what is comma
        @self.pg.production('NonEmpty_Argument_List : Expression')
        @self.pg.production('NonEmpty_Argument_List : NonEmpty_Argument_List , Expression')
        def onEmpty_Argument_List(P):
            print("matched onEmpty_Argument_List")
        #17
        @self.pg.production('Block Statements : Braces Statements Braces')
        def BlockStatements(P):
            print("matched Block Statements")

        #18
        @self.pg.production('WhetherDo_Statement : Condition Arithmetic Operation Condition_Expression Arithmetic Operation Block Statements Condition Statement')
        def WhetherDo_Statement(P):
            print("matched WhetherDo_Statement")

        #19
        @self.pg.production('Condition_Expression : Condition')
        @self.pg.production('Condition_Expression : Condition Condition_Op Condition')
        def Condition_Expression(P):
            print("matched  Condition_Expression")

        #20
        # and | or not not token nor rule but there is && || which is logic operators
        @self.pg.production('Condition_Op : Logic operators')
        def Condition_Op(P):
            print("matched  Condition_Op)

        #21
        @self.pg.production('Condition : Expression Comparison_Op Expression Constant Access Operator')
        def Condition(P):
                print("matched  Condition)

        #22
        @self.pg.production('Comparison_Op : relational operators')
        def Comparison_Op(P):
            print("matched  Comparison_Op)

        #23
        # () is not defiend
        @self.pg.production('RingWhen_Statement : Loop ( Condition _Expression ) Block Statements Condition Statement')
        def RingWhen_Statement(P):
            print("matched  RingWhen_Statement)

        #24
        #extra space after backed value
        @self.pg.production('BackedValue_Statement : Return Delimiter Expression Delimiter')
        @self.pg.production('BackedValue_Statement : Return Delimiter ID Expression Delimiter')
        def BackedValue_Statement(P):
            print("matched  BackedValue_Statement)

        #25
        @self.pg.production('terminatethis_Statement : Break Delimiter')
        def terminatethis_Statement(P):
            print("matched  terminatethis_Statement)

        #26
        @self.pg.production('Expression : Term')
        @self.pg.production('Expression : Expression Delimiter Add_Op Delimiter Term')
        def Expression(P):
            print("matched  Expression)

        #27
        @self.pg.production('Add_Op : Arithmetic Operation')
        def Add_Op(P):
            print("matched  Add_Op)

       #28
       @self.pg.production('Term : Factor')
       @self.pg.production('Term : Term Delimiter Mul_Op Delimiter Factor')
       def Term(P):
            print("matched  Term)

       #29
       @self.pg.production('Mul_Op : Arithmetic Operation')
       def Mul_Op(P):
            print("matched  Mul_Op)

       #30
       #what is number , id
       @self.pg.production('Factor : ID')
       @self.pg.production('Factor : Number')
       def Factor(P):
            print("matched  Factor)



       #31
       #what is STR
       @self.pg.production('Comment : Comment STR Comment')
       @self.pg.production('Comment : Comment STR Comment')
       @self.pg.production('Comment : Comment STR')
       def Comment(P):
            print("matched  Comment)

       #32
       #what is () and f_name.txt represent or meanly txt
       @self.pg.production('using_command :  Inclusion (F_name Access Operator txt) Delimiter')
       def using_command(P):
            print("matched  using_command)

       #33
       #what is  STR
       @self.pg.production('F_name : STR')
       def F_name(P):
            print("matched  F_name)

       @self.pg.error
       def error_handle(token):
           raise ValueError(token)

       def get_parser(self):
           return self.pg.build()























































         @self.pg.production('expression : expression DIFF expression')
         @self.pg.production('expression : expression TIMES expression')
         @self.pg.production('expression : expression DIVIDE expression')
         @self.pg.production('expression : expression SUM expression')
         def expression(p):
             left = p[0]
             right = p[2]
             operator = p[1]
             if operator.gettokentype() == 'SUM':
                 return Sum(left, right)
             elif p[1].gettokentype() == 'DIFF':
                 return Sub(left, right)
             elif p[1].gettokentype() == 'TIMES':
                 return Mul(left, right)
             elif p[1].gettokentype() == 'DIVIDE':
                return Div(left, right)
             else:
                raise AssertionError('error!')

         @self.pg.production('expression : NUMBER')
         def number(p):
             Number(int(p[0].getstr()))


         @self.pg.error
         def error_handle(token):
            raise ValueError(token)

         def get_parser(self):
            return self.pg.build()