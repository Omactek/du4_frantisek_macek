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
        poly_seg.append(self.points[0])
        counter = 0
        counter =+ 1
        if max_length < dist(self.points[0], self.points[1]):
            half_point = [(self.points[0][0]+self.points[1][0])/2, (self.points[0][1]+self.points[1][1])/2]
            seg = Segment([self.points[0], half_point])
            seg.divide(max_length)
            print(half_point)


poly = Polyline([p0,p05,p1])
print(poly.points)

seg = Segment([coordinates[0],coordinates[1]])
seg.divide(200)
