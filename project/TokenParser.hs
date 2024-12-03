module TokenParser where 

    import Data as D
    import Data.Maybe
    import qualified Parser as P
    import Control.Applicative
    import Lexer as L
    import Utils

    

    sat :: (Token -> Bool) -> P.Parser Token
    sat p = do 
        x <- P.item 
        if p x then return x else empty

    --handling each token
    col :: P.Parser Token
    col = sat isColonToken

    lab :: P.Parser Token 
    lab = sat isLabelToken

    tabs :: P.Parser Int
    tabs = do
        xs <- many (sat isTabToken)
        return (length xs)

    --there are a bunch of lines we don't care about 
    eatLine :: P.Parser AST
    eatLine = do 
        _ <- many (sat (not . isTabToken))
        return ASTLine
        

    var :: P.Parser Var 
    var = do varName <$> sat isVarToken

    openParen :: P.Parser Token 
    openParen = sat isOpenParen

    closeParen :: P.Parser Token
    closeParen = sat isCloseParen


    val :: P.Parser Val 
    val = do getVal <$> sat isValToken

    varDefineToken :: P.Parser Token 
    varDefineToken = sat isVarDefine 

    dollarToken :: P.Parser Token 
    dollarToken = sat isDollarToken

    orToken :: P.Parser Token 
    orToken = do sat isOrToken 

    andToken :: P.Parser Token 
    andToken = do sat isAndToken

    text :: P.Parser String 
    text = do textVal <$> sat isTextToken

    symbol :: P.Parser String 
    symbol = do symbVal <$> sat isSymbolToken

    condition :: P.Parser Token 
    condition = sat isConditionToken

    jumpToken :: P.Parser Token 
    jumpToken = sat isJumpToken
    
    menu :: P.Parser Token 
    menu = sat isMenuToken 
    
    extend :: P.Parser Token 
    extend = sat isExtendToken



    --types of lines

    --a label is just "label <labelName>:"
    label :: Int -> P.Parser AST 
    label d = do 
        _ <- lab 
        str <- var 
        _ <- col
        body <- many (ls (d+1))
        return (ASTLabel str body)

    --jumps are just "jump <labelName>"
    jump :: P.Parser AST 
    jump = do 
        _ <- jumpToken 
        ASTJump <$> var

    --the beginning of a choice branch is goofy and stupid.
    choiceBranch :: P.Parser AST 
    choiceBranch = do 
        _ <- menu 
        _ <- col
        d <- tabs
        _ <- extend 
        _ <- text
        ASTChoices <$> many (choice d)

    --a choice itself is text and maybe a condition followed by lines
    -- I don't like that I can't just do "parserName" in a do block when it's inside the lambda :(
    choice :: Int -> P.Parser Choice
    choice d = P.P (\s -> do
        let (numTabs, rest) = head $ P.runParser tabs s
        if numTabs /= d then empty else do 
                    let (str, strRest) = head $ P.runParser text rest
                    let condResult = P.runParser inLineConditional strRest
                    if (condResult /= []) then do
                        let (cond, condRest) = head condResult
                        let (omg, idc) = head $ P.runParser col condRest
                        let (body, finalRest) = head $ P.runParser (many (ls (d+1))) idc
                        return (D.Choice (take 30 (drop 4 str) ++ "...") (Just cond) body, finalRest)
                    else do
                        let (omg, idc) = head $ P.runParser col strRest
                        let (body, finalRest) = head $ P.runParser (many (ls (d+1))) idc
                        return (D.Choice (take 30 (drop 4 str) ++ "...") Nothing body, finalRest)
                    
        )


    inLineConditional :: P.Parser D.Cond 
    inLineConditional = do 
        _ <- condition
        exp <- boolExp
        return (D.If exp [])


    --conditional will parse the entire expression 
    conditional :: Int -> P.Parser D.Cond
    conditional d = do 
        ifType <- condition
        case ifType of 
            (Cond L.Else) -> do 
                _ <- col
                body <- many (ls (d+1))
                return (D.Else body)
            _ -> do 
                exp <- boolExp
                _ <- col
                body <- many (ls (d+1)) 
                case ifType of 
                    (Cond L.If) -> do return (D.If exp body)
                    (Cond L.Elif) -> do return (D.Elif exp body)

    --a bool exp = check | (check) | check OR exp | check AND exp 
    boolExp :: P.Parser Flag 
    boolExp = do 
        c <- check 
        do 
            o <- orToken
            Or c <$> boolExp
            <|> do 
                a <- andToken
                And c <$> boolExp
            <|> do 
                return c

    --check = var == val | var != val | var > val, etc.
    check :: P.Parser Flag 
    check = do 
        oP <- openParen 
        inC <- innerCheck 
        cP <- closeParen 
        return inC
        <|> do innerCheck


    innerCheck :: P.Parser Flag 
    innerCheck = do
        v1 <- var 
        s <- symbol
        v2 <- val 
        case s of 
            "==" -> return (Eq (D.Var v1) (Val v2))
            "!=" -> return (Neq (D.Var v1) (Val v2))
            ">" -> return (Gt (D.Var v1) (Val v2))
            "<" -> return (Lt (D.Var v1) (Val v2))
        <|> do
            v1 <- var 
            return (Base v1) 

    
    define :: P.Parser (Var, Val)
    define = do 
        _ <- varDefineToken 
        name <- var 
        s <- symbol 
        if s == "=" then do 
            v <- val 
            return (name, v) 
        else empty

    assign :: P.Parser AST
    assign = do 
        _ <- dollarToken 
        name <- var 
        s <- symbol 
        if s == "=" then do 
            ASTAssign . Assign name . D.Val <$> val
        else if s == "+=" then do 
            ASTAssign . Inc name . D.Val <$> val
        else if s == "-=" then do 
            ASTAssign . Dec name . D.Val <$> val
        else empty



    --line = 
        -- label | jump | start of choices
        --D is expected number of tabs, since renPy is based on whitespace the same way Python is.
    ls :: Int -> P.Parser AST
    ls d = P.P (\s -> do 
        let (tDepth, tabRest) = head $ P.runParser tabs s
        if tDepth /= d then empty else case head tabRest of
            Label -> P.runParser (label d) tabRest 
            Jump -> P.runParser jump tabRest 
            Dollar -> P.runParser assign tabRest 
            Menu -> P.runParser choiceBranch tabRest
            Cond _ -> do 
                let (conds, condRest) = head $ P.runParser (conditional d) tabRest 
                return (ASTConds [conds], condRest)
            _ -> P.runParser eatLine tabRest
        )

    top :: P.Parser [AST]
    top = do many (label 0)

