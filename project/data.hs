import diagrams
import Data.Graph.DAG as dag
import parsers 


--we want the ... Variable variable to hold both name and value.
newtype Var a = (String, a)

--Jumps just hold the destination of the jump statement
data Jump = J dest

data Choice = (String, [Line])

data Line = 
    Label String |
    Cond Exp (Either Line | Line Line) | --either then or then else
    SetVar String a | --renPy has two types of these, one is for instantiation
    Audio Bool String String [String] | --(true for play, false for stop) channel, file, options
    Text String String | --speaker, text
    Branch [Choice]



transferLine :: String -> Line

