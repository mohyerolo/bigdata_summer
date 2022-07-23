import pandas as pd

datas = {'학생명': ['김철수', '신짱구', '유리'], '프논이': [70, 80, 90], '교양': [90, 80, 95]}
df = pd.DataFrame(datas)
print(type(df))
print(df)

# 일차원은 series로 넣어주면 되고 합치기가 되고
# concat으로 이차원처럼 보여줄 수는 있음