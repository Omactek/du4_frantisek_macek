import argparse
import os
import json
import line_classes_module


def get_arguments():
    parser = argparse.ArgumentParser(description='Test argparse')
    parser.add_argument("-f", help = "input file path", required = True)
    parser.add_argument("-l", help = "segment length", required = True)
    parser.add_argument("-o", help = "out file name", required = True)
    args = parser.parse_args()
    return args

def load_file(file_path): #načte vstupní soubor a ověří, jestli existuje, je prázdný a jestli k němu má přístup
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

args = get_arguments()
data = load_file(args.f)

for feature in data["features"]:
    point_list = feature["geometry"]["coordinates"]
    segm_list = []
    for i in range(len(point_list)-1):
        seg = line_classes_module.Segment([point_list[i], point_list[i+1]])
        segm_list.append(seg)
    temp_poly = line_classes_module.Polyline(segm_list)
    temp_poly.divide_long_segments(int(args.l))
    feature["geometry"]["coordinates"] = temp_poly.points()

jsonString = json.dumps(data)
jsonFile = open(f"{args.o}.json", "w")
jsonFile.write(jsonString)
jsonFile.close()