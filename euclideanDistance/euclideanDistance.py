import math 
#Coordinates
points = [(3,4),
          (5,12),
          (8,5),
          (4,3)]


# Distance function
def euclideanDistance(point1, point2 ):
    (x1,y1)=point1
    (x2,y2)= point2

    euclidean= (math.sqrt((x2-x1)**2 + (y2-y1)**2))
    return euclidean

# Creating empty list
distences=[]


# Using distance function to create distances list 
for i in range((len(points))):
    for j in range(i+1,len(points)):
        distance=euclideanDistance(points[i],points[j])
        distences.append(distance)

# Finding min distance

minDistance= min(distences)
print(minDistance)