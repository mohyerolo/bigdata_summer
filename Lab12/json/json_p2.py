import json

info_dic = {'name':'신짱구', 'birth':'1224', 'age': 20}

# 파일을 이용하는게 아닐 때 dumps, 들여쓰기: indent
info_data = json.dumps(info_dic, indent=4, ensure_ascii = False)
print(info_data)

# 파일에서 가져오는게 아닌 파일 객체에서 가져올때 loads
info_out = json.loads(info_data)
print(info_out)

num_list = json.dumps([10, 20, 30, 40, 50], indent=4)
print(num_list)