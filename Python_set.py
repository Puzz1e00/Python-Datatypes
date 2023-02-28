"""<Set is unordered>
<set is dictionary without key bracket pairs>
<Syntax is s={1,2,3...}>
<Set elements are unique result of s={1,1,2,3} is s={1,2,3}>
<Set is mutable but it's objects shoud be immutable Eg- s={[1,2],2} is error but s={(1,2),3} is correct since tupple is
immutable>"""
#We can add or update set
s1={1,2,3}
s1.add(4)
print(s1)
#remove elements from set
#Discard method
s1.discard(4)
print(s1)
#s1.discard(7)-this gives none
#Clear method
s1.clear()
print(s1)
s1={1,2,3,4}
#Remove method
s1.remove(4)
print(s1)
#s1.remove(5)- this gives error
#Pop Method
s1={1,2,3,4}
z=s1.pop()
print(s1)# removes randomly
print(z)# return type
#Methods in Python Set
a={1,2,3,4}
b={1,3,5,7}
#Union
c=a.union(b)
print(c)
#Intersection
d=a.intersection(b)
print(d)
#difference
e=a.difference(b)
print(e)
#Symmetric Difference
f=a.symmetric_difference(b)
print(f)