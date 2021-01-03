maths=int(input('Marks scored in maths'))
physics=int(input('Marks scored in physics'))
chemistry=int(input('Marks scored in chemistry'))

if maths>=35:
    print('student has Passed in maths')
else:
    print('student has failed in maths')

if physics>=35:
    print('student has passed in physics')
else:
    print('student has failed in physics')
if chemistry>=35:
     print('student has passed in chemistry')
else:
    print('student has failed in chemistry')

average=(maths+physics+chemistry)/3
if  average<=59:
    print('C GRADE')

if average<=69:
    print('B GRADE')

if average>69:
    print('A GRADE')
