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


    -- Evaluating expressions
    evalExp :: Exp -> Bool
    evalExp (EqExp (IntVar _ v) (Int i)) = v == i
    evalExp (EqExp (BoolVar _ v) (Bool i)) = v == i
    evalExp (EqExp (StringVar _ v) (String i)) = v == i
    evalExp (NeqExp (IntVar _ v) (Int i)) = v /= i
    evalExp (NeqExp (BoolVar _ v) (Bool i)) = v /= i
    evalExp (NeqExp (StringVar _ v) (String i)) = v /= i
    evalExp (GTExp (IntVar  _ v) (Int i)) = v > i
    evalExp (LTExp (IntVar  _ v) (Int i)) = v < i
    evalExp (OrExp e1 e2) = evalExp e1 || evalExp e2
    evalExp (AndExp e1 e2) = evalExp e1 && evalExp e2
    evalExp _ = error "Invalid expression or mismatched types."

    -- Evaluating conditions
    evalCond :: Cond -> Bool
    evalCond (If e) = evalExp e
    evalCond (ElseIf e) = evalExp e
    evalCond (Else e) = evalExp e