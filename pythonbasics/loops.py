#in this code i will practice some questions related to loops to make my basics more strong...
#-------------------------------------------------------------------------------------
# in this 1st code i am going to print any range of  numberz
#for this i use a built in function range()
'''n=int(input('Enter number: '))
for n in range(1,n+1):
    print(n)'''
#---------------------------------------------------
'''n=int(input('Enter number: '))
evenS=0
evcount=0
oddS=0
odcount=0
for n in range(1,n+1):
    print(n)
    if n%2==0:
        evenS=evenS+n
        evcount=evcount+1

    else:
        n%2!=0
        oddS=oddS+n
        odcount=odcount+1
     

print('the sum of all even numbers is:',evenS)
print('the total even numbers are:',evcount)
print('the sum of all the odd numbers is',oddS)
print('the total odd numbers are:',odcount)'''
#-------------------------------------------------------------------------------------
'''n=int(input('Enter number 2: '))
print('The table of',n)
for n in range(1,11):
    print(2,'*',n+0,'=',n*2)
'''
#---------------------------------------
#table of any number
'''num=int(input('Enter number:'))
for i in range(1,11):
    print(num,'*',i,'=',num*i)'''
#------------------------------------------------------------------------
# squares and cubes of any numbers
'''num=int(input('Enter number:'))
print('The square and cubes:')
for i in range(1,num+1):
    print('number:',i)
    print('square:',i**2)
    print('cube:',i**3)
    print('-------------------------')'''
#--------------------------------------------------------------------------
'''n=int(input('Enter number:'))
for i in range(1,n+1):
        if n>=10:
          print(n+i)'''
#-----------------------------------------------------------------------------
'''num=int(input('Enter the number: '))
print('Print only that number that is divisible by 3 only:')
for i in range(1,num+1):
    if i%3==0:
        print(i) ''' 
#---------------------------------------------------------------
#taking input from the user and printing thier sum
'''n=int(input('Enter number:'))
sum=0
for i in range(1,n+1):
    sum=sum+i
print('The sum of all the value from 1 to',n,'is:',sum)'''
#-------------------------------------------------------------------------------------
#taking input from the user and printing the sum of just even numberz
'''n=int(input('Enter the numer: '))
even=0
sum=0
for i in range(1,n+1):
    if i%2==0:
        even=i
        sum=sum+even
print('The sum of all the even numbers from 1 to',n,'is:',sum)'''
#---------------------------------------------------------------------------
#take any number to print its factorial
'''n=int(input('Enter the number:'))
print('The factorial of number')
f=1
for i in range(1,n+1):
    f=f*i
    print(f)
print('the factorial of',n,'is',f)'''
#------------------------------------------------------------------------
#to check the positive or negative number...
n=int(input('Enter the number:'))
for i in range(1,n+1):
    