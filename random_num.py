import random

c1 = random.randint(1,13)
c2 = random.randint(1,13)
c3 = random.randint(1,13)

if c1>=10 and c2>=10 :
    print(f"ใบแรกสุ่มได้ :{c1}",f"ใบสองสุ่มได้ : {c2}")
    print('point : 10')

elif c1 == c2 :
    print(f"ใบแรกสุ่มได้ :{c1}",f"ใบสองสุ่มได้ : {c2}")
    print(f"{c1} = {c2}")
    print(f"{c1} = {c2}")

score = c1 + c2 % 10
point = score
if point == 9 :
    print(f'แสดงว่า : {point} เป็น P9')
elif point == 8 :
    print(f'แสดงว่า : {point} เป็น P8')
elif point < 4 :
    pass

if c3 >= 10 :
    print(f"ใบแรกสุ่มได้ : {c3}")
    print("point : 10")
elif c3 == c1 and c2 :
    point = c1 + c2 +c3 % 10
print(f"ใบแรก : {c1}/ ใบสอง : {c2}/ ใบสาม : {c3}")
print(f"แต้มที่ได้ : {score}")
pass