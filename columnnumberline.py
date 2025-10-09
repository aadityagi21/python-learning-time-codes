n=int(input(":"))
for i in range(0,n):
    a=i+1
    for j in range(0,n):
        print(a,end="  ")
        a+=n
    print()
