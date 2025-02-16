import random


try :
    print("\n[เดาตัวเลข]")
    ran_num = random.randint(1,10)
    ans_num = 0
    round = 1
    print(ran_num)
    while ans_num != ran_num :
        try :
            ans_num=int(input(f"[{round}]Answer is :"))
            if ran_num > ans_num :
                print (f"++มากกว่า {ans_num}")
            elif ran_num < ans_num :
                print (f"--น้อยกว่า {ans_num}")
            else :
                print ("ถูกต้อง!!!")
                break
            round+=1
        except ValueError :
            print("กำหนดข้อมูลเป็นตัวเลข")
    print (f"*** You take {round} rounds ***")

except KeyboardInterrupt :
    print("END")
    
except :
    print("ใส่ตัวเลข")

finally :
    print("END")
    