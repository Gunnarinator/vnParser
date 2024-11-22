module Generate where

-- The abstract syntax tree for our program
data AST = ASTLabel Label AST
      | Jump Label
      | Menu Choices
      | Menu2 AST Choices
      | AstAsign Asign
      | AstCond Cond
      deriving Show

-- The choices in the graph
data Choices = Choice AST Choices
            | LastChoice AST
            deriving Show

-- A label
newtype Label = Label String deriving Show

-- Assignment and increment statements
data Asign = Asign Var Exp
      | Inc Var Exp
      | Dec Var Exp
      deriving Show

-- Conditional logic
data Cond = If Flag
        | Elif Flag
        | Else
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
