module Reading where 

    import System.IO
    import Lexer


    lexOneLine :: [String] -> Int -> IO() 
    lexOneLine [] _ = do print "done lexing!"
    lexOneLine (x:xs) i = do 
        -- handle <- openFile "lexedoutput.txt" ReadWriteMode
        -- hPutStr handle (show (alexScanTokens x))
        print ((alexScanTokens x))
        lexOneLine xs (i+1)

    readingThings :: IO()
    readingThings = do 
        content <- readFile "singleScript.rpy"
        let linesOfFiles = lines content
        lexOneLine linesOfFiles 0
        