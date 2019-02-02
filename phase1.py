import sys
import string
import pandas as pd
import numpy as np
from google import google

filename = sys.argv[1] if len(sys.argv) > 1 else 'sample_mobile_data_1000.csv'
data = pd.read_csv(filename)
data['brand'] = 'Unknown'

search_cnt = 0

def detect_brand(info):
	#s = info.title + " # # # " + info.desc
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
	twos = [ones[i] + ones[i+1] for i in range(len(ones) - 1)]
	tres = [ones[i] + ones[i+1] + ones[i+2] for i in range(len(ones) - 2)]
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
		]): posib.append('APPLE')

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
		]): posib.append('SAMSUNG')
	
	if has(bag,
		[
		'نوکیا',
		'nokia',
		]): posib.append('NOKIA')
	
	if has(bag,
		[
		'هواوی',
		'هوآوی',
		'هوآوى',
		'هوواوی',
		'هووآوی',
		'huawei',
		'honor',
		]): posib.append('HUAWEI')


	if has(bag,
		[
		'z1',
		'experia',
		'sony',
		'سونی',
		'سونی',
		'اکسپریا',
		]): posib.append('SONY')


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
		]): posib.append('MICROSOFT')

	if has(bag,
		[
		'بلکبری',
		'blackberry',
		]): posib.append('BLACKBERRY')

	if has(bag,
		[
		'انایسی',
		'nec',
		]): posib.append('NEC')

	if has(bag,
		[
		'شیاومی',
		'xiaomi',
		]): posib.append('XIAOMI')
	
#	print(posib)
	info.brand = posib[0] if len(posib) == 1 else 'Unknown'
	return info


def google_detect(info):
	if (info.brand != 'Unknown'): return info

	lst = ['ACER', 'ALCATEL', 'ALLVIEW', 'AMAZON', 'AMOI', 'APPLE', 
			'ARCHOS', 'ASUS', 'AT&T', 'BENEFON', 'BENQ', 'BENQ-SIMENS',
			'BIRD', 'BLACKBERRY', 'BLACKVIEW', 'BLU', 'BOSCH', 'BQ', 
			'CASIO', 'CAT', 'CELKON', 'CHEA', 'COOLPAD', 'DELL', 'EMPORIA',
			'ENERGIZER', 'ERICSSON', 'ETEN', 'FUJITSU SIMENS', 'GARMIN-ASUS', 
			'GIGABYTE', 'GIONEE', 'GOOGLE', 'HAIER', 'HONOR', 'HP', 'HTC',
			'HUAWEI', 'I-MATE', 'I-MOBILE', 'ICEMOBILE', 'INFINIX', 'INNOSTREAM',
			'INQ', 'INTEX', 'JOLLA', 'KARBONN', 'KYOCERA', 'LAVA', 'LEECO', 'LENOVO',
			'LG', 'MAXON', 'MAXWEST', 'MEIZU', 'MICROMAX', 'MICROSOFT', 'MITAC', 
			'MITSUBISHI', 'MODU', 'MOTOROLA', 'MWG', 'NEC', 'NENONODE', 'NIU', 'O2',
			'ONEPLUS', 'OPPO', 'ORANGE', 'PALM', 'PANASONIC', 'PANTECH',
			'PARLA', 'PHILIPS', 'PLUM', 'POSH', 'PRESTIGIO', 'QMOBILE', 'QTEK', 'RAZER',
			'REALME', 'SAGEM', 'SAMSUNG', 'SENDO', 'SEWON', 'SHARP', 'SIMENS', 'SONIM', 'SONY',
			'SONY ERICSSON', 'SPICE', 'T-MOBILE', 'TECNO', 'TEL.ME.', 'TELIT', 'THURAYA',
			'TOSHIBA', 'UNNECTO', 'VERTU', 'VERYKOOL', 'VIVO', 'VK MOBILE', 'VODAFONE',
			'WIKO', 'WND', 'XCUTE', 'XIAOMI', 'XOLO', 'YEZZ', 'YOTA', 'YU', 'ZTE',
			]


	search_results = google.search(info.title + ' mobile phone', 1)
	text = ''
	for x in search_results:
		text += x.description + ' ' + x.name + ' '
	text = text.lower()

	def score(word):
		return text.count(word.lower())

	best = max(lst, key=score)

	global search_cnt 
	search_cnt += 1

	print('search {}'.format(search_cnt), file=sys.stderr)
	info.brand = best

	return info 
	

data = data.apply(detect_brand, axis=1)


print('Unknowns before google search: {} \n {} \n {}'.format( (data.brand=='Unknown').sum(), data.index[data.brand=='Unknown'].tolist(), data[data.brand=='Unknown'].sample(3, random_state=204) ), file=sys.stderr)

data = data.apply(google_detect, axis=1)
data.to_csv('output.csv')
