{
module Parser2 where

import Lexer (Token(..), Cond(..))
import Data

}

%name parse
%tokentype { Token }
%error { parseError }

%token
    label           { Lexer.Label }
    ":"             { Lexer.Colon }
    tab             { Lexer.Tab }
    jump            { Lexer.Jump }
    comment         { Lexer.PythonComment }
    NextArg         { Lexer.NextArg }
    if              { Lexer.Cond Lexer.If }
    elif            { Lexer.Cond Lexer.Elif }
    else            { Lexer.Cond Lexer.Else }
    Choice          { Lexer.Choice $$ }
    or              { Lexer.BoolOr }
    Index           { Lexer.Index $$ }
    and             { Lexer.BoolAnd }
    "("             { Lexer.OpenParen }
    Dollar          { Lexer.Dollar }
    VarDefine       { Lexer.VarDefine }
    var             { Lexer.Var $$ }
    num             { Lexer.Num $$ }
    bool            { Lexer.Bool $$ }
    text            { Lexer.Text $$ }
    Symbol          { Lexer.Symbol $$ }
    List            { Lexer.List $$ }
    TitleShow       { Lexer.TitleShow }
    play            { Lexer.Play }
    ")"             { Lexer.CloseParen }
    show            { Lexer.Show }
    loop            { Lexer.LoopAudio }
    onlayer         { Lexer.Layer }
    voice           { Lexer.VoiceLine }
    menu            { Lexer.Menu }
    Extend          { Lexer.Extend }
    Bg              { Lexer.Bg }
    Pos             { Lexer.Pos }

%%

Var : var { Data.Var $1 }

{

parseError :: [Token] -> a
parseError _ = error "Parse error"

}