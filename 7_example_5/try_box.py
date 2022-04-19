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
    "/createRandomBox",
    name = "Create Random Box",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM),
        #hs.HopsNumber("R range of randomness", "R", "Maximum randomness for Radius", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
       hs.HopsBrep("Random Spheres","RS","List of generated random Spheres ", hs.HopsParamAccess.LIST)
    ]
)
def createRandomSphere(count, rX, rY, rZ):

    randomBox = []
    

    for i in range(count):

        #in each itereation generate some random points and radii
        random_x = r.randrange(-rX, rX, 2)
        random_y = r.randrange(-rY, rY, 2)
        random_z = r.randrange(-rZ, rZ, 2)
        #random_r = r.randrange(-rR, rR, 2)

        #create a sphere with rhino3dm
        random_center = rg.Point3d(random_x, random_y, random_z)
        random_box = rg.Box(rg.BoundingBox(random_x,random_y))
        random_box = rg.Box.ToBrep(random_box)
        
        #add sphere to the list
        randomBox.append(random_box)

    return randomBox

# @hops.component(
#     "/moreRandomSphere",
#     name = "More Random Sphere",
#     inputs=[
#         hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
#         hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
#         hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
#         hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM),
#         hs.HopsNumber("R range of randomness", "R", "Maximum randomness for Radius", hs.HopsParamAccess.ITEM)
#     ],
#     outputs=[
#        hs.HopsBrep("Random Spheres","RS","List of generated random Spheres ", hs.HopsParamAccess.LIST)
#     ]
# )
# def moreRandomSphere(count, rX, rY, rZ, rR):

#     randomSphere = geo.createRandomSphere(count, rX, rY, rZ, rR)
#     return randomSphere





if __name__== "__main__":
    app.run(debug=True)