import random
answer = random.randint(1, 100)
my_answer = 0
count = 5

print(f"목숨:{count}")
while  True :
    my_answer = int(input("1부터 100 사이 숫자를 입력:"))
    
    if count == 0:
        print("기회를 모두 사용하였습니다")
        break
    elif my_answer > answer:
        print("더 작은 수를 입력하세요")
        count -= 1
        print(f"남은 기회: {count}")
        
    elif my_answer < answer:
        print("더 큰 수를 입력하세요")
        count -= 1
        print(f"남은 기회: {count}")
    
    else:
        print("정답입니다")     
