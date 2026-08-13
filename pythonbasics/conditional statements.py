#in this file i am going to write the code related to conditional statments only...
#================================basic-===============================
'''n=int(input("Enter any number to check weather it is even/odd/zero: "))
if n%2==0:
    print("This number is even")
elif n%2!=0:
    print("This number is odd")
elif n==0:
    print("This number is zero")
else:
    print("Error!!")'''
#-----------------------------------------------------------
'''age=int(input("Enter your age to check the status: "))
if age<18:
    print("Child")
elif age==18:
    print("Teenage")
elif age>18:
    print("adult")
else:
    print("Error!!")'''
#---------------------------------------------------------------------------------
'''t=int(input("Enter Temperature in degree celceious: "))
if t<=20:
    print("COLD")
elif t>=30:
    print("HOT")
elif t==25:
    print("NORMAL")
else:
    print("Error!!")'''
#------------------------------------------------------------------
'''m=int(input("Enter your marks to check the grades: "))
if m<=20:
    print("F")
elif m==30:
    print("E")
elif m==40:
    print("D")
elif m==50:
    print("C")
elif m==75:
    print("B")
elif m>=85:
    print("A")
else:
    print("Error!!")'''
#-------------------------------------------------------
"""mn=int(input("Enter any numbers from 1-12 to see the name of months: "))
if mn==1:
    print("January")
elif mn==2:
    print("Febraury")
elif mn==3:
    print("March")
elif mn==4:
    print("April")
elif mn==5:
    print("May")
elif mn==6:
    print("June")
elif mn==7:
    print("July")
elif mn==8:
    print("August")
elif mn==9:
    print("September")
elif mn==10:
    print("October")
elif mn==11:
    print("November")
elif mn==12:
    print("December")
else:
    print("Error!!")"""
#----------------------------------------------------------------------------
'''am=int(input('Enter shopping amount to check the eligibility for discount: '))
if am==10000:
    print("30% ")
elif am==5000:
    print("10%")
elif am==3000:
    print("5%")
elif am==1000:
    print("no discount")
else:
    print("Error!!")'''
#---------------------------------------------------------
#=============================Logical Conditions========================================
'''num=int(input('Enter number to check weather it is +tive and even/odd:'))
if num>0 and num%2==0:
    print("It is positive and even")
elif num<0 and num%2!=0:
    print("it is positive and odd")
elif num==0:
    print("it is zero")
else:
    print('error!')'''
#------------------------------------------------
#any number divisible by 3 and 5
num=int(input("Enter the number: "))
if num%3==0 and num%5==0:
    print("Yes, it is divisible both 3 and 5...")
else:
    print("iincorrect ans...")
    

