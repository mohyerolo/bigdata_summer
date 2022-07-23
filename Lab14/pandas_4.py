import pandas as pd

data = [[1, 2, 3], [10, 20, 30]]
df = pd.DataFrame(data, index=['신짱구', '김철수'], columns=['프논이', '교양1', '교양2'])
print("df")
print('-' * 10)
print(df)
print(df.values) # numpy로 변환할 때 values를 쓸 수 있음
print()

row_sum = df.sum(axis = 0)
print("row_sum")
print('-' * 10)
print(row_sum)
print()

col_sum = df.sum(axis = 1)
print("col_sum")
print('-' * 10)
print(col_sum)
print()

df['총점'] = col_sum
print("df + 총점")
print('-' * 10)
print(df)
print()

print("df.keys()")
print('-' * 10)
print(df.keys())
print()

print("프논이 평균, 교양2 최댓값")
print('-' * 10)
print(df['프논이'].mean())
print(df['교양2'].max())
score = df['프논이']
print(score[score > 5])
print()

names = ['신짱구', '김철수', '유리']
data = [90, 90, 90, 270]
sr1 = pd.Series(data, index=['프논이', '교양1', '교양2', '총점'])
df = df.append(sr1, ignore_index=True)
df = df.set_index(keys=[names])
print(df)
print(df.sort_index())
print(df.sort_values(by='총점', ascending=False))