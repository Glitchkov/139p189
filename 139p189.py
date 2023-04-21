list=[]
for x in range(0, 41):
    for y in range(0, 41):
        if 5*(x-20)+3*(y-20)==-2:
            list.append((x-20, y-20))
print(str(list))