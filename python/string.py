s="You are awesome"
print(s)

s1="""    You are
the creator
of your destiny    """
print(s1)
#INDEXING IS TO FIND OR LOCATE A SPECIFIC VALUE IN A STRING IS CALLED INDEXING
print (s[0])
print(s[1])

print(s1[4])
#REPITITON IS TO REPEAT A PARTICULAR VARIABLE NUMEROUS TIMES USING *(STAROPERATOR)

print(s *2)


#LENGTH

print(len(s1))

#SLICING

print(s[0:5:2])
print(s[:8])
print(s[-3:-1])
print(s1[35::-1])

#STRIP

print(s1.rstrip())
print(s1.strip())

#FIND
print(s.find('awe',0,len(s)))
#COUNT
print(s.count("a"))
#REPLACE
print(s.replace("awesome","amazing"))

#UPPER,LOWER,TITLE
print(s.upper())
print(s.lower())
print(s.title())
