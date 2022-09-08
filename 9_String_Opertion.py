#!/usr/bin/env python
# coding: utf-8

# # String Slicing
# 
# 
# 

# In[25]:


name="Logic First"

#  L   O   G  I  C      F  I  R   S   T
#  0   1   2  3  4  5  6  7  8   9   10
# -11 -10 -9 -8 -7 -6 -5 -4 -3  -2   -1


    


# # Using Indexing
# 
# str[Start: stop: Index]
# we can leave empty start , empty stop

# In[4]:


print(name[3])


# In[6]:


print(name[0:4]) #[start index : stop index]


# In[7]:


print(name[:4])


# In[8]:


print(name[2:4])


# In[9]:


print(name[2:])


# In[12]:


print(name[2:10:2]) # [start, stop, Step]


# In[15]:


print(name[::-1])


# In[24]:


print(name[-2: :1])


# In[28]:


print(name[2:-2])


# # Using Slice Method

# In[30]:


x= slice(2,-2)
print(name[x])


# In[34]:


val = "Happy"
print(val[0])
print(val[:2])
print(val[:3])
print(val[:4])
print(val[:5])


# In[40]:


print(val[-1])
print(val[-2:])
print(val[-3:])
print(val[-4:])
print(val[-5:])


# In[ ]:




