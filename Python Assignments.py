#!/usr/bin/env python
# coding: utf-8

# Number Division

# In[1]:


items = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p, 2)
    if x%5 == 0:
        items.append(p)
print(','.join(items))


# Sorting

# In[2]:


s = 'John,19,80 John,20,90 John,17,91 John,17,93'

lst = [tuple(x.split(',')) for x in s.split()]

print(sorted(lst, key=lambda x: (x[0], x[1], x[2])))

