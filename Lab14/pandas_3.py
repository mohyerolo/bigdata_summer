import pandas as pd

data = ['김철수', 70, 80]
sr1 = pd.Series(data, index=['학생명', '프논이', '교양'])
print(sr1)