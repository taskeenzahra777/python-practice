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
if o>=80:
    g='A'
    if currentA>=75:
        status='Pass'
        
if o==65:
    g='B'
if o<=50:
    g='C'

print('=====================================================================================')
print('                                      RESULT                                         ')
print('=====================================================================================')
print('Name:',name)
print('Rollnumber:',r)
