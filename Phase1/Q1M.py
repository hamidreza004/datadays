import sys
import string
import pandas as pd
import numpy as np
from google import google

def main():

    filename = sys.argv[1] if len(sys.argv) > 1 else 'sample_mobile_data_1000.csv'
    data = pd.read_csv(filename)
    print("end")

main()