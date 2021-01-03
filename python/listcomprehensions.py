#Even numbers in a list:

"""lst=[x for x in range(2,21,2)]
print(lst)"""

"""lst=[x for x in range(1,21) if x%2==0]
print(lst)"""

#Products in a list:

"""a=[1,2,3,4,5]
b=[4,7,8,2,4]

z=[] # Empty list
'''for i in range(len(a)):
    z.append(a[i]*b[i])'''

z=[a[i]*b[i] for i in range(len(a))]

print(z)"""

#Common elements in  a list:
a=[2,4,6,8]
b=[1,2,3,4]
result=[]
'''for i in a:
    if i in b:
        result.append(i)'''
result=[i for i in a if i in b]
print(result)


a=[1,2,3,4,5]
b=[8,7,9,6,2]


z=[a[i]*b[i]for i in range(len(a))]

print(z)

x=[4,8,9,5,4]
y=[5,7,9,2,1]

result=[]

result=[i for i in x if i in y ]
print(result)
