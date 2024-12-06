{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}
module Main where 

    import System.IO
    import Data.Char
    import Lexer
    import TokenParser as TP
    import Parser as P
    import Data
    import Utils
    import HTMLify as H
    import qualified Data.Set as Set

    --at the top level... there should only be labels
    getTopEdges :: [AST] -> [Node] -> ([Edge], [Node])
    getTopEdges [] nodeEnv = ([], nodeEnv)
    getTopEdges (a:as) nodeEnv = case a of 
        (ASTLabel str body) -> do 
            let (n, newEnv) = findNode str nodeEnv Red
            let (bodyEdges, bodyEnv) = getEdges body n newEnv "" 
            let (restOfEs, finalEnv) = getTopEdges as bodyEnv
            (bodyEdges ++ restOfEs, finalEnv)
        _ -> getTopEdges as nodeEnv

    --getEdges is the supreme function, all hail getEdges 
    getEdges :: [AST] -> Node -> [Node] -> String -> ([Edge], [Node])
    getEdges [] _ nodeEnv _ = ([], nodeEnv) 
    getEdges (a:as) curN nodeEnv curLabel = case a of 
        --lines are trash, assigns are currently trash, keep moving
        ASTLine -> getEdges as curN nodeEnv curLabel 
        (ASTAssign a) -> getEdges as curN nodeEnv curLabel 

        --if we find a new label we want to draw a new edge then move into that one, then continue
        (ASTLabel str body) -> do 
            let (n, newEnv) = findNode str nodeEnv Red
            let e = Edge curN n curLabel
            let (bodyEdges, bodyEnv) = getEdges body n newEnv curLabel 
            let (restOfEs, finalEnv) = getEdges as curN bodyEnv curLabel
            (e:(bodyEdges ++ restOfEs), finalEnv)

        --for Jumps we need to draw an edge from this node to that node
        (ASTJump to) -> do 
            let (n, newEnv) = findNode to nodeEnv Red
            let e = Edge curN n curLabel
            let (restOfEs, finalEnv) = getEdges as curN newEnv curLabel
            (e:restOfEs, finalEnv)
    
        --Conditionals have many conds, and each cond has a body 
        (ASTConds cs) -> do 
            let (es, newEnv) = travelConds cs curN nodeEnv 
            let (restOfEs, finalEnv) = getEdges as curN newEnv curLabel 
            (es++restOfEs, finalEnv)
        --For choices we want to... do complicated stuff
        (ASTChoices cs) -> do 
            let (es, newEnv) = travelChoices cs curN nodeEnv 
            let (restOfEs, finalEnv) = getEdges as curN newEnv curLabel 
            (es++restOfEs, finalEnv)
 
         
    --goes through a conditional branch
    travelConds :: [Data.Cond] -> Node -> [Node] -> ([Edge], [Node])
    travelConds [] _ nodeEnv = ([], nodeEnv)
    travelConds (c:cs) from nodeEnv = case c of 
        (Data.If cond body) -> do 
            let (es, newEnv) = getEdges body from nodeEnv (show cond)
            let (restOfEs, finalEnv) = travelConds cs from newEnv
            (es++restOfEs, finalEnv)
        (Data.Elif cond body) -> do 
            let (es, newEnv) = getEdges body from nodeEnv (show cond)
            let (restOfEs, finalEnv) = travelConds cs from newEnv
            (es++restOfEs, finalEnv)
        (Data.Else body) -> getEdges body from nodeEnv "Else"

    --goes through a choice menu/branch
    travelChoices :: [Choice] -> Node -> [Node] -> ([Edge], [Node])
    travelChoices [] _ nodeEnv = ([], nodeEnv)
    travelChoices ((Data.Choice opt cond body):cs) from nodeEnv = do
        let temp = Node opt (length nodeEnv) Blue
        let label = case cond of Nothing -> "" ; (Just x) -> getFlag x
        let (es, newEnv) = getEdges body temp (temp:nodeEnv) label
        --if there's only one edge i'd prefer it be "from -> to, via opt"
        if length es == 1 then do 
            let (Edge f t l) = head es 
            let singleEdge = Edge from t (opt ++ l)
            let (restOfEs, finalEnv) = travelChoices cs from newEnv  
            (singleEdge:restOfEs, finalEnv)
        else if es /= [] then do
            --if there is more than one jump in this choice, then we can make the choice a node
            --let hmm = [Edge from temp ""]
            let thisChoiceEs = connect from es
            let (restOfEs, finalEnv) = travelChoices cs from (temp:newEnv) 
            (es++thisChoiceEs++restOfEs, finalEnv)
        else 
            --there are no real edges and the opt shouldn't be its own Node
            travelChoices cs from nodeEnv

    



    --takes each line, parses it into tokens, unless it's only whitespace, adds them all together
    lexEachLine :: [String] -> [Token]
    lexEachLine [] = []
    lexEachLine (x:xs) = 
        if (not . all isSpace) x && (not . elem '#') x 
            then alexScanTokens x ++ lexEachLine xs 
            else lexEachLine xs
        
    printEachLine :: [String] -> IO [Token]
    printEachLine [] = return []
    printEachLine (x:xs) = 
        if (not . all isSpace) x && (not . elem '#') x 
            then do 
                print (show $ alexScanTokens x)
                printEachLine xs 
            else printEachLine xs

    main :: IO ()
    main = do 
        sourceFile <- readFile "singleScript.rpy"
        --printEachLine (lines sourceFile)
        let lexed = lexEachLine (lines sourceFile)
        writeFile "output/finalLexed.txt" (toString lexed)
        print "finished lexing"
        let forest = fst $ head $ P.runParser top lexed
        writeFile "output/finalTree.txt" (show forest)
        print "finished parsing"
        let (es, ns) = getTopEdges forest []
        let bigTree = cleanResults (ns, es)
        writeFile "output/finalFolded.txt" (show bigTree)
        print "finished flattening"
        let output = H.htmlIfy bigTree
        print "finished making it HTML"
        writeFile "output/finalOutput.html" output
        print "all done!"
        
    