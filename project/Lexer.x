{
module Lexer where
}

%wrapper "basic"

$digit = [0-9 \-]            -- digits
$alpha = [a-zA-Z]       -- alphabetic characters
$text = [$alpha $digit '•' ' ' \- \[ \] \— \_ \\ \: \' \( \) \/ \{ \} \. \, \= \# \! \? \}]

tokens :-

  -- labels and jumps
  label                     { \s -> Label}  
  jump                      { \s -> Jump}
  [$alpha] [$alpha $digit \_ \.]+ \( [$text \$ \" \']* \)   {\s -> FunctionCall s}

  _ \( [$text] \)                      {\s -> TitleShow}

  \" \{ 'i' \} '•' [$text]+ \{ '/' 'i' \} \"    {\s -> Choice (takeWhile (/= '{') (drop 6 s))}

  --colons appear after labels, conditionals, and at the beginning of choices 
  :                         {\s -> Colon}

  --boolean stuff
  or                        {\s -> BoolOr}
  and                       {\s -> BoolAnd}


  --conditionals
  if                        {\s -> Cond If}
  elif                      {\s -> Cond Elif}
  else                      {\s -> Cond Else}

  


  --rpy AV stuff. We don't need them but it'd be cool to have it not crash
  play                      {\s -> Play}
  show                      {\s -> Show}
  loop                      {\s -> LoopAudio} 
  scene                     {\s -> Bg}
  onlayer                   {\s -> Layer}
  Position \( [$alpha \= \, $digit]+ \)                  {\s -> Pos}
  voice                     {\s -> VoiceLine}
  

  --default is used to define vars
  default                   {\s -> VarDefine}
  --$ is *normally* used when setting variables.
  \$                        {\s -> Dollar}
  [$alpha] [$alpha $digit \_ \, \.]*     {\s -> Var s}
  [\_] [$alpha $digit \_ \, \.]+     {\s -> Var s}
  [\= \+ \> \< \!]+         {\s -> Symbol s}
  

  --variables, as far as I've seen, are Bool, Int, or String.
  $digit* [\.]* $digit+     {\s -> Num s}
  \" [$text $white]* \"     {\s -> Text (tail (reverse (tail (reverse s))))}
  \' [$text $white \8211 \8226 \16]* \'     {\s -> Text (tail (reverse (tail (reverse s))))}
  True                      {\s -> Bool True}
  False                     {\s -> Bool False}

  \[ [$text $white \" \'] \] {\s -> Index s}
  

  --the choices always seem to have 'extend ""' at the beginning.
  \"\"\"                      {\s -> PythonComment}

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
  | PythonComment
  | Cond Cond
  | ChoiceStart
  | Choice String
  | BoolOr
  | Index String
  | BoolAnd
  | OpenParen
  | Dollar
  | VarDefine
  | Var String
  | Num String
  | Bool Bool
  | Text String
  | Symbol String
  | TitleShow
  | FunctionCall String
  | Play 
  | CloseParen
  | Show 
  | LoopAudio 
  | Layer
  | VoiceLine
  | Bg
  | Pos
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