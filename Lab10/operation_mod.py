def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

# 현재 파일에서 실행하면 출력하지만 다른 파일에서 모듈로 쓰이면
# 밑에가 수행되지 않음
if __name__ == "__main__":
    print(add(4,5))
    print(__name__)