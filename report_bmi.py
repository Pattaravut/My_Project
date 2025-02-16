try :   

    def bmi(wi,hi):
        thebmi=round(wi/(hi/100)**2,2)
        if thebmi >=30 :
            thestate="อ้วนระดับ2"
        elif thebmi >=25 :
            thestate="อ้วนระดับ1"
        elif thebmi >=23 :
            thestate="น้ำหนักเกิน"
        elif thebmi >=18.5 :
            thestate="สมส่วน"
        elif thebmi < 18.5 :
            thestate="ต่ำกว่าเกณฑ์"
        return thebmi,thestate


    print("[BMI]")
    while True :
        weight = float(input("น้ำหนัก (kg) :")) 
        height = float(input("ส่วนสูง (cm) :"))
        print("กำหนดค่าเป็นตัวเลข")
        mybmi,mystate=bmi(weight,height)
        print (f"+++ค่า BMI={mybmi} สถานะ{mystate}")
        break

except ZeroDivisionError as error :
    print ("ห้ามใส่ 0 ")

except KeyboardInterrupt :
    print("END")

finally :
    print("END")