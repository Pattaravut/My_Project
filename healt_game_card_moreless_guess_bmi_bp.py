import datetime
import random
from re import L

# menu หลัก
def mainmenu():
    print("\n[เมนูหลัก]")
    print("1.ตรวจสุขภาพ")
    print("2.เล่นเกมส์")
    print("0.ออกจากโปรแกรม")
    
# menu 1 ตรวจสุขภาพ
def menu_healt() :
    while True :
        print("\n[ตรวจสุขภาพ]")
        print("1.BMI")
        print("2.ตรวจความดัน")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work = int(input("เลือก : "))
        if work == 9 :
            return 9
        elif work == 0 :
            return 0
        elif work == 1 :
            bmi()
        else:
            pass

# menu 2 เล่นเกมส์
def menu_game() :
    while True :
        print("\n[เล่นเกมส]")
        print("1.เดาตัวเลข")
        print("2.ไพ่89")
        print("3.มากกว่าน้อยกว่า")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work = int(input("เลือก : "))
        if work == 9 :
            return 9
        elif work == 0 :
            return 0
        elif work == 1 :
            guess()
        elif work == 2 :
            card89()
        elif work == 3        :
            moreorless()
        else:
            pass


def card89() :
    print("\n[ไพ่89]")
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


def moreorless() :
    print("\n[มากกว่าน้อยกว่า]")
    r1 = random.randint(1,10)
    money = int(input("Input u money:"))
    round = 0
    while money != 0 and round !=5 :
        round += 1
        r2 = random.randint(1,10)
        print(f"Round : ",round )
        print(f"Money : ",money)
        print(f"Number : ",r1)
        z = input("More or Less than >> More press M << | >> Less press L << :")
        y = int(input("Bet : "))
        print("---------------------------------------------------------")

        if r1 == r2 :
            money = money
            print ("DRAW")
        elif r2 < r1 and z == 'M' :
            money = money + y 
            print ('True')
        else : 
            money = money - y
            print ('False')
        print(r2)
        r1 = r2 
    if round > 5 :
        print("Lost")
    else :
        print("Balances : ")


        
def guess() :
        print("\n[เดาตัวเลข]")
        ran_num = random.randint(0,9)
        round = 0
        while True :
            round = round+1
            answer = int(input("ระบุ number :"))
            if answer == ran_num :
                break
        print("คำตอยคือ : ",ran_num)
        print("you win")
        print("เล่นไปทั้งหมด :",round,"รอบ")



def bmi() :
    print("[BMI]")
    wi = float(input("น้ำหนัก (kg) :")) 
    hi = float(input("ส่วนสูง (cm) :"))
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
    print (f"+++ค่า BMI={thebmi} สถานะ{thestate}")

def bp() :
    print("[ตรวจความดัน]")
    a = int(input("ระบุความดันตัวบน : "))
    b = int(input("ระบุความดันตัวล่าง : "))
    if a<=120 and b<=80 :
        print("ความดัน ปกติ,ควบคุมอาหาร ออกกำลังกายหมั่นเช็คความดัน")
    elif a<=139 and b<=89 :
        print("ความดัน เริ่มสูง,ควบบคุมอาหาร ออกกำลังกายหมั่นเช็คความดัน")
    elif a<=159 and b<=99 : 
        print("ความดัน สูง,พบแพทย์")
    elif a>=160 and b>=100 :
        print("ความดัน สูงมาก,พบแพทย์ด่วน")
    else :
        pass

def greet (name) :
    thistime=datetime.datetime.now().hour
    if(thistime<=12) :
        thegreet="ตอนเช้า"
    else :
        thegreet="ตอนบ่าย"
    print (f"สวัสดี{thegreet} คุณ{name}\n")

def farewell(name) :
    print(f"\n++ ลาก่อนคุณ{name}")
    print("ขอบคุณที่ใช้บริการ")
    print("--------------")



# main program
print("--------------")
myname= input("ชื่อ:")
greet(myname)


while True :
    mainmenu()
    work=int(input("เลือกหัวข้อเพื่อทำงาน : "))
    if work == 0 :
        farewell(myname)
        break
    elif work==1:
        if menu_healt() == 0:
            farewell(myname)
            break
    elif work==2:
        if menu_game() == 0:
            farewell(myname)
            break
    else :
        pass