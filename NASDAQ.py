#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


NASDAQ = pd.read_csv('/Users/jayantvelichety/Desktop/PIVOTAI/NASDAQ_daily_.csv')


# In[3]:


NASDAQ.head()


# In[4]:


NASDAQ.describe()


# In[5]:


NASDAQ.info()


# In[6]:


NASDAQ.isnull().sum()


# In[8]:


#Checking for Duplicates
NASDAQ.duplicated().sum()


# In[10]:


NASDAQ.select_dtypes(include='number').corr()


# In[11]:


corr_matrix = NASDAQ.select_dtypes(include='number').corr()


# In[12]:


# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# In[10]:


NASDAQ.corr()


# In[13]:


NASDAQ_Clean = NASDAQ.dropna(subset= ['Open', 'High', 'Low','Close','Adj Close','Volume'], how = "all")


# In[12]:


NASDAQ_Clean.corr()


# In[13]:


NASDAQ_Clean.isnull().sum()


# In[14]:


#Using Z score method
from scipy.stats import zscore
import pandas as pd

# Optional: make a clean copy
NASDAQ_Clean = NASDAQ_Clean.copy()

# Make sure 'Close' doesn't have nulls before calculating z-score
NASDAQ_Clean = NASDAQ_Clean[NASDAQ_Clean['Close'].notnull()]

# Calculate z-score correctly
NASDAQ_Clean['zscore'] = zscore(NASDAQ_Clean['Close'])

# Flag anomalies
NASDAQ_anomalies = NASDAQ_Clean[(NASDAQ_Clean['zscore'] > 1.5) | (NASDAQ_Clean['zscore'] < -1.5)]

# Display
print(NASDAQ_anomalies[['Close', 'zscore']])


# In[15]:


import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(NASDAQ_Clean['Close'], label='Close Price')
plt.scatter(NASDAQ_anomalies.index, NASDAQ_anomalies['Close'], color='red', label='Anomalies')
plt.title('NASDAQ Close Price with Z-Score Anomalies (±1.5)')
plt.legend()
plt.show()


# In[16]:


#Using Rolling Time Series
window = 14
NASDAQ_Clean['rolling_mean'] = NASDAQ_Clean['Close'].rolling(window=window).mean()
NASDAQ_Clean['rolling_std'] = NASDAQ_Clean['Close'].rolling(window=window).std()
NASDAQ_Clean['anamoly'] = abs(NASDAQ_Clean['Close']- NASDAQ_Clean['rolling_mean']) > 2 * NASDAQ_Clean['rolling_std']
NASDAQ_anomalies = NASDAQ_Clean[NASDAQ_Clean['anamoly']]


# In[17]:


print(NASDAQ_anomalies[['Close', 'rolling_mean', 'rolling_std']].head())
print(f"Total anomalies detected: {len(NASDAQ_anomalies)}")


# In[18]:


#Converting to date time and year
NASDAQ_Clean['Date'] = pd.to_datetime(NASDAQ_Clean['Date'])
NASDAQ_Clean['Year'] = NASDAQ_Clean['Date'].dt.year


# In[22]:


#Plotting for Open and clossing to understand YOY change
import matplotlib.pyplot as plt
import pandas as pd

# Make sure date is in datetime format and Year column exists
NASDAQ_Clean['Date'] = pd.to_datetime(NASDAQ_Clean['Date'])
NASDAQ_Clean['Year'] = NASDAQ_Clean['Date'].dt.year

# Drop rows with missing Open or Close values
NASDAQ_Clean = NASDAQ_Clean.dropna(subset=['Open', 'Close'])

# Group by year and calculate mean
yearly_oc = NASDAQ_Clean.groupby('Year')[['Open', 'Close']].mean()

# Plot
plt.figure(figsize=(12,6))
plt.plot(yearly_oc.index, yearly_oc['Open'], label='Open', color='red')
plt.plot(yearly_oc.index, yearly_oc['Close'], label='Close', color='green')
plt.title('Yearly Average Open and Close Prices - NASDAQ')
plt.xlabel('Year')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[23]:


#Plotting High and Low to know YOY change
# Group by Year and calculate average
yearly_hl = NASDAQ_Clean.groupby('Year')[['High', 'Low']].mean()

# Plot
plt.figure(figsize=(12,6))
plt.plot(yearly_hl.index, yearly_hl['High'], label='High', color='red')
plt.plot(yearly_hl.index, yearly_hl['Low'], label='Low', color='blue')
plt.title('Yearly Average High and Low Prices - NASDAQ')
plt.xlabel('Year')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




