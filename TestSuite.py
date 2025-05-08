"""
Test case matrice:
    INSERT:         0 to 14  : 15
    ASSIGN:         15 to 29: 15
    BEGIN, END:     30 to 44: 15
    LOOKUP:         45 to 54: 10
    PRINT:          55 to 64: 10
    RPRINT:         65 to 75: 10
    FORMAT:         75 to 84: 15
    BIGTEST:        85 to 89: 5
    ...
    Total:          0 to 89: 90
"""
import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):

    ############################## INSERT ############################## 
    def test_0(self): 
        input = [
            "INSERT var0 number"
        ]
        expected = ["success"] 

        self.assertTrue(TestUtils.check(input, expected, 1000))

    def test_1(self): 
        input = [
            "INSERT var0 string"
        ]
        expected = ["success"] 

        self.assertTrue(TestUtils.check(input, expected, 1001))

    def test_2(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1002))

    def test_3(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "INSERT var0 number"
        ]
        expected = ["Redeclared: INSERT var0 number"]

        self.assertTrue(TestUtils.check(input, expected, 1003))

    def test_4(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "INSERT var0 string"
        ]
        expected = ["Redeclared: INSERT var0 string"]

        self.assertTrue(TestUtils.check(input, expected, 1004))

    def test_5(self):
        input = [
            "INSERT Var0 number",
            "INSERT var1 string",
            "INSERT var0 number"
        ]
        expected = ["Invalid: INSERT Var0 number"]

        self.assertTrue(TestUtils.check(input, expected, 1005))

    def test_6(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "INSERT var0 number"
        ]
        expected = ["Redeclared: INSERT var0 number"]

        self.assertTrue(TestUtils.check(input, expected, 1006))

    def test_7(self):
        input = [
            "INSERT var0_ number",
            "INSERT var1 string",
            "INSERT var0 number"
        ]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1007))

    def test_8(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "INSERT var0 Number"
        ]
        expected = ["Invalid: INSERT var0 Number"]

        self.assertTrue(TestUtils.check(input, expected, 1008))

    def test_9(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 String",
            "INSERT var0 number"
        ]
        expected = ["Invalid: INSERT var1 String"]

        self.assertTrue(TestUtils.check(input, expected, 1009))

    def test_10(self):
        input = [
            "INSERT vAr0 number",
            "INSERT var1 string",
            "INSERT var0 number"
        ]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1010))

    def test_11(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "INSERT var@0 number"
        ]
        expected = ["Invalid: INSERT var@0 number"]

        self.assertTrue(TestUtils.check(input, expected, 1011))

    def test_12(self):
        input = [
            "INSERT var0 number",
            "INSERT va@1 string",
            "INSERT var0 number"
        ]
        expected = ["Invalid: INSERT va@1 string"]

        self.assertTrue(TestUtils.check(input, expected, 1012))

    def test_13(self):
        input = [
            "INSERT var0 number INSERT var1 string",
            "INSERT var0 number"
        ]
        expected = ["Invalid: INSERT var0 number INSERT var1 string"]

        self.assertTrue(TestUtils.check(input, expected, 1013))

    def test_14(self):
        input = [
            "INSERT  var0 number",
        ]
        expected = ["Invalid: INSERT  var0 number"]

        self.assertTrue(TestUtils.check(input, expected, 1014))

    ############################## ASSIGN ############################## 
    def test_15(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "ASSIGN var0 10"
        ]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1015))

    def test_16(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "ASSIGN var1 'helllo'"
        ]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1016))

    def test_17(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "ASSIGN var1 'hello'",
            "ASSIGN var0 10"
        ]
        expected = ["success", "success","success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1017))

    def test_18(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "ASSIGN var0 'hello'",
            "ASSIGN var1 10"
        ]
        expected = ["TypeMismatch: ASSIGN var0 'hello'"]

        self.assertTrue(TestUtils.check(input, expected, 1018))

    def test_19(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "ASSIGN var1 10",
            "ASSIGN var0 'hello'"
        ]
        expected = ["TypeMismatch: ASSIGN var1 10"]

        self.assertTrue(TestUtils.check(input, expected, 1019))

    def test_20(self):
        input = [
            "INSERT var0 string",
            "INSERT var1 string",
            "ASSIGN var0 var1"
        ]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1020))

    def test_21(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 number",
            "ASSIGN var1 var0"
        ]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1021))

    def test_22(self):
        input = [
            "INSERT var0 string",
            "INSERT var1 number",
            "ASSIGN var0 var1"
        ]
        expected = ["TypeMismatch: ASSIGN var0 var1"]

        self.assertTrue(TestUtils.check(input, expected, 1022))

    def test_23(self):
        input = [
            "INSERT var0 string",
            "INSERT var1 number",
            "ASSIGN var1 var0"
        ]
        expected = ["TypeMismatch: ASSIGN var1 var0"]

        self.assertTrue(TestUtils.check(input, expected, 1023))

    def test_24(self):
        input = [
            "ASSIGN var0 10"
        ]
        expected = ["Undeclared: ASSIGN var0 10"]

        self.assertTrue(TestUtils.check(input, expected, 1024))

    def test_25(self):
        input = [
            "ASSIGN 10 var0"
        ]
        expected = ["Invalid: ASSIGN 10 var0"]

        self.assertTrue(TestUtils.check(input, expected, 1025))

    def test_26(self):
        input = [
            "INSERT var0 number", 
            "ASSIGN var0 -123"
        ]
        expected = ["Invalid: ASSIGN var0 -123"]

        self.assertTrue(TestUtils.check(input, expected, 1026))

    def test_27(self):
        input = [
            "INSERT var0 number", 
            "ASSIGN var0 1.3"
        ]
        expected = ["Invalid: ASSIGN var0 1.3"]

        self.assertTrue(TestUtils.check(input, expected, 1027))

    def test_28(self):
        input = [
            "INSERT var0 string", 
            "ASSIGN var0 'm&v'"
        ]
        expected = ["Invalid: ASSIGN var0 'm&v'"]

        self.assertTrue(TestUtils.check(input, expected, 1028))

    def test_29(self):
        input = [
            "ASSIGN var@ 10"
        ]
        expected = ["Invalid: ASSIGN var@ 10"]

        self.assertTrue(TestUtils.check(input, expected, 1029))

    ############################## BEGIN + END ############################## 
    def test_30(self):
        input = [
            "INSERT var0 number",
            "BEGIN",
            "END"
        ]
        expected = ["success"]

        self.assertTrue(TestUtils.check(input, expected, 1030))

    def test_31(self):
        input = [
            "INSERT var0 number",
            "BEGIN",
            "INSERT var1 string",
            "END"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1031))

    def test_32(self):
        input = [
            "INSERT var0 number",
            "BEGIN",
            "INSERT var0 string",
            "END"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1032))

    def test_33(self):
        input = [
            "INSERT var0 number",
            "BEGIN",
            "INSERT var0 number",
            "END"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1033))

    def test_34(self):
        input = [
            "INSERT var0 number",
            "BEGIN"
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 1034))

    def test_35(self):
        input = [
            "INSERT var0 number",
            "END"
        ]
        expected = ["UnknownBlock"]

        self.assertTrue(TestUtils.check(input, expected, 1035))

    def test_36(self):
        input = [
            "INSERT var0 number",
            "BEGIN",
            "INSERT var0 number",
            "BEGIN",
            "END"
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 1036))

    def test_37(self):
        input = [
            "INSERT var0 number",
            "BEGIN",
            "ASSIGN var0 10",
            "END"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1037))

    def test_38(self):
        input = [
            "INSERT var0 number",
            "BEGIN",
            "INSERT var1 string",
            "END",
            "BEGIN",
            "INSERT var1 string",
            "END"
        ]
        expected = ["success","success","success"]

        self.assertTrue(TestUtils.check(input, expected, 1038))

    def test_39(self):
        input = [
            "INSERT var0 number",
            "BEGIN",
            "INSERT var1 string",
            "END",
            "BEGIN",
            "ASSIGN var1 'hello'",
            "END"
        ]
        expected = ["Undeclared: ASSIGN var1 'hello'"]

        self.assertTrue(TestUtils.check(input, expected, 1039))

    def test_40(self):
        input = [
            "BEGIN",
            "INSERT var1 string",
            "END",
            "BEGIN",
            "INSERT var1 string",
            "END"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 1040))

    def test_41(self):
        input = [
            "BEGIN",
            "END",
            "BEGIN",
            "INSERT var1 string",
            "END"
        ]
        expected = ["success"]

        self.assertTrue(TestUtils.check(input, expected, 1041))

    def test_42(self):
        input = [
            "BEGIN",
            "INSERT var1 string",
            "END",
            "BEGIN",
            "END",
        ]
        expected = ["success"]

        self.assertTrue(TestUtils.check(input, expected, 1042))

    def test_43(self):
        input = [
            "BEGIN abc"
        ]
        expected = ["Invalid: BEGIN abc"]

        self.assertTrue(TestUtils.check(input, expected, 1043))

    def test_44(self):
        input = [
            "END abc"
        ]
        expected = ["Invalid: END abc"]

        self.assertTrue(TestUtils.check(input, expected, 1044))

    ############################## LOOKUP ############################## 
    def test_45(self):
        input = [
            "INSERT var0 number",
            "LOOKUP var0"
        ]
        expected = ["success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 1045))

    def test_46(self):
        input = [
            "INSERT var0 string",
            "LOOKUP var0"
        ]
        expected = ["success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 1046))

    def test_47(self):
        input = [
            "LOOKUP var0"
        ]
        expected = ["Undeclared: LOOKUP var0"]

        self.assertTrue(TestUtils.check(input, expected, 1047))

    def test_48(self):
        input = [
            "INSERT var0 string",
            "BEGIN",
            "LOOKUP var0",
            "END"
        ]
        expected = ["success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 1048))

    def test_49(self):
        input = [
            "INSERT var0 string",
            "BEGIN",
            "INSERT var0 number",
            "LOOKUP var0",
            "END"
        ]
        expected = ["success", "success", "1"]

        self.assertTrue(TestUtils.check(input, expected, 1049))

    def test_50(self):
        input = [
            "INSERT var0 string",
            "BEGIN",
            "INSERT var1 number",
            "LOOKUP var1",
            "END",
            "BEGIN",
            "LOOKUP var1",
            "END"
        ]
        expected = ["Undeclared: LOOKUP var1"]

        self.assertTrue(TestUtils.check(input, expected, 1050))

    def test_51(self):
        input = [
            "INSERT var0 string",
            "BEGIN",
            "INSERT var1 number",
            "LOOKUP var1",
            "LOOKUP var0",
            "END"
        ]
        expected = ["success", "success", "1", "0"]

        self.assertTrue(TestUtils.check(input, expected, 1051))

    def test_52(self):
        input = [
            "INSERT var0 string",
            "BEGIN",
            "LOOKUP var0",
            "INSERT var1 number",
            "LOOKUP var1",
            "END"
        ]
        expected = ["success", "0", "success", "1"]

        self.assertTrue(TestUtils.check(input, expected, 1052))

    def test_53(self):
        input = [
            "LOOKUP var0 10"
        ]
        expected = ["Invalid: LOOKUP var0 10"]

        self.assertTrue(TestUtils.check(input, expected, 1053))

    def test_54(self):
        input = [
            "LOOKUP var0 'hello'"
        ]
        expected = ["Invalid: LOOKUP var0 'hello'"]

        self.assertTrue(TestUtils.check(input, expected, 1054))

    ############################## PRINT ##############################
    def test_55(self):
        input = [
            "PRINT"
        ]
        expected = [""]

        self.assertTrue(TestUtils.check(input, expected, 1055))

    def test_56(self):
        input = [
            "INSERT var0 number",
            "PRINT"
        ]
        expected = ["success", "var0//0"]

        self.assertTrue(TestUtils.check(input, expected, 1056))

    def test_57(self):
        input = [
            "PRINT "
        ]
        expected = ["Invalid: PRINT "]

        self.assertTrue(TestUtils.check(input, expected, 1057))

    def test_58(self):
        input = [
            "PRINT number"
        ]
        expected = ["Invalid: PRINT number"]

        self.assertTrue(TestUtils.check(input, expected, 1058))

    def test_59(self):
        input = [
            "PRINT string"
        ]
        expected = ["Invalid: PRINT string"]

        self.assertTrue(TestUtils.check(input, expected, 1059))

    def test_60(self):
        input = [
            "PRINT abc"
        ]
        expected = ["Invalid: PRINT abc"]

        self.assertTrue(TestUtils.check(input, expected, 1060))

    def test_61(self):
        input = [
            "PRINT 10"
        ]
        expected = ["Invalid: PRINT 10"]

        self.assertTrue(TestUtils.check(input, expected, 1061))

    def test_62(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "BEGIN",
            "PRINT",
            "END"
        ]
        expected = ["success", "success", "var0//0 var1//0"]

        self.assertTrue(TestUtils.check(input, expected, 1062))

    def test_63(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "BEGIN",
            "INSERT var0 string",
            "PRINT",
            "END"
        ]
        expected = ["success", "success", "success", "var1//0 var0//1"]

        self.assertTrue(TestUtils.check(input, expected, 1063))

    def test_64(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "BEGIN",
            "INSERT var0 string",
            "END",
            "PRINT"
        ]
        expected = ["success", "success", "success", "var0//0 var1//0"]

        self.assertTrue(TestUtils.check(input, expected, 1064))

    ############################## RPRINT ##############################
    def test_65(self):
        input = [
            "RPRINT"
        ]
        expected = [""]

        self.assertTrue(TestUtils.check(input, expected, 1065))

    def test_66(self):
        input = [
            "INSERT var0 number",
            "RPRINT"
        ]
        expected = ["success", "var0//0"]

        self.assertTrue(TestUtils.check(input, expected, 1066))

    def test_67(self):
        input = [
            "RPRINT "
        ]
        expected = ["Invalid: RPRINT "]

        self.assertTrue(TestUtils.check(input, expected, 1067))

    def test_68(self):
        input = [
            "RPRINT number"
        ]
        expected = ["Invalid: RPRINT number"]

        self.assertTrue(TestUtils.check(input, expected, 1068))

    def test_69(self):
        input = [
            "RPRINT string"
        ]
        expected = ["Invalid: RPRINT string"]

        self.assertTrue(TestUtils.check(input, expected, 1069))

    def test_70(self):
        input = [
            "RPRINT abc"
        ]
        expected = ["Invalid: RPRINT abc"]

        self.assertTrue(TestUtils.check(input, expected, 1070))

    def test_71(self):
        input = [
            "RPRINT 10"
        ]
        expected = ["Invalid: RPRINT 10"]

        self.assertTrue(TestUtils.check(input, expected, 1071))

    def test_72(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "BEGIN",
            "RPRINT",
            "END"
        ]
        expected = ["success", "success", "var1//0 var0//0"]

        self.assertTrue(TestUtils.check(input, expected, 1072))

    def test_73(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "BEGIN",
            "INSERT var0 string",
            "RPRINT",
            "END"
        ]
        expected = ["success", "success", "success", "var0//1 var1//0"]

        self.assertTrue(TestUtils.check(input, expected, 1073))

    def test_74(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "BEGIN",
            "INSERT var0 string",
            "END",
            "RPRINT"
        ]
        expected = ["success", "success", "success", "var1//0 var0//0"]

        self.assertTrue(TestUtils.check(input, expected, 1074))

    ############################## FORMAT ##############################
    def test_75(self):
        input = [
            "Insert var0 number"
        ]
        expected = ["Invalid: Insert var0 number"]

        self.assertTrue(TestUtils.check(input, expected, 1075))

    def test_76(self):
        input = [
            "INSERT  x  string"
        ]
        expected = ["Invalid: INSERT  x  string"]

        self.assertTrue(TestUtils.check(input, expected, 1076))

    def test_77(self):
        input = [
            "ASSIGN 4var 10"
        ]
        expected = ["Invalid: ASSIGN 4var 10"]

        self.assertTrue(TestUtils.check(input, expected, 1077))

    def test_78(self):
        input = [
            "BEGIN END"
        ]
        expected = ["Invalid: BEGIN END"]

        self.assertTrue(TestUtils.check(input, expected, 1078))

    def test_79(self):
        input = [
            " BEGIN"
        ]
        expected = ["Invalid:  BEGIN"]

        self.assertTrue(TestUtils.check(input, expected, 1079))

    def test_80(self):
        input = [
            "LOOKUP 10"
        ]
        expected = ["Invalid: LOOKUP 10"]

        self.assertTrue(TestUtils.check(input, expected, 1080))

    def test_81(self):
        input = [
            ""
        ]
        expected = ["Invalid: "]

        self.assertTrue(TestUtils.check(input, expected, 1081))

    def test_82(self):
        input = [
            " "
        ]
        expected = ["Invalid:  "]

        self.assertTrue(TestUtils.check(input, expected, 1082))

    def test_83(self):
        input = [
            " a "
        ]
        expected = ["Invalid:  a "]

        self.assertTrue(TestUtils.check(input, expected, 1083))

    def test_84(self):
        input = [
            "INSERT x number",
            "ASSIGn x 10"
        ]
        expected = ["Invalid: ASSIGn x 10"]

        self.assertTrue(TestUtils.check(input, expected, 1084))

############################## BIGTESTCASE ##############################
    def test_85(self):
        input = [
            "INSERT var0 number",
            "ASSIGN var0 100",
            "BEGIN",
            "BEGIN",
            "LOOKUP var0",
            "INSERT var1 string",
            "PRINT",
            "END",
            "INSERT var1 number",
            "RPRINT",
            "END",
            "LOOKUP var0"
        ]
        expected = ["success", "success", "0", "success", "var0//0 var1//2","success", "var1//1 var0//0", "0"]

        self.assertTrue(TestUtils.check(input, expected, 1085))

    def test_86(self):
        input = [
            "RPRINT",
            "PRINT",
            "INSERT var0 number",
            "ASSIGN var0 100",
            "BEGIN",
            "BEGIN",
            "LOOKUP var0",
            "INSERT var1 string",
            "PRINT",
            "END",
            "INSERT var1 number",
            "RPRINT",
            "END"
        ]
        expected = ["","", "success", "success", "0", "success", "var0//0 var1//2","success", "var1//1 var0//0"]

        self.assertTrue(TestUtils.check(input, expected, 1086))

    def test_87(self):
        input = [
            "INSERT var0 number",
            "ASSIGN var0 100",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "END",
            "LOOKUP var0",
            "INSERT var1 string",
            "PRINT",
            "BEGIN",
            "INSERT var3 string",
            "END",
            "END",
            "INSERT var1 number",
            "RPRINT",
            "END"
        ]
        expected = ["success", "success", "0", "success", "var0//0 var1//2", "success", "success", "var1//1 var0//0"]

        self.assertTrue(TestUtils.check(input, expected, 1087))

    def test_88(self):
        input = [
            "INSERT var0 number",
            "INSERT var1 string",
            "BEGIN",
            "INSERT var2 number",
            "BEGIN",
            "INSERT var0 number",
            "INSERT var3 string",
            "ASSIGN var0 var2",
            "END",
            "BEGIN",
            "INSERT var4 string",
            "END",
            "INSERT var5 number",
            "PRINT",
            "END",
            "INSERT var6 number",
            "RPRINT"
        ]
        expected = ["success","success","success","success","success","success","success","success","var0//0 var1//0 var2//1 var5//1","success","var6//0 var1//0 var0//0"]

        self.assertTrue(TestUtils.check(input, expected, 1088))

    def test_89(self):
        input = [
            "BEGIN", 
            "INSERT var0 number", 
            "END", 
            "INSERT var0 number", 
            "BEGIN", 
            "INSERT var0 number", 
            "END", 
            "LOOKUP var0"
        ]
        expected = ["success", "success", "success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 1089))
