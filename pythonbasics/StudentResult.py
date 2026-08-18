#==============students result and scholarship eligibility checker========================
print('=====================================================================================')
print('                              STUDENT RESULT SYSTEM                                  ')
print('=====================================================================================')
name=str(input('Enter your name: '))
r=int(input('Enter rollnumber: '))
a=int(input('Enter age: '))
totalMarks=100
o=int(input('Enter obtained marks out of 100: '))
totalA=100
currentA=float(input('Enter attendance:'))
totalAssignment=200
assign=int(input('Enter obtained marks in assignmemts out of 200: '))
fi=int(input('Enter total family income:'))
#------------------------------------------------------------------------------------
print('=====================================================================================')
print('                                      RESULT                                         ')
print('=====================================================================================')
print('Name:',name)
print('Rollnumber:',r)
print('Age:',a)
if o>=50 and assign>=150:
   print('Grade: A')
   print('Status:Pass')
elif o>=45 and assign>=100:
    print('Grade:B')
    print('Status:Pass')
elif o<45 and assign<=80:
    print('Grade:C')
    print('Status:Fail')
else:
    print('Error')
#------------------------------------------------------------------------------------    
if fi<=40000:
    print('Eligible for scholarship')
else:
    print('Not eligible!!')



