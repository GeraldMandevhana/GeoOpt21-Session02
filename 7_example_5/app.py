from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/placeRandomPoints",
    name = "Place Random Points",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z","Maximum randomness in Z direction", hs.HopsParamAccess.ITEM),
        #hs.HopsInteger("Radius", "R","Radius", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
       hs.HopsPoint("Random Points","RP","List of generated random points ", hs.HopsParamAccess.LIST)
       #hs.HopsBrep("Random Breps","RB","List of generated random breps ", hs.HopsParamAccess.LIST)
    ]
)
def createRandomPoints(count,rX, rY, rZ):
   
    randomPts = []
    for i in range(count):

        #in each itereation generate some random points
        random_x = r.uniform(-rX, rX)
        random_y = r.uniform(-rY, rY)
        random_z = r.uniform(-rZ, rZ)

        #create a point with rhino3dm
        random_pt = rg.Point3d(random_x, random_y, random_z)

        #create a radius
        #radius_r = r.uniform(1,3)
        

        #create a sphere with rhino3dm
        #random_pt = rg.Sphere(random_pt, radius_r )


        #add point to the list
        randomPts.append(random_pt)

    return randomPts



@hops.component(
    "/addRandomPoints",
    name = "Add Random Points",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM)

    ],
    outputs=[
       hs.HopsPoint("Random Points","RP","List of generated random points ", hs.HopsParamAccess.LIST)
    ]
)
def moreRandomPoints(count,rX, rY):

    randomPts = geo.createRandomPoints(count, rX, rY)
    return randomPts





if __name__== "__main__":
    app.run(debug=True)