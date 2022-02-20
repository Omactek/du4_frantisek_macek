from math import dist

p1 = [12,58.5]
p0 = [5,3]
p05 = [(p1[0]+p0[0])/2,(p1[1]+p0[1])/2]
poly_seg = []

coordinates =[
					[ -729120.2305283286, -1047412.9380170368 ],
					[ -729117.334126506, -1047426.4983255751 ],
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
        counter = 0
        start_point = self.points[0]
        end_point = self.points[1]
        while max_length < dist(start_point, end_point):
            counter =+ 1
            half_point = [(start_point[0]+end_point[0])/2, (start_point[1]+end_point[1])/2]
            end_point = half_point
        for i in range(counter):
            poly_seg.append([[start_point[0]+(dist(start_point[0],end_point[0])*2**i)],[start_point[1]+(dist(start_point[1],end_point[1])*2**i)]])
        


poly = Polyline([p0,p05,p1])
print(poly.points)

seg = Segment([coordinates[0],coordinates[1]])
seg.divide(0)
print(poly_seg)
