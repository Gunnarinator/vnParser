module Main where 

import Control.Exception
import Data
import Utils


--to properly place a line in the tree, we need
    -- the tree, so we can search it for other nodes
    -- the VarEnv
    -- the paragraph we're in, so we can put this line into this paragraph
    -- the line we're evaluating
constructTree = 
    


--step 1, find all labels, get a list of labels and paragraphs, conds, etc.
--step 2, manage jumps to construct the tree

findJumps :: [Paragraph] -> DTree
findJumps (p:ps) = undefined


drawTree :: DTree -> IO()
drawTree = undefined

main :: IO() 
main = undefined