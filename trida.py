from math import dist

p1 = [12,58.5]
p0 = [5,3]
p05 = [(p1[0]+p0[0])/2,(p1[1]+p0[1])/2]
poly_seg = []

coordinates =[
					[4,4],
					[16,16],
					[ -729114.9620250128, -1047445.0871372782 ],
					[ -729113.5667241365, -1047465.0529498458 ],
					[ -729103.7995179854, -1047550.0110033341 ],
					[ -729100.86941614, -1047574.6584188528 ],
					[ -729095.1458125375, -1047612.6914427951 ],
					[ -729092.5928109288, -1047647.5884647667 ]]


class Polyline:
    def __init__(self, points):
        self.points = points

class Segment:
    def __init__(self, points):
        self.points = points
        print(self.points)

    def divide(self, max_length):
        counter = 0 #initiate counter
        start_point = self.points[0]
        end_point = self.points[1] #initiates list for polyline out of segment
        while max_length < dist(start_point, end_point): #if segment is longer than max langth splits segment in two and repeats
            counter += 1
            half_point = [(start_point[0]+end_point[0])/2, (start_point[1]+end_point[1])/2]
            end_point = half_point
        for i in range(2**counter+1): #calculates and appends coordinates based on number of recursions and smallest segment
            poly_seg.append([start_point[0]+abs(start_point[0]-end_point[0])*i,start_point[1]+abs(start_point[1]-end_point[1])*i])
        return poly_seg

seg = Segment([coordinates[0],coordinates[1]])
poly_seg2 = seg.divide(2)
print(poly_seg2)
print(abs(poly_seg2[-1][1]-seg.points[1][1]))
print(abs(poly_seg2[-2][1]-seg.points[1][1]))
print(dist(poly_seg2[-1],seg.points[1]))
print(dist(poly_seg2[-2],seg.points[1]))
