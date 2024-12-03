module Main where 

    import System.IO
    import Data.Char
    import Lexer
    import TokenParser as TP
    import Parser as P
    import Data
    import Utils
    import HTMLify
    import qualified Data.Set as Set

    --just gimme a list of all the nodes and edges
    flattenForest :: [AST] -> ([Node], [Edge]) 
    flattenForest [] = ([], [])
    flattenForest (x:xs) = let (Node l edges) = nodifyLabel x in 
        let (ns, es) = flattenForest xs in 
            (Node l [] : ns, edges++es)


    --flattenForest is good at getting edges but bad at getting nodes
    readEdges :: ([Node], [Edge]) -> ([Node], [Edge])
    readEdges ([], _) = ([], [])
    readEdges (_, []) = ([], [])
    readEdges (ns, es) = let (n, (Edge from to c)) = (head ns, head es) in 
        let (n2, e2) = readEdges (tail ns, tail es) in (from:to:n2, es)

    --turns a label into a node
    nodifyLabel :: AST -> Node
    nodifyLabel (ASTLabel from xs) = 
        let f = Node from [] in 
            Node from (getEdges xs f "")

    --turns a choice into a node
    nodifyChoice :: Choice -> Node 
    nodifyChoice (Data.Choice opt cond body) = do
        let o = Node opt []
        let edges = case cond of
                Nothing -> getEdges body o ""
                Just c -> getEdges body o (show c)
        if edges /= []
            then Node opt (replaceAll (Node opt edges) edges)
            else Node opt []


    replaceAll :: Node -> [Edge] -> [Edge]
    replaceAll n [] = [] 
    replaceAll n ((Edge from to cond):xs) = 
        Edge n to cond : replaceAll n xs

    --gets the edges
    getEdges :: [AST] -> Node -> String -> [Edge]
    getEdges [] _ _ = [] 
    getEdges (x:xs) from cond = case x of 
        (ASTLine) -> getEdges xs from cond 
        (ASTLabel str t) -> [Edge from (nodifyLabel x) cond]
        (ASTAssign a) -> getEdges xs from cond 
        (ASTJump to) -> Edge from (Node to []) cond : getEdges xs from cond 
        (ASTConds ys) -> travelConds ys from ++ getEdges xs from cond 
        (ASTChoices ys) -> let cs = removeEmpty (travelChoices ys) in connect from cs ++ getEdges xs from cond 
         


    
    --goes through a conditional branch
    travelConds :: [Data.Cond] -> Node -> [Edge]
    travelConds [] _ = [] 
    travelConds (x:xs) from = case x of 
        (Data.If cond body) -> getEdges body from (show cond) ++ travelConds xs from
        (Data.Elif cond body) -> getEdges body from (show cond) ++ travelConds xs from
        (Data.Else body) -> getEdges body from ""

    --goes through a choice menu/branch
    travelChoices :: [Choice] -> [CNode]
    travelChoices [] = [] 
    travelChoices ((Data.Choice opt cond body):xs) = 
        let node = nodifyChoice (Data.Choice opt cond body) in 
            (node, opt) : travelChoices xs

    
    --takes each line, parses it into tokens, unless it's only whitespace, adds them all together
    lexEachLine :: [String] -> [Token]
    lexEachLine [] = []
    lexEachLine (x:xs) = if (not . all isSpace) x then alexScanTokens x ++ lexEachLine xs else lexEachLine xs
        --print (alexScanTokens x)


    setIfy :: ([Node], [Edge]) -> ([Node], [Edge]) 
    setIfy (ns, es) = (Set.toList $ Set.fromList ns, es)

    main :: IO ()
    main = do 
        sourceFile <- readFile "../scripts/paths/prisoner/prisoner_1/prisoner_1_encounter.rpy"
        let lexed = lexEachLine (lines sourceFile)
        writeFile "output/prisonerEncounterLexed.txt" (toString lexed)
        print "finished lexing"
        let forest = fst $ head $ P.runParser top lexed
        writeFile "output/prisonerEncounterTree.txt" (show forest)
        print "finished parsing"
        let bigTree = flattenForest forest 
        writeFile "output/prisonerEncounterFolded.txt" (show bigTree)
        print "finished flattening"
        let output = htmlIfy bigTree
        print "finished making it HTML"
        writeFile "output/prisonerEncounterOutput.html" output
        print "all done!"
        
    