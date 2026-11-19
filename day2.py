"""s='good Morning good afternoon'
print(s[-27:-23:1])
print(s[-17:-21-1:-2])
#ggirM
print(s[-14:-22-1:-2])"""


#conditional statements
"""s=(eval(input("enter tuple:")))
if type(s)==(tuple):
    print("given string is tuple")
else:
    print("given string is not tuple")


s=input("enter string:")
if len(s)==5:
    print("sting has 5 char")
else:
    print("string doesnt have 5 char")

num=int(input("enetr digit:"))
if 10<=num<=99:
    print("yes 2 digit")
else:
    print("not 2 digit")

s="i am manushree"
print(s.upper())


s=(input("enter string:"))
if 'A'<=ch<='Z':
    print("upper")
elif 'a'<=ch<='z':
    print("lower")
elif 0<=int(ch)<=9:
    print("it is digit")
else:
    print("special chracter")


l=eval(input("enter list:"))
if type(l)==(list):
    if len(l)%2==0:
        print("l ")
    else:
        print("it is list")
else:
    print("it is not a list")


i=1
while i<6:
    print("hello")
    i+=1


list=eval(input("enter list:"))
i=0
while i<len(list):
    print(list[i])
    i+=1       
       

num=int(input("enter number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

print(rev)


for i in range(5):
    print("hello world")


s=input("enter string:")
output=""
for i in s:
    if 'A'<=i<='Z':
        output=output+chr(ord(i)+32)
    else:
        output=output+i
print(output)

s=input("enter string:")
output=""
for i in s:
    if 'a'<=i<='z':
        output=output+chr(ord(i)-32)
    else:
        output=output+i
print(output)


s=[12,10,'hello','Good',5j,'Bye']
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)

def convert():
    s=input("enter string:")
    output=""
    for i in s:
        if 'A'<=i<='Z':
            output=output+chr(ord(i)+32)
        else:
            output=output+i
    print(output)
convert()"""







