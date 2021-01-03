lst=[12,52,"HARI",10.5,9.0,54,23,14]
print(lst)
print(lst[2])
print(lst[0:6:2])
print(lst*3)
print(len(lst))

lst.append(40)
print(lst)
lst.remove('HARI')
print(lst)
del(lst[1])
print(lst)

print (max(lst))
print (min(lst))

lst.insert(2,'python')
print(lst)

lst.sort(reverse=True)
print(lst)
