s="python is very easy"

c=0
for i in s:
    c+=1
print(c)

print(s)


s="python is very easy"
l=[]
x=""
for i in s:
    if i!=" ":
        x+=i
    else:
        l.append(x)
        print(x)
        x=""
print(x)
l.append(x)
print(l)

a=input(":")
b=input(":")
c=input(":")
d=input(":")
e=input(":")
l=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)
print(l)

l=[]
n=int(input(":"))
for i in range(n):
    l.append(int(input(":")))
print(l)
print(l[::-1])

a=input(":")
l=['a','e','i','o','u']
if a.lower() in l:
    print("Vowel")
else:
    print("Consonant")
    
    
l=['a','b','c']
print(" ".join(l))

print(l*2)
