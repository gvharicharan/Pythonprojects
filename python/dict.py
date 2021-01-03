dict={1:"Charan",2:"Morgan",3:"Alex"}
print(dict)

print(dict.items())

c=dict.keys()
for i in c:
    print(i)

v=dict.values()
for i in v:
    print(i)

del dict[3]
print(dict)
