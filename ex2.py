score = int(input("점수를 입력하세요:"))
if score >= 90:
    print("A")  
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
  
elif score < 60 and score >= 0:
    print("F")

else:
    print("잘못된 점수입니다.")     