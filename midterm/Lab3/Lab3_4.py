a = input("1번 전지가 있습니까? (y/n) ")
b = input("2번 전지가 있습니까? (y/n) ")
if a == 'y' and b == 'y':
    print("직렬연결: 전구에 불이 켜집니다.")
    print("병렬연결: 전구에 불이 켜집니다.")
elif a == 'n' and b == 'n':
    print("직렬연결: 전구에 불이 꺼집니다.")
    print("병렬연결: 전구에 불이 꺼집니다.")
else:
    print("직렬연결: 전구에 불이 꺼집니다.")
    print("병렬연결: 전구에 불이 켜집니다.")
