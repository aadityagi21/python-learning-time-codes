lower=0
upper=0
f=input(":")
for i in f:
    if(i.islower()):
        lower+=1
    elif(i.isupper()):
        upper+=1
print("No of Lower characters are",lower)
print("No of upper characters are",upper)
