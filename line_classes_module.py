from math import dist

class Segment:
    start_point = []
    end_point = []

    def __init__(self, points):
        self.start_point = points[0]
        self.end_point = points[1]

    def divide(self, max_length):
        point_dist = dist(self.start_point, self.end_point)
        seg_list = []

        if point_dist > max_length:
            half_point = [(self.start_point[0]+self.end_point[0])/2, (self.start_point[1]+self.end_point[1])/2]

            seg1 = Segment([self.start_point, half_point])
            seg2 = Segment([half_point, self.end_point])
            seg_list.append(seg1)
            seg_list.append(seg2)
        else:
            seg_list.append(self)

        return seg_list

class Polyline:
    segment_list = []
    isSplit = False

    def __init__(self, segments):
        self.segment_list = segments

    def divide_long_segments(self, max_length):
        sorting_segs = self.segment_list
        temp_segs = []

        if self.isSplit == True:
            return False

        too_long = True

        while too_long == True:
            too_long = False
            for i in range(len(sorting_segs)):
                sorted_segs = sorting_segs[i].divide(max_length)
                if len(sorted_segs) == 2:
                    too_long = True
                temp_segs.extend(sorted_segs)
            sorting_segs = temp_segs
            temp_segs = []

        self.segment_list = sorting_segs
        self.isSplit = True
        return True

    def points(self):
        return_points = []
        for i in range(len(self.segment_list)):
            return_points.append(self.segment_list[i].start_point)

        return_points.append(self.segment_list[-1].end_point)

        return return_points