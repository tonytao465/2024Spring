#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


transac_data = pd.read_csv("C://Users//Tony Tao//Downloads//cust_data.csv")


cust_data = pd.read_csv('C://Users//Tony Tao//Downloads//transaction_data.csv')


# In[3]:


transac_data


# In[4]:


cust_data


# In[108]:


df = pd.merge(transac_data, cust_data, on="Customer ID", how="left")



# In[111]:


df


# In[38]:


from datetime import timedelta


# In[110]:


df['Order Date'] = pd.to_datetime(df['Order Date'])

# Set the treatment date
treatment_date = pd.to_datetime('2019-03-02')

# Create a new column 'Profit 60 days before treatment'
df['Profit 60 days before treatment'] = df.loc[(df['Order Date'] >= treatment_date - timedelta(days=60)) & 
                                                (df['Order Date'] < treatment_date)] \
                                            .groupby('Customer ID')['Profit'].transform('sum')

# Create a new column 'Profit 60 days after treatment'
df['Profit 60 days after treatment'] = df.loc[(df['Order Date'] >= treatment_date) & 
                                               (df['Order Date'] < treatment_date + timedelta(days=60))] \
                                            .groupby('Customer ID')['Profit'].transform('sum')



# In[ ]:





# In[122]:


max_profit_before = df.groupby('Customer ID').agg({
    'State': 'first',
    'Treatment Group': 'first',
    'Profit 60 days before treatment': 'max',
    'Profit 60 days after treatment': 'max'
})

# Reset the index for a cleaner output
max_profit_before = max_profit_before.reset_index()

# Rename columns for clarity
max_profit_before.columns = ['Customer ID', 'State', 'Treatment Group', 'Profit 60 days before treatment', 'Profit 60 days after treatment']

# Display the result
print(max_profit_before)


# In[ ]:





# In[ ]:





# In[ ]:





# In[132]:


mean_before = max_profit_before['Profit 60 days before treatment'].sum()/12000
std_before = max_profit_before['Profit 60 days before treatment'].std()


mean_after = max_profit_before['Profit 60 days after treatment'].sum()/12000
std_after = max_profit_before['Profit 60 days after treatment'].std()

# Display the results
print("Mean Profit 60 days before treatment:", mean_before)
print("Standard Deviation Profit 60 days before treatment:", std_before)
print("\nMean Profit 60 days after treatment:", mean_after)
print("Standard Deviation Profit 60 days after treatment:", std_after)


# In[ ]:





# In[ ]:





# In[129]:


print(max_profit_before)


# In[ ]:




