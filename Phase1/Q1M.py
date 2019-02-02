import sys
import pandas as pd
from collections import Counter


def most_common(lst):
    return max(set(lst), key=lst.count)


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else 'output3.csv'
    data = pd.read_csv(filename, lineterminator="\n")
    arr = Counter("")
    cnt = 0
    sep = ".,،:;"
    for x in data.desc:
        for c in sep:
            x = x.replace(c, ' ')
        if cnt % 100 == 0:
            print(cnt)
        cnt += 1
        arr += Counter(x.split())
        if len(arr) > 1000000:
            arr = arr.most_common(100000)
    print(arr.most_common(100))


main()
