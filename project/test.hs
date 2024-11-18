module Reading where 

    import System.IO
    import Lexer


    lexOneLine :: [String] -> IO() 
    lexOneLine [] = do print "done lexing!"
    lexOneLine (x:xs) = do 
        -- handle <- openFile "lexedoutput.txt" ReadWriteMode
        -- hPutStr handle (show (alexScanTokens x))
        print (alexScanTokens x)
        lexOneLine xs

    readingThings :: IO()
    readingThings = do 
        content <- readFile "../scripts/paths/spectre/spectre_1/spectre_1_start.rpy"
        let linesOfFiles = lines content
        lexOneLine linesOfFiles
        