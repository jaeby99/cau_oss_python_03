width = float(input("가로: "))
length = float(input("세로: "))
height = float(input("높이: "))

volume = width + length + height

if volume <= 80:
    fee = 5000
elif volume <= 100:
    fee = 8000
elif volume <= 120:
    fee = 10000
elif volume <= 160:
    fee = 13000

if volume <= 160:
    print("해당 택배의 배송요금은", fee, "입니다")
else:
    print("해당 택배의 길이는 배송불가입니다.")