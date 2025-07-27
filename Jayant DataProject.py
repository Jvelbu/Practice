#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Let's import the relevant Python packages here
# Feel free to import any other packages for this project

# Data Wrangling
import numpy as np
import pandas as pd

# Plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Load the College dataset using pandas
college_data = pd.read_csv('/Users/jayantvelichety/Desktop/College.csv')


# In[4]:


# View the first few rows of the dataset
print(college_data.head())


# In[5]:


# Set the 'Names' column as the index
college_data.set_index('Names', inplace=True)


# In[6]:


# View the first few rows of the dataset with the updated index
print(college_data.head())


# In[8]:


# Display information about the dataset
college_data.info()

    


# In[9]:


# Scatter plot of enrollment vs out-of-state tuition
plt.figure(figsize=(10, 6))  # Set the figure size
plt.scatter(college_data['Enroll'], college_data['Outstate'], alpha=0.6)  # Create the scatter plot
plt.xlabel('Enrollment')  # Set the x-axis label
plt.ylabel('Out-of-State Tuition')  # Set the y-axis label
plt.title('Scatter Plot: Enrollment vs Out-of-State Tuition')  # Set the plot title
plt.show()  # Display the plot


# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
sns.histplot(college_data['Apps'], bins=200, kde=False)
plt.title('Number of Applications Histogram')
plt.xlabel('Number of Applications')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# In[11]:


college_data_copy = college_data.copy()
college_data_copy['acceptance_rate'] = college_data_copy['Accept'] / college_data_copy['Apps']
plt.figure(figsize=(10, 6))
plt.scatter(college_data_copy['Top10perc'], college_data_copy['acceptance_rate'], alpha=0.6)
plt.xlabel('Percentage of Students in Top 10% of HS')
plt.ylabel('Acceptance Rate')
plt.title('Scatter Plot: Top 10% vs Acceptance Rate')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




