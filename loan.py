money = float(input("จำนวนเงินที่ต้องการกู้ : "))
print(money,"บาท")

mounth = float(input("จำนวนเดือนที่ต้องการชำระ :"))
print(mounth,"เดือน")

htp = (money/mounth) + money *  (2/100)/(mounth)
print("จำนวเงินทที่ต้องการจ่าย %d /เดือน : " %(htp))

total = htp*mounth
print("จำนวเงินที่ต้องจ่ายทั้งหมด %d" %(total))