import pandas as pd
import matplotlib.pyplot as plt

q6 = pd.read_csv("Lab12\\q6_input.csv", encoding='utf-8')
print(q6)

print(q6['이름'])

data = q6['퇴직년도'] - q6['입사년도'] + 1
q6['재직기간'] = data
print(q6)
print(q6.shape)
r, c = q6.shape
print(r)

print(q6.loc[0]) # 홍길동 데이터를 가지고 옴. print(q6.iloc[0])도 같음
print(q6.iloc[0][2]) # 이렇게 하면 홍길동의 퇴직년도 출력 가능
print(q6.loc[0]['퇴직년도']) # iloc는 index로 가져올 수있고 loc는 이름으로 가져오는 것

print(q6.loc[2:5])
print(q6.loc[2:5, ['이름', '재직기간']])
print(q6.loc[:, ['이름', '재직기간']])
print(q6.groupby('퇴직년도')['입사년도'].max())


plt.rcParams['font.family'] = 'Malgun Gothic'
x = q6['이름']
print(x.values)
y = q6['재직기간']
print(y.values)

plt.plot(x, y, 'sm')
plt.xlabel("이름")
plt.ylabel("년도")
plt.show()