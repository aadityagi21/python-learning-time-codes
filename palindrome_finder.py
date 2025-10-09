n=int(input("Enter Number :"))
t=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("This Number is Palindrome" if t==rev else "This Number is not Palindrome")  
