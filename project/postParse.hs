module Main where 

import Control.Exception
import Data
import Utils


--to properly place a line in the tree, we need
    -- the tree, so we can search it for other nodes
    -- the VarEnv
    -- the paragraph we're in, so we can put this line into this paragraph
    -- the line we're evaluating
evalPara :: VarEnv -> Paragraph -> [Line] -> (Paragraph, VarEnv)
evalPara varEnv para [] = (para, varEnv)
evalPara varEnv para (l:ls) = case l of 
    Label ln -> undefined --if there's a new label, this is the end of the paragraph, return
    VarDefine var val -> --add the variable to the env
        let newEnv = addVar var val varEnv in 
            evalPara newEnv para ls
    VarSet var val -> --if it's there, update the value, if not, error 
        let newEnv = setVar var val varEnv in 
            evalPara newEnv para ls
    Condition c tbody fbody -> --make the two bodies the children of this paragraph
        let (tChild, tEnv) = evalPara varEnv para tbody in 
            let (fChild, fEnv) = evalPara tEnv para fbody in
                undefined
    Choice os -> undefined --idk how we're gonna represent choice branches yet
    _ -> undefined




--step 1, find all labels, get a list of labels and paragraphs, conds, etc.
--step 2, manage jumps to construct the tree

findJumps :: [Paragraph] -> DTree
findJumps (p:ps) = undefined


drawTree :: DTree -> IO()
drawTree = undefined

main :: IO() 
main = undefined