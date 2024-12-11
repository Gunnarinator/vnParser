module Utils where 
    import Control.Exception
    import Lexer as L
    import Data as D
    import qualified Data.Set as Set
    import Data.List
    import Data.Char (isDigit)

    --single token satisfier functions

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

    isLineStartToken :: Token -> Bool
    isLineStartToken Tab = True 
    isLineStartToken Label = True 
    isLineStartToken _ = False

    --the following functions are token unpackers
    varName :: Token -> String 
    varName (L.Var x) = x 
    varName _ = ""

    getVal :: Token -> Val 
    getVal (Num x) = Int (read x) 
    getVal (L.Bool True) = D.Bool True
    getVal (L.Bool False) = D.Bool False
    getVal (L.Var "True") = D.Bool True
    getVal (L.Var "False") = D.Bool False
    getVal (Text x) = String x 

    textVal :: Token -> String 
    textVal (Text x) = x 
    textVal _ = ""

    symbVal :: Token -> String 
    symbVal (Symbol x) = x 
    symbVal _ = ""

    getFlag :: D.Cond -> String 
    getFlag (D.If cond body) = show cond 
    getFlag (D.Elif cond body) = show cond 
    getFlag _ = ""

    --the strings of text often have italic tags and we wanna drop those.
    cleanStr :: String -> String 
    cleanStr s = let s2 = drop 4 (reverse $ drop 4 (reverse s)) in 
        if length s2 > 30 then take 27 s2 ++ "..." else s2
    
    --these two functions are just "Show" on a list of tokens but with newlines on tab
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


    --wrapper for findNextNode
    getNext :: [AST] -> [Node] -> Node -> (Node, [Node])
    getNext as ns n = 
        let (cNext, cEnv) = findNextNode as ns in 
            if cNext == defNode
                then (n, ns) 
                else (cNext, cEnv)

    --try to find the next node that we should be pointing to.
    findNextNode :: [AST] -> [Node] -> (Node, [Node])
    findNextNode [] nEnv = (defNode, nEnv)
    findNextNode (a:as) nEnv = 
        case a of 
            ASTLabel str _ -> findNode str nEnv Blue
            ASTJump str -> findNode str nEnv Blue
            _ -> findNextNode as nEnv

    --finds a node in a list with a given label or adds that node
    findNode :: String -> [Node] -> NodeColor -> (Node, [Node]) 
    findNode str ns c = let (b, n) = strInNEnv str ns in 
        if b then (n, ns) else let new = Node str (length ns) c in (new, new:ns)

    -- tries to find a node by label and id
    isNum :: String -> Bool
    isNum "" = True
    isNum (c:cs) = if isDigit c then isNum cs else False

    -- tries to find a node by id first and then by label if that's not available
    findNodeIdLabel :: String -> [Node] -> Maybe Node
    findNodeIdLabel s = if isNum s then findNodeId (read s) else findNodeLabel s

    -- find a node in a list by the label
    findNodeLabel :: String -> [Node] -> Maybe Node
    findNodeLabel l = find (\(Node l' _ _) -> l' == l)

    -- find a node in a list by the id
    findNodeId :: Int -> [Node] -> Maybe Node
    findNodeId i = find (\(Node _ i' _) -> i' == i)

    strInNEnv :: String -> [Node] -> (Bool, Node)
    strInNEnv _ [] = (False, defNode)
    strInNEnv str ((Node l i c):ns) = if str == l then (True, Node l i c) else strInNEnv str ns

    --if we turn it into a set, then turn it back... it'll get rid of the duplicates.
    dropDupes :: Ord a => [a] -> [a] 
    dropDupes xs = Set.toList $ Set.fromList xs

    --delete edges that point to themselves
    delSame :: [Edge] -> [Edge]
    delSame [] = [] 
    delSame (e:es) = 
        if getF e == getT e then delSame es 
        else e:delSame es

    --default Edge
    defEdge :: Edge 
    defEdge = Edge (Node "" 0 Blue) (Node "" 0 Blue) ""

    --a node is "linear" if it points to one node and one node points to it.
    isLinear :: Node -> [Edge] -> Either Bool (Edge, Edge)
    isLinear n es = isLinearInner n es (defEdge, defEdge)

    isLinearInner :: Node -> [Edge] -> (Edge, Edge) -> Either Bool (Edge, Edge)
    isLinearInner n [] (f1, t1) = 
        if f1 == defEdge || t1 == defEdge 
            then Left False 
            else Right (f1, t1)

    isLinearInner n ((Edge f t l):es) (f1,t1) 
        | n == f = if f1 == defEdge && Edge f t l /= f1 && Edge f t l /= t1
                then isLinearInner n es (Edge f t l, t1)
                else Left False
        | n == t = if t1 == defEdge && Edge f t l /= f1 && Edge f t l /= t1
            then isLinearInner n es (f1, Edge f t l)
            else Left False
        | otherwise = isLinearInner n es (f1, t1)


    weldEdge :: (Edge, Edge) -> Edge 
    weldEdge (Edge f1 t1 l1, Edge f2 t2 l2) =
        Edge f1 t2 ""

    --remove linear nodes from the list of nodes, remove their edges from the list of edges.
    cullEdges :: [Node] -> [Edge] -> [Edge]
    cullEdges [] es = es 
    cullEdges (n:ns) es = 
        case isLinear n es of 
            Left _ -> cullEdges ns es 
            Right (t, f) -> 
                cullEdges ns (dropDupes (weldEdge (f, t) : delete f (delete t es)))

    --remove all linear nodes and all of their edges
    fullCull :: [Node] -> [Edge] -> [Edge] 
    fullCull ns es = 
        let nextEs = cullEdges ns es in 
            if nextEs == es then nextEs 
            else fullCull ns nextEs

    
    cleanResults :: ([Node], [Edge]) -> ([Node], [Edge])
    cleanResults (ns, es) = 
        let finalEs = dropDupes (fullCull ns (delSame es)) in 
            (dropDupes $ readEdges finalEs, dropDupes finalEs)

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


    --return the choices from the list that don't go anywhere.
    getEmpties :: [Choice] -> [Edge] -> [Choice]
    getEmpties cs es = getEmptiesInner cs es [] es
    
    getEmptiesInner :: [Choice] -> [Edge] -> [Choice] -> [Edge] -> [Choice]
    --for c in cs, if c is in no edges, then add it to the retval list
    getEmptiesInner [] _ ret _ = ret 
    getEmptiesInner (c:cs) [] ret ogEs = getEmptiesInner cs ogEs (c:ret) ogEs
    getEmptiesInner (c:cs) ((Edge f t l):es) ret ogEs = 
        if getChoiceLabel c == l 
            then getEmptiesInner cs ogEs ret ogEs
            else getEmptiesInner (c:cs) es ret ogEs



    --let checkEs = checkChoices cs curN (head as)
    checkChoices :: [Choice] -> Node -> AST -> [Edge] -> [Choice]
    checkChoices [] _ _ _ = []
    checkChoices _ _ _ [] = []
    checkChoices cs n a es = 
        case a of 
            ASTLabel _ _ -> getEmpties cs es
            _ -> []

    --some vars for cull edges testing
    a = Node "a" 1 Blue 
    b = Node "b" 2 Blue 
    c = Node "c" 3 Blue 
    d = Node "d" 4 Blue
    e = Node "e" 5 Blue

    ab = Edge a b "" 
    bc = Edge b c "" 
    bd = Edge b d "" 
    cd = Edge c d ""
    de = Edge d e ""


    ns = [a, b, c, d, e]
    es = [ab, bc, bd, cd, de]