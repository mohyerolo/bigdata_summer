import matplotlib
import pandas
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
q6 = pandas.read_csv("Lab12\\q6_input.csv", encoding="utf-8")

data = q6.groupby("퇴직년도")['입사년도'].mean()
print(data)
data.plot()
plt.title("퇴직연도별 입사년도 평균")
plt.legend(['평균'])
plt.show()