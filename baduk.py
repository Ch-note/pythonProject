n = int(input("숫자:"))
level = 1
count = 0

while level <= n:
    print(level) #확인용
    count += level
    level += 1
print(count)
