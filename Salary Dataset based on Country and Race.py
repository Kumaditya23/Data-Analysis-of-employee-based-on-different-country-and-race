#!/usr/bin/env python
# coding: utf-8

# ### Import important library

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Upload and Read Data

# In[6]:


df = pd.read_csv(r"C:\Users\meanu\Downloads\salary dataset based on country and race\Salary_Data_Based_country_and_race.csv")


# ### Get Top 5 Data

# In[7]:


df.head()


# ### Know the shape of data

# In[8]:


df.shape


# ### Get bottom 5 data

# In[9]:


df.tail()


# ### Describe the dataset

# In[10]:


df.describe


# ### Get the Unique element from the Job Title data 

# In[12]:


df['Job Title'].unique()


# ### Get the unique element from the Education label data

# In[14]:


df['Education Level'].unique()


# ### Data cleaning

# In[15]:


df.isna()


# In[17]:


df.isna().sum()


# ### Total salary count

# In[20]:


df.Salary.value_counts()


# In[21]:


df.iloc[0,1]


# In[22]:


df.iloc[5555,5]


# ### Arrange identical data into groups 

# In[23]:


df.groupby('Salary').max()


# In[24]:


df['Race'].unique()


# In[26]:


df.groupby('Years of Experience').max()


# ### Drop the duplicate values

# In[27]:


df= df.drop_duplicates()


# ### Getting information about the dataset

# In[28]:


df.info()


# In[31]:


Salary_counts = df['Salary'].value_counts()


# ### Data visualization using matplotlib and seaborn

# In[32]:


plt.figure(figsize=(12, 8), dpi = 200)
ax = sns.barplot(x = Salary_counts.index, y = Salary_counts.values, width = 0.7)
for bars in ax.containers:
    ax.bar_label(bars)
plt.xlabel('Job Title')
plt.ylabel('Salary')
plt.title('Salary by Job Title')

plt.show()


# In[33]:


Age_counts = df['Age'].value_counts()
Age_counts


# In[35]:


plt.figure(figsize=(12,8), dpi = 200)

ax = sns.barplot(x = Age_counts.index, y = Age_counts.values, width = 0.7)

for bars in ax.containers:
    ax.bar_label(bars)
plt.xlabel('Age')
plt.ylabel('Years of Experience')
plt.title('Age by years of experience')

plt.show()


# In[36]:


Gender_counts = df['Gender'].value_counts()
Gender_counts


# In[38]:


plt.figure(figsize= (12,8), dpi = 200)
sns.histplot(df['Gender'])

plt.xlabel('Gender')
plt.ylabel('Race')
plt.title('Race by Gender')

plt.show()


# In[40]:


plt.figure(figsize= (12,8), dpi = 200)

ax = sns.scatterplot(x= 'Age', y = 'Job Title' , data = df)
for scatters in ax.containers:
    ax.scatter_label(scatters)
    
plt.xlabel('Age')
plt.ylabel('Job Title')
plt.title('Job Title by Age')

plt.show()


# In[41]:


plt.figure(figsize = (12,8), dpi = 200)

ax = sns.countplot(data = df, x = 'Years of Experience')
ax.bar_label(ax.containers[0])
plt.title('salary by year of experience')

plt.show()


# In[ ]:




