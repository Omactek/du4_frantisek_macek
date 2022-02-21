import argparse
import os
import json
import line_classes_module

#function setups parser arguments
def get_arguments():
    parser = argparse.ArgumentParser(description='Test argparse')
    parser.add_argument("-f", help = "input file path", required = True)
    parser.add_argument("-l", help = "segment length", required = True)
    parser.add_argument("-o", help = "out file name", required = True)
    args = parser.parse_args()
    return args

#function loads input file, verifies that it is not emty, it is not missing, it is right file format and can be accesed
def load_file(file_path):
    try:
        if os.path.getsize(file_path) == 0:
            print("File is empty")
            quit()
    except FileNotFoundError:
        print("File is missing")
        quit()
    try:    
        with open(file_path, encoding="utf8") as file_name:
            data = json.load(file_name)
            return data
    except ValueError:
        print("Wrong file format.")
        quit()
    except PermissionError:
        print("Denied permission to acces file")
        quit()

#loads arguments
args = get_arguments()

#loads data
data = load_file(args.f)

#starts division of segments on polystrings
for feature in data["features"]:
    point_list = feature["geometry"]["coordinates"] #loads coordinates of one linestring
    segm_list = [] #initiates list for segments of one linestring
    for i in range(len(point_list)-1):
        seg = line_classes_module.Segment([point_list[i], point_list[i+1]]) #creates segment objects
        segm_list.append(seg) #saves segments to list
    temp_poly = line_classes_module.Polyline(segm_list) #creates polyline objects from polystrings
    temp_poly.divide_long_segments(int(args.l)) #calls divide_long_segments method with max length on polyline objects
    feature["geometry"]["coordinates"] = temp_poly.points() #saves split polylines to data

#creates json file with divided segments
jsonString = json.dumps(data)
jsonFile = open(f"{args.o}.geojson", "w")
jsonFile.write(jsonString)
jsonFile.close()