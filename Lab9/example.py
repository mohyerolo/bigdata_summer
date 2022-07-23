print("----abs(x)----")
print(abs(3))
print(abs(-3))
print(abs(1.2))

print("\n----pow(x, y)----")
print(pow(2,4))
print(pow(3,3))

print("\n----sum()----")
print(sum([1,2,3]))

print("\n----max()----")
print(max([1,2,3]))
print(max("python"))

print("\n----min()----")
print(min([1,2,3]))
print(min("python"))

print("\n----divmod()----")
print(divmod(7,3))
print(divmod(1.3, 0.2))

print("\n----round(number,[ndigits])----")
print(round(10.5))
print(round(9.5))
print(round(5.678, 2))

print("\n----int()----")
print(int('3'))
print(int(3.4))
print(int('11', 2))
print(int('1A', 16))

print("\n----float()----")
print(float('3.14'))
print(float(4))
print(float(5.0))

print("\n----str()----")
print(str(3))
print(str('hi'))
print(str('hi'.upper()))

print("\n----eval()----")
print(eval('1+2'))
print(eval("'hi' + 'a'"))
x = 10
print(eval('x + 1'))

exp = input("파이썬의 수식을 입력하시오: ")
print(eval(exp))

print("\n----len()----")
print(len("python"))
print(len([1,2,3]))
print(len((1, 'a')))

print("\n----sorted(iterable)----")
s1 = sorted([3, 1, 2])
print(s1)

s2 = sorted(['a', 'c', 'b'])
print(s2)

s3 = sorted("zero")
print(s3)

s4 = sorted((3, 2, 1))
print(s4)

s5 = sorted((3,2,1), reverse = True)
print(s5)

print("\n----ord()----")
print(ord('a'))
print(ord('0'))

print("\n----chr()----")
print(chr(97))
print(chr(48))

print("\n----hex(x)----")
print(hex(234))
print(hex(3))

print("\n----oct(x)----")  
print(oct(34))
print(oct(12345))

print("\n----isdigit()----")
a ="hello"
print(a.isdigit())

a ="123"
print(a.isdigit())

a ="123abc"
print(a.isdigit())

a ="abc123"
print(a.isdigit())

print("\n----isalpha()----")
a="hello"
print(a.isalpha())
a="hello3"
print(a.isalpha())
a="123abc"
print(a.isalpha())


print("\n----dir()----")
print(dir([1,2,3]))
print(dir({'1':'a'}))