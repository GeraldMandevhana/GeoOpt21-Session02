from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry_copy as geo

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createEgoGraph",
    name = "Create Ego Graph",
    inputs=[
        hs.HopsInteger("Number of nodes", "n", "Number of nodes", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Connected nodes", "m", " Number of edges to attach from a new node to existing nodes", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Seed", "Seed", "Indicator of random number generation state", hs.HopsParamAccess.ITEM, default= 50),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 1),


    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def createBarabasiGraph(n, m, seed, layout):

    G = geo.createBarabasiGraph(n, m, seed)
    GW = geo.addRandomWeights(G)

    nodes = geo.getNodes(GW, layout)
    edges = geo.getEdges(GW, layout) 

    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)