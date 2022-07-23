def average(*args):
    sorted_args = tuple(sorted(args, key=lambda x: x))
    print("매개변수로 전달된 값: ", end=" ")

    sum = 0
    for i in sorted_args:
        print(i, end=" ")
        sum += i
    print()
    return sum / len(args)

print("평균: ", average(1, 2, 3, 4, 5))
print("-" * 40)
print("평균: ", average(30, 10, 20))