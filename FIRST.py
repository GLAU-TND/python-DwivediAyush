
n=int(input())
l=[int(i) for i in input().split()]
s=set(l)
max=0
print(s)

for i in s:
    if max<l.count(i):
        max=l.count(i)
print(max)

