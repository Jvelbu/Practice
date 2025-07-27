#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.datasets import load_boston

# Load the Boston dataset
boston_dataset = load_boston()

# Create a DataFrame from the dataset's data and feature names
boston = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)

# Add the 'MEDV' (Median value of owner-occupied homes) column to the DataFrame
boston['MEDV'] = pd.Series(boston_dataset.target)

# Display the first few rows of the DataFrame
boston.head()


# In[2]:


{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "FinalExam.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "eBBlbpbC34DF"
      },
      "outputs": [],
      "source": [
        "# Let's import the relevant Python packages here\n",
        "# Feel free to import any other packages for this project\n",
        "\n",
        "#Data Wrangling\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "\n",
        "#Plotting\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "%matplotlib inline"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EmmKwHid34DQ"
      },
      "source": [
        "Let’s turn to the Boston housing dataset, which contains the following variables from 506 different towns in Boston collected by the US Census Service:\n",
        "\n",
        "|Column |Description|\n",
        "|:-|:-|\n",
        "|CRIM | per capita crime rate by town|\n",
        "|ZN | proportion of residential land zoned for lots over 25,000 sq.ft|\n",
        "|INDUS | proportion of non-retail business acres per town|\n",
        "|CHAS | Charles River dummy variable (1 if tract bounds river; 0 otherwise)|\n",
        "|NOX | nitric oxides concentration (parts per 10 million)|\n",
        "|RM | average number of rooms per dwelling|\n",
        "|AGE | proportion of owner-occupied units built prior to 1940|\n",
        "|DIS | weighted distances to five Boston employment centres|\n",
        "|RAD | index of accessibility to radial highways|\n",
        "|TAX | full-value property-tax rate per \\$10,000|\n",
        "|PTRATIO | pupil-teacher ratio by town|\n",
        "|B | $1000(B_k - 0.63)^2$ where $B_k$ is the proportion of African Americans by town|\n",
        "|LSTAT | \\% lower status of the population|\n",
        "|MEDV | Median value of owner-occupied homes in \\$1000's|"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "yHIkcK1t34DR"
      },
      "source":
        from sklearn.datasets import load_boston

# Load the Boston dataset
boston_dataset = load_boston()

# Create a DataFrame from the dataset's data and feature names
boston = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)

# Add the 'MEDV' (Median value of owner-occupied homes) column to the DataFrame
boston['MEDV'] = pd.Series(boston_dataset.target)

# Display the first few rows of the DataFrame
boston.head()


# In[4]:


#1
from sklearn.datasets import load_boston
import pandas as pd
# Load the Boston dataset
boston_dataset = load_boston()

# Create a DataFrame from the dataset's data and feature names
boston = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)

# Add the 'MEDV' (Median value of owner-occupied homes) column to the DataFrame
boston['MEDV'] = pd.Series(boston_dataset.target)

# Display the first few rows of the DataFrame
boston.head()


# In[7]:


# 2)Select a subset of predictors for pairwise scatterplots
selected_predictors = ['CRIM', 'RM', 'AGE', 'DIS', 'MEDV']
import matplotlib.pyplot as plt
import seaborn as sns
# Create pairwise scatterplots using matplotlib
plt.figure(figsize=(12, 8))
sns.set(style='ticks')
sns.pairplot(boston[selected_predictors])
plt.suptitle("Pairwise Scatterplots of Selected Predictors", y=1.02)
plt.show()


# In[8]:


# 3)Calculate correlation coefficients between CRIM and other predictors
correlation_with_CRIM = boston.corr()['CRIM'].sort_values(ascending=False)

# Print the correlation coefficients
print(correlation_with_CRIM)

# Get the predictor with the highest correlation with CRIM (excluding CRIM itself)
highest_correlation_predictor = correlation_with_CRIM.index[1]
print("Predictor with highest correlation to CRIM (besides CRIM itself):", highest_correlation_predictor)


# In[9]:


# 4)Calculate the range of each predictor
predictor_ranges = boston.describe().loc[['min', 'max']]

# Identify the town number with the highest crime rate
town_highest_crime = boston[boston['CRIM'] == boston['CRIM'].max()]['CRIM']
town_highest_crime_number = town_highest_crime.index[0]

# Identify the town number with the lowest tax rate
town_lowest_tax = boston[boston['TAX'] == boston['TAX'].min()]['TAX']
town_lowest_tax_number = town_lowest_tax.index[0]

# Print the results
print("Range of predictors:")
print(predictor_ranges)
print("\nTown number with the highest crime rate:", town_highest_crime_number)
print("Town number with the lowest tax rate:", town_lowest_tax_number)


# In[11]:


# 5)Count the number of towns bound to the Charles River
charles = boston[boston['CHAS'] == 1].shape[0]

# Print the result
print("Number of towns bound to the Charles River:", charles)


# In[14]:


# 6)Calculate the median pupil-teacher ratio
med_pt = boston['PTRATIO'].median()

# Print the result
print("Median pupil-teacher ratio:", med_pt)
  


# In[15]:


#7) Find the index of the town with the lowest MEDV
min_medv = boston['MEDV'].idxmin()

# Print the index
print("Index of town with lowest MEDV:", min_medv)

# Display the data for that suburb
print("\nData for suburb with lowest MEDV:")
print(boston.loc[min_medv])


# In[16]:


# 8)Find the number of suburbs with more than eight rooms per dwelling
num_rooms = len(boston[boston['RM'] > 8])

# Print the number of suburbs
print("Number of suburbs with more than eight rooms per dwelling:", num_rooms)


# In[ ]:




