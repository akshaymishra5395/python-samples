from collections import OrderedDict
ordict1 = OrderedDict()
ordict1['age']=21
ordict1['name']='akshay'
print(ordict1.items())
#orderdict remember the order of items 
#it works on all methods of dict
#.keys(),values(),.items() gives ordered keys
#two dict fed same key,value in diff order are same , two orderdict fed with same values in diff order are different 
#it has doubly link list implementation
#it can be used as stack , by popitem(), that pops last inserted.
#reverse the order also