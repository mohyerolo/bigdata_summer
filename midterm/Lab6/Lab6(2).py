s = {1, 2, 3, 4, 5, 1, 2, 3}
print(s)    
s.add(10)
print(s)

s.discard(20)
print(s)

t = {9, 8, 5, 3, 1}
print(s.union(t))
print(s.difference(t))
print(t.difference(s))