{
module Lexer where
}

%wrapper "basic"

$digit = 0-9            -- digits
$alpha = [a-zA-Z]       -- alphabetic characters
$text = [$alpha $digit \8226 \• '•' ' ' \- \[ \] \— \_ \\ \' \( \) \/ \{ \} \. \, \= \# \! \? \}]

tokens :-

  

  -- labels and jumps
  label                     { \s -> Label}  
  jump                      { \s -> Jump}

  _ \(                       {\s -> TitleShow}
  \) {\s -> CloseParen}
  \( {\s -> OpenParen}
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

  [$alpha] [$alpha $digit \_ \.]+ \( [$alpha $digit \_ \.]* \)   {\s -> FunctionCall s}


  --rpy AV stuff. We don't need them but it'd be cool to have it not crash
  play                      {\s -> Play}
  show                      {\s -> Show}
  loop                      {\s -> LoopAudio} 
  scene                     {\s -> Bg}
  onlayer                   {\s -> Layer}
  Position \( [$alpha]+ \= [$digit]+ \)                  {\s -> Pos}
  voice                     {\s -> VoiceLine}
  

  --default is used to define vars
  default                   {\s -> VarDefine}
  --$ is *normally* used when setting variables.
  \$                        {\s -> Dollar}
  [$alpha] [$alpha $digit \_ \, \.]*     {\s -> Var s}
  [\= \+ \> \< \!]+         {\s -> Symbol s}
  

  --variables, as far as I've seen, are Bool, Int, or String.
  $digit+ [\.]* $digit*     {\s -> Num s}
  \" [$text $white \8211 \8226 \160]+ \"     {\s -> Text (tail (reverse (tail (reverse s))))}
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
  | Choice String
  | BoolOr
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