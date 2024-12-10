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

    edgeFromNode :: Node -> Edge -> Bool
    edgeFromNode n (Edge s _ _) = if s == n then True else False

    edgesFromNode :: Node -> [Edge] -> [Edge]
    edgesFromNode node edges = filter (\e -> edgeFromNode node e) edges

    minRes :: [([Node], [Edge], Int)] -> ([Node], [Edge], Int)
    minRes = minimumBy (comparing (\(_, _, i) -> i))

    pathFind :: ([Node], [Edge]) -> Node -> Node -> [Node] -> [Edge] -> Int -> ([Node], [Edge], Int)
    pathFind (ns, es) start end vN vE dist
        | start == end = ((end:vN), vE, dist + 1)
        | (vN, vE) == (ns, es) = ([], [], 1000000)
        | otherwise = minRes (map (\e@(Edge _ s2 _) -> pathFind (ns, es) s2 end (start:vN) (e:vE) (dist + 1)) (filter (`notElem` vE) (edgesFromNode start es)))

    adjustColors :: ([Node], [Edge]) -> Node -> Node -> ([Node], [Edge])
    adjustColors (ns, es) start end = let (pns, _, _) = pathFind (ns, es) start end [] [] 0
                                        in (map (\n@(Node l i c) -> if n `elem` pns then Node l i Red else n) ns, es)
    -- adjustColors (ns,es) a e 
    -- H.htmlIfy (adjustColors (ns,es) a e)