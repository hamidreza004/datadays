import sys
import pandas as pd
from collections import Counter


def most_common(lst):
    return max(set(lst), key=lst.count)


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else 'output3.csv'
    data = pd.read_csv(filename, lineterminator="\n")
    arr = Counter("")
    for x in data.desc:
        arr.add(Counter(x.split()))
    arr.most_common(100)
    print("end")


main()
