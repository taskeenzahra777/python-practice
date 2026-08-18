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

if o>=50:
   print('Grade: A')
   print('Status:Pass')
elif o==45:
    print('Grade:B')
    print('Status:Pass')
elif o<45:
    print('Grade:C')
    print('Status:Pass')
elif o>=20:
    print('Grade:F')
    print('Status:Fail')
else:
    print('Error')    


print('=====================================================================================')
print('                                      RESULT                                         ')
print('=====================================================================================')
print('Name:',name)
print('Rollnumber:',r)
print('Age:',a)
print("Grade:",g)
print('Status:',status)
print('Eligibility for scholarship:',e)
