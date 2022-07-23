num = [1, 2, 3, 4, 5, 6, 7, 8, 8, 10]

evenF = lambda x : x % 2 == 0
oddF = lambda x : x % 2 != 0

even = list(filter(evenF, num))
odd = list(filter(oddF, num))

print("원래 리스트:", num)
print("짝수 리스트:", even)
print("홀수 리스트:", odd)