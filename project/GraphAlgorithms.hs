module GraphAlgorithms where
    import Data as D
    import HTMLify as H
    import Data.List (minimumBy)
    import Data.Ord (comparing)

    a = Node "a" 1 Blue 
    b = Node "b" 2 Blue
    c = Node "c" 3 Blue
    d = Node "d" 4 Blue
    e = Node "e" 5 Blue

    ab = Edge a b "" 
    bc = Edge b c "" 
    bd = Edge b d "" 
    cd = Edge c d ""
    de = Edge d e ""


    ns = [a, b, c, d, e]
    es = [ab, bc, bd, cd, de]

    -- get the edge going from a certain node
    edgeFromNode :: Node -> Edge -> Bool
    edgeFromNode n (Edge s _ _) = if s == n then True else False

    -- get a list of the edges from a certain node
    edgesFromNode :: Node -> [Edge] -> [Edge]
    edgesFromNode node edges = filter (\e -> edgeFromNode node e) edges

    -- get the result with the least distance
    minRes :: [([Node], [Edge], Int)] -> ([Node], [Edge], Int)
    minRes = minimumBy (comparing (\(_, _, i) -> i))

    -- find the shortest path between two points
    pathFind :: ([Node], [Edge]) -> Node -> Node -> [Node] -> [Edge] -> Int -> ([Node], [Edge], Int)
    pathFind (ns, es) start end vN vE dist
        | start == end = (end:vN, vE, dist + 1)
        | (vN == ns) || (start `elem` vN) = ([], [], 1000000)
        | otherwise = minRes (map (\e@(Edge _ s2 _) -> pathFind (ns, es) s2 end (start:vN) (e:vE) (dist + 1)) (filter (`notElem` vE) (edgesFromNode start es)))

    -- adjust node colors based on the path found
    adjustNodeColors :: [Node] -> [Node] -> [Node]
    adjustNodeColors pns = map (\n@(Node l i c) -> if n `elem` pns then Node l i Red else n)

    -- adjust edges based on the updated nodes in the path
    adjustEdgeColors :: [Edge] -> [Edge] -> [Edge]
    adjustEdgeColors pes = map (\e@(Edge (Node l1 i1 _) (Node l2 i2 _) label) -> if e `elem` pes then Edge (Node l1 i1 Red) (Node l2 i2 Red) label else e)

    -- use the shortest path to adjust the colors of the path elements
    adjustColors :: ([Node], [Edge]) -> Node -> Node -> ([Node], [Edge])
    adjustColors (ns, es) start end = let (pns, pes, _) = pathFind (ns, es) start end [] [] 0
                                        in (adjustNodeColors pns ns, adjustEdgeColors pes es)
    -- adjustColors (ns,es) a e 
    -- H.htmlIfy (adjustColors (ns,es) a e)
    -- writeFile "test.html" (H.htmlIfy (adjustColors (ns,es) a e))