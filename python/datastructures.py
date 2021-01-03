students={"Franklin":["django","python","DRF"],"Jacobs":['java','spring'],"Marcus":['js','node','graphicdesign']}
keys=students.keys()
for eachKey in keys:
    print("courses taken by" ,eachKey," are:  ")
    for eachcourse in students[eachKey]:
        print(eachcourse)
