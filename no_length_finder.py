n=int(input(":"))
length=0
sum=0
while(n>0):
    sum+=n%10
    length=length+1
    n=n//10
print(length,sum,sep=",")
