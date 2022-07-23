# reduce()함수를 사용하여 10!를 구하여 출력하는 프로그램을 작성하시오.
from functools import reduce
print(reduce(lambda x, y : x * y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))