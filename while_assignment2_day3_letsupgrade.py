x=int(input("enter how many prime numbers do you want to print"))
i=1
while x>=i:
    s=0
    j=1
    while j<=i:
        if i%j==0:
            s+=1
        j+=1
    if s<=2:
        print(i)
    i+=1
