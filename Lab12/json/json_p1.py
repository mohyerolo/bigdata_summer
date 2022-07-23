import json


import json

data_w = {'name': '김철수', 'birth': '0101', 'age': 10}
with open("Lab12\\info1_w.json", "w") as outfile:
    # ensure_ascii = False: 한글 깨지는 거 막으려고
    json.dump(data_w, outfile, ensure_ascii = False)