import json
import csv
import sys

def write_csv_file(filePath, lines):
    with open(filePath,'w',newline="") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
        try:
            spamwriter.writerows(lines)
        except:
            raise ValueError("you may have invalid values in your csv rows")


def make_line(length,models):
    if not isinstance(length,int) or length==0:
        raise ValueError("length should be a  positive integer.")

    line = [""]*length
    for key,value in dict(models).items():
        try:
            idx = int(key)
            line[idx] = value
        except:
            raise ValueError("bad value for key in keywords set (integer expected).")
    return line


def make_lines(length, rows):
    return [make_line(length, row) for row in rows]


def convert_to_csv(jsonfile):
    with open(jsonfile,"r") as jsf:
        data_set = json.load(jsf)
    for data in data_set:
        filepath = data["title"]+".csv"
        lines = make_lines(data["length"],data["lines"])
        write_csv_file(filepath,lines)


if  __name__=="__main__":
    convert_to_csv(sys.argv[1])
