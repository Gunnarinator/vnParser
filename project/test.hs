{-# OPTIONS_GHC -w #-}
module Test where

import Generate
import qualified Data.Array as Happy_Data_Array
import qualified Data.Bits as Bits
import Control.Applicative(Applicative(..))
import Control.Monad (ap)

-- parser produced by Happy Version 1.20.1.1

data HappyAbsSyn t4 t5 t6 t7 t8 t9 t10 t11 t12 t13
	= HappyTerminal (Token)
	| HappyErrorToken Prelude.Int
	| HappyAbsSyn4 t4
	| HappyAbsSyn5 t5
	| HappyAbsSyn6 t6
	| HappyAbsSyn7 t7
	| HappyAbsSyn8 t8
	| HappyAbsSyn9 t9
	| HappyAbsSyn10 t10
	| HappyAbsSyn11 t11
	| HappyAbsSyn12 t12
	| HappyAbsSyn13 t13

happyExpList :: Happy_Data_Array.Array Prelude.Int Prelude.Int
happyExpList = Happy_Data_Array.listArray (0,184) ([0,61440,103,0,53216,0,49152,415,0,0,0,0,0,0,0,1,248,0,61440,1,0,0,2048,0,1,0,512,0,0,4,0,0,0,0,0,256,0,0,0,0,0,0,61440,103,0,0,0,49152,927,7936,0,0,0,0,31744,0,0,248,0,0,63488,51,0,2060,0,2040,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3072,8,0,53216,0,0,64,7936,0,0,62,0,0,65024,12,248,0,61440,1,0,992,0,49152,7,0,3968,0,0,31,0,15872,0,0,124,0,0,64512,25,0,2048,0,60,0,0,0,0,240,0,57344,1,0,0,2048,0,0,2,0,512,0,63488,51,0,0,0,0,32,0,0,0,0,128,49152,3,0,1920,0,0,15,0,7680,0,0,0,0,0,0,0,0,0,0,0,0,0,256,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,128,0,0,8,0,0,0
	])

{-# NOINLINE happyExpListPerState #-}
happyExpListPerState st =
    token_strs_expected
  where token_strs = ["error","%dummy","%start_parse","Lines","Choices","AST","Asign","Cond","Flag","Exp","Val","Var","Label","int","float","var","true","false","\"+\"","\"-\"","\"*\"","\"/\"","\"==\"","\"!=\"","\">\"","\"<\"","and","or","if","elif","else","\"=\"","\"+=\"","\"-=\"","label","\"{\"","\"}\"","menu","jump","choice","%eof"]
        bit_start = st Prelude.* 41
        bit_end = (st Prelude.+ 1) Prelude.* 41
        read_bit = readArrayBit happyExpList
        bits = Prelude.map read_bit [bit_start..bit_end Prelude.- 1]
        bits_indexed = Prelude.zip bits [0..40]
        token_strs_expected = Prelude.concatMap f bits_indexed
        f (Prelude.False, _) = []
        f (Prelude.True, nr) = [token_strs Prelude.!! nr]

action_0 (29) = happyShift action_6
action_0 (30) = happyShift action_7
action_0 (31) = happyShift action_8
action_0 (32) = happyShift action_9
action_0 (33) = happyShift action_10
action_0 (34) = happyShift action_11
action_0 (35) = happyShift action_12
action_0 (38) = happyShift action_13
action_0 (39) = happyShift action_14
action_0 (4) = happyGoto action_15
action_0 (6) = happyGoto action_16
action_0 (7) = happyGoto action_3
action_0 (8) = happyGoto action_4
action_0 (13) = happyGoto action_5
action_0 _ = happyFail (happyExpListPerState 0)

action_1 (29) = happyShift action_6
action_1 (30) = happyShift action_7
action_1 (31) = happyShift action_8
action_1 (32) = happyShift action_9
action_1 (33) = happyShift action_10
action_1 (34) = happyShift action_11
action_1 (35) = happyShift action_12
action_1 (38) = happyShift action_13
action_1 (39) = happyShift action_14
action_1 (6) = happyGoto action_2
action_1 (7) = happyGoto action_3
action_1 (8) = happyGoto action_4
action_1 (13) = happyGoto action_5
action_1 _ = happyFail (happyExpListPerState 1)

action_2 (29) = happyShift action_6
action_2 (30) = happyShift action_7
action_2 (31) = happyShift action_8
action_2 (32) = happyShift action_9
action_2 (33) = happyShift action_10
action_2 (34) = happyShift action_11
action_2 (35) = happyShift action_12
action_2 (38) = happyShift action_13
action_2 (39) = happyShift action_14
action_2 (4) = happyGoto action_17
action_2 (6) = happyGoto action_16
action_2 (7) = happyGoto action_3
action_2 (8) = happyGoto action_4
action_2 (13) = happyGoto action_5
action_2 _ = happyFail (happyExpListPerState 2)

action_3 _ = happyReduce_9

action_4 _ = happyReduce_10

action_5 (36) = happyShift action_33
action_5 _ = happyFail (happyExpListPerState 5)

action_6 (14) = happyShift action_28
action_6 (15) = happyShift action_29
action_6 (16) = happyShift action_20
action_6 (17) = happyShift action_30
action_6 (18) = happyShift action_31
action_6 (9) = happyGoto action_32
action_6 (10) = happyGoto action_25
action_6 (11) = happyGoto action_26
action_6 (12) = happyGoto action_27
action_6 _ = happyFail (happyExpListPerState 6)

action_7 (14) = happyShift action_28
action_7 (15) = happyShift action_29
action_7 (16) = happyShift action_20
action_7 (17) = happyShift action_30
action_7 (18) = happyShift action_31
action_7 (9) = happyGoto action_24
action_7 (10) = happyGoto action_25
action_7 (11) = happyGoto action_26
action_7 (12) = happyGoto action_27
action_7 _ = happyFail (happyExpListPerState 7)

action_8 (36) = happyShift action_23
action_8 _ = happyFail (happyExpListPerState 8)

action_9 (16) = happyShift action_20
action_9 (12) = happyGoto action_22
action_9 _ = happyFail (happyExpListPerState 9)

action_10 (16) = happyShift action_20
action_10 (12) = happyGoto action_21
action_10 _ = happyFail (happyExpListPerState 10)

action_11 (16) = happyShift action_20
action_11 (12) = happyGoto action_19
action_11 _ = happyFail (happyExpListPerState 11)

action_12 _ = happyReduce_35

action_13 (36) = happyShift action_18
action_13 _ = happyFail (happyExpListPerState 13)

action_14 _ = happyReduce_6

action_15 (41) = happyAccept
action_15 _ = happyFail (happyExpListPerState 15)

action_16 (29) = happyShift action_6
action_16 (30) = happyShift action_7
action_16 (31) = happyShift action_8
action_16 (32) = happyShift action_9
action_16 (33) = happyShift action_10
action_16 (34) = happyShift action_11
action_16 (35) = happyShift action_12
action_16 (38) = happyShift action_13
action_16 (39) = happyShift action_14
action_16 (4) = happyGoto action_17
action_16 (6) = happyGoto action_16
action_16 (7) = happyGoto action_3
action_16 (8) = happyGoto action_4
action_16 (13) = happyGoto action_5
action_16 _ = happyReduce_2

action_17 _ = happyReduce_1

action_18 (29) = happyShift action_6
action_18 (30) = happyShift action_7
action_18 (31) = happyShift action_8
action_18 (32) = happyShift action_9
action_18 (33) = happyShift action_10
action_18 (34) = happyShift action_11
action_18 (35) = happyShift action_12
action_18 (38) = happyShift action_13
action_18 (39) = happyShift action_14
action_18 (40) = happyShift action_54
action_18 (4) = happyGoto action_52
action_18 (5) = happyGoto action_53
action_18 (6) = happyGoto action_16
action_18 (7) = happyGoto action_3
action_18 (8) = happyGoto action_4
action_18 (13) = happyGoto action_5
action_18 _ = happyFail (happyExpListPerState 18)

action_19 (14) = happyShift action_28
action_19 (15) = happyShift action_29
action_19 (16) = happyShift action_20
action_19 (17) = happyShift action_30
action_19 (18) = happyShift action_31
action_19 (10) = happyGoto action_51
action_19 (11) = happyGoto action_26
action_19 (12) = happyGoto action_49
action_19 _ = happyFail (happyExpListPerState 19)

action_20 _ = happyReduce_34

action_21 (14) = happyShift action_28
action_21 (15) = happyShift action_29
action_21 (16) = happyShift action_20
action_21 (17) = happyShift action_30
action_21 (18) = happyShift action_31
action_21 (10) = happyGoto action_50
action_21 (11) = happyGoto action_26
action_21 (12) = happyGoto action_49
action_21 _ = happyFail (happyExpListPerState 21)

action_22 (14) = happyShift action_28
action_22 (15) = happyShift action_29
action_22 (16) = happyShift action_20
action_22 (17) = happyShift action_30
action_22 (18) = happyShift action_31
action_22 (10) = happyGoto action_48
action_22 (11) = happyGoto action_26
action_22 (12) = happyGoto action_49
action_22 _ = happyFail (happyExpListPerState 22)

action_23 (29) = happyShift action_6
action_23 (30) = happyShift action_7
action_23 (31) = happyShift action_8
action_23 (32) = happyShift action_9
action_23 (33) = happyShift action_10
action_23 (34) = happyShift action_11
action_23 (35) = happyShift action_12
action_23 (38) = happyShift action_13
action_23 (39) = happyShift action_14
action_23 (4) = happyGoto action_47
action_23 (6) = happyGoto action_16
action_23 (7) = happyGoto action_3
action_23 (8) = happyGoto action_4
action_23 (13) = happyGoto action_5
action_23 _ = happyFail (happyExpListPerState 23)

action_24 (27) = happyShift action_35
action_24 (28) = happyShift action_36
action_24 (36) = happyShift action_46
action_24 _ = happyFail (happyExpListPerState 24)

action_25 (19) = happyShift action_38
action_25 (20) = happyShift action_39
action_25 (21) = happyShift action_40
action_25 (22) = happyShift action_41
action_25 (23) = happyShift action_42
action_25 (24) = happyShift action_43
action_25 (25) = happyShift action_44
action_25 (26) = happyShift action_45
action_25 _ = happyFail (happyExpListPerState 25)

action_26 _ = happyReduce_25

action_27 (27) = happyReduce_17
action_27 (28) = happyReduce_17
action_27 (36) = happyReduce_17
action_27 _ = happyReduce_24

action_28 _ = happyReduce_30

action_29 _ = happyReduce_31

action_30 _ = happyReduce_32

action_31 _ = happyReduce_33

action_32 (27) = happyShift action_35
action_32 (28) = happyShift action_36
action_32 (36) = happyShift action_37
action_32 _ = happyFail (happyExpListPerState 32)

action_33 (29) = happyShift action_6
action_33 (30) = happyShift action_7
action_33 (31) = happyShift action_8
action_33 (32) = happyShift action_9
action_33 (33) = happyShift action_10
action_33 (34) = happyShift action_11
action_33 (35) = happyShift action_12
action_33 (38) = happyShift action_13
action_33 (39) = happyShift action_14
action_33 (4) = happyGoto action_34
action_33 (6) = happyGoto action_16
action_33 (7) = happyGoto action_3
action_33 (8) = happyGoto action_4
action_33 (13) = happyGoto action_5
action_33 _ = happyFail (happyExpListPerState 33)

action_34 (37) = happyShift action_71
action_34 _ = happyFail (happyExpListPerState 34)

action_35 (14) = happyShift action_28
action_35 (15) = happyShift action_29
action_35 (16) = happyShift action_20
action_35 (17) = happyShift action_30
action_35 (18) = happyShift action_31
action_35 (9) = happyGoto action_70
action_35 (10) = happyGoto action_25
action_35 (11) = happyGoto action_26
action_35 (12) = happyGoto action_27
action_35 _ = happyFail (happyExpListPerState 35)

action_36 (14) = happyShift action_28
action_36 (15) = happyShift action_29
action_36 (16) = happyShift action_20
action_36 (17) = happyShift action_30
action_36 (18) = happyShift action_31
action_36 (9) = happyGoto action_69
action_36 (10) = happyGoto action_25
action_36 (11) = happyGoto action_26
action_36 (12) = happyGoto action_27
action_36 _ = happyFail (happyExpListPerState 36)

action_37 (29) = happyShift action_6
action_37 (30) = happyShift action_7
action_37 (31) = happyShift action_8
action_37 (32) = happyShift action_9
action_37 (33) = happyShift action_10
action_37 (34) = happyShift action_11
action_37 (35) = happyShift action_12
action_37 (38) = happyShift action_13
action_37 (39) = happyShift action_14
action_37 (4) = happyGoto action_68
action_37 (6) = happyGoto action_16
action_37 (7) = happyGoto action_3
action_37 (8) = happyGoto action_4
action_37 (13) = happyGoto action_5
action_37 _ = happyFail (happyExpListPerState 37)

action_38 (14) = happyShift action_28
action_38 (15) = happyShift action_29
action_38 (16) = happyShift action_20
action_38 (17) = happyShift action_30
action_38 (18) = happyShift action_31
action_38 (10) = happyGoto action_67
action_38 (11) = happyGoto action_26
action_38 (12) = happyGoto action_49
action_38 _ = happyFail (happyExpListPerState 38)

action_39 (14) = happyShift action_28
action_39 (15) = happyShift action_29
action_39 (16) = happyShift action_20
action_39 (17) = happyShift action_30
action_39 (18) = happyShift action_31
action_39 (10) = happyGoto action_66
action_39 (11) = happyGoto action_26
action_39 (12) = happyGoto action_49
action_39 _ = happyFail (happyExpListPerState 39)

action_40 (14) = happyShift action_28
action_40 (15) = happyShift action_29
action_40 (16) = happyShift action_20
action_40 (17) = happyShift action_30
action_40 (18) = happyShift action_31
action_40 (10) = happyGoto action_65
action_40 (11) = happyGoto action_26
action_40 (12) = happyGoto action_49
action_40 _ = happyFail (happyExpListPerState 40)

action_41 (14) = happyShift action_28
action_41 (15) = happyShift action_29
action_41 (16) = happyShift action_20
action_41 (17) = happyShift action_30
action_41 (18) = happyShift action_31
action_41 (10) = happyGoto action_64
action_41 (11) = happyGoto action_26
action_41 (12) = happyGoto action_49
action_41 _ = happyFail (happyExpListPerState 41)

action_42 (14) = happyShift action_28
action_42 (15) = happyShift action_29
action_42 (16) = happyShift action_20
action_42 (17) = happyShift action_30
action_42 (18) = happyShift action_31
action_42 (10) = happyGoto action_63
action_42 (11) = happyGoto action_26
action_42 (12) = happyGoto action_49
action_42 _ = happyFail (happyExpListPerState 42)

action_43 (14) = happyShift action_28
action_43 (15) = happyShift action_29
action_43 (16) = happyShift action_20
action_43 (17) = happyShift action_30
action_43 (18) = happyShift action_31
action_43 (10) = happyGoto action_62
action_43 (11) = happyGoto action_26
action_43 (12) = happyGoto action_49
action_43 _ = happyFail (happyExpListPerState 43)

action_44 (14) = happyShift action_28
action_44 (15) = happyShift action_29
action_44 (16) = happyShift action_20
action_44 (17) = happyShift action_30
action_44 (18) = happyShift action_31
action_44 (10) = happyGoto action_61
action_44 (11) = happyGoto action_26
action_44 (12) = happyGoto action_49
action_44 _ = happyFail (happyExpListPerState 44)

action_45 (14) = happyShift action_28
action_45 (15) = happyShift action_29
action_45 (16) = happyShift action_20
action_45 (17) = happyShift action_30
action_45 (18) = happyShift action_31
action_45 (10) = happyGoto action_60
action_45 (11) = happyGoto action_26
action_45 (12) = happyGoto action_49
action_45 _ = happyFail (happyExpListPerState 45)

action_46 (29) = happyShift action_6
action_46 (30) = happyShift action_7
action_46 (31) = happyShift action_8
action_46 (32) = happyShift action_9
action_46 (33) = happyShift action_10
action_46 (34) = happyShift action_11
action_46 (35) = happyShift action_12
action_46 (38) = happyShift action_13
action_46 (39) = happyShift action_14
action_46 (4) = happyGoto action_59
action_46 (6) = happyGoto action_16
action_46 (7) = happyGoto action_3
action_46 (8) = happyGoto action_4
action_46 (13) = happyGoto action_5
action_46 _ = happyFail (happyExpListPerState 46)

action_47 (37) = happyShift action_58
action_47 _ = happyFail (happyExpListPerState 47)

action_48 (19) = happyShift action_38
action_48 (20) = happyShift action_39
action_48 (21) = happyShift action_40
action_48 (22) = happyShift action_41
action_48 _ = happyReduce_11

action_49 _ = happyReduce_24

action_50 (19) = happyShift action_38
action_50 (20) = happyShift action_39
action_50 (21) = happyShift action_40
action_50 (22) = happyShift action_41
action_50 _ = happyReduce_12

action_51 (19) = happyShift action_38
action_51 (20) = happyShift action_39
action_51 (21) = happyShift action_40
action_51 (22) = happyShift action_41
action_51 _ = happyReduce_13

action_52 (40) = happyShift action_54
action_52 (5) = happyGoto action_57
action_52 _ = happyFail (happyExpListPerState 52)

action_53 (37) = happyShift action_56
action_53 _ = happyFail (happyExpListPerState 53)

action_54 (36) = happyShift action_55
action_54 _ = happyFail (happyExpListPerState 54)

action_55 (29) = happyShift action_6
action_55 (30) = happyShift action_7
action_55 (31) = happyShift action_8
action_55 (32) = happyShift action_9
action_55 (33) = happyShift action_10
action_55 (34) = happyShift action_11
action_55 (35) = happyShift action_12
action_55 (38) = happyShift action_13
action_55 (39) = happyShift action_14
action_55 (4) = happyGoto action_75
action_55 (6) = happyGoto action_16
action_55 (7) = happyGoto action_3
action_55 (8) = happyGoto action_4
action_55 (13) = happyGoto action_5
action_55 _ = happyFail (happyExpListPerState 55)

action_56 _ = happyReduce_7

action_57 (37) = happyShift action_74
action_57 _ = happyFail (happyExpListPerState 57)

action_58 _ = happyReduce_16

action_59 (37) = happyShift action_73
action_59 _ = happyFail (happyExpListPerState 59)

action_60 (19) = happyShift action_38
action_60 (20) = happyShift action_39
action_60 (21) = happyShift action_40
action_60 (22) = happyShift action_41
action_60 _ = happyReduce_21

action_61 (19) = happyShift action_38
action_61 (20) = happyShift action_39
action_61 (21) = happyShift action_40
action_61 (22) = happyShift action_41
action_61 _ = happyReduce_20

action_62 (19) = happyShift action_38
action_62 (20) = happyShift action_39
action_62 (21) = happyShift action_40
action_62 (22) = happyShift action_41
action_62 _ = happyReduce_19

action_63 (19) = happyShift action_38
action_63 (20) = happyShift action_39
action_63 (21) = happyShift action_40
action_63 (22) = happyShift action_41
action_63 _ = happyReduce_18

action_64 (19) = happyShift action_38
action_64 (20) = happyShift action_39
action_64 (21) = happyShift action_40
action_64 (22) = happyShift action_41
action_64 _ = happyReduce_29

action_65 (19) = happyShift action_38
action_65 (20) = happyShift action_39
action_65 (21) = happyShift action_40
action_65 (22) = happyShift action_41
action_65 _ = happyReduce_28

action_66 (19) = happyShift action_38
action_66 (20) = happyShift action_39
action_66 (21) = happyShift action_40
action_66 (22) = happyShift action_41
action_66 _ = happyReduce_27

action_67 (19) = happyShift action_38
action_67 (20) = happyShift action_39
action_67 (21) = happyShift action_40
action_67 (22) = happyShift action_41
action_67 _ = happyReduce_26

action_68 (37) = happyShift action_72
action_68 _ = happyFail (happyExpListPerState 68)

action_69 (27) = happyShift action_35
action_69 (28) = happyShift action_36
action_69 _ = happyReduce_23

action_70 (27) = happyShift action_35
action_70 (28) = happyShift action_36
action_70 _ = happyReduce_22

action_71 _ = happyReduce_5

action_72 _ = happyReduce_14

action_73 _ = happyReduce_15

action_74 _ = happyReduce_8

action_75 (37) = happyShift action_76
action_75 _ = happyFail (happyExpListPerState 75)

action_76 (40) = happyShift action_54
action_76 (5) = happyGoto action_77
action_76 _ = happyReduce_4

action_77 _ = happyReduce_3

happyReduce_1 = happySpecReduce_2  4 happyReduction_1
happyReduction_1 (HappyAbsSyn4  happy_var_2)
	(HappyAbsSyn6  happy_var_1)
	 =  HappyAbsSyn4
		 (Lines (happy_var_1 : unwrapLines happy_var_2 )
	)
happyReduction_1 _ _  = notHappyAtAll 

happyReduce_2 = happySpecReduce_1  4 happyReduction_2
happyReduction_2 (HappyAbsSyn6  happy_var_1)
	 =  HappyAbsSyn4
		 (Lines [happy_var_1]
	)
happyReduction_2 _  = notHappyAtAll 

happyReduce_3 = happyReduce 5 5 happyReduction_3
happyReduction_3 ((HappyAbsSyn5  happy_var_5) `HappyStk`
	_ `HappyStk`
	(HappyAbsSyn4  happy_var_3) `HappyStk`
	_ `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn5
		 (Choices (happy_var_3 : unwrapChoices happy_var_5 )
	) `HappyStk` happyRest

happyReduce_4 = happyReduce 4 5 happyReduction_4
happyReduction_4 (_ `HappyStk`
	(HappyAbsSyn4  happy_var_3) `HappyStk`
	_ `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn5
		 (Choices [happy_var_3]
	) `HappyStk` happyRest

happyReduce_5 = happyReduce 4 6 happyReduction_5
happyReduction_5 (_ `HappyStk`
	(HappyAbsSyn4  happy_var_3) `HappyStk`
	_ `HappyStk`
	(HappyAbsSyn13  happy_var_1) `HappyStk`
	happyRest)
	 = HappyAbsSyn6
		 (ASTLabel happy_var_1 happy_var_3
	) `HappyStk` happyRest

happyReduce_6 = happySpecReduce_1  6 happyReduction_6
happyReduction_6 (HappyTerminal (TokenJump happy_var_1))
	 =  HappyAbsSyn6
		 (Jump happy_var_1
	)
happyReduction_6 _  = notHappyAtAll 

happyReduce_7 = happyReduce 4 6 happyReduction_7
happyReduction_7 (_ `HappyStk`
	(HappyAbsSyn5  happy_var_3) `HappyStk`
	_ `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn6
		 (Menu happy_var_3
	) `HappyStk` happyRest

happyReduce_8 = happyReduce 5 6 happyReduction_8
happyReduction_8 (_ `HappyStk`
	(HappyAbsSyn5  happy_var_4) `HappyStk`
	(HappyAbsSyn4  happy_var_3) `HappyStk`
	_ `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn6
		 (Menu2 happy_var_3 happy_var_4
	) `HappyStk` happyRest

happyReduce_9 = happySpecReduce_1  6 happyReduction_9
happyReduction_9 (HappyAbsSyn7  happy_var_1)
	 =  HappyAbsSyn6
		 (AstAsign happy_var_1
	)
happyReduction_9 _  = notHappyAtAll 

happyReduce_10 = happySpecReduce_1  6 happyReduction_10
happyReduction_10 (HappyAbsSyn8  happy_var_1)
	 =  HappyAbsSyn6
		 (AstCond happy_var_1
	)
happyReduction_10 _  = notHappyAtAll 

happyReduce_11 = happySpecReduce_3  7 happyReduction_11
happyReduction_11 (HappyAbsSyn10  happy_var_3)
	(HappyAbsSyn12  happy_var_2)
	_
	 =  HappyAbsSyn7
		 (Asign happy_var_2 happy_var_3
	)
happyReduction_11 _ _ _  = notHappyAtAll 

happyReduce_12 = happySpecReduce_3  7 happyReduction_12
happyReduction_12 (HappyAbsSyn10  happy_var_3)
	(HappyAbsSyn12  happy_var_2)
	_
	 =  HappyAbsSyn7
		 (Inc happy_var_2 happy_var_3
	)
happyReduction_12 _ _ _  = notHappyAtAll 

happyReduce_13 = happySpecReduce_3  7 happyReduction_13
happyReduction_13 (HappyAbsSyn10  happy_var_3)
	(HappyAbsSyn12  happy_var_2)
	_
	 =  HappyAbsSyn7
		 (Dec happy_var_2 happy_var_3
	)
happyReduction_13 _ _ _  = notHappyAtAll 

happyReduce_14 = happyReduce 5 8 happyReduction_14
happyReduction_14 (_ `HappyStk`
	(HappyAbsSyn4  happy_var_4) `HappyStk`
	_ `HappyStk`
	(HappyAbsSyn9  happy_var_2) `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn8
		 (If happy_var_2 happy_var_4
	) `HappyStk` happyRest

happyReduce_15 = happyReduce 5 8 happyReduction_15
happyReduction_15 (_ `HappyStk`
	(HappyAbsSyn4  happy_var_4) `HappyStk`
	_ `HappyStk`
	(HappyAbsSyn9  happy_var_2) `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn8
		 (Elif happy_var_2 happy_var_4
	) `HappyStk` happyRest

happyReduce_16 = happyReduce 4 8 happyReduction_16
happyReduction_16 (_ `HappyStk`
	(HappyAbsSyn4  happy_var_3) `HappyStk`
	_ `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn8
		 (Else happy_var_3
	) `HappyStk` happyRest

happyReduce_17 = happySpecReduce_1  9 happyReduction_17
happyReduction_17 (HappyAbsSyn12  happy_var_1)
	 =  HappyAbsSyn9
		 (Flag happy_var_1
	)
happyReduction_17 _  = notHappyAtAll 

happyReduce_18 = happySpecReduce_3  9 happyReduction_18
happyReduction_18 (HappyAbsSyn10  happy_var_3)
	_
	(HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn9
		 (Eq happy_var_1 happy_var_3
	)
happyReduction_18 _ _ _  = notHappyAtAll 

happyReduce_19 = happySpecReduce_3  9 happyReduction_19
happyReduction_19 (HappyAbsSyn10  happy_var_3)
	_
	(HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn9
		 (Neq happy_var_1 happy_var_3
	)
happyReduction_19 _ _ _  = notHappyAtAll 

happyReduce_20 = happySpecReduce_3  9 happyReduction_20
happyReduction_20 (HappyAbsSyn10  happy_var_3)
	_
	(HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn9
		 (Gt happy_var_1 happy_var_3
	)
happyReduction_20 _ _ _  = notHappyAtAll 

happyReduce_21 = happySpecReduce_3  9 happyReduction_21
happyReduction_21 (HappyAbsSyn10  happy_var_3)
	_
	(HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn9
		 (Lt happy_var_1 happy_var_3
	)
happyReduction_21 _ _ _  = notHappyAtAll 

happyReduce_22 = happySpecReduce_3  9 happyReduction_22
happyReduction_22 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn9
		 (And happy_var_1 happy_var_3
	)
happyReduction_22 _ _ _  = notHappyAtAll 

happyReduce_23 = happySpecReduce_3  9 happyReduction_23
happyReduction_23 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn9
		 (Or happy_var_1 happy_var_3
	)
happyReduction_23 _ _ _  = notHappyAtAll 

happyReduce_24 = happySpecReduce_1  10 happyReduction_24
happyReduction_24 (HappyAbsSyn12  happy_var_1)
	 =  HappyAbsSyn10
		 (ExpVar happy_var_1
	)
happyReduction_24 _  = notHappyAtAll 

happyReduce_25 = happySpecReduce_1  10 happyReduction_25
happyReduction_25 (HappyAbsSyn11  happy_var_1)
	 =  HappyAbsSyn10
		 (ExpVal happy_var_1
	)
happyReduction_25 _  = notHappyAtAll 

happyReduce_26 = happySpecReduce_3  10 happyReduction_26
happyReduction_26 (HappyAbsSyn10  happy_var_3)
	_
	(HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn10
		 (Add happy_var_1 happy_var_3
	)
happyReduction_26 _ _ _  = notHappyAtAll 

happyReduce_27 = happySpecReduce_3  10 happyReduction_27
happyReduction_27 (HappyAbsSyn10  happy_var_3)
	_
	(HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn10
		 (Sub happy_var_1 happy_var_3
	)
happyReduction_27 _ _ _  = notHappyAtAll 

happyReduce_28 = happySpecReduce_3  10 happyReduction_28
happyReduction_28 (HappyAbsSyn10  happy_var_3)
	_
	(HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn10
		 (Mul happy_var_1 happy_var_3
	)
happyReduction_28 _ _ _  = notHappyAtAll 

happyReduce_29 = happySpecReduce_3  10 happyReduction_29
happyReduction_29 (HappyAbsSyn10  happy_var_3)
	_
	(HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn10
		 (Div happy_var_1 happy_var_3
	)
happyReduction_29 _ _ _  = notHappyAtAll 

happyReduce_30 = happySpecReduce_1  11 happyReduction_30
happyReduction_30 (HappyTerminal (TokenInt happy_var_1))
	 =  HappyAbsSyn11
		 (Int happy_var_1
	)
happyReduction_30 _  = notHappyAtAll 

happyReduce_31 = happySpecReduce_1  11 happyReduction_31
happyReduction_31 (HappyTerminal (TokenFloat happy_var_1))
	 =  HappyAbsSyn11
		 (Float happy_var_1
	)
happyReduction_31 _  = notHappyAtAll 

happyReduce_32 = happySpecReduce_1  11 happyReduction_32
happyReduction_32 _
	 =  HappyAbsSyn11
		 (Bool True
	)

happyReduce_33 = happySpecReduce_1  11 happyReduction_33
happyReduction_33 _
	 =  HappyAbsSyn11
		 (Bool False
	)

happyReduce_34 = happySpecReduce_1  12 happyReduction_34
happyReduction_34 (HappyTerminal (TokenVar happy_var_1))
	 =  HappyAbsSyn12
		 (Var happy_var_1
	)
happyReduction_34 _  = notHappyAtAll 

happyReduce_35 = happySpecReduce_1  13 happyReduction_35
happyReduction_35 (HappyTerminal (TokenLabel happy_var_1))
	 =  HappyAbsSyn13
		 (Label happy_var_1
	)
happyReduction_35 _  = notHappyAtAll 

happyNewToken action sts stk [] =
	action 41 41 notHappyAtAll (HappyState action) sts stk []

happyNewToken action sts stk (tk:tks) =
	let cont i = action i i tk (HappyState action) sts stk tks in
	case tk of {
	TokenInt happy_dollar_dollar -> cont 14;
	TokenFloat happy_dollar_dollar -> cont 15;
	TokenVar happy_dollar_dollar -> cont 16;
	TokenTrue -> cont 17;
	TokenFalse -> cont 18;
	TokenAdd -> cont 19;
	TokenSub -> cont 20;
	TokenMul -> cont 21;
	TokenDiv -> cont 22;
	TokenEq -> cont 23;
	TokenNeq -> cont 24;
	TokenGt -> cont 25;
	TokenLt -> cont 26;
	TokenAnd -> cont 27;
	TokenOr -> cont 28;
	TokenIf -> cont 29;
	TokenElif -> cont 30;
	TokenElse -> cont 31;
	TokenAsign -> cont 32;
	TokenInc -> cont 33;
	TokenDec -> cont 34;
	TokenLabel happy_dollar_dollar -> cont 35;
	TokenBlockStart -> cont 36;
	TokenBlockEnd -> cont 37;
	TokenMenu -> cont 38;
	TokenJump happy_dollar_dollar -> cont 39;
	TokenChoice -> cont 40;
	_ -> happyError' ((tk:tks), [])
	}

happyError_ explist 41 tk tks = happyError' (tks, explist)
happyError_ explist _ tk tks = happyError' ((tk:tks), explist)

newtype HappyIdentity a = HappyIdentity a
happyIdentity = HappyIdentity
happyRunIdentity (HappyIdentity a) = a

instance Prelude.Functor HappyIdentity where
    fmap f (HappyIdentity a) = HappyIdentity (f a)

instance Applicative HappyIdentity where
    pure  = HappyIdentity
    (<*>) = ap
instance Prelude.Monad HappyIdentity where
    return = pure
    (HappyIdentity p) >>= q = q p

happyThen :: () => HappyIdentity a -> (a -> HappyIdentity b) -> HappyIdentity b
happyThen = (Prelude.>>=)
happyReturn :: () => a -> HappyIdentity a
happyReturn = (Prelude.return)
happyThen1 m k tks = (Prelude.>>=) m (\a -> k a tks)
happyReturn1 :: () => a -> b -> HappyIdentity a
happyReturn1 = \a tks -> (Prelude.return) a
happyError' :: () => ([(Token)], [Prelude.String]) -> HappyIdentity a
happyError' = HappyIdentity Prelude.. (\(tokens, _) -> parseError tokens)
parse tks = happyRunIdentity happySomeParser where
 happySomeParser = happyThen (happyParse action_0 tks) (\x -> case x of {HappyAbsSyn4 z -> happyReturn z; _other -> notHappyAtAll })

happySeq = happyDontSeq


parseError :: [Token] -> a
parseError _ = error "Parse error"

unwrapChoices :: Choices -> [Lines]
unwrapChoices (Choices xs) = xs

unwrapLines :: Lines -> [AST]
unwrapLines (Lines x) = x

data Token
      = TokenInt Int
        | TokenFloat Float
        | TokenVar String
        | TokenTrue
        | TokenFalse
        | TokenAdd
        | TokenSub
        | TokenMul
        | TokenDiv
        | TokenEq
        | TokenNeq
        | TokenGt
        | TokenLt
        | TokenAnd
        | TokenOr
        | TokenIf
        | TokenElif
        | TokenElse
        | TokenAsign
        | TokenInc
        | TokenDec
        | TokenLabel String
        | TokenBlockStart
        | TokenBlockEnd
        | TokenMenu
        | TokenJump String
        | TokenChoice
 deriving Show
{-# LINE 1 "templates/GenericTemplate.hs" #-}
-- $Id: GenericTemplate.hs,v 1.26 2005/01/14 14:47:22 simonmar Exp $










































data Happy_IntList = HappyCons Prelude.Int Happy_IntList








































infixr 9 `HappyStk`
data HappyStk a = HappyStk a (HappyStk a)

-----------------------------------------------------------------------------
-- starting the parse

happyParse start_state = happyNewToken start_state notHappyAtAll notHappyAtAll

-----------------------------------------------------------------------------
-- Accepting the parse

-- If the current token is ERROR_TOK, it means we've just accepted a partial
-- parse (a %partial parser).  We must ignore the saved token on the top of
-- the stack in this case.
happyAccept (1) tk st sts (_ `HappyStk` ans `HappyStk` _) =
        happyReturn1 ans
happyAccept j tk st sts (HappyStk ans _) = 
         (happyReturn1 ans)

-----------------------------------------------------------------------------
-- Arrays only: do the next action









































indexShortOffAddr arr off = arr Happy_Data_Array.! off


{-# INLINE happyLt #-}
happyLt x y = (x Prelude.< y)






readArrayBit arr bit =
    Bits.testBit (indexShortOffAddr arr (bit `Prelude.div` 16)) (bit `Prelude.mod` 16)






-----------------------------------------------------------------------------
-- HappyState data type (not arrays)



newtype HappyState b c = HappyState
        (Prelude.Int ->                    -- token number
         Prelude.Int ->                    -- token number (yes, again)
         b ->                           -- token semantic value
         HappyState b c ->              -- current state
         [HappyState b c] ->            -- state stack
         c)



-----------------------------------------------------------------------------
-- Shifting a token

happyShift new_state (1) tk st sts stk@(x `HappyStk` _) =
     let i = (case x of { HappyErrorToken (i) -> i }) in
--     trace "shifting the error token" $
     new_state i i tk (HappyState (new_state)) ((st):(sts)) (stk)

happyShift new_state i tk st sts stk =
     happyNewToken new_state ((st):(sts)) ((HappyTerminal (tk))`HappyStk`stk)

-- happyReduce is specialised for the common cases.

happySpecReduce_0 i fn (1) tk st sts stk
     = happyFail [] (1) tk st sts stk
happySpecReduce_0 nt fn j tk st@((HappyState (action))) sts stk
     = action nt j tk st ((st):(sts)) (fn `HappyStk` stk)

happySpecReduce_1 i fn (1) tk st sts stk
     = happyFail [] (1) tk st sts stk
happySpecReduce_1 nt fn j tk _ sts@(((st@(HappyState (action))):(_))) (v1`HappyStk`stk')
     = let r = fn v1 in
       happySeq r (action nt j tk st sts (r `HappyStk` stk'))

happySpecReduce_2 i fn (1) tk st sts stk
     = happyFail [] (1) tk st sts stk
happySpecReduce_2 nt fn j tk _ ((_):(sts@(((st@(HappyState (action))):(_))))) (v1`HappyStk`v2`HappyStk`stk')
     = let r = fn v1 v2 in
       happySeq r (action nt j tk st sts (r `HappyStk` stk'))

happySpecReduce_3 i fn (1) tk st sts stk
     = happyFail [] (1) tk st sts stk
happySpecReduce_3 nt fn j tk _ ((_):(((_):(sts@(((st@(HappyState (action))):(_))))))) (v1`HappyStk`v2`HappyStk`v3`HappyStk`stk')
     = let r = fn v1 v2 v3 in
       happySeq r (action nt j tk st sts (r `HappyStk` stk'))

happyReduce k i fn (1) tk st sts stk
     = happyFail [] (1) tk st sts stk
happyReduce k nt fn j tk st sts stk
     = case happyDrop (k Prelude.- ((1) :: Prelude.Int)) sts of
         sts1@(((st1@(HappyState (action))):(_))) ->
                let r = fn stk in  -- it doesn't hurt to always seq here...
                happyDoSeq r (action nt j tk st1 sts1 r)

happyMonadReduce k nt fn (1) tk st sts stk
     = happyFail [] (1) tk st sts stk
happyMonadReduce k nt fn j tk st sts stk =
      case happyDrop k ((st):(sts)) of
        sts1@(((st1@(HappyState (action))):(_))) ->
          let drop_stk = happyDropStk k stk in
          happyThen1 (fn stk tk) (\r -> action nt j tk st1 sts1 (r `HappyStk` drop_stk))

happyMonad2Reduce k nt fn (1) tk st sts stk
     = happyFail [] (1) tk st sts stk
happyMonad2Reduce k nt fn j tk st sts stk =
      case happyDrop k ((st):(sts)) of
        sts1@(((st1@(HappyState (action))):(_))) ->
         let drop_stk = happyDropStk k stk





             _ = nt :: Prelude.Int
             new_state = action

          in
          happyThen1 (fn stk tk) (\r -> happyNewToken new_state sts1 (r `HappyStk` drop_stk))

happyDrop (0) l = l
happyDrop n ((_):(t)) = happyDrop (n Prelude.- ((1) :: Prelude.Int)) t

happyDropStk (0) l = l
happyDropStk n (x `HappyStk` xs) = happyDropStk (n Prelude.- ((1)::Prelude.Int)) xs

-----------------------------------------------------------------------------
-- Moving to a new state after a reduction









happyGoto action j tk st = action j j tk (HappyState action)


-----------------------------------------------------------------------------
-- Error recovery (ERROR_TOK is the error token)

-- parse error if we are in recovery and we fail again
happyFail explist (1) tk old_st _ stk@(x `HappyStk` _) =
     let i = (case x of { HappyErrorToken (i) -> i }) in
--      trace "failing" $ 
        happyError_ explist i tk

{-  We don't need state discarding for our restricted implementation of
    "error".  In fact, it can cause some bogus parses, so I've disabled it
    for now --SDM

-- discard a state
happyFail  ERROR_TOK tk old_st CONS(HAPPYSTATE(action),sts) 
                                                (saved_tok `HappyStk` _ `HappyStk` stk) =
--      trace ("discarding state, depth " ++ show (length stk))  $
        DO_ACTION(action,ERROR_TOK,tk,sts,(saved_tok`HappyStk`stk))
-}

-- Enter error recovery: generate an error token,
--                       save the old token and carry on.
happyFail explist i tk (HappyState (action)) sts stk =
--      trace "entering error recovery" $
        action (1) (1) tk (HappyState (action)) sts ((HappyErrorToken (i)) `HappyStk` stk)

-- Internal happy errors:

notHappyAtAll :: a
notHappyAtAll = Prelude.error "Internal Happy error\n"

-----------------------------------------------------------------------------
-- Hack to get the typechecker to accept our action functions







-----------------------------------------------------------------------------
-- Seq-ing.  If the --strict flag is given, then Happy emits 
--      happySeq = happyDoSeq
-- otherwise it emits
--      happySeq = happyDontSeq

happyDoSeq, happyDontSeq :: a -> b -> b
happyDoSeq   a b = a `Prelude.seq` b
happyDontSeq a b = b

-----------------------------------------------------------------------------
-- Don't inline any functions from the template.  GHC has a nasty habit
-- of deciding to inline happyGoto everywhere, which increases the size of
-- the generated parser quite a bit.









{-# NOINLINE happyShift #-}
{-# NOINLINE happySpecReduce_0 #-}
{-# NOINLINE happySpecReduce_1 #-}
{-# NOINLINE happySpecReduce_2 #-}
{-# NOINLINE happySpecReduce_3 #-}
{-# NOINLINE happyReduce #-}
{-# NOINLINE happyMonadReduce #-}
{-# NOINLINE happyGoto #-}
{-# NOINLINE happyFail #-}

-- end of Happy Template.
