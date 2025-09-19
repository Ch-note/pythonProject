n = int(input("몇 번째 구구단까지?:"))
a = 1
b = 1

while a <= n:
    while b <= 9:
        print(f"{a} x {b} = {a*b}")
        b+=1
    a+=1
    b=1
