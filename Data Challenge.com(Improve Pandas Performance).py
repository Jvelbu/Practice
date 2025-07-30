#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd

# === Load the datasets ===
ride_1500 = pd.read_csv('ride_1500.csv')
rider_500 = pd.read_csv('rider_500.csv')

# === Question 1 ===
# Filter riders with rating > 2.5
filtered_rider_df = rider_500[rider_500['rating'] > 2.5]

# Merge filtered riders with rides
merged_df = filtered_rider_df.merge(ride_1500, how='inner', on='rider_id')

# Calculate average fare per rider
output_df = merged_df.groupby(['rider_id', 'name', 'rating'])['fare'].mean().reset_index()
output_df.rename(columns={'fare': 'average_fare'}, inplace=True)

print("✅ Question 1: Average fare of riders with rating > 2.5")
print(output_df)

# === Question 2 ===
# Parse the datetime in 'start_time'
ride_1500['start_time'] = pd.to_datetime(ride_1500['start_time'], errors='coerce')

# Filter rides that occurred in 2022
rides_2022 = ride_1500[ride_1500['start_time'].dt.year == 2022]

# Merge with rider info
rides_2022_merged = rides_2022.merge(rider_500, how='inner', on='rider_id')

# Get rider with highest rating who rode in 2022
top_rider = rides_2022_merged[['rider_id', 'name', 'rating']].drop_duplicates()
top_rider = top_rider.sort_values(by='rating', ascending=False).head(1)

print("\n✅ Question 2: Rider with highest rating who rode in 2022")
print(top_rider)


# In[ ]:




