from matplotlib import pyplot as plt
# 이게 있어야 한글이 안 깨짐
plt.rcParams['font.family'] = 'Malgun Gothic'

x = [1, 2, 3]
y = [1, 2, 3]

plt.plot(x, y, marker='o') 
plt.title("1차원 그래프")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(['test'])
plt.show()