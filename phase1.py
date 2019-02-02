import sys
from nltk.tokenize import word_tokenize
import string
import pandas as pd
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else 'sample_mobile_data_1000.csv'
data = pd.read_csv(filename)


def detect_brand(info):
    # s = info.title + " # # # " + info.desc
    s = info.title
    s.replace('\u0649', '\u06CC')

    posib = []

    def mysplit(s):
        sep = list(string.digits + '۱۲۳۴۵۶۷۸۹۰' + string.punctuation + '.،:؛')
        orig = s.split()
        for x in sep:
            s = s.replace(x, ' ')
        return s.split() + orig

    ones = [w.lower() for w in mysplit(s)]
    twos = [ones[i] + ones[i + 1] for i in range(len(ones) - 1)]
    tres = [ones[i] + ones[i + 1] + ones[i + 2] for i in range(len(ones) - 2)]
    bag = ones + twos + tres

    def has(lst, items):
        for word in lst:
            for item in items:
                if word.count(item) or word.startswith(item) or word.endswith(item):
                    return True
        return False

    if has(bag,
           [
               'اپل',
               'ایفون',
               'آیفون',
               'apple',
               'iphone',
               'iphon',
               '6s',
               '5s',
               '4s',
               'سیکساس',
               'فایواسگ',
           ]): posib.append('Apple')

    if has(bag,
           [
               'الجی',
               'lg',
           ]): posib.append('LG')

    if has(bag,
           [
               'جیالایکس',
               'glx',
           ]): posib.append('GLX')

    if has(bag,
           [
               'سامسونگ',
               'ace',
               'samsung',
               'galaxy',
               'گلکسی',
               'گالاکسی',
               'نکسوس',
               'nexus',
               'j1',
               'j2',
               'j3',
               'j4',
               'j5',
               'j6',
               'j7',
               'جی۷',
               'کوربی',
               'corby',
               'edge',
               'note',
           ]): posib.append('Samsung')

    if has(bag,
           [
               'نوکیا',
               'nokia',
           ]): posib.append('Nokia')

    if has(bag,
           [
               'هواوی',
               'هوآوی',
               'هوآوى',
               'هوواوی',
               'هووآوی',
               'huawei',
               'honor',
               'y330',
           ]): posib.append('Huawei')

    if has(bag,
           [
               'z1',
               'experia',
               'sony',
               'سونی',
               'سونی',
               'اکسپریا',
           ]): posib.append('Sony')

    if has(bag,
           [
               'htc',
               'اچتیسی',
           ]): posib.append('HTC')

    if has(bag,
           [
               'مایکروسافت',
               'ماکروسافت',
               'microsoft',
           ]): posib.append('Microsoft')

    if has(bag,
           [
               'بلکبری',
               'blackberry',
           ]): posib.append('BlackBerry')

    if has(bag,
           [
               'انایسی',
               'nec',
           ]): posib.append('nec')

    if has(bag,
           [
               'شیاومی',
               'xiaomi',
               'mi',
           ]): posib.append('xiaomi')

    #	print(posib)
    return posib[0] if len(posib) == 1 else 'Unknown'


# detect_brand(data.iloc[48])
data['brand'] = data.apply(detect_brand, axis=1)
print('Unknowns: {} \n {} \n {}'.format((data.brand == 'Unknown').sum(), data.index[data.brand == 'Unknown'].tolist(),
                                        data[data.brand == 'Unknown'].sample(3, random_state=189)), file=sys.stderr)
