module Dotify where 

    import Data

    dotStart :: String 
    dotStart = "digraph gname {\n\n"

    dotEnd :: String
    dotEnd = "\n\n}"

    dotifyNodes :: [Node] -> String 
    dotifyNodes [] = "" 
    dotifyNodes ((Node str i c):ns) = 
        show i ++ " [label=\""++str ++"\", fill="++show c ++"];\n" ++
            dotifyNodes ns


    dotifyEdges :: [Edge] -> String 
    dotifyEdges [] = "" 
    dotifyEdges ((Edge (Node _ i1 _) (Node _ i2 _) l):es) = 
        show i1 ++ " -> " ++ show i2 ++ " [label =\"" ++ l ++ "\"];\n" ++ 
            dotifyEdges es


    dotify :: ([Node], [Edge]) -> String 
    dotify (ns, es) = 
        dotStart ++ dotifyNodes ns ++ dotifyEdges es ++ dotEnd