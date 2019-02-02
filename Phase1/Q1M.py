import sys
import string
import pandas as pd
import numpy as np
from google import google

def main():

    filename = sys.argv[1] if len(sys.argv) > 1 else 'divar_posts_dataset.csv'
    data = pd.read_csv(filename, lineterminator="\n")
    print("end")

main()