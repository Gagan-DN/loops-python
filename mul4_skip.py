
#3 loop to print each integers in list but skip if number multiple of 4
lnum=[12,14,20,3,5,6,7,32,23]
for i in lnum:
    if i%4==0:
        continue
    else:
        print(i)
    i+=1
