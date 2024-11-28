module Data where 

    import Control.Exception

    -- Labels, jumps, and variables
    type Label = String
    type Jump = String
    type Var = String

    type VarEnv = [(Var, Val)]

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
    data Cond = If Flag [AST]
        | Elif Flag [AST]
        | Else [AST]
        deriving (Show, Eq)

    -- Assignment/increment
    data Assign = Assign Var Exp
        | Inc Var Exp
        | Dec Var Exp
        deriving (Show, Eq)

    -- Full AST
    data Choice = Choice String (Maybe Cond) [AST]
        deriving (Show, Eq)

    data AST = ASTLabel Label [AST]
            | ASTChoices [Choice]
            | ASTJump Label
            | ASTConds [Cond]
            | ASTAssign Assign
            deriving (Show, Eq)


    
    --Each Node is its label and the list of things it points to
    data Node = Node Label [Edge] deriving (Show, Eq)
    
    --CNodes are an intermediary so the node can hang onto the choice text
    type CNode = (Node, String)
    --edges are "from, to, (maybe edgeLabel)"
    data Edge = Edge Node Node String deriving (Show, Eq)