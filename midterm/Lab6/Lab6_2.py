abbreviation = {'CS':'Computer science', 'IT':'Information Technology',
'IoT': 'Internet of Things', 'HAND':'Have A Nice Day',
'thx':'Thanks', 'BBL':'Be Back Later'}

print("번역할 문장을 입력하시오:")
word = input()
if word in abbreviation:
    print(abbreviation[word])

#print(abbreviation[word], '없음')