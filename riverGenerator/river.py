from maskCanvas import canvas, reverse_mask, point, line_seg
import numpy as np
import random
from math import cos, sin
class river(canvas):
    def __init__(self, pitch, path):
        super().__init__()
        for i in range(len(path)):
            super().registerLineSeg([path[i-1],path[i]])
        self.registerMask(reverse_mask(path))
        self.pitch = pitch
        self.surfaceFunction = self.createSurfaceFunction(0.7)
        

    def getHeightPoint(self, point_, length):
        return point(point_.x, point_.y - cos(self.pitch)*length)

    def getPointWithNoise(self, point):
        return self.getHeightPoint(point, self.surfaceFunction(point))


    def createSurfaceFunction(self, max_amplitude):
        def function(point):
            return max_amplitude*cos(point.x)*sin(point.y)

        return function

    def getLength(self, point1, point2):
        return np.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)

    def getMidPoint(self, point1, point2):
        return point((point1.x+point2.x)/2, (point1.y+point2.y)/2)

    def splitPoints(self, points):
        unit_line_length = 1
        while(unit_line_length < self.getLength(points[0], points[1])):
            for i in range(len(points)-1, 0, -1):
                    points.insert(i, self.getMidPoint(points[i],points[i-1]))
        return points

    def registerLineSeg(self, line):
        if(not isinstance(line, line_seg)):
            line = line_seg(line, self.color, self.thickness)
        points = self.splitPoints(line.points)
        noised_points = []
        for p in points:
            noised_points.append(self.getPointWithNoise(p))

        for i in range(len(noised_points)-1):
            super().registerLineSeg([noised_points[i],noised_points[i+1]])
