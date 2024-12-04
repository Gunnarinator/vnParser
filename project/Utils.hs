module Utils where 
    import Control.Exception
    import Lexer as L
    import Data as D
    import State as S
    import qualified Data.Set as Set

    isColonToken :: Token -> Bool 
    isColonToken Colon = True 
    isColonToken _ = False

    isOrToken :: Token -> Bool
    isOrToken BoolOr = True
    isOrToken _ = False

    isAndToken :: Token -> Bool
    isAndToken BoolAnd = True
    isAndToken _ = False

    isTextToken :: Token -> Bool 
    isTextToken (Text x) = True
    isTextToken _ = False

    isSymbolToken :: Token -> Bool 
    isSymbolToken (Symbol x) = True
    isSymbolToken _ = False

    isLabelToken :: Token -> Bool 
    isLabelToken Label = True 
    isLabelToken _ = False

    isJumpToken :: Token -> Bool 
    isJumpToken Jump = True
    isJumpToken _ = False

    isTabToken :: Token -> Bool 
    isTabToken Tab = True 
    isTabToken _ = False

    isExtendToken :: Token -> Bool 
    isExtendToken Extend = True 
    isExtendToken _ = False

    isMenuToken :: Token -> Bool 
    isMenuToken Menu = True 
    isMenuToken _ = False

    isVarToken :: Token -> Bool 
    isVarToken (L.Var x) = True
    isVarToken _ = False

    varVal :: Token -> String 
    varVal (L.Var x) = x 
    varval _ = ""

    isOpenParen :: Token -> Bool 
    isOpenParen OpenParen = True 
    isOpenParen _ = False

    isCloseParen :: Token -> Bool 
    isCloseParen CloseParen = True 
    isCloseParen _ = False

    isConditionToken :: Token -> Bool 
    isConditionToken (Cond x) = True 
    isConditionToken _ = False

    isDollarToken :: Token -> Bool 
    isDollarToken Dollar = True
    isDollarToken _ = False 

    isVarDefine :: Token -> Bool 
    isVarDefine VarDefine = True 
    isVarDefine _ = False

    isValToken :: Token -> Bool 
    isValToken (L.Num x) = True 
    isValToken (L.Var "True") = True 
    isValToken (L.Var "False") = True 
    isValToken (L.Bool x) = True 
    isValToken (Text x) = True 
    isValToken _ = False 

    --There are SO MANY tokens we don't care about
    isLineStartToken :: Token -> Bool
    isLineStartToken Tab = True 
    isLineStartToken Label = True 
    isLineStartToken _ = False

    getVal :: Token -> Val 
    getVal (Num x) = Int (read x) 
    getVal (L.Bool True) = D.Bool True
    getVal (L.Bool False) = D.Bool False
    getVal (L.Var "True") = D.Bool True
    getVal (L.Var "False") = D.Bool False
    getVal (Text x) = String x 



    varName :: Token -> String 
    varName (L.Var x) = x 
    varName _ = ""

    textVal :: Token -> String 
    textVal (Text x) = x 
    textVal _ = ""

    symbVal :: Token -> String 
    symbVal (Symbol x) = x 
    symbVal _ = ""


    hasThings :: [a] -> Bool 
    hasThings [] = False 
    hasThings _ = True

    cleanStr :: String -> String 
    cleanStr s = let s2 = drop 4 (reverse $ drop 4 (reverse s)) in 
        if length s2 > 30 then take 27 s2 ++ "..." else s2
    

    toString :: [Token] -> String 
    toString [] = ""
    toString (x:xs) = case x of 
        Tab -> show x ++ ", " ++ toString xs 
        _ -> lineToString (x:xs)

    lineToString :: [Token] -> String 
    lineToString [] = "" 
    lineToString (x:xs) = case x of 
        Tab -> "\n" ++ show x ++ ", " ++ toString xs 
        y -> show y ++ ", " ++ lineToString xs

    getFlag :: D.Cond -> String 
    getFlag (D.If cond body) = show cond 
    getFlag (D.Elif cond body) = show cond 
    getFlag _ = ""


    --finds a node in a list with a given label or adds that node
    findNode :: String -> [Node] -> NodeColor -> (Node, [Node]) 
    findNode str ns c = let (b, n) = strInNEnv str ns in 
        if b then (n, ns) else let new = Node str (length ns) c in (new, new:ns)

    strInNEnv :: String -> [Node] -> (Bool, Node)
    strInNEnv _ [] = (False, Node "" 0 Red)
    strInNEnv str ((Node l i c):ns) = if str == l then (True, Node l i c) else strInNEnv str ns

    dropDupes :: Ord a => [a] -> [a] 
    dropDupes xs = Set.toList $ Set.fromList xs

    --delete edges that point to themselves
    delSame :: [Edge] -> [Edge]
    delSame [] = [] 
    delSame (e:es) = 
        if getF e == getT e then delSame es 
        else e:delSame es

    cleanResults :: ([Node], [Edge]) -> ([Node], [Edge])
    cleanResults (ns, es) = (dropDupes $ readEdges es, dropDupes (delSame es))

    --connect the node to the first node in each of the edges
    connect :: Node -> [Edge] -> [Edge]
    connect _ [] = [] 
    connect n ((Edge f t l):es) = 
        if n /= f && n /= t then Edge n f "" : connect n es
        else connect n es
    
    --we got all the edges from node 1 to node 2, just make a list of nodes
    readEdges :: [Edge] -> [Node]
    readEdges [] = []
    readEdges ((Edge from to _):es) = [from, to] ++ readEdges es
    