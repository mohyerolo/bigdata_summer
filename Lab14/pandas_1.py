import pandas as pd

data = [80, 90, 100]
sr1 = pd.Series(data) # 리스트를 판다스로 변경
# print(type(sr1))
# print(sr1)

data = [10, 20, 30]
sr2 = pd.Series(data)

print("인덱스")
seri_hap = pd.concat([sr1, sr2])
print(seri_hap)
print()

# 인덱스를 무시하고 연속으로 붙이기
print("인덱스 무시, 행")
seri_hap = pd.concat([sr1, sr2], ignore_index= True)
# seri_hap = pd.concat([sr1, sr2], ignore_index= True, axis = 0) # 이렇게 해도 같음
print(seri_hap)
print()

#똑같이 인덱스 무시하지만 열로 붙이는것
print("인덱스 무시, 열")
seri_hap = pd.concat([sr1, sr2], ignore_index= True, axis=1)
print(seri_hap)
print()