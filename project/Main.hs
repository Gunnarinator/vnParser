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
    import Dotify
    import GraphAlgorithms as G
    import Control.Monad.IO.Class (MonadIO(liftIO))
    
    
    --at the top level there *should* only be labels
    getTopEdges :: [AST] -> [Node] -> ([Edge], [Node])
    getTopEdges [] nodeEnv = ([], nodeEnv)
    getTopEdges (a:as) nodeEnv = case a of
        (ASTLabel str body) -> do 
            let (n, newEnv) = findNode str nodeEnv Blue
            let (nextNode, nextNodeEnv) = getNext as newEnv n
            let (bodyEdges, bodyEnv) = getEdges True body n nextNode nextNodeEnv ""
            let (restOfEs, finalEnv) = getTopEdges as bodyEnv
            if null bodyEdges
                then do
                    let (nextN, nextEnv) = findNode (getLabelText (head as)) finalEnv Blue
                    let bodyEdges = [Edge n nextN ""]
                    (bodyEdges ++ restOfEs, finalEnv)
                else 
                    (bodyEdges ++ restOfEs, finalEnv)
        _ -> getTopEdges as nodeEnv

    --getEdges is the supreme function, all hail getEdges 
    getEdges :: Bool -> [AST] -> Node -> Node -> [Node] -> String -> ([Edge], [Node])
    getEdges _ [] _ _ nodeEnv _ = ([], nodeEnv) 
    getEdges getAll (a:as) curN nextN nodeEnv curLabel = case a of 
        --lines are trash, assigns are currently trash, keep moving
        ASTLine -> case (getAll, as) of 
            (True, []) -> ([Edge curN nextN curLabel], nodeEnv)
            (_, _) -> getEdges getAll as curN nextN nodeEnv curLabel 
        (ASTAssign a) -> case (getAll, as) of 
            (True, []) -> ([Edge curN nextN curLabel], nodeEnv)
            (_, _) -> getEdges getAll as curN nextN nodeEnv curLabel 

        --if we find a new label we want to draw a new edge then move into that one, then continue
        (ASTLabel str body) -> do 
            let (n, newEnv) = findNode str nodeEnv Blue
            let e = Edge curN n curLabel
            let (newNext, nextEnv) = getNext as newEnv nextN 
            let (bodyEdges, bodyEnv) = getEdges True body n newNext nextEnv curLabel 
            let (restOfEs, finalEnv) = getEdges getAll as curN newNext bodyEnv curLabel
            if null bodyEdges
                then (e:restOfEs, finalEnv)
                else (e:(bodyEdges ++ restOfEs), finalEnv)
            

        --for Jumps we need to draw an edge from this node to that node
        (ASTJump to) -> do 
            let (n, newEnv) = findNode to nodeEnv Blue
            let e = Edge curN n curLabel
            let (restOfEs, finalEnv) = getEdges True as curN nextN newEnv curLabel
            (e:restOfEs, finalEnv)
    
        --Conditionals have many conds, and each cond has a body 
        (ASTConds cs) -> do 
            let (es, newEnv) = travelConds cs curN nextN nodeEnv 
            case (getAll, as) of 
                (_, []) -> (es++[Edge curN nextN curLabel], newEnv)
                (_, _) -> let (restOfEs, finalEnv) = getEdges getAll as curN nextN newEnv curLabel in 
                    (es++restOfEs, finalEnv)
        --For choices we want to... do complicated stuff
        (ASTChoices cs) -> do
            --look through the choices, if any have jumps, then do
                --from curN to jumpDestination via choiceText
            let (es, newEnv) = travelChoices cs curN nextN nodeEnv 
            --if the next line is a label and there are choices that don't have jumps, do
                --from curN to nextLabel via choiceText
            if (not . null) as && (not . null) es && (not . null) (checkChoices cs curN (head as) es)
                then do 
                    let empChoices = checkChoices cs curN (head as) es
                    let (restOfEs, superDuperFinalEnv) = getEdges getAll as curN nextN newEnv curLabel
                    let empEs = map (Edge curN nextN . getChoiceLabel) empChoices
                    (es ++ empEs ++ restOfEs, superDuperFinalEnv)
                else do 
                    let (restOfEs, finalEnv) = getEdges getAll as curN nextN newEnv curLabel
                    (es++restOfEs, finalEnv)

            --go get the rest of the edges
            
 
         
    --goes through a conditional branch
    travelConds :: [Data.Cond] -> Node -> Node -> [Node] -> ([Edge], [Node])
    travelConds [] _ _ nodeEnv = ([], nodeEnv)
    travelConds (c:cs) from next nodeEnv = case c of 
        (Data.If cond body) -> do 
            let (es, newEnv) = getEdges False body from next nodeEnv (show cond)
            let (restOfEs, finalEnv) = travelConds cs from next newEnv
            (es++restOfEs, finalEnv)
        (Data.Elif cond body) -> do 
            let (es, newEnv) = getEdges False body from next nodeEnv (show cond)
            let (restOfEs, finalEnv) = travelConds cs from next newEnv
            (es++restOfEs, finalEnv)
        (Data.Else body) -> getEdges False body from next nodeEnv "Else"


    --goes through a choice menu/branch
    travelChoices :: [Choice] -> Node -> Node -> [Node] -> ([Edge], [Node])
    travelChoices [] _ _ nodeEnv = ([], nodeEnv)
    travelChoices ((Data.Choice opt cond body):cs) from next nodeEnv = do
        let temp = Node opt (length nodeEnv) Blue
        let label = case cond of Nothing -> "" ; (Just x) -> getFlag x
        let (es, newEnv) = getEdges False body temp next (temp:nodeEnv) label
        --if there's only one edge i'd prefer it be "from -> to, via opt"
        if length es == 1 then do 
            let (Edge f t l) = head es 
            let singleEdge = Edge from t (opt ++ l)
            let (restOfEs, finalEnv) = travelChoices cs from next newEnv  
            (singleEdge:restOfEs, finalEnv)
        else if es /= [] then do
            --if there is more than one jump in this choice, then we can make the choice a node
            --let hmm = [Edge from temp ""]
            let thisChoiceEs = connect from es
            let (restOfEs, finalEnv) = travelChoices cs from next (temp:newEnv) 
            (es++thisChoiceEs++restOfEs, finalEnv)
        else 
            --there are no real edges and the opt shouldn't be its own Node
            travelChoices cs from next newEnv

    



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

    -- functionality to render path between two points
    -- try with showPath G.g
    showPath :: ([Node], [Edge]) -> String -> IO ()
    showPath (ns, es) outF = do
        start <- getLine
        case start of
            "y" -> do
                    print "Enter a starting node label or a node id:"
                    l1 <- getLine
                    let n1 = findNodeIdLabel l1 ns
                    print "Enter an ending node label:"
                    l2 <- getLine
                    let n2 = findNodeIdLabel l2 ns
                    case (n1, n2) of
                        (Just tn1, Just tn2) -> do
                                            print tn1
                                            print tn2
                                            let res = adjustColors (ns, es) tn1 tn2
                                            case res of
                                                Just final -> do
                                                    let output = H.htmlIfy final
                                                    writeFile outF output
                                                    print ("Path found. See generated file " ++ outF)
                                                Nothing -> print "No path found"
                        (Just tn1, Nothing) -> print (l2 ++ " is not a valid label")
                        (Nothing, Just tn2) -> print (l1 ++ " is not a valid label")
                        (Nothing, Nothing) -> print "Both labels were invalid"
                    print "Would you like to go again (y/n)?"
                    showPath (ns, es) outF
            _ -> print "Understood, program complete!"


    main :: IO ()
    main = do 
        putStr "\nplease enter an input filename: \n"
        inF <- getLine
        putStr "\nplease enter an output filename: \n"
        outF <- getLine
        main' inF outF
    
    main' :: String -> String -> IO ()
    main' inF outF = do 
        sourceFile <- readFile inF
        -- printEachLine (lines sourceFile)
        let lexed = lexEachLine (lines sourceFile)
        -- writeFile "output/trueLexed.txt" (toString lexed)
        print "finished lexing"
        let forest = fst $ head $ P.runParser top lexed
        --writeFile "output/trueTree.txt" (show forest)
        print "finished parsing"
        let (es, ns) = getTopEdges forest []
        let bigTree = cleanResults (ns, es)
        --writeFile "output/trueFolded.txt" (show bigTree)
        print "finished flattening"
        --writeFile "output/trueDot.dot" (dotify bigTree)
        print "finished making it a DOT"
        let output = H.htmlIfy bigTree
        print "finished making it HTML"
        writeFile outF output
        print "all done!"
        print "Woud you also like to find the path between two nodes? (y/n)"
        showPath bigTree outF

    testMain = main' "prisoner_1_encounter.rpy" "output/colorTest.html"
    