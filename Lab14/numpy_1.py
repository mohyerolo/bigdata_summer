import pandas as pd
import numpy as np
df = pd.DataFrame({'상품명': ['커피', '우유', '펜', '마스크'],
'판매가': [2000, 2500, 1000, 500],
'제조사': ['aaa', 'bbb', 'aaa', 'ccc']})
print(df)
print(df.iloc[:,0]) #첫번째 열 출력
print(df.iloc[0, 2]) #첫번째 열의 3번째 데이터 출력
print(df.loc[1]) #첫번째 행
print(df.loc[:, '제조사']) #열 이름으로 출력
nums1 = df.groupby('제조사')['판매가'].sum() #제조사 별로 판매가 계산
print(nums1)
df['평점'] = np.random.rand(4) * 10
print(df)