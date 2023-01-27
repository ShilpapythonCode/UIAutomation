print('Hello Using Single Quotes')
print("Hello Using Double Quotes")
print('''Hello Using Triple Quotes''')
'''This is just practice programme'''
s='''Myself Shilpa'''
print(s.capitalize())
print(s.casefold())
print(s.center(10,'$'))

s="block:hello:mango:banana"
m=s.split(':')
print(m)
n=[]
for li in m:
    n.append(li)
print(s.title())

list=['ab1','cd2','ef3','tr4']
sum=0
for i in list:
    for j in i:
        if j.isdigit():
            sum=sum+int(j)
print(sum)


