n=int(input("enter the number:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()
for i in range(1,n):
    for j in range(1,n-i):
        print("*",end="")
    print()
