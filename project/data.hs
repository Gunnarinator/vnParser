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
        deriving Eq
    
    instance Show Flag where 
        show (And x y) = show x ++ " && " ++ show y 
        show (Or x y) = show x ++ " || " ++ show y 
        show (Base v) = show v 
        show (Eq x y) = show x ++ " == " ++ show y 
        show (Neq x y) = show x ++ " != " ++ show y 
        show (Gt x y) = show x ++ " > " ++ show y
        show (Lt x y) = show x ++ " < " ++ show y

    -- Conditions
    data Cond = If Flag [AST]
        | Elif Flag [AST]
        | Else [AST]
        deriving (Show, Eq)

    -- Assignment/increment
    data Assign = Assign Var Exp
        | Inc Var Exp
        | Dec Var Exp
        deriving Eq
    
    instance Show Assign where 
        show (Assign v xp) = "Assign " ++ show v ++ " = " ++ show xp
        show (Inc v xp) = "Assign " ++ show v ++ " += " ++ show xp
        show (Dec v xp) = "Assign " ++ show v ++ " -= " ++ show xp
    

    -- Full AST
    data Choice = Choice String (Maybe Cond) [AST]
        deriving Eq
    
    instance Show Choice where 
        show (Choice str mc xp) = case mc of 
            Just c -> "Choice - " ++ str ++ show c ++ "\n" ++ show xp
            Nothing -> "Choice - " ++ str ++ "\n" ++ show xp

    data AST = ASTLabel Label [AST]
            | ASTChoices [Choice]
            | ASTJump Label
            | ASTConds [Cond]
            | ASTAssign Assign
            | ASTLine
        deriving Eq

    instance Show AST where 
        show ASTLine = "" 
        show (ASTLabel x xs) = "\n{Label: " ++ x ++ "\n" ++ show xs ++ "}\n"
        show (ASTChoices cs) = "\n{Choice Branch: " ++ show cs ++ "}\n"
        show (ASTAssign a) = "\n" ++ show a ++ ""
        show (ASTConds cs) = "\n" ++ show cs ++ "\n"
        show (ASTJump x) = "\nJump to " ++ x ++ "\n"



    
    --Each Node is its label and the list of things it points to
    data Node = Node Label [Edge] deriving Eq 
    instance Show Node where 
        show (Node l _) = "\nNode: " ++ l

    instance Ord Node where 
        (Node one _) <= (Node two _) = one <= two
    
    --CNodes are an intermediary so the node can hang onto the choice text
    type CNode = (Node, String)
    --edges are "from, to, (maybe edgeLabel)"
    data Edge = Edge Node Node String deriving Eq 
    instance Show Edge where 
        show (Edge (Node f _) (Node t _) c) = case c of 
            "" -> "\nEdge\n\tFrom: " ++ f ++ "\n\tTo: " ++ t ++ "\n\n"
            _ -> "\nEdge\n\tFrom: " ++ f ++ "\n\tTo: " ++ t ++ "\n\tVia: " ++ c ++ "\n"