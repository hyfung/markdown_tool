#!/usr./bin/python3

import argparse
import csv

"""
File format for input:
col1,col2,col3
val1,val2,val3
val4,val5,val6

String format for output:
|col1|col2|col3|
|----|----|----|
|val1|val2|val3|
|val4|val5|val6|

"""

def leftpad(in_str: str, width: int, pad_char=' ') -> str:
    """Pad a string from with free character on left side"""
    in_str = str(in_str)
    if width < len(in_str):
        return in_str
    return pad_char * (width - len(in_str)) + in_str

def rightpad(in_str: str, width: int, pad_char=' ') -> str:
    """Pad a string from with free character on right side"""
    in_str = str(in_str)
    if width < len(in_str):
        return in_str
    return in_str + pad_char * (width - len(in_str))

def get_max_len(arr: 'list of string') -> int:
    """Get the maximum length of element in a list of string"""
    return max([len(x) for x in arr])

def find_all_titles(filename: str) -> list:
    """Returns a list of string starting with '#' """
    with open(filename, 'r') as f:
        return [x for x in f.readlines() if x.startswith('#')]
    

def main():
    row_width = []

    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=True, help="Name of CSV file")

    args = vars(ap.parse_args())

    with open(args['file'], newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for tup in list(zip(*list(csv_reader))):
            row_width.append(get_max_len(tup))
    print(row_width)

if __name__ == '__main__':
    main()
