{
module Test where

import Generate

}

%name parse
%tokentype { Token }
%error { parseError }

%token
      int             { TokenInt $$ }
      float           { TokenFloat $$ }
      var             { TokenVar $$ }
      true            { TokenTrue }
      false           { TokenFalse }
      "+"             { TokenAdd }
      "-"             { TokenSub }
      "*"             { TokenMul }
      "/"             { TokenDiv }
      "=="            { TokenEq }
      "!="            { TokenNeq }
      ">"             { TokenGt }
      "<"             { TokenLt }
      and             { TokenAnd }
      or              { TokenOr }
      if              { TokenIf }
      elif            { TokenElif }
      else            { TokenElse }
      "="             { TokenAsign }
      "+="            { TokenInc }
      "-="            { TokenDec }
      label           { TokenLabel $$ }
      "{"             { TokenBlockStart }
      "}"             { TokenBlockEnd }
      menu            { TokenMenu }
      jump            { TokenJump $$ }
      choice          { TokenChoice }

%%

Lines : AST Lines                     { Lines ($1 : unwrapLines $2 ) }
      | AST                           { Lines [$1] }

Choices : choice "{" Lines "}" Choices          { Choices ($3 : unwrapChoices $5 ) }
      | choice "{" Lines "}"                    { Choices [$3] }

AST : Label "{" Lines "}"           { ASTLabel $1 $3 }
    | jump                          { Jump $1 }
    | menu "{" Choices "}"          { Menu $3 }
    | menu "{" Lines Choices "}"    { Menu2 $3 $4 }
    | Asign                         { AstAsign $1 }
    | Cond                          { AstCond $1 }

Asign : "=" Var Exp                 { Asign $2 $3 }
      | "+=" Var Exp                { Inc $2 $3 }
      | "-=" Var Exp                { Dec $2 $3 }

Cond  : if Flag "{" Lines "}"       { If $2 $4 }
      | elif Flag "{" Lines "}"     { Elif $2 $4 }
      | else "{" Lines "}"          { Else $3 }

Flag : Var                          { Flag $1 }
     | Exp "==" Exp                 { Eq $1 $3 }
     | Exp "!=" Exp                 { Neq $1 $3 }
     | Exp ">" Exp                  { Gt $1 $3 }
     | Exp "<" Exp                  { Lt $1 $3 }
     | Flag and Flag                { And $1 $3 }
     | Flag or Flag                 { Or $1 $3 }

Exp : Var                           { ExpVar $1 }
    | Val                           { ExpVal $1 }
    | Exp "+" Exp                   { Add $1 $3 }
    | Exp "-" Exp                   { Sub $1 $3 }
    | Exp "*" Exp                   { Mul $1 $3 }
    | Exp "/" Exp                   { Div $1 $3 }

Val   : int                         { Int $1 }
      | float                       { Float $1 }
      | true                        { Bool True }
      | false                       { Bool False }  

Var   : var                         { Var $1 }

Label : label                        { Label $1 }


{

parseError :: [Token] -> a
parseError _ = error "Parse error"

unwrapChoices :: Choices -> [Lines]
unwrapChoices (Choices xs) = xs

unwrapLines :: Lines -> [AST]
unwrapLines (Lines x) = x

data Token
      = TokenInt Int
        | TokenFloat Float
        | TokenVar String
        | TokenTrue
        | TokenFalse
        | TokenAdd
        | TokenSub
        | TokenMul
        | TokenDiv
        | TokenEq
        | TokenNeq
        | TokenGt
        | TokenLt
        | TokenAnd
        | TokenOr
        | TokenIf
        | TokenElif
        | TokenElse
        | TokenAsign
        | TokenInc
        | TokenDec
        | TokenLabel String
        | TokenBlockStart
        | TokenBlockEnd
        | TokenMenu
        | TokenJump String
        | TokenChoice
 deriving Show

}