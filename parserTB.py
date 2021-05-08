from rply import ParserGenerator
from ast import Number, Sum, Print,Diff,Times,Div


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['Class', 'Inheritance', 'CONDITION', 'Integer',
             'Character', 'String', 'Float', 'SFloat', 'Void',
             'Break','Loop','Return','Struct','Switch','Start_Statement',
             'End_Statement','Comment','Arithmetic_Operation','Logic_operators',
             'relational_operators','Assignment_operator','Access_operator','Braces'
             ,'Quotation_Mark','Inclusion','Delimiter','Constant','IDENTIFIER','Angle_brackets']
        )

    #@self.pg.production(':')
    def parse(self):
        #1
        @self.pg.production('Program : Start_Statement ClassDeclaration Delimiter End_Statement Access_Operator')
        @self.pg.production('Program : Comment Delimiter using_command')
        def Program(P):
            print("matched Program")

        #2
        @self.pg.production('ClassDeclaration : Class Delimiter IDENTIFIER Braces Class_Implementation Braces')
        @self.pg.production('ClassDeclaration : Class Delimiter IDENTIFIER Delimiter Inheritance Braces Class_Implementation Braces')
        def ClassDeclaration(P):
            print("matched ClassDeclaration")

        #3
        @self.pg.production('Class_Implementation : VarDeclaration Class_Implementation')
        @self.pg.production('Class_Implementation : MethodDeclaration Class_Implementation')
        @self.pg.production('Class_Implementation : Comment Class_Implementation')
        @self.pg.production('Class_Implementation : Func_Call Class_Implementation')
        #@self.pg.production('empty')
        def Class_Implementation(P):
            print("matched Class_Implementation")
        #4
        @self.pg.production('MethodDeclaration : Func Decl Delimiter')
        @self.pg.production('MethodDeclaration : Func Decl Braces VarDeclaration Statements Braces')
        def MethodDeclaration(P):
            print("matched MethodDeclaration")

        #5
        @self.pg.production('Func Decl : Type Delimiter IDENTIFIER Angle_brackets ParameterList Angle_brackets')
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
        @self.pg.production('ParameterList : empty')
        @self.pg.production('ParameterList : NoneValue')
        @self.pg.production('ParameterList : Non-Empty List')
        def ParameterList(P):
            print("matched ParameterList")

        #8
        @self.pg.production('Non-Empty List : Type Delimiter IDENTIFIER')
        @self.pg.production('Non-Empty List : Non-Empty List , Type Delimiter IDENTIFIER')
        def NonEmptyList(P):
            print("matched Non-Empty List")

        #9
        #@self.pg.production('VarDeclaration : empty')
        @self.pg.production('VarDeclaration : Type Delimiter ID_List Delimiter VarDeclaration')
        def VarDeclaration(P):
            print("matched VarDeclaration")

        #10
        @self.pg.production('ID_List : IDENTIFIER')
        @self.pg.production('ID_List : ID_List , IDENTIFIER')
        def ID_List(P):
            print("matched ID_List")

        #11
        @self.pg.production('Statements : empty')
        @self.pg.production('Statements : Statement Statements')
        def Statements(P):
            print("matched Statements")

        #12
        @self.pg.production('Statement : Assignment')
        @self.pg.production('Statement : WhetherDo_Statement')
        @self.pg.production('Statement : RingWhen_Statement')
        @self.pg.production('Statement : BackedValue_Statement')
        @self.pg.production('Statement : terminatethis_Statement')
        @self.pg.production('Statement : read Angle_brackets IDENTIFIER Angle_brackets Delimiter')
        @self.pg.production('Statement : write Angle_brackets Expression Angle_brackets Delimiter')
        def Statement(P):
             print("matched Statement")

        #13
        @self.pg.production('Assignment : VarDeclaration Assignment_operator Expression Delimiter')
        def Assignment(P):
            print("matched Assignment")

        #14
        @self.pg.production('Func_Call : IDENTIFIER Angle_brackets Argument_List Angle_brackets Delimiter')
        def Func_Call(P):
            print("matched Func_Call")

        #15
        @self.pg.production('Argument_List : empty')
        @self.pg.production('Argument_List : NonEmpty_Argument_List')
        def Argument_List(P):
            print("matched Argument_List")

        #16
        @self.pg.production('NonEmpty_Argument_List : Expression')
        @self.pg.production('NonEmpty_Argument_List : NonEmpty_Argument_List , Expression')
        def onEmpty_Argument_List(P):
            print("matched onEmpty_Argument_List")
        #17
        @self.pg.production('Block Statements : Braces Statements Braces')
        def BlockStatements(P):
            print("matched Block Statements")

        #18
        @self.pg.production('WhetherDo_Statement : CONDITION Angle_brackets Condition_Expression Angle_brackets Block Statements CONDITION Statement')
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
            print("matched  Condition_Op")

        #21
        @self.pg.production('Condition : Expression Comparison_Op Expression Constant Access_operator')
        def Condition(P):
                print("matched  Condition")

        #22
        @self.pg.production('Comparison_Op : relational_operators')
        def Comparison_Op(P):
            print("matched  Comparison_Op")

        #23
        @self.pg.production('RingWhen_Statement : Loop Angle_brackets Condition_Expression Angle_brackets Block Statements')
        def RingWhen_Statement(P):
            print("matched  RingWhen_Statement")

        #24
        #extra space after backed value
        @self.pg.production('BackedValue_Statement : Return Delimiter Expression Delimiter')
        @self.pg.production('BackedValue_Statement : Return Delimiter ID Expression Delimiter')
        def BackedValue_Statement(P):
            print("matched  BackedValue_Statement")

        #25
        @self.pg.production('terminatethis_Statement : Break Delimiter')
        def terminatethis_Statement(P):
            print("matched  terminatethis_Statement")

        #26
        @self.pg.production('Expression : Term')
        @self.pg.production('Expression : Expression Delimiter Add_Op Delimiter Term')
        def Expression(P):
            print("matched  Expression")

        #27
        @self.pg.production('Add_Op : Arithmetic_Operation')
        def Add_Op(P):
            print("matched  Add_Op")

        #28
        @self.pg.production('Term : Factor')
        @self.pg.production('Term : Term Delimiter Mul_Op Delimiter Factor')
        def Term(P):
            print("matched  Term")

        #29
        @self.pg.production('Mul_Op : Arithmetic_Operation')
        def Mul_Op(P):
            print("matched  Mul_Op")

        #30
        @self.pg.production('Factor : IDENTIFIER')
        @self.pg.production('Factor : Number')
        def Factor(P):
            print("matched  Factor")



        #31
        #what is STR
        @self.pg.production('Comment : Comment String Comment')
        @self.pg.production('Comment : Comment String Comment')
        @self.pg.production('Comment : Comment String')
        def Comment(P):
            print("matched  Comment")

        #32
        @self.pg.production('using_command :  Inclusion Angle_brackets F_name Access Operator txt Angle_brackets Delimiter')
        def using_command(P):
            print("matched  using_command")

        #33
        #what is  STR
        @self.pg.production('F_name : String')
        def F_name(P):
            print("matched  F_name")

        @self.pg.error
        def error_handle(token):
           raise ValueError(token)

        def get_parser(self):
          return self.pg.build()























































         # @self.pg.production('expression : expression DIFF expression')
         # @self.pg.production('expression : expression TIMES expression')
         # @self.pg.production('expression : expression DIVIDE expression')
         # @self.pg.production('expression : expression SUM expression')
         # def expression(p):
         #     left = p[0]
         #     right = p[2]
         #     operator = p[1]
         #     if operator.gettokentype() == 'SUM':
         #         return Sum(left, right)
         #     elif p[1].gettokentype() == 'DIFF':
         #         return Sub(left, right)
         #     elif p[1].gettokentype() == 'TIMES':
         #         return Mul(left, right)
         #     elif p[1].gettokentype() == 'DIVIDE':
         #        return Div(left, right)
         #     else:
         #        raise AssertionError('error!')
         #
         # @self.pg.production('expression : NUMBER')
         # def number(p):
         #     Number(int(p[0].getstr()))
         #
         #
         # @self.pg.error
         # def error_handle(token):
         #    raise ValueError(token)
         #
         # def get_parser(self):
         #    return self.pg.build()