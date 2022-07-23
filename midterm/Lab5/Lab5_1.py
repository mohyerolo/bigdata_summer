def game369(num):
    n = str(num)
    for s in n: 
        if s == '3' or s == '6' or s == '9':
            return "짝"
    else: return num
    
for i in range(1, 100):
    print(game369(i), end=" ")