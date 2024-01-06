

#4 loop that counts (10 to 1) and print "Lift OFF" 
# and skip the numbers multiple of 3 using 'continue'
    
for k in range(10,0,-1):
    if not (k%3==0):
        print(k)
    else:
        continue
    
print("Lift Off!")
