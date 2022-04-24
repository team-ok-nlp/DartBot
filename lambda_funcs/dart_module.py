import dart_fss as dart
from constants import DART_API_KEY

from time import time

# Open DART API KEY 설정
dart.set_api_key(api_key=DART_API_KEY)

def name2corp(corp_name):
	# get list of all corp
	# To be change DB
	start = time()
	corp_list = dart.get_corp_list()
	print(f"get corp list time : {time()-start}")

	# get corp class by corp name in corp_list
	corp_info = corp_list.find_by_corp_name(corp_name, exactly=True)[0]
	return corp_info

def name2code(corp_name):
	# get list of all corp
	# To be change DB
	start = time()
	corp_list = dart.get_corp_list()
	print(f"get corp list time : {time()-start}")

	# get corp code by corp name in corp_list
	corp_info = corp_list.find_by_corp_name(corp_name, exactly=True)[0]
	corp_code = corp_info.corp_code
	return corp_code

# # name2code test
# corp_name = "삼성전자"
# corp_code = name2code(corp_name)
# print(f"code : {corp_code}")

# name2corp test
corp_name = "삼성전자"
corp_info = name2corp(corp_name)
fs = corp_info.extract_fs(bgn_de='20210101')
# fs.save()
# print(type(fs))
df_fs = fs['bs']
print(df_fs.head(5))