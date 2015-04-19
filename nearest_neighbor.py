from sys import argv
import re
import math


class Point(object):
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


def print_point(P):
    print "x: %g, y: %g" % (P.x, P.y)

def distance(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

def find_nearest_neighbor(points):
    smallest_distance = float("inf")

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            print "points %f amd %f - distance: %f" % (i, j, dist)
            if dist < smallest_distance:
                smallest_distance = dist

    print "smallest distance: %f" % smallest_distance


#######################
#### BEGIN PROGRAM ####
#######################

script, filename = argv
txt = open(filename)

i = 0

points = []

for line in txt:    
    i += 1
    x, y = map(float, re.findall(r'[+-]?\d+.\d+',line))
    
    ## Create a Point object and append to list of points
    p = Point(x, y)
    points.append(p)


    ## Create a Point object and print its components
    # p = Point(x, y)
    # print "point: %d" %i
    # print_point(p)


    ## Print a single point
    # print "point %i x: %g, y: %g" % (i, x, y)

find_nearest_neighbor(points)

## Print the list of points
# for point in points:
#     print_point(point)
