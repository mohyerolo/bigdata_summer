def abs_func(x):
    if x > 0: return x
    else: return -x

nums = [-6, 7, -1, 3, -55]
result = list(map(abs_func, nums))
print(result)

nums = [1,2,3,4,5,6]
f = lambda x : x % 2 == 0
result = list(filter(f, nums))
print(result)