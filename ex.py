ramen = 2000
bread = 1500
soda = 2000
snack = 1500

ramen_eat = int(input("라면 몇 개를 먹었나요?:"))
bread_eat = int(input("빵 몇 개를 먹었나요?:"))
soda_eat = int(input("음료 몇 개를 먹었나요?:"))
snack_eat = int(input("과자 몇 개를 먹었나요?:"))
total = (ramen * ramen_eat) + (bread * bread_eat) + (soda * soda_eat) + (snack * snack_eat)
print(f"계산서: 라면 {ramen_eat}개, 빵{bread_eat}개, 음료{soda_eat}개, 과자{snack_eat}개로 총 {total}원 입니다."   )


