import datetime
import os

# เมนู
def customer() :
        print("===============================")
        print("[Category Book]\n")
        print("1.Novel")
        print("2.Cartoon")
        print("3.Study Book")
        print("0.Close program\n")
        print("===============================")
            
# นิยาย                
def N() :
    os.system('cls')
    sum_credit=0
    N_set=set()
    work=1
    count=1
    print("\n Novel \n")
    for i in novel:
        print(count,".",i,)
        count += 1
    print("\n Print End or end to stop")      
    while work != 0 :
        N_set,sum_credit,work = Nov(N_set,sum_credit,work)
    os.system('cls')
    print(f"Books  {len(N_set)} book  , Price {sum_credit} bath")
    show_novel()
    con=str(input("\n You want to place a new order Y/N : "))
    if con == "Y" :
        os.system('cls')
        N_set.clear()
        return N()
    elif con == "N" :
        os.system('cls')
        return 0  
    
def Nov(answer,sum_credit,work):
    answer = input("\n Choose :")
    if answer in novel.keys() :
        N_set.add(answer)
        sum_credit = sum_credit + novel[answer]
    else :
        if answer == "End" :
            work = 0
        elif answer == "end" :
            work = 0
        elif answer == 0 :
            work = 0   
        else :
            print("Notfound '%s'"%answer)
    return N_set,sum_credit,work

def show_novel() :
    count = 1
    for i in N_set :
        print(count,".",i,)
        count += 1     

# การ์ตูน
def M() :
    os.system('cls')
    sum_credit=0
    M_set=set()
    work=1
    count=1
    print("\nCartoon\n")
    for i in manga :
        print(count,".",i,)
        count += 1
    print("\nPrint End or end to stop")      
    while work != 0 :
        M_set,sum_credit,work = Mang(M_set,sum_credit,work)
    os.system('cls')
    print(f"Books  {len(M_set)} book  , Prices {sum_credit} bath")
    show_manga()
    con=str(input("\n You want to make a new list Y/N : "))
    if con == "Y" :
        os.system('cls')
        M_set.clear()
        return M()
    elif con == "N" :
        os.system('cls')
        return 0

def Mang(answer,sum_credit,work):
    answer = input("\n Choose :")
    if answer in manga.keys() :
        M_set.add(answer)
        sum_credit = sum_credit + manga[answer]
    else :
        if answer == "End" :
            work = 0
        elif answer == "end" :
            work = 0
        elif answer == 0 :
            work = 0   
        else :
            print("Notfound '%s'"%answer)
    return M_set,sum_credit,work

def show_manga() :
    count = 1
    for i in M_set :
        print(count,".",i,)
        count += 1  

# หนังสือเรียน
def S() :
    os.system('cls')
    sum_credit=0
    S_set=set()
    work=1
    count=1
    print("\n Study Book \n")
    for i in stubook :
        print(count,".",i,)
        count += 1
    print("\n Print End or end to stop")      
    while work != 0 :
        S_set,sum_credit,work = Stu(S_set,sum_credit,work)
    os.system('cls')
    print(f"Books  {len(S_set)} book  , Prices {sum_credit} bath")
    show_stubook()
    con=str(input("\n You want to make a new list Y/N : "))
    if con == "Y" :
        os.system('cls')
        S_set.clear()
        return S()
    elif con == "N" :
        os.system('cls')
        return 0

def Stu(answer,sum_credit,work):
    answer = input("\n choose :")
    if answer in stubook.keys() :
        S_set.add(answer)
        sum_credit = sum_credit + stubook[answer]
    else :
        if answer == "End" :
            work = 0
        elif answer == "end" :
            work = 0
        elif answer == 0 :
            work = 0   
        else :
            print("Notfound '%s'"%answer)
    return S_set,sum_credit,work      

def show_stubook():
    count=1
    for s in S_set :
        print(count,".",s)
        count += 1

# Time
def greet (name) :
    thistime=datetime.datetime.now().hour
    if(thistime<=12) :
        thegreet="Morning"
    else :
        thegreet="Evening"
    print (f"Helllo,{thegreet} : {name}")
    print(f"Welcome to bookstore : {name}\n ")
    print("=================================")

# Bye Bye
def farewell(name) :
    print("==============================")
    print(f"\n++ Goodbye {name}")
    print("Thank you for using the service.")
    print("==============================") 

novel= {"The Eminence in Shadow":325,
        "Isekai de Cheat Nouryoku":285,
        "Solo Leveling":295,
        "Re:Zero":150,
        "Assassin's Pride":150,
        "86 eighty-six":289,
        "The Misfit of Demon King Academy":349,
        "Fate/Strange fake":170
        }

manga = {"Karneval":59,
         "Blue Lock":69,
         "Alloswand":69,
         "Tokyo Revenger":59,
         "Elden ring":80,
         "Coffee Vanilla":59,
         "Kaiju No.8":80,
         "Spy x Family":69,
         "Ayakashi Triangle":69,
         "Berserk":109,
         "One-Punch Man":89,
         "Dandadan":69                
        }

stubook = {"New world 1":180,
           "New world 2":180,
           "New world 3":180,
           "New world 4":180,
           "New world 5":180,
           "New world 6":180,
           "Thai language":180,
           "Smart Choice":299,
           "Headway":299,
           "American Family and Friends":389,
           "Oxford Picture Dictionary":819  
        }

# main program
print("==============================")
myname= input("Name:")
os.system('cls')
greet(myname)
N_set=set()
M_set=set()
S_set=set()
while True :
    try :
        customer()
        work=int(input("Choose : "))
        if work == 0 :
            farewell(myname)
            break
        elif work == 1 :
            N()
        elif work == 2 :
            M()
        elif work == 3 :
            S()
        else :
            os.system('cls')
            print("Error information, please try again.")

    except ValueError :
        os.system('cls')
        print("set as numbers only")