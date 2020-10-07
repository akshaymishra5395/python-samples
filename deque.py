from collections import deque
d= deque()

d.append(1)
d.appendleft(2)
d.extend("abc")
d.extendleft('pqr')
d.pop()
d.popleft()
d.remove('p')   



#is called double ended queue
#remove ,pop out first occurence of element