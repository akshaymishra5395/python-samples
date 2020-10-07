from collections import defaultdict

d = defaultdict(lambda : "default params")
d[0]=0
print(d[1])

d1 = defaultdict(list)
s= {"a":1,"b":2,"a":3,"b":4}
for k,v in s.items():
    d1[k] = v

print(list(d1))

d1 = defaultdict(int)
s= "missisipi"
for x in s:
    d[x]+=1
print(d1)