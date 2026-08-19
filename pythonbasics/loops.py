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
n=int(input('Enter number to see its table: '))
print('The table of',n)
for n in range(1,11):
    print(2,'*',n+0,'=',n*2)


