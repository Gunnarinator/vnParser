module Generate where

-- The abstract syntax tree for our program
data AST = ASTLabel Label Lines
      | Jump String
      | Menu Choices
      | Menu2 Lines Choices
      | AstAsign Asign
      | AstCond Cond
      deriving Show

-- Structure for multiple lines
newtype Lines = Lines [AST]
                deriving Show

-- The choices in the graph
newtype Choices = Choices [Lines]
                deriving Show

-- A label
newtype Label = Label String deriving Show

-- Assignment and increment statements
data Asign = Asign Var Exp
      | Inc Var Exp
      | Dec Var Exp
      deriving Show

-- Conditional logic
data Cond = If Flag Lines
        | Elif Flag Lines
        | Else Lines
        deriving Show

-- Boolean conditions
data Flag = Flag Var
      | Eq Exp Exp
      | Neq Exp Exp
      | Gt Exp Exp
      | Lt Exp Exp
      | And Flag Flag
      | Or Flag Flag
      deriving Show

-- Expressions
data Exp = ExpVal Val
      | ExpVar Var
      | Add Exp Exp
      | Sub Exp Exp
      | Mul Exp Exp
      | Div Exp Exp
      deriving Show

-- Values
data Val
      = Int Int
        | Float Float
        | Bool Bool
      deriving Show

-- Variables
newtype Var = Var String deriving Show


-- Some examples
-- parse [TokenAsign, TokenVar "x", TokenInt 1]
test1 :: Lines
test1 = Lines [AstAsign (Asign (Var "x") (ExpVal (Int 1)))]

-- parse [TokenAsign, TokenVar "x", TokenInt 1, TokenLabel "start_label", TokenBlockStart, TokenMenu, TokenBlockStart, TokenChoice, TokenBlockStart, TokenJump, TokenLabel "start_label", TokenBlockEnd, TokenBlockEnd, TokenBlockEnd]
test2 :: Lines
test2 = Lines [AstAsign (Asign (Var "x") (ExpVal (Int 1))),ASTLabel (Label "start_label") (Lines [Menu (Choices [Lines [Jump "start_label"]])])]

-- parse [TokenIf, TokenVar "x", TokenEq, TokenInt 1, TokenBlockStart, TokenInc, TokenVar "x", TokenInt 1, TokenBlockEnd]
test3 :: Lines
test3 = Lines [AstCond (If (Eq (ExpVar (Var "x")) (ExpVal (Int 1))) (Lines [AstAsign (Inc (Var "x") (ExpVal (Int 1)))]))]