from collections import namedtuple
student = namedtuple('Student',["name","age","address"])

s1 = student("a",21,"wz") 
print(s1[0])