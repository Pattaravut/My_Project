total = float(input("จำนวเงิน :"))

m500 = int(total/500)
m500_1 = total%500
print ("แบ้ง 500 :",m500,"ใบ")

m100 = int(m500_1/100)
m100_1 = m500_1%100
print ("แบ้ง 100 :",m100,"ใบ")

m50 = int(m100_1/50)
m50_1 = m100_1%50
print ("แบ้ง 50 : ",m50,"ใบ")

m20 = int(m50_1/20)
m20_1 = m50_1%20
print ("แบ้ง 20 :",m20,"ใบ")
print("เหรีญ :",m20_1,"เหรียญ")