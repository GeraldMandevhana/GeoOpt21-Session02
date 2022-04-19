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
    "/createExpoParetoSphere",
    name = "Create Expo Pareto Sphere",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X direction", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y direction", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z direction", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("R range of randomness", "Radius", "Maximum randomness for Radius", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
       hs.HopsBrep("ExpoPareto Spheres", "EPS", "List of generated Spheres ", hs.HopsParamAccess.LIST)
    ]
)
def createExpoParetoSphere(count, rX, rY, rZ, radius):

    randomSphere = []
    alpha = 1
    

    for i in range(count):

        #in each iteration generate some random points
        random_x = r.uniform(-rX, rX)
        random_y = r.uniform(-rY, rY)
        random_z = r.randrange(-rZ, rZ, 5)
        
        #create radius variable for the points
        if radius < 0:
            random_r = r.expovariate(radius*alpha)

        elif radius == 0:
            random_r = 1

        else:
            random_r = r.paretovariate(radius*alpha)

        #create a sphere with rhino3dm
        random_center = rg.Point3d(random_x, random_y, random_z)
        random_sphere = rg.Sphere(random_center, abs(random_r))
        random_sphere_a = rg.Sphere.ToBrep(random_sphere)
        
        #add sphere to the list
        randomSphere.append(random_sphere_a)

    return randomSphere

@hops.component(
    "/moreExpoParetoSphere",
    name = "More ExpoPareto Sphere",
    inputs=[
        hs.HopsInteger("Count", "C", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("R range of randomness", "Radius_", "Maximum randomness for Radius", hs.HopsParamAccess.ITEM)
    ],
    outputs=[
       hs.HopsBrep("ExpoPareto Spheres", "EPS", "List of generated Spheres ", hs.HopsParamAccess.LIST)
    ]
)
def moreExpoParetoSphere(count, rX, rY, rZ, radius):

    randomSphere = geo.createExpoParetoSphere(count, rX, rY, rZ, radius)
    return randomSphere


if __name__== "__main__":
    app.run(debug=True)