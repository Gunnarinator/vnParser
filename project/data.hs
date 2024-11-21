module Data where 

    import Control.Exception

    -- Labels, jumps, and variables
    type Label = String
    type Jump = String
    type Var = String

    -- Values
    data Val = String String
        | Bool Bool
        | Int Int
        | Tuple [Val]
        | Lines [Val]
        deriving (Show, Eq)

    -- Values or variables
    data Exp = Var Var
        | Val Val
        | Add Exp Exp
        | Sub Exp Exp
        | Mul Exp Exp
        | Div Exp Exp
        deriving (Show, Eq)

    -- Flags
    data Flag = Base Var
        | Eq Exp Exp
        | Neq Exp Exp
        | Gt Exp Exp
        | Lt Exp Exp
        | And Flag Flag
        | Or Flag Flag
        deriving (Show, Eq)

    -- Conditions
    data Cond = If Flag
        | Elif Flag
        | Else
        deriving (Show, Eq)

    -- Assignment/increment
    data Asign = Asign Var Exp
        | Inc Var Exp
        | Dec Var Exp
        deriving (Show, Eq)

    -- Full AST
    type Choice = AST
    data AST = ASTLabel Label [AST]
            | ASTChoices [Choice]
            | ASTLines [AST]
            | ASTJump Label
            | ASTConds [Cond]
            | ASTAsign Asign
            deriving (Show, Eq)