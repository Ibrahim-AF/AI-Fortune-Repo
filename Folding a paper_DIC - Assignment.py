#!/usr/bin/env python
# coding: utf-8

# [Problem 1] Create using the exponentiation arithmetic operator

# In[12]:


THICKNESS = 0.00008
folded_thickness = THICKNESS*2**43
print("thickness : {} meters". format(folded_thickness))


# [Problem 2] Unit Conversion

# In[11]:


# Convert meters to kilometers and display with two decimal places

print("Thickness:{:.2f} kilometers". format(folded_thickness/10000))


# [Problem 3] Create using a for statement
# 

# In[19]:


def paper(num_folds=43, thickness=0.00008):
    for i in range(1, num_folds):
      thickness = thickness*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2
      print("Thickness: {} meters". format(thicknes))
      if thickness >= 10000:
         print("Thickness: {:.2f} km". format(thickness/10000))
      else:
         print("Thickness: {:.2f} meters". format(thickness/10000))


# [Problem 4] Comparison of calculation time

# In[13]:


import time
start = time.time()
THICKNESS = 0.00008
folded_thickness = THICKNESS*2**43
print("Thickness: {}meters". format(folded_thickness))
elapsed_time = time.time() - start
print("time : {}[s]". format(elapsed_time))


# In[14]:


get_ipython().run_cell_magic('timeit', '', 'folded_thickness = THICKNESS*2**43\nfolded_thickness')


# [Problem 5] Saving to a list

# In[20]:


list2 = [0.00008]
fold_num = 44
thickness = 0.00008
for i in range(1, fold_num):
  folded_thickness = thickness*2**i
  list2.append(folded_thickness)
  print(list2)
  print(len(list2))


# [Problem 6] Displaying a line graph

# In[32]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.title("thickness of folded paper")
plt.xlabel("number of foldes")
plt.ylabel("thickness[M]")
plt.tick_params(labelsize=10) 
plt.plot(list2=0.00008, linewidth=20)
plt.show()


# [Problem 7] Customizing graphs

# In[35]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.tick_params(labelsize=10) 
plt.plot("List2=0.00008", color='red')
plt.show()

