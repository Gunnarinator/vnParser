module HTMLify where
    import Data 
    


    htmlIfy :: ([Node], [Edge]) -> String 
    htmlIfy (ns, es) = let (htmlNs, htmlEs) = (htmlIfyNodes ns, htmlIfyEdges es) in
        htmlStart ++ 
        "nodes = new vis.DataSet([" ++ htmlNs ++ "\n" ++ 
        "edges = new vis.DataSet([" ++ htmlEs ++ "\n" ++ 
        htmlEnd
        

    htmlIfyNodes :: [Node] -> String
    htmlIfyNodes [] = ""
    htmlIfyNodes (x:xs) = case xs of 
        [] -> htmlIfyNode x ++ "]);"
        thing -> htmlIfyNode x ++ "," ++ htmlIfyNodes xs 


    htmlIfyNode :: Node -> String 
    htmlIfyNode (Node l i c) =
        "{\"color\": \"" ++ show c ++ "\",  \"id\": \"" ++ show i ++ 
            "\", \"label\": \"" ++ l ++ 
            "\", \"shape\": \"dot\", \"size\": 10}"

    
    htmlIfyEdges :: [Edge] -> String 
    htmlIfyEdges (x:xs) = 
        case xs of
            [] -> htmlIfyEdgeInner x "]);"
            anything -> htmlIfyEdgeInner x "," ++ htmlIfyEdges xs
    
    -- determine a color for an edge
    determineColor :: Edge -> String
    determineColor (Edge (Node _ _ c1) (Node _ _ c2) _) 
        | c1 == c2 = "\"color\": {\"color\": \"" ++ show c1 ++ "\"}"
        | ((c1 == Red) && (c2 == Green)) || ((c1 == Green) && (c2 == Red)) = "\"color\": {\"color\": \"" ++ show Green ++ "\"}"
        | otherwise = "\"color\": {\"color\": \"" ++ show Blue ++ "\"}"

    --{"arrows": "to", "from": "fromLabel", "label": "edgeLabelText", "to": "toLabel", "width": 1}
    htmlIfyEdgeInner :: Edge -> String -> String 
    htmlIfyEdgeInner e@(Edge (Node from i1 c) (Node to i2 c2) label) backEnd =
        let front = "{\"arrows\": \"to\", \"from\": \"" ++ show i1 ++ "\"" 
            back = ", \"to\": \"" ++ show i2 ++ "\", \"width\": 1, " ++ determineColor e ++ " }" in 
                case label of 
                    "" -> front ++ back ++ backEnd
                    thing -> front ++ ", label: \"" ++ cleanLabel thing ++ "\"" ++ back ++ backEnd

    --replace " with \"
    cleanLabel :: String -> String 
    cleanLabel [] = [] 
    cleanLabel (x:xs) = case x of 
        '\"' -> "\\\"" ++ cleanLabel xs 
        _ -> x:cleanLabel xs


    htmlStart :: String 
    htmlStart = "<html>\n\
\    <head>\n\
\        <meta charset=\"utf-8\">\n\
\        \n\
\            <script src=\"lib/bindings/utils.js\"></script>\n\
\            <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/dist/vis-network.min.css\" integrity=\"sha512-WgxfT5LWjfszlPHXRmBWHkV2eceiWTOBvrKCNbdgDYTHrT2AeLCGbF4sZlZw3UMN3WtL0tGUoIAKsu8mllg/XA==\" crossorigin=\"anonymous\" referrerpolicy=\"no-referrer\" />\n\
\            <script src=\"https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js\" integrity=\"sha512-LnvoEWDFrqGHlHmDD2101OrLcbsfkrzoSpvtSQtxK3RMnRV0eOkhhBN2dXHKRrUU8p2DGRTk35n4O8nWSVe1mQ==\" crossorigin=\"anonymous\" referrerpolicy=\"no-referrer\"></script>\n\
\            \n\
\        \n\
\<center>\n\
\<h1></h1>\n\
\</center>\n\
\\n\
\<!-- <link rel=\"stylesheet\" href=\"../node_modules/vis/dist/vis.min.css\" type=\"text/css\" />\n\
\<script type=\"text/javascript\" src=\"../node_modules/vis/dist/vis.js\"> </script>-->\n\
\        <link\n\
\          href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css\"\n\
\          rel=\"stylesheet\"\n\
\          integrity=\"sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6\"\n\
\          crossorigin=\"anonymous\"\n\
\        />\n\
\        <script\n\
\          src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js\"\n\
\          integrity=\"sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf\"\n\
\          crossorigin=\"anonymous\"\n\
\        ></script>\n\
\\n\
\\n\
\        <center>\n\
\          <h1></h1>\n\
\        </center>\n\
\        <style type=\"text/css\">\n\
\\n\
\             #mynetwork {\n\
\                 width: 2000px;\n\
\                 height: 2000px;\n\
\                 background-color: #ffffff;\n\
\                 border: 1px solid lightgray;\n\
\                 position: relative;\n\
\                 float: left;\n\
\             }\n\
\\n\
\             \n\
\\n\
\             \n\
\\n\
\             \n\
\        </style>\n\
\    </head>\n\
\\n\
\\n\
\    <body>\n\
\        <div class=\"card\" style=\"width: 100%\">\n\
\            \n\
\            \n\
\            <div id=\"mynetwork\" class=\"card-body\"></div>\n\
\        </div>\n\
\\n\
\        \n\
\        \n\
\\n\
\        <script type=\"text/javascript\">\n\
\\n\
\              // initialize global variables.\n\
\              var edges;\n\
\              var nodes;\n\
\              var allNodes;\n\
\              var allEdges;\n\
\              var nodeColors;\n\
\              var originalNodes;\n\
\              var network;\n\
\              var container;\n\
\              var options, data;\n\
\              var filter = {\n\
\                  item : '',\n\
\                  property : '',\n\
\                  value : []\n\
\              };\n\
\\n\
\              \n\
\\n\
\              \n\
\\n\
\              // This method is responsible for drawing the graph, returns the drawn network\n\
\              function drawGraph() {\n\
\                  var container = document.getElementById('mynetwork');\n\
\ " 

    htmlEnd :: String 
    htmlEnd = "\n\
\                  nodeColors = {};\n\
\                  allNodes = nodes.get({ returnType: \"Object\" });\n\
\                  for (nodeId in allNodes) {\n\
\                    nodeColors[nodeId] = allNodes[nodeId].color;\n\
\                  }\n\
\                  allEdges = edges.get({ returnType: \"Object\" });\n\
\                  // adding nodes and edges to the graph\n\
\                  data = {nodes: nodes, edges: edges};\n\
\\n\
\                  var options = {\n\
\    \"configure\": {\n\
\        \"enabled\": false\n\
\    },\n\
\    \"edges\": {\n\
\        \"smooth\": {\n\
\            \"enabled\": true,\n\
\            \"type\": \"dynamic\"\n\
\        }\n\
\    },\n\
\    \"interaction\": {\n\
\        \"dragNodes\": true,\n\
\        \"hideEdgesOnDrag\": false,\n\
\        \"hideNodesOnDrag\": false\n\
\    },\n\
\    \"physics\": {\n\
\        \"enabled\": true,\n\
\        \"stabilization\": {\n\
\            \"enabled\": true,\n\
\            \"fit\": true,\n\
\            \"iterations\": 1000,\n\
\            \"onlyDynamicEdges\": false,\n\
\            \"updateInterval\": 50\n\
\        }\n\
\    }\n\
\};\n\
\\n\
\                  \n\
\\n\
\\n\
\                  \n\
\\n\
\                  network = new vis.Network(container, data, options);\n\
\\n\
\                  \n\
\\n\
\                  \n\
\\n\
\                  \n\
\\n\
\\n\
\                  \n\
\\n\
\                  return network;\n\
\\n\
\              }\n\
\              drawGraph();\n\
\        </script>\n\
\    </body>\n\
\</html> "