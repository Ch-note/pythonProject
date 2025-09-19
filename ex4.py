a = int(input("숫자를 입력하세요:"))
b = int(input("몇 번째 자리로 갈까요:"))

c = (a // (10 ** (b - 1))) % 10
print(c)
    