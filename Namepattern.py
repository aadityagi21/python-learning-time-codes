# for i in range(0,5):
#     for j in range(0,5):
#         if i==0 or i==2 or j==0 or j==4 or i==4 :print("*",end="  ")
#         else:print(" ",end="  ")
#     print()    
    
n=5
for i in range(0,n):
    # for j in range(0,n):
    #     if i==0 or j==0 or i==n-1 or (i==n//2 and j>=n//2) or (j==n-1 and i>=n//2) :print("_",end="  ")
    #     else:print(" ",end="  ")
    

    for j in range(0,5):
        if i==0 or i==2 :print("_",end="  ")
        elif j==0 or j==4 :print("|",end="  ")
        else:print(" ",end="  ")
    print(end="  ")    
    
  
    
    for j in range(0,5):
        if i==0 or i==4 or j==0 or j==4  :print("_",end="  ")
        else:print(" ",end="  ")
    print(end="  ")  
    
    
    for j in range(0,5):
        if i==0 or i==4 :print("_",end="  ")
        elif j==n//2 :print("|",end="  ")
        else:print(" ",end="  ")
    print(end="  ")  
    
    
    for j in range(0,5):
        if i==0 :print("_",end="  ")
        elif j==n//2 :print("|",end="  ")
        else:print(" ",end="  ")
    print(end="  ")  
    
    
    for j in range(0,5):
        if i==1 or i==4 or (i==0 and j==0) or j==4 :print("_",end="  ")
        else:print(" ",end="  ")
    print(end="  ")  
    
    
    for j in range(0,5):
        if i==0 or i==2 :print("_",end="  ")
        elif j==0 or j==4 :print("|",end="  ")
        else:print(" ",end="  ")
    print()
