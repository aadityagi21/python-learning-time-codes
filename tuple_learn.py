a=('ddfdf',"AADI",43,"@#!")
b="aditya_tyagi"
print(a)
c=tuple(b)
print(c)
print('a' in c)
print('rhb' in c)
one,two,three,four=a##unpacking
print(one)
print(two)
print(three)
print(four)

five,*six=c
print(five)
print(six)

print(a.count('b'))
print(c.count('a'))

f=("fj","f","jsjo","fjd")

x=sorted(f,key=len)
print(x)
