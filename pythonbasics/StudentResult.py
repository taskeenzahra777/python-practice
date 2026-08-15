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
    if assign>=180:
        if currentA>=75:
                g='A'
                status='Pass'
if o==45:
    if assign>=100 and assign<=150:
        if currentA>=75:
                g='B'
                status='Pass'
if o<45:
    if assign<100:
        if currentA<75:
                g='C'
                status='Fail'


print('=====================================================================================')
print('                                      RESULT                                         ')
print('=====================================================================================')
print('Name:',name)
print('Rollnumber:',r)
