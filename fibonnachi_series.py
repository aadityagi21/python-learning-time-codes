
n=int(input(":"))
a=0
b=1

print(a)
print(b)
for i in range(2,n+1):
    next=a+b
    print(next)
    a=b
    b=next
    
