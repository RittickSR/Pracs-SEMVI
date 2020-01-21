#!/usr/bin/env python
# coding: utf-8

# In[34]:


import re
lex=input("Enter a string")
test=re.findall('[a-zA-Z][a-zA-Z0-9]*',lex)
print(test)
keyword=['int','float','double','char','string','print']
special=[',',';','(',')']
op=['+','-','*','/','%','=']
test1=re.findall('[0-9]+',lex)
print(test1)
for i in test1:
    print(i+" is a number")
for i in test:
    if(i in keyword):
        print(i+" is keyword")
    elif(re.match('[a-zA-Z]+',i) is not None):
        print(i+" is identifier")
for i in lex:
    if (i in special):
        print(i+" is special character")
    elif (i in op):
        print(i+" is operator")

