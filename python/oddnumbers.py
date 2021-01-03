x=int(input('Enter minimum number'))
y=int(input('Enter maximum number'))

a=x
if a%2==0:a+=1
while a<=y:
    print(a)
    a+=2
