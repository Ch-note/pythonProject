n = int(input("숫자를 입력하세요:"))
a = 1
m = 1
while a <= n:
    print(a) #확인용
    
    m *= a
    a += 1
print(m)