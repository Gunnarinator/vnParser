module Utils where 
    import Control.Exception
    import Lexer as L
    import Data as D

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

    --draw edges from n to everything in xs
    connect :: Node -> [CNode] -> [Edge]
    connect _ [] = [] 
    connect n ((x, str):xs) = Edge n x str : connect n xs

    --if a node doesn't have edges I sometimes don't care about it
    removeEmpty :: [CNode] -> [CNode]
    removeEmpty [] = [] 
    removeEmpty (x:xs) = case x of 
        (Node _ [], _) -> removeEmpty xs 
        _ -> x:removeEmpty xs
    

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