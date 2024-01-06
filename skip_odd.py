#2 using continue in for loop to skipodd numbers and print only even
i=0
for i in range(0,50):
    if i%2==0:
        print(i)
    else:
        continue
    i+=1
