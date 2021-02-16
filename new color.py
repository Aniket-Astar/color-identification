#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:



img = cv2.imread('C:\\Users\\A-STAR\\Downloads\\c3.png')


# In[ ]:


plt.figure(figsize=(20,8))
plt.imshow(img)


# In[ ]:


rgb1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.figure(figsize=(20,8))
plt.imshow(rgb1)


# In[ ]:


hsv = cv2.cvtColor(rgb1, cv2.COLOR_RGB2HSV)


plt.figure(figsize=(20,8))
plt.imshow(hsv)


# In[ ]:


#lower_range = np.array([82,100,100])
#upper_range = np.array([164,255,5])
#lower_range = np.array([190,99,56])
#upper_range = np.array([228,99,56])
#lower_range = np.array([0,50,50])
#upper_range = np.array([17,255,255])
lower_range = np.array([80,50,50])
upper_range = np.array([120,255,255])
mask = cv2.inRange(hsv, lower_range, upper_range)



# In[ ]:


mask = cv2.inRange(hsv, lower_range, upper_range)


plt.figure(figsize=(20,8))
plt.imshow(mask)


# In[ ]:


res = cv2.bitwise_and(rgb1,rgb1,mask=mask)


# In[ ]:



plt.figure(figsize=(20,8))
plt.imshow(res)


# In[ ]:


cv2.imshow('image', rgb1)


cv2.imshow('Result', res)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[ ]:




