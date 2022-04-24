import dart_fss as dart
from constants import DART_API_KEY

from time import time

# Open DART API KEY 설정
dart.set_api_key(api_key=DART_API_KEY)

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

# test
corp_name = "삼성전자"
corp_code = name2code(corp_name)
print(f"code : {corp_code}")