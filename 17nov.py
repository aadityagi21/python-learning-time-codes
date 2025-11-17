a=(1,2,2,3,4,5,6,7)
# (5,6,7,4,1,2,3)
print(a[len(a)//2+1:]+a[len(a)//2:len(a)//2+1]+a[:len(a)//2])

print(a.count(19))
del a
a=(2,2)
del(a)

a=(1,2)
b=(2)
c=(3,)
print(type(a),type(b),type(c))

a,b,c,d=10,20,30,40
print(a)
print(b)#packing and unpacking

print([i for i in range(1,101)])
print(tuple(i for i in range(1,101)))
print((i for i in range(1,101)))

print(tuple(i for i in range(0,101,2)))
print(tuple(i for i in range(0,101) if i%2==0))

a,b=map(int,input(":").split(" "))
print(a+b)


