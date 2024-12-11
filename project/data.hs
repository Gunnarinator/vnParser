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
        | GtEq Exp Exp 
        | LtEq Exp Exp
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
        show (LtEq x y) = show x ++ " <= " ++ show y
        show (GtEq x y) = show x ++ " >= " ++ show y

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

    getChoiceLabel :: Choice -> String
    getChoiceLabel (Choice s _ _) = s
    
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
        show (ASTAssign a) = "\n" ++ show a ++ "\n"
        show (ASTConds cs) = "\n" ++ show cs ++ "\n"
        show (ASTJump x) = "\nJump to " ++ x ++ "\n"


    getLabelText :: AST -> Label
    getLabelText (ASTLabel x _) = x

    data NodeColor = Red | Blue | Green deriving (Eq)
    instance Show NodeColor where 
        show Red = "#FF0000"
        show Blue = "#0000FF"
        show Green = "#00FF00"

    
    --Each Node is its label and the list of things it points to
    data Node = Node Label Int NodeColor deriving Eq
    instance Show Node where 
        show (Node l i c) = "\nNode " ++ l ++ " " ++ show i ++ " " ++ show c

    --default node
    defNode = Node "" 0 Red

    instance Ord Node where 
        (Node _ a _) <= (Node _ b _) = a <= b
    
    --edges are "from, to, (maybe edgeLabel)"
    data Edge = Edge Node Node String
    instance Show Edge where 
        show (Edge (Node f fi _) (Node t ti _) c) = case c of 
            "" -> "\nEdge\n\tFrom: " ++ show fi ++ " ( " ++ f ++ ")\n\tTo: " ++ show ti ++ " ( " ++ t ++ ")\n\n"
            "Nothing" -> "\nEdge\n\tFrom: " ++ show fi ++ " ( " ++ f ++ ")\n\tTo: " ++ show ti ++ " ( " ++ t ++ ")\n\n"
            thing -> "\nEdge\n\tFrom: " ++ show fi ++ " ( " ++ f ++ ")\n\tTo: " ++ show ti ++ " ( " ++ t ++ ")\n\tVia: " ++ c ++ "\n"

    instance Eq Edge where 
        (Edge f1 t1 _) == (Edge f2 t2 _) = 
            f1 == f2 && t1 == t2

    instance Ord Edge where 
        (Edge a1 a2 _) <= (Edge b1 b2 _) = (show a1 ++ show a2) <= (show b1 ++ show b2)

    
    getF :: Edge -> Node 
    getF (Edge f _ _) = f 

    getT :: Edge -> Node 
    getT (Edge _ t _) = t