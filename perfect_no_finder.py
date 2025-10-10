
n=int(input())
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
print("Number is perfect" if(sum==n) else "This Number is not perfect number")
   


    
