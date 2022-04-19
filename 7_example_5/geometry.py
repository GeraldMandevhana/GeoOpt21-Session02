#we import all the libraries that our functions need here too
import random as r
import rhino3dm as rg

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