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
      jump            { TokenJump }
      choice          { TokenChoice }

%%

AST : Label "{" AST "}"             { ASTLabel $1 $3 }
      | jump Label                  { Jump $2 }
      | menu "{" Choices "}"        { Menu $3 }
      | menu "{" AST Choices "}"    { Menu2 $3 $4 }
      | Asign                       { AstAsign $1 }
      | Cond AST                    { AstCond $1 }

Choices : choice AST Choices        { Choice $2 $3 }
      | choice AST                  { LastChoice $2 }

Asign : "=" Var Exp                 { Asign $2 $3 }
      | "+=" Var Exp                { Inc $2 $3 }
      | "-=" Var Exp                { Dec $2 $3 }

Cond  : if Flag                     { If $2}
      | elif Flag                   { Elif $2}
      | else                        { Else }

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
        | TokenJump
        | TokenChoice
 deriving Show

}