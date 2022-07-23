n = input("어떤 수 입력: ")

try:
    result = 10 % int(n)
except TypeError:
    print("자료형이 숫자가 아님")
except ValueError as e:
    print(e)
    print("숫자가 아닌 다른 자료형")
except:
    print("다른 기타 예외")
else:
    print(result)
finally:
    print("다른 거")