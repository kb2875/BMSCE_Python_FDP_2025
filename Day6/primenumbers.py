#to print prime numbers upto n
n=int(input("enter a number:"))
i=2
prime=True
while i <= n:
    for j in range (2,i):
        if((i % j)!= 0):
            continue
        else:
            prime=False
            break
    print(f"{i} = prime" if prime else f"{i}=not prime")
    i += 1

