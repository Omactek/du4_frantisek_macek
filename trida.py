from math import dist

class Segment:
    def __init__(self, points):
        self.points = points
    
    def divide(self, max_length):
        start_point = self.points[0]
        end_point = self.points[1]
        if max_length < dist(start_point,end_point):
            half_point = [(start_point[0]+end_point[0])/2, (start_point[1]+end_point[1])/2]
            return [start_point,half_point,end_point]
        else:
            return [start_point,end_point]

class Polyline:
    def __init__(self,coords):
        self.point_list = coords
        self.isSplit = False

    def divide_long_segments(self, max_length):
        if isSplit == True:
            return False
        return_points = self.point_list
        temp_points = []
        too_long = True

        while too_long == True:
            too_long = False
            temp_points = return_points
            temp_segments = []

            for i in range(temp_points-1):
                x = Segment(temp_points[i], temp_points[i+1])
                temp_segments.append(x)

            return_points = []

            for x in temp_segments:
                temp_result = x.divide(max_length)
            
            if (len(temp_result) == 3):
                if dist(temp_result[0], temp_result[1]) > max_length:
                    too_long = True
                
                result = temp_result[0], temp_result[1], temp_result[1], temp_result[2]
                return_points.append(result)
            
            else:
                return_points.append(x.start_point,x.end_point)

        return_points.append(return_points[-1])
        return_points = return_points[::2]

        self.point_list = return_points
        isSplit = True
        return True