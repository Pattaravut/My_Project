income = float(input("จำนวนเงิน บาท ต่อ 1 ปอนด์ :"))

player = (input("player name :"))

week = float(input("นักเตะได้รับ(ปอนด์)ต่อสัปดาห์ :"))
print(player,"ได้รับ",week*income,"บาท ต่อสัปดาห์")

day = week/7
print(player,"ได้รับ",day,"บาท ต่อวัน")

hours = day/24
print(player,"ได้รับ",hours,"บาท ต่อชั่วโมง")

minute = hours/60
print(player,"ได้รับ",minute,"บาท ต่อนาที")

second = minute/60
print(player,"ได้รับ",second,"บาท ต่อวินาที")