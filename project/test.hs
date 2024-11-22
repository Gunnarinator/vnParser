{-# OPTIONS_GHC -w #-}
module Test where

import Generate
import qualified Data.Array as Happy_Data_Array
import qualified Data.Bits as Bits
import Control.Applicative(Applicative(..))
import Control.Monad (ap)

-- parser produced by Happy Version 1.20.1.1

data HappyAbsSyn t4 t5 t6 t7 t8 t9 t10 t11 t12
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

happyExpList :: Happy_Data_Array.Array Prelude.Int Prelude.Int
happyExpList = Happy_Data_Array.listArray (0,154) ([0,63488,51,0,512,0,0,4,0,0,0,0,0,0,0,0,0,0,496,0,61440,1,0,0,0,16384,0,0,64,0,16384,0,0,0,1024,0,0,2,0,0,0,63488,115,496,0,0,0,0,496,0,61440,1,0,0,6,0,510,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,63488,51,0,2048,61440,1,0,496,0,61440,1,0,496,0,61440,1,0,496,0,61440,1,0,496,0,61440,1,0,496,0,0,30,0,0,0,0,30,0,7680,0,0,0,64,0,2048,0,63488,51,0,16384,0,0,0,0,2048,0,30,0,7680,0,0,30,0,7680,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
	])

{-# NOINLINE happyExpListPerState #-}
happyExpListPerState st =
    token_strs_expected
  where token_strs = ["error","%dummy","%start_parse","AST","Choices","Asign","Cond","Flag","Exp","Val","Var","Label","int","float","var","true","false","\"+\"","\"-\"","\"*\"","\"/\"","\"==\"","\"!=\"","\">\"","\"<\"","and","or","if","elif","else","\"=\"","\"+=\"","\"-=\"","label","\"{\"","\"}\"","menu","jump","choice","%eof"]
        bit_start = st Prelude.* 40
        bit_end = (st Prelude.+ 1) Prelude.* 40
        read_bit = readArrayBit happyExpList
        bits = Prelude.map read_bit [bit_start..bit_end Prelude.- 1]
        bits_indexed = Prelude.zip bits [0..39]
        token_strs_expected = Prelude.concatMap f bits_indexed
        f (Prelude.False, _) = []
        f (Prelude.True, nr) = [token_strs Prelude.!! nr]

action_0 (28) = happyShift action_7
action_0 (29) = happyShift action_8
action_0 (30) = happyShift action_9
action_0 (31) = happyShift action_10
action_0 (32) = happyShift action_11
action_0 (33) = happyShift action_12
action_0 (34) = happyShift action_3
action_0 (37) = happyShift action_13
action_0 (38) = happyShift action_14
action_0 (4) = happyGoto action_4
action_0 (6) = happyGoto action_5
action_0 (7) = happyGoto action_6
action_0 (12) = happyGoto action_2
action_0 _ = happyFail (happyExpListPerState 0)

action_1 (34) = happyShift action_3
action_1 (12) = happyGoto action_2
action_1 _ = happyFail (happyExpListPerState 1)

action_2 (35) = happyShift action_30
action_2 _ = happyFail (happyExpListPerState 2)

action_3 _ = happyReduce_33

action_4 (40) = happyAccept
action_4 _ = happyFail (happyExpListPerState 4)

action_5 _ = happyReduce_5

action_6 _ = happyReduce_6

action_7 (13) = happyShift action_25
action_7 (14) = happyShift action_26
action_7 (15) = happyShift action_18
action_7 (16) = happyShift action_27
action_7 (17) = happyShift action_28
action_7 (8) = happyGoto action_29
action_7 (9) = happyGoto action_22
action_7 (10) = happyGoto action_23
action_7 (11) = happyGoto action_24
action_7 _ = happyFail (happyExpListPerState 7)

action_8 (13) = happyShift action_25
action_8 (14) = happyShift action_26
action_8 (15) = happyShift action_18
action_8 (16) = happyShift action_27
action_8 (17) = happyShift action_28
action_8 (8) = happyGoto action_21
action_8 (9) = happyGoto action_22
action_8 (10) = happyGoto action_23
action_8 (11) = happyGoto action_24
action_8 _ = happyFail (happyExpListPerState 8)

action_9 _ = happyReduce_14

action_10 (15) = happyShift action_18
action_10 (11) = happyGoto action_20
action_10 _ = happyFail (happyExpListPerState 10)

action_11 (15) = happyShift action_18
action_11 (11) = happyGoto action_19
action_11 _ = happyFail (happyExpListPerState 11)

action_12 (15) = happyShift action_18
action_12 (11) = happyGoto action_17
action_12 _ = happyFail (happyExpListPerState 12)

action_13 (35) = happyShift action_16
action_13 _ = happyFail (happyExpListPerState 13)

action_14 (34) = happyShift action_3
action_14 (12) = happyGoto action_15
action_14 _ = happyFail (happyExpListPerState 14)

action_15 _ = happyReduce_2

action_16 (28) = happyShift action_7
action_16 (29) = happyShift action_8
action_16 (30) = happyShift action_9
action_16 (31) = happyShift action_10
action_16 (32) = happyShift action_11
action_16 (33) = happyShift action_12
action_16 (34) = happyShift action_3
action_16 (37) = happyShift action_13
action_16 (38) = happyShift action_14
action_16 (39) = happyShift action_48
action_16 (4) = happyGoto action_46
action_16 (5) = happyGoto action_47
action_16 (6) = happyGoto action_5
action_16 (7) = happyGoto action_6
action_16 (12) = happyGoto action_2
action_16 _ = happyFail (happyExpListPerState 16)

action_17 (13) = happyShift action_25
action_17 (14) = happyShift action_26
action_17 (15) = happyShift action_18
action_17 (16) = happyShift action_27
action_17 (17) = happyShift action_28
action_17 (9) = happyGoto action_45
action_17 (10) = happyGoto action_23
action_17 (11) = happyGoto action_43
action_17 _ = happyFail (happyExpListPerState 17)

action_18 _ = happyReduce_32

action_19 (13) = happyShift action_25
action_19 (14) = happyShift action_26
action_19 (15) = happyShift action_18
action_19 (16) = happyShift action_27
action_19 (17) = happyShift action_28
action_19 (9) = happyGoto action_44
action_19 (10) = happyGoto action_23
action_19 (11) = happyGoto action_43
action_19 _ = happyFail (happyExpListPerState 19)

action_20 (13) = happyShift action_25
action_20 (14) = happyShift action_26
action_20 (15) = happyShift action_18
action_20 (16) = happyShift action_27
action_20 (17) = happyShift action_28
action_20 (9) = happyGoto action_42
action_20 (10) = happyGoto action_23
action_20 (11) = happyGoto action_43
action_20 _ = happyFail (happyExpListPerState 20)

action_21 (26) = happyShift action_32
action_21 (27) = happyShift action_33
action_21 _ = happyReduce_13

action_22 (18) = happyShift action_34
action_22 (19) = happyShift action_35
action_22 (20) = happyShift action_36
action_22 (21) = happyShift action_37
action_22 (22) = happyShift action_38
action_22 (23) = happyShift action_39
action_22 (24) = happyShift action_40
action_22 (25) = happyShift action_41
action_22 _ = happyFail (happyExpListPerState 22)

action_23 _ = happyReduce_23

action_24 (26) = happyReduce_15
action_24 (27) = happyReduce_15
action_24 (36) = happyReduce_15
action_24 (39) = happyReduce_15
action_24 (40) = happyReduce_15
action_24 _ = happyReduce_22

action_25 _ = happyReduce_28

action_26 _ = happyReduce_29

action_27 _ = happyReduce_30

action_28 _ = happyReduce_31

action_29 (26) = happyShift action_32
action_29 (27) = happyShift action_33
action_29 _ = happyReduce_12

action_30 (28) = happyShift action_7
action_30 (29) = happyShift action_8
action_30 (30) = happyShift action_9
action_30 (31) = happyShift action_10
action_30 (32) = happyShift action_11
action_30 (33) = happyShift action_12
action_30 (34) = happyShift action_3
action_30 (37) = happyShift action_13
action_30 (38) = happyShift action_14
action_30 (4) = happyGoto action_31
action_30 (6) = happyGoto action_5
action_30 (7) = happyGoto action_6
action_30 (12) = happyGoto action_2
action_30 _ = happyFail (happyExpListPerState 30)

action_31 (36) = happyShift action_62
action_31 _ = happyFail (happyExpListPerState 31)

action_32 (13) = happyShift action_25
action_32 (14) = happyShift action_26
action_32 (15) = happyShift action_18
action_32 (16) = happyShift action_27
action_32 (17) = happyShift action_28
action_32 (8) = happyGoto action_61
action_32 (9) = happyGoto action_22
action_32 (10) = happyGoto action_23
action_32 (11) = happyGoto action_24
action_32 _ = happyFail (happyExpListPerState 32)

action_33 (13) = happyShift action_25
action_33 (14) = happyShift action_26
action_33 (15) = happyShift action_18
action_33 (16) = happyShift action_27
action_33 (17) = happyShift action_28
action_33 (8) = happyGoto action_60
action_33 (9) = happyGoto action_22
action_33 (10) = happyGoto action_23
action_33 (11) = happyGoto action_24
action_33 _ = happyFail (happyExpListPerState 33)

action_34 (13) = happyShift action_25
action_34 (14) = happyShift action_26
action_34 (15) = happyShift action_18
action_34 (16) = happyShift action_27
action_34 (17) = happyShift action_28
action_34 (9) = happyGoto action_59
action_34 (10) = happyGoto action_23
action_34 (11) = happyGoto action_43
action_34 _ = happyFail (happyExpListPerState 34)

action_35 (13) = happyShift action_25
action_35 (14) = happyShift action_26
action_35 (15) = happyShift action_18
action_35 (16) = happyShift action_27
action_35 (17) = happyShift action_28
action_35 (9) = happyGoto action_58
action_35 (10) = happyGoto action_23
action_35 (11) = happyGoto action_43
action_35 _ = happyFail (happyExpListPerState 35)

action_36 (13) = happyShift action_25
action_36 (14) = happyShift action_26
action_36 (15) = happyShift action_18
action_36 (16) = happyShift action_27
action_36 (17) = happyShift action_28
action_36 (9) = happyGoto action_57
action_36 (10) = happyGoto action_23
action_36 (11) = happyGoto action_43
action_36 _ = happyFail (happyExpListPerState 36)

action_37 (13) = happyShift action_25
action_37 (14) = happyShift action_26
action_37 (15) = happyShift action_18
action_37 (16) = happyShift action_27
action_37 (17) = happyShift action_28
action_37 (9) = happyGoto action_56
action_37 (10) = happyGoto action_23
action_37 (11) = happyGoto action_43
action_37 _ = happyFail (happyExpListPerState 37)

action_38 (13) = happyShift action_25
action_38 (14) = happyShift action_26
action_38 (15) = happyShift action_18
action_38 (16) = happyShift action_27
action_38 (17) = happyShift action_28
action_38 (9) = happyGoto action_55
action_38 (10) = happyGoto action_23
action_38 (11) = happyGoto action_43
action_38 _ = happyFail (happyExpListPerState 38)

action_39 (13) = happyShift action_25
action_39 (14) = happyShift action_26
action_39 (15) = happyShift action_18
action_39 (16) = happyShift action_27
action_39 (17) = happyShift action_28
action_39 (9) = happyGoto action_54
action_39 (10) = happyGoto action_23
action_39 (11) = happyGoto action_43
action_39 _ = happyFail (happyExpListPerState 39)

action_40 (13) = happyShift action_25
action_40 (14) = happyShift action_26
action_40 (15) = happyShift action_18
action_40 (16) = happyShift action_27
action_40 (17) = happyShift action_28
action_40 (9) = happyGoto action_53
action_40 (10) = happyGoto action_23
action_40 (11) = happyGoto action_43
action_40 _ = happyFail (happyExpListPerState 40)

action_41 (13) = happyShift action_25
action_41 (14) = happyShift action_26
action_41 (15) = happyShift action_18
action_41 (16) = happyShift action_27
action_41 (17) = happyShift action_28
action_41 (9) = happyGoto action_52
action_41 (10) = happyGoto action_23
action_41 (11) = happyGoto action_43
action_41 _ = happyFail (happyExpListPerState 41)

action_42 (18) = happyShift action_34
action_42 (19) = happyShift action_35
action_42 (20) = happyShift action_36
action_42 (21) = happyShift action_37
action_42 _ = happyReduce_9

action_43 _ = happyReduce_22

action_44 (18) = happyShift action_34
action_44 (19) = happyShift action_35
action_44 (20) = happyShift action_36
action_44 (21) = happyShift action_37
action_44 _ = happyReduce_10

action_45 (18) = happyShift action_34
action_45 (19) = happyShift action_35
action_45 (20) = happyShift action_36
action_45 (21) = happyShift action_37
action_45 _ = happyReduce_11

action_46 (39) = happyShift action_48
action_46 (5) = happyGoto action_51
action_46 _ = happyFail (happyExpListPerState 46)

action_47 (36) = happyShift action_50
action_47 _ = happyFail (happyExpListPerState 47)

action_48 (28) = happyShift action_7
action_48 (29) = happyShift action_8
action_48 (30) = happyShift action_9
action_48 (31) = happyShift action_10
action_48 (32) = happyShift action_11
action_48 (33) = happyShift action_12
action_48 (34) = happyShift action_3
action_48 (37) = happyShift action_13
action_48 (38) = happyShift action_14
action_48 (4) = happyGoto action_49
action_48 (6) = happyGoto action_5
action_48 (7) = happyGoto action_6
action_48 (12) = happyGoto action_2
action_48 _ = happyFail (happyExpListPerState 48)

action_49 (39) = happyShift action_48
action_49 (5) = happyGoto action_64
action_49 _ = happyReduce_8

action_50 _ = happyReduce_3

action_51 (36) = happyShift action_63
action_51 _ = happyFail (happyExpListPerState 51)

action_52 (18) = happyShift action_34
action_52 (19) = happyShift action_35
action_52 (20) = happyShift action_36
action_52 (21) = happyShift action_37
action_52 _ = happyReduce_19

action_53 (18) = happyShift action_34
action_53 (19) = happyShift action_35
action_53 (20) = happyShift action_36
action_53 (21) = happyShift action_37
action_53 _ = happyReduce_18

action_54 (18) = happyShift action_34
action_54 (19) = happyShift action_35
action_54 (20) = happyShift action_36
action_54 (21) = happyShift action_37
action_54 _ = happyReduce_17

action_55 (18) = happyShift action_34
action_55 (19) = happyShift action_35
action_55 (20) = happyShift action_36
action_55 (21) = happyShift action_37
action_55 _ = happyReduce_16

action_56 (18) = happyShift action_34
action_56 (19) = happyShift action_35
action_56 (20) = happyShift action_36
action_56 (21) = happyShift action_37
action_56 _ = happyReduce_27

action_57 (18) = happyShift action_34
action_57 (19) = happyShift action_35
action_57 (20) = happyShift action_36
action_57 (21) = happyShift action_37
action_57 _ = happyReduce_26

action_58 (18) = happyShift action_34
action_58 (19) = happyShift action_35
action_58 (20) = happyShift action_36
action_58 (21) = happyShift action_37
action_58 _ = happyReduce_25

action_59 (18) = happyShift action_34
action_59 (19) = happyShift action_35
action_59 (20) = happyShift action_36
action_59 (21) = happyShift action_37
action_59 _ = happyReduce_24

action_60 (26) = happyShift action_32
action_60 (27) = happyShift action_33
action_60 _ = happyReduce_21

action_61 (26) = happyShift action_32
action_61 (27) = happyShift action_33
action_61 _ = happyReduce_20

action_62 _ = happyReduce_1

action_63 _ = happyReduce_4

action_64 _ = happyReduce_7

happyReduce_1 = happyReduce 4 4 happyReduction_1
happyReduction_1 (_ `HappyStk`
	(HappyAbsSyn4  happy_var_3) `HappyStk`
	_ `HappyStk`
	(HappyAbsSyn12  happy_var_1) `HappyStk`
	happyRest)
	 = HappyAbsSyn4
		 (ASTLabel happy_var_1 happy_var_3
	) `HappyStk` happyRest

happyReduce_2 = happySpecReduce_2  4 happyReduction_2
happyReduction_2 (HappyAbsSyn12  happy_var_2)
	_
	 =  HappyAbsSyn4
		 (Jump happy_var_2
	)
happyReduction_2 _ _  = notHappyAtAll 

happyReduce_3 = happyReduce 4 4 happyReduction_3
happyReduction_3 (_ `HappyStk`
	(HappyAbsSyn5  happy_var_3) `HappyStk`
	_ `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn4
		 (Menu happy_var_3
	) `HappyStk` happyRest

happyReduce_4 = happyReduce 5 4 happyReduction_4
happyReduction_4 (_ `HappyStk`
	(HappyAbsSyn5  happy_var_4) `HappyStk`
	(HappyAbsSyn4  happy_var_3) `HappyStk`
	_ `HappyStk`
	_ `HappyStk`
	happyRest)
	 = HappyAbsSyn4
		 (Menu2 happy_var_3 happy_var_4
	) `HappyStk` happyRest

happyReduce_5 = happySpecReduce_1  4 happyReduction_5
happyReduction_5 (HappyAbsSyn6  happy_var_1)
	 =  HappyAbsSyn4
		 (AstAsign happy_var_1
	)
happyReduction_5 _  = notHappyAtAll 

happyReduce_6 = happySpecReduce_1  4 happyReduction_6
happyReduction_6 (HappyAbsSyn7  happy_var_1)
	 =  HappyAbsSyn4
		 (AstCond happy_var_1
	)
happyReduction_6 _  = notHappyAtAll 

happyReduce_7 = happySpecReduce_3  5 happyReduction_7
happyReduction_7 (HappyAbsSyn5  happy_var_3)
	(HappyAbsSyn4  happy_var_2)
	_
	 =  HappyAbsSyn5
		 (Choice happy_var_2 happy_var_3
	)
happyReduction_7 _ _ _  = notHappyAtAll 

happyReduce_8 = happySpecReduce_2  5 happyReduction_8
happyReduction_8 (HappyAbsSyn4  happy_var_2)
	_
	 =  HappyAbsSyn5
		 (LastChoice happy_var_2
	)
happyReduction_8 _ _  = notHappyAtAll 

happyReduce_9 = happySpecReduce_3  6 happyReduction_9
happyReduction_9 (HappyAbsSyn9  happy_var_3)
	(HappyAbsSyn11  happy_var_2)
	_
	 =  HappyAbsSyn6
		 (Asign happy_var_2 happy_var_3
	)
happyReduction_9 _ _ _  = notHappyAtAll 

happyReduce_10 = happySpecReduce_3  6 happyReduction_10
happyReduction_10 (HappyAbsSyn9  happy_var_3)
	(HappyAbsSyn11  happy_var_2)
	_
	 =  HappyAbsSyn6
		 (Inc happy_var_2 happy_var_3
	)
happyReduction_10 _ _ _  = notHappyAtAll 

happyReduce_11 = happySpecReduce_3  6 happyReduction_11
happyReduction_11 (HappyAbsSyn9  happy_var_3)
	(HappyAbsSyn11  happy_var_2)
	_
	 =  HappyAbsSyn6
		 (Dec happy_var_2 happy_var_3
	)
happyReduction_11 _ _ _  = notHappyAtAll 

happyReduce_12 = happySpecReduce_2  7 happyReduction_12
happyReduction_12 (HappyAbsSyn8  happy_var_2)
	_
	 =  HappyAbsSyn7
		 (If happy_var_2
	)
happyReduction_12 _ _  = notHappyAtAll 

happyReduce_13 = happySpecReduce_2  7 happyReduction_13
happyReduction_13 (HappyAbsSyn8  happy_var_2)
	_
	 =  HappyAbsSyn7
		 (Elif happy_var_2
	)
happyReduction_13 _ _  = notHappyAtAll 

happyReduce_14 = happySpecReduce_1  7 happyReduction_14
happyReduction_14 _
	 =  HappyAbsSyn7
		 (Else
	)

happyReduce_15 = happySpecReduce_1  8 happyReduction_15
happyReduction_15 (HappyAbsSyn11  happy_var_1)
	 =  HappyAbsSyn8
		 (Flag happy_var_1
	)
happyReduction_15 _  = notHappyAtAll 

happyReduce_16 = happySpecReduce_3  8 happyReduction_16
happyReduction_16 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn8
		 (Eq happy_var_1 happy_var_3
	)
happyReduction_16 _ _ _  = notHappyAtAll 

happyReduce_17 = happySpecReduce_3  8 happyReduction_17
happyReduction_17 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn8
		 (Neq happy_var_1 happy_var_3
	)
happyReduction_17 _ _ _  = notHappyAtAll 

happyReduce_18 = happySpecReduce_3  8 happyReduction_18
happyReduction_18 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn8
		 (Gt happy_var_1 happy_var_3
	)
happyReduction_18 _ _ _  = notHappyAtAll 

happyReduce_19 = happySpecReduce_3  8 happyReduction_19
happyReduction_19 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn8
		 (Lt happy_var_1 happy_var_3
	)
happyReduction_19 _ _ _  = notHappyAtAll 

happyReduce_20 = happySpecReduce_3  8 happyReduction_20
happyReduction_20 (HappyAbsSyn8  happy_var_3)
	_
	(HappyAbsSyn8  happy_var_1)
	 =  HappyAbsSyn8
		 (And happy_var_1 happy_var_3
	)
happyReduction_20 _ _ _  = notHappyAtAll 

happyReduce_21 = happySpecReduce_3  8 happyReduction_21
happyReduction_21 (HappyAbsSyn8  happy_var_3)
	_
	(HappyAbsSyn8  happy_var_1)
	 =  HappyAbsSyn8
		 (Or happy_var_1 happy_var_3
	)
happyReduction_21 _ _ _  = notHappyAtAll 

happyReduce_22 = happySpecReduce_1  9 happyReduction_22
happyReduction_22 (HappyAbsSyn11  happy_var_1)
	 =  HappyAbsSyn9
		 (ExpVar happy_var_1
	)
happyReduction_22 _  = notHappyAtAll 

happyReduce_23 = happySpecReduce_1  9 happyReduction_23
happyReduction_23 (HappyAbsSyn10  happy_var_1)
	 =  HappyAbsSyn9
		 (ExpVal happy_var_1
	)
happyReduction_23 _  = notHappyAtAll 

happyReduce_24 = happySpecReduce_3  9 happyReduction_24
happyReduction_24 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn9
		 (Add happy_var_1 happy_var_3
	)
happyReduction_24 _ _ _  = notHappyAtAll 

happyReduce_25 = happySpecReduce_3  9 happyReduction_25
happyReduction_25 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn9
		 (Sub happy_var_1 happy_var_3
	)
happyReduction_25 _ _ _  = notHappyAtAll 

happyReduce_26 = happySpecReduce_3  9 happyReduction_26
happyReduction_26 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn9
		 (Mul happy_var_1 happy_var_3
	)
happyReduction_26 _ _ _  = notHappyAtAll 

happyReduce_27 = happySpecReduce_3  9 happyReduction_27
happyReduction_27 (HappyAbsSyn9  happy_var_3)
	_
	(HappyAbsSyn9  happy_var_1)
	 =  HappyAbsSyn9
		 (Div happy_var_1 happy_var_3
	)
happyReduction_27 _ _ _  = notHappyAtAll 

happyReduce_28 = happySpecReduce_1  10 happyReduction_28
happyReduction_28 (HappyTerminal (TokenInt happy_var_1))
	 =  HappyAbsSyn10
		 (Int happy_var_1
	)
happyReduction_28 _  = notHappyAtAll 

happyReduce_29 = happySpecReduce_1  10 happyReduction_29
happyReduction_29 (HappyTerminal (TokenFloat happy_var_1))
	 =  HappyAbsSyn10
		 (Float happy_var_1
	)
happyReduction_29 _  = notHappyAtAll 

happyReduce_30 = happySpecReduce_1  10 happyReduction_30
happyReduction_30 _
	 =  HappyAbsSyn10
		 (Bool True
	)

happyReduce_31 = happySpecReduce_1  10 happyReduction_31
happyReduction_31 _
	 =  HappyAbsSyn10
		 (Bool False
	)

happyReduce_32 = happySpecReduce_1  11 happyReduction_32
happyReduction_32 (HappyTerminal (TokenVar happy_var_1))
	 =  HappyAbsSyn11
		 (Var happy_var_1
	)
happyReduction_32 _  = notHappyAtAll 

happyReduce_33 = happySpecReduce_1  12 happyReduction_33
happyReduction_33 (HappyTerminal (TokenLabel happy_var_1))
	 =  HappyAbsSyn12
		 (Label happy_var_1
	)
happyReduction_33 _  = notHappyAtAll 

happyNewToken action sts stk [] =
	action 40 40 notHappyAtAll (HappyState action) sts stk []

happyNewToken action sts stk (tk:tks) =
	let cont i = action i i tk (HappyState action) sts stk tks in
	case tk of {
	TokenInt happy_dollar_dollar -> cont 13;
	TokenFloat happy_dollar_dollar -> cont 14;
	TokenVar happy_dollar_dollar -> cont 15;
	TokenTrue -> cont 16;
	TokenFalse -> cont 17;
	TokenAdd -> cont 18;
	TokenSub -> cont 19;
	TokenMul -> cont 20;
	TokenDiv -> cont 21;
	TokenEq -> cont 22;
	TokenNeq -> cont 23;
	TokenGt -> cont 24;
	TokenLt -> cont 25;
	TokenAnd -> cont 26;
	TokenOr -> cont 27;
	TokenIf -> cont 28;
	TokenElif -> cont 29;
	TokenElse -> cont 30;
	TokenAsign -> cont 31;
	TokenInc -> cont 32;
	TokenDec -> cont 33;
	TokenLabel happy_dollar_dollar -> cont 34;
	TokenBlockStart -> cont 35;
	TokenBlockEnd -> cont 36;
	TokenMenu -> cont 37;
	TokenJump -> cont 38;
	TokenChoice -> cont 39;
	_ -> happyError' ((tk:tks), [])
	}

happyError_ explist 40 tk tks = happyError' (tks, explist)
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

-- data AST = ASTLabel Label AST
--       | Jump Label
--       | Menu Choices
--       | Menu2 AST Choices
--       | AstAsign Asign
--       | AstCond Cond

-- data Choices = Choice AST Choices
--             | LastChoice AST

-- newtype Label = Label String deriving Show

-- data Asign = Asign Var Exp
--       | Inc Var Exp
--       | Dec Var Exp
--       deriving Show

-- data Cond = If Flag
--         | Elif Flag
--         | Else
--         deriving Show

-- data Flag = Flag Var
--       | Eq Exp Exp
--       | Neq Exp Exp
--       | Gt Exp Exp
--       | Lt Exp Exp
--       | And Flag Flag
--       | Or Flag Flag
--       deriving Show

-- data Exp = ExpVal Val
--       | ExpVar Var
--       | Add Exp Exp
--       | Sub Exp Exp
--       | Mul Exp Exp
--       | Div Exp Exp
--       deriving Show

-- data Val
--       = Int Int
--         | Float Float
--         | Bool Bool
--       deriving Show

-- newtype Var = Var String deriving Show

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
        | TokenJump
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
