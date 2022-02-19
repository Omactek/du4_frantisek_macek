import argparse
import os
"""
def get_arguments()
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
            data = json.load(file_path)
            return data
    except ValueError:
        print("Wrong file format.")
        quit()
    except PermissionError:
        print("Denied permission to acces file")
        quit()

args = get_arguments()
data = load_file()
print(data)
"""
