size=5
for i in range(size):
    for j in range(size-i-1):
        print(" ", end=" ")
    for k in range ((2*i)+1):
        print("*", end=" ")
    print()
for i in range(size):
    for j in range(size-i-1, size):
        print(" ", end=" ")
    for k in range ((size+1)-(2*i)+1):
        print("*", end=" ")
    print()