a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2,8,9,10]
c=[10]
a.append(c)
print(a)
a.extend(c)
print(a)
a.insert(0,3.342)
print(a)
a.remove(3.342)#remove only one occurance
print(a)
a.pop()#default value is last
print(a)
a.pop(0)
print(a)
a.clear()
print(a)
a.extend(b)
print(a)
d=[4,2,5,12,5656,45]
a.extend(d)
print(a)
a.sort()
print(a)
x=sorted(a)#this func make a new list instead of modifying
print(x)
a.reverse()
print(a)
a.append("java")
print(a)
x=a.index('java')
print(x)
