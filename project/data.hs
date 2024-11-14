module Data where 

    import Control.Exception


    --type definitions 
    type Label = String 
    type Jump = String 

    data Var = 
        IntVar String Int 
        | BoolVar String Bool 
        | StringVar String String 
        deriving (Show, Eq)

    data Val = 
        Int Int 
        | Bool Bool 
        | String String
        deriving (Show, Eq)

    --the conditional bit in an if statement
    data Exp = 
        EqExp Var Val 
        | NeqExp Var Val 
        | GTExp Var Val 
        | LTExp Var Val 
        | OrExp Exp Exp 
        | AndExp Exp Exp
        deriving (Show, Eq)

    data Cond = 
        If Exp 
        | ElseIf Exp 
        | Else Exp 
        deriving (Show, Eq)

    data Line = 
        Label Label 
        | Jump Jump 
        | VarDefine Var Val 
        | VarSet Var Val 
        | Condition Cond [Line] 
        | Choice [Line]
        deriving (Show, Eq)

    type Paragraph = (Label, [Line])
    type VarEnv = [(Var, Val)]


    -- Errors.
    data VarError =
        NotInEnv String
        | TypeMisMatch Var Var
        deriving (Show)
    instance Exception VarError


    
    data DTree = Leaf Paragraph | Node Paragraph [DTree]

