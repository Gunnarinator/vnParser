module TestGrammer where

import Data (Var(..), Val(..), Exp(..), Cond(..), evalExp, evalCond)

-- Example variables
var1 = IntVar "x" 0
var2 = BoolVar "flag" False
var3 = StringVar "name" "Alice"

-- Example values
val1 = Int 10
val2 = Bool True
val3 = String "Bob"

-- Example expressions
exp1 = EqExp var1 val1
exp2 = NeqExp var2 val2
exp3 = GTExp var1 (Int 5)
exp4 = AndExp exp1 exp3
exp5 = OrExp exp2 (EqExp var3 val3)

-- Example conditions
cond1 = If exp1
cond2 = ElseIf exp2
cond3 = Else exp3

-- Example test function
testExpressions :: IO ()
testExpressions = do
    -- Print evaluation results for individual expressions
    print (evalExp exp1)
    print (evalExp exp2)
    print (evalExp exp3)
    print (evalExp exp4)
    print (evalExp exp5)
    print "\n"
    print (evalCond cond1)
    print (evalCond cond2)
    print (evalCond cond3)


-- Call the test function in main
main :: IO ()
main = testExpressions