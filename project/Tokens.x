{
module Tokens where
}

%wrapper "basic"

$digit = 0-9            -- digits
$alpha = [a-zA-Z]       -- alphabetic characters
$text = [$alpha $digit ' ' \' \( \) \/ \{ \. \, \! \? \} \•]

tokens :-

  

  -- labels and jumps
  label                     { \s -> Label}  
  jump                      { \s -> Jump}

  --colons appear after labels, conditionals, and at the beginning of choices 
  :                         {\s -> Colon}

  --boolean stuff
  or                        {\s -> BoolOr}
  and                       {\s -> BoolAnd}


  --conditionals
  if                        {\s -> Cond If}
  elif                      {\s -> Cond Elif}
  else                      {\s -> Cond Else}

  --default is used to define vars
  default                   {\s -> VarDefine}
  --$ is *normally* used when setting variables.
  \$                        {\s -> Dollar}
  [$alpha $digit \_]+       {\s -> Var s}
  [\= \+ \> \< \!]+         {\s -> Symbol s}
  

  --variables, as far as I've seen, are Bool, Int, or String.
  $digit+                   {\s -> Int (read s)}
  \" [$text $white]+ \"     {\s -> Text (tail (reverse (tail (reverse s))))}
  True                      {\s -> Bool True}
  False                     {\s -> Bool False}

  --the choices always seem to have 'extend ""' at the beginning.
  \"\"                      {\s -> ChoiceStart}

  --ignore comments and blank lines
  "#".*                              ;
  $white+                            ;

{
-- Each action has type :: String -> Token

--Condition Enum
data Cond = If | Elif | Else
  deriving (Eq, Show)

-- The token type:
data Token
  = Label 
  | Colon
  | Jump 
  | Cond Cond
  | ChoiceStart
  | BoolOr
  | BoolAnd
  | Dollar
  | VarDefine
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