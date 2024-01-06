#function in function
def marks():
    maths=int(input("enter your maths marks: "))
    kannada=int(input("enter your kannada marks: "))
    english=int(input("enter your english marks: "))
    social=int(input("enter your soical marks: "))
    science=int(input("enter your science marks: "))
    computer=int(input("enter your computer marks: "))
    tmarks=[maths,kannada,english,social,science,computer]
    return tmarks
def total(marks_list):
    tot=0
    for i in marks_list:
        tot+=i
    return tot
def avrage(tot):
    avg=tot/6
    return avg
def percentage(tot):
    per=(tot*100)/600
    return per
def highest(tmarks):
    k=max(tmarks)
    print("The highest marks of all is ",k)
def pf(tmarks):
    for i in tmarks:
        if i<35:
            print(" fail, better luck next time ",i)
        else:
            print("congratulations, you are pass ",i)

x=marks()
y=total(x)
z=avrage(y)
p=percentage(y)

print("marks:",x)
print("total marks: ",y)
print("average marks: ",z)
print("percentage",p)
q=highest(x)
r=pf(x)
