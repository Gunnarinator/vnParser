{
module Main (main) where
}

%wrapper "basic"

$digit = 0-9            -- digits
$alpha = [a-zA-Z]       -- alphabetic characters
$text = [$alpha $digit ' ' \' \( \) \/ \{ \. \, \! \? \} \•]

tokens :-


  "#".*                              ;
  label                     { \s -> Label}  
  \"\"                      {\s -> ChoiceStart}
  jump                      { \s -> Jump} 
  True                      {\s -> Bool True}
  False                     {\s -> Bool False}
  $digit+                   {\s -> Int (read s)}
  [if elif else]            {\s -> Cond}
  [\= \+ \> \< \!]+         {\s -> Symbol s}
  [$alpha $digit \_]+       {\s -> Var s}
  :                         {\s -> Colon}
  \$                        {\s -> Dollar}
  \" [$text $white]+ \"     {\s -> Text (tail (reverse (tail (reverse s))))}
  $white+                            ;
--  "default ".$varName." = ".$digit   { \s -> VarDefine s}    
--  "default ".$varName." = ".$alpha   { \s -> VarDefine s}    
--  "$ ".$varName." = ".$digit         { \s -> VarSet s}
--  "$ ".$varName." = ".$alpha         { \s -> VarSet s}
--  "if ".$varName                     { \s -> Cond s}
--  "{i}".*."{/i} if ".*               { \s -> CondBranch s}
--  "{i}".*."{/i}"                     { \s -> Branch s}

{
-- Each action has type :: String -> Token

-- The token type:
data Token
  = Label 
  | Colon
  | Jump 
  | Cond
  | ChoiceStart
  | Dollar
  | Var String
  | Int Int 
  | Bool Bool
  | Text String
  | Symbol String
--  | VarDefine String String
--  | VarSet String String
--  | Cond String --either then or then else; this should get parsed to Cond Exp (Either [Line] ([Line],[Line]))
--  | CondBranch [String] --indicates a choice.
--  | Branch String
  deriving (Eq, Show)

main = do
  s <- getContents
  print (alexScanTokens s)
}