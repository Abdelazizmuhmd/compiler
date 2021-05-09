from rply import ParserGenerator
from ast import Number,Print


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['Class', 'Inheritance', 'CONDITION', 'Integer',
             'Character', 'Float', 'SFloat', 'Void','SInteger',
             'Break','Loop','Return','Start_Statement',
             'End_Statement','Comment','Arithmetic_Operation','Logic_operators',
             'relational_operators','Assignment_operator','Access_operator','Braces'
             ,'Inclusion','Delimiter','Constant','IDENTIFIER','Angle_brackets',',','Void','STR']
        )


    #@self.pg.production(':')
    def parse(self):
        #1
        @self.pg.production('Program : Start_Statement Delimiter ClassDeclaration Delimiter End_Statement Access_operator')
        def Program(p):
            print("matched Program")
            return Print(p[2])
        @self.pg.production('Program : COMMENT Delimiter using_command')
        def Program(p):
            print("matched Program")
            return p[2]

        #2
        @self.pg.production('ClassDeclaration : Class Delimiter IDENTIFIER Braces Class_Implementation Braces')
        def ClassDeclaration(p):
            print("matched ClassDeclaration")
            return (p[4])
        @self.pg.production('ClassDeclaration : Class Delimiter IDENTIFIER Delimiter Inheritance Braces Class_Implementation Braces')
        def ClassDeclaration(p):
            print("matched ClassDeclaration")
            return (p[6])

        #3
        #empty
        @self.pg.production('Class_Implementation :')
        def Class_Implementation(p):
            return
        @self.pg.production('Class_Implementation : VarDeclaration Class_Implementation')
        def Class_Implementation(p):
            print("matched Class_Implementation")
            return Print(p[0]),Print(p[1])
        @self.pg.production('Class_Implementation : MethodDeclaration Class_Implementation')
        def Class_Implementation(p):
            print("matched Class_Implementation")
            return Print(p[0]),Print(p[1])
        @self.pg.production('Class_Implementation : COMMENT Class_Implementation')
        def Class_Implementation(p):
            print("matched Class_Implementation")
            return (p[1])
        @self.pg.production('Class_Implementation : Func_Call Class_Implementation')
        def Class_Implementation(p):
            print("matched Class_Implementation")
            return (p[0],p[1])



        #4
        @self.pg.production('MethodDeclaration : Func_Decl Delimiter')
        def MethodDeclaration(p):
            print("matched MethodDeclaration")
            return (p[0])
        @self.pg.production('MethodDeclaration : Func_Decl Braces VarDeclaration Statements Braces')
        def MethodDeclaration(p):
            print("matched MethodDeclaration")
            return (p[0],p[2],p[3])

        #5
        @self.pg.production('Func_Decl : Type Delimiter IDENTIFIER Angle_brackets ParameterList Angle_brackets')
        def Func_Decl(p):
            print("matched Func_Decl")
            return Print(p[0]),Print(p[4])

        #7
        @self.pg.production('ParameterList : Non-Empty_List')
        def ParameterList(p):
            print("matched ParameterList")
            return Print(p[0])

        #8
        @self.pg.production('Non-Empty_List : Type Delimiter IDENTIFIER')
        def NonEmpty_List(p):
            print("matched Non-Empty_List")
            return (p[0])
        #idk about comma , no end
        @self.pg.production('Non-Empty_List : Non-Empty_List , Type Delimiter IDENTIFIER')
        def NonEmpty_List(p):
            print("matched Non-Empty_List")
            return (p[0],p[1])

        #9
        @self.pg.production('VarDeclaration :')
        def VarDeclaration(p):
            return
        @self.pg.production('VarDeclaration : Type Delimiter ID_List Delimiter VarDeclaration')
        def VarDeclaration(p):
            print("matched VarDeclaration")
            return (p[0],p[2],p[4])
        #10
        #idk about comma
        @self.pg.production('ID_List : ID_List , IDENTIFIER')
        def ID_List(p):
            print("matched ID_List")
            return (p[0])

        #11
        @self.pg.production('Statements :')
        def Statements(p):
            return
        @self.pg.production('Statements : Statement Statements')
        def Statements(p):
            print("matched Statements")
            return (p[0],p[1])

        #12

        @self.pg.production('Statement : WhetherDo_Statement')
        def Statement(p):
            print("matched Statement")
            return (p[0])

        #18
        @self.pg.production('WhetherDo_Statement : CONDITION Angle_brackets Condition_Expression Angle_brackets Block_Statements CONDITION Statement')
        def WhetherDo_Statement(p):
            print("matched WhetherDo_Statement")
            return (p[2],p[4],p[6])


        @self.pg.production('Statement : Assignment')
        def Statement(p):
            print("matched Statement")
            return (p[0])

        @self.pg.production('Statement : RingWhen_Statement')
        def Statement(p):
            print("matched Statement")
            return (p[0])
        @self.pg.production('Statement : BackedValue_Statement')
        def Statement(p):
            print("matched Statement")
            return (p[0])
        @self.pg.production('Statement : terminatethis_Statement')
        def Statement(p):
            print("matched Statement")
            return (p[0])
        #idk about them
        @self.pg.production('Statement : STR Angle_brackets Expression Angle_brackets Delimiter')
        def Statement(p):
             print("matched Statement")
             return (p[2])
        #should moved down
        @self.pg.production('Statement : STR Angle_brackets IDENTIFIER Angle_brackets Delimiter')
        def Statement(P):
             print("matched Statement")

        #13
        @self.pg.production('Assignment : VarDeclaration Assignment_operator Expression Delimiter')
        def Assignment(p):
            print("matched Assignment")
            return (p[0],p[2])

        #14
        @self.pg.production('Func_Call : IDENTIFIER Angle_brackets Argument_List Angle_brackets Delimiter')
        def Func_Call(p):
            print("matched Func_Call")
            return (p[2])

        #15
        @self.pg.production('Argument_List :')
        def Argument_List(p):
            return
        @self.pg.production('Argument_List : NonEmpty_Argument_List')
        def Argument_List(p):
            print("matched Argument_List")
            return (p[0])

        #16
        #idk about comma
        @self.pg.production('NonEmpty_Argument_List : NonEmpty_Argument_List , Expression')
        def onEmpty_Argument_List(p):
            print("matched onEmpty_Argument_List")
            return (p[0])
        @self.pg.production('NonEmpty_Argument_List : Expression')
        def onEmpty_Argument_List(p):
            print("matched onEmpty_Argument_List")
            return (p[0])

        #23
        @self.pg.production('RingWhen_Statement : Loop Angle_brackets Condition_Expression Angle_brackets Block_Statements')
        def RingWhen_Statement(p):
            print("matched  RingWhen_Statement")
            return (p[2],p[4])

        #17
        @self.pg.production('Block_Statements : Braces Statements Braces')
        def BlockS_tatements(p):
            print("matched Block_Statements")
            return (p[1])



        #19
        @self.pg.production('Condition_Expression : Condition')
        def Condition_Expression(p):
            print("matched  Condition_Expression")
            return (p[0])
        @self.pg.production('Condition_Expression : Condition Condition_Op Condition')
        def Condition_Expression(p):
            print("matched  Condition_Expression")
            return (p[0],p[1],p[2])



        #21
        @self.pg.production('Condition : Expression Comparison_Op Expression Constant Access_operator')
        def Condition(p):
                print("matched  Condition")
                return (p[0],p[1],p[2])




        #24
        #extra space after backed value
        @self.pg.production('BackedValue_Statement : Return Delimiter Expression Delimiter')
        def BackedValue_Statement(p):
            print("matched  BackedValue_Statement")
            return (p[2])
        @self.pg.production('BackedValue_Statement : Return Delimiter IDENTIFIER Expression Delimiter')
        def BackedValue_Statement(p):
            print("matched  BackedValue_Statement")
            return (p[3])



        #26
        @self.pg.production('Expression : Expression Delimiter Add_Op Delimiter Term')
        def Expression(p):
            print("matched  Expression")
            return (p[0],p[2],p[4])
        @self.pg.production('Expression : Term')
        def Expression(p):
            print("matched  Expression")
            return (p[0])



        #28
        @self.pg.production('Term : Factor')
        def Term(p):
            print("matched  Term")
            return (p[0])
        @self.pg.production('Term : Term Delimiter Mul_Op Delimiter Factor')
        def Term(p):
            print("matched  Term")
            return (p[0],p[2],p[4])

        #32
        @self.pg.production('using_command :  Inclusion Angle_brackets F_name Access_operator STR Angle_brackets Delimiter')
        def using_command(p):
            print("matched  using_command")
            return (p[2])

        #33
        #what is  STR
        @self.pg.production('F_name : STR')
        def F_name(p):
            print("matched  F_name")
            return

        #31
        #what is changed STR to String
        @self.pg.production('COMMENT : Comment STR Comment')
        @self.pg.production('COMMENT : Comment STR')
        def COMMENT(p):
            print("matched  COMMENT")
            return
        #6
        @self.pg.production('Type : Integer')
        @self.pg.production('Type : SInteger')
        @self.pg.production('Type : Character')
        @self.pg.production('Type : STR')
        @self.pg.production('Type : Float')
        @self.pg.production('Type : SFloat')
        @self.pg.production('Type : Void')
        def Type(p):
            print("matched Type")
            return

        #7
        #empty
        @self.pg.production('ParameterList :')
        def ParameterList(p):
            print("matched ParameterList")
            return
        @self.pg.production('ParameterList : Void')
        def ParameterList(p):
            print("matched ParameterList")
            return

        #9
        @self.pg.production('VarDeclaration :')
        def VarDeclaration(p):
            return

        #3
        #empty
        @self.pg.production('Class_Implementation :')
        def Class_Implementation(p):
            print("matched Class_Implementation")
            return

        #10
        @self.pg.production('ID_List : IDENTIFIER')
        def ID_List(P):
            print("matched ID_List")
            return

        #11
        @self.pg.production('Statements :')
        def Statements(p):
            return
        #15
        @self.pg.production('Argument_List :')
        def Argument_List(p):
            return


        #20
        @self.pg.production('Condition_Op : Logic_operators')
        def Condition_Op(p):
            print("matched  Condition_Op")
            return

        #22
        @self.pg.production('Comparison_Op : relational_operators')
        def Comparison_Op(p):
            print("matched  Comparison_Op")
            return
        #25
        @self.pg.production('terminatethis_Statement : Break Delimiter')
        def terminatethis_Statement(p):
            print("matched  terminatethis_Statement")
            return


        #27
        @self.pg.production('Add_Op : Arithmetic_Operation')
        def Add_Op(p):
            print("matched  Add_Op")
            return

        #29
        @self.pg.production('Mul_Op : Arithmetic_Operation')
        def Mul_Op(p):
            print("matched  Mul_Op")
            return

        #30
        @self.pg.production('Factor : IDENTIFIER')
        def Factor(p):
            print("matched  Factor")
            return

        # idk about number so i made it constant
        @self.pg.production('Factor : Constant')
        def Factor(p):
            print("matched  Factor")
            return


        @self.pg.error
        def error_handle(token):
           print(token)
           raise ValueError("Ran into a %s where it was't expected" % token.gettokentype())
        return





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