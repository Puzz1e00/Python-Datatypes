"""
triple quoted can be used to write comments
"""
a="broadway"
b="infosys"
#Operations
print(a+b)#concatenation- combine
print(a*3)#repitition
print(a[4])#indexing
print('b'in a)#membership
#Built In Functions
print(bool(''))
c=len('Hello')#len is count
print(c)
strl="Hello World"
x=slice(2,5)#slicing
print(strl[x])
#Python String methods
d=strl.capitalize()#capitalization- capitalizes first letter in first word
print(d)
e=strl.upper()#Capitalizes all letters in the string
print(e)
f=strl.lower()# all small letters
print(f)
g=strl.title()#Capitalize first letter in all words of the string
print(g)
str1="Cookie cutter"
str2="cut"
str3="Cut"
h=str1.find(str2)#finding cut(str2) in cookie cutter(str1)
print(h)
i=str1.find(str3)
print(i)#If it cannot find Cut in str1 then the result is always -1, Cut and cut is not the same
str4="hip hip hurray"
j=str4.replace('hip','Hip')#replacing
print(j)
k=j.replace('Hip','hip', 1)#replacing with indexing
print(k)
l=strl.split()#splits the string and makes it into a list, since there is space between the brackets and nothing else it
#splits from space
print(l)
pets='cat,dog,mouse'
m=pets.split(',')#splits from comma
print(m)
n="".join(l)#joins the list l=["hello","world"] and since there is a space in between "" it joins from space
print(n)
o=",".join(m)
print(o)
#String formating
message=f"I study at {a}"
print(message)
print('i am {} and I am {} years old.'.format('John Doe',23))#another way of formating
print('{a}, {b}, {c}'.format(a='foo', b='bar', c='baz'))#anothe rway of formating
print(f'{{2+3}}')
print(f"{(2+3)}")