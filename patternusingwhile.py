n=int(input(":"))
print("")

i=0
while(i<n):
    j=0
    while(j<n):
        if(j==0 or j==n-1 or (i<=n//2 and i==j<n//2) or i+j==n-1 and i<n//2):print("R",end="   ")
        else:print(end="    ")
        j+=1
    i+=1    
    print() 
    
print()   
print()
print()
    
i=0
while(i<n):
    j=0
    while(j<n):
        if( i==0 or i==n-1 or j==n-1 or j==0 and i <= n//2 or i==n//2 ) : print("*",end="   ")
        else:print(end="    ")
        j+=1
        
    i+=1
    print()
