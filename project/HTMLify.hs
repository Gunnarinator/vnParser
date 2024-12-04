module HTMLify where
    import Data 
    

    data HTMLNode = HTMLNode Label Int
    instance Show HTMLNode where 
        show (HTMLNode l i) = 
            "\nNode " ++ show i ++ ": " ++ l
    htmlLabel (HTMLNode l i) = l 
    htmlID (HTMLNode l i) = i

    --adds id numbers to the nodes so that nodes with the same label are different
    addIDs :: [Node] -> [HTMLNode]
    addIDs ns = addIDsWeak ns 0 

    --should this use a state transformer, maybe
    --if I have time I'll go back and redo it
    addIDsWeak :: [Node] -> Int -> [HTMLNode]
    addIDsWeak [] _ = [] 
    addIDsWeak ((Node l _):ns) i = 
        HTMLNode l i :addIDsWeak ns (i+1)

    htmlIfy :: ([HTMLNode], [Edge]) -> String 
    htmlIfy (ns, es) = let (htmlNs, htmlEs) = (htmlIfyNodes ns, htmlIfyEdges es) in
        htmlStart ++ 
        "nodes = new vis.DataSet([" ++ htmlNs ++ "\n" ++ 
        "edges = new vis.DataSet([" ++ htmlEs ++ "\n" ++ 
        htmlEnd
        

    htmlIfyNodes :: [HTMLNode] -> String
    htmlIfyNodes [] = ""
    htmlIfyNodes (x:xs) = case xs of 
        [] -> htmlIfyNode x ++ "]);"
        thing -> htmlIfyNode x ++ "," ++ htmlIfyNodes xs 


    htmlIfyNode :: HTMLNode -> String 
    htmlIfyNode (HTMLNode l i) = 
        "{\"color\": \"#97c2fc\", \"id\": \"" ++ (show i) ++ 
            "\", \"label\": \"" ++ l ++ 
            "\", \"shape\": \"dot\", \"size\": 10}"

    
    htmlIfyEdges :: [Edge] -> String 
    htmlIfyEdges (x:xs) = 
        case xs of
            [] -> htmlIfyEdgeInner x "]);"
            anything -> htmlIfyEdgeInner x "," ++ htmlIfyEdges xs
                
    --{"arrows": "to", "from": "fromLabel", "label": "edgeLabelText", "to": "toLabel", "width": 1}
    htmlIfyEdgeInner :: Edge -> String -> String 
    htmlIfyEdgeInner (Edge (Node from i1) (Node to i2) label) backEnd =
        let front = "{\"arrows\": \"to\", \"from\": \"" ++ i1 ++ "\""in 
            let back = ", \"to\": \"" ++ i2 ++ "\", \"width\": 1}" in 
                --case label of 
                    {-"" -> -}front ++ back ++ backEnd
                    --thing -> front ++ ", label: \"" ++ thing ++ "\"" ++ back ++ backEnd


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
\                 width: 800px;\n\
\                 height: 800px;\n\
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
\        \"color\": {\n\
\            \"inherit\": true\n\
\        },\n\
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