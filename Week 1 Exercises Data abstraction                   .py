#!/usr/bin/env python
# coding: utf-8

# In[107]:


#import required libraries
from pyforest import *
import plotly.express as px
import pandas as pd


# In[108]:


pd.set_option('display.float_format', lambda x: '%.5f' % x)


# In[50]:


#read excel workbook into pandas dataframe
data=pd.read_excel('D:\\CS5346\\New folder\\Assessment Docs (Exercises, Assig\Weekly Exercises\\Aid Data.xlsx',usecols="A:G",skiprows=[0])


# In[51]:


#drop all the NA values
data=data.dropna()


# In[52]:


#check the shape of the datframe
data.shape


# In[53]:


#get max of aiddata_id
data['aiddata_id'].max()


# In[54]:


#get min of aiddata_id
data['aiddata_id'].min()


# In[55]:


#get max of year
data['year'].max()


# In[56]:


#get min of year
data['year'].min()


# In[ ]:


#get max of commitment_amount_usd_constant
data['commitment_amount_usd_constant'].max()


# In[ ]:


#get min of commitment_amount_usd_constant
data['commitment_amount_usd_constant'].min()


# In[69]:


len(data['aiddata_id'].unique())


# In[70]:


len(data['year'].unique())


# In[71]:


len(data['commitment_amount_usd_constant'].unique())


# In[159]:


len(data['donor'].unique())


# In[160]:


len(data['recipient'].unique())


# In[164]:


len(data['coalesced_purpose_code'].unique())


# In[165]:


len(data['coalesced_purpose_name'].unique())


# In[138]:


#transform data to get commitment_amount_usd_constant by ['year','donor','recipient']
donor_data=data.groupby(['year','donor','recipient','coalesced_purpose_name'])['commitment_amount_usd_constant'].sum().reset_index()


# In[139]:


#filter the data for France
df_france=donor_data[donor_data['donor']=='France']
df_france_year=df_france.groupby(['year','donor'])['commitment_amount_usd_constant'].sum().reset_index()
df_france_recipient=df_france.groupby(['recipient','donor'])['commitment_amount_usd_constant'].sum().reset_index()
df_france_coalesced_purpose_name=df_france.groupby(['coalesced_purpose_name','donor'])['commitment_amount_usd_constant'].sum().reset_index()


# In[121]:


#plot the aid provided by year
fig = px.line(df_france_year, x="year", y="commitment_amount_usd_constant", color='donor')
fig.show()


# In[135]:


px.pie(df_france_recipient, values='commitment_amount_usd_constant', names='recipient', title='Distribution of commitment_amount_usd_constant among recipient')


# In[142]:


px.pie(df_france_coalesced_purpose_name, values='commitment_amount_usd_constant', names='coalesced_purpose_name', title='Distribution of commitment_amount_usd_constant among coalesced_purpose_name')


# In[153]:


#filter the data for France
df_peru=donor_data[donor_data['recipient']=='Peru']
df_peru_year=df_peru.groupby(['year','recipient'])['commitment_amount_usd_constant'].sum().reset_index()
df_peru_donor=df_peru.groupby(['recipient','donor'])['commitment_amount_usd_constant'].sum().reset_index()
df_peru_coalesced_purpose_name=df_peru.groupby(['coalesced_purpose_name','recipient'])['commitment_amount_usd_constant'].sum().reset_index()


# In[154]:


#plot the aid provided by year
px.line(df_peru_year, x="year", y="commitment_amount_usd_constant", color='recipient')


# In[155]:


px.pie(df_peru_donor, values='commitment_amount_usd_constant', names='donor', title='Distribution of commitment_amount_usd_constant by donor')


# In[156]:


px.pie(df_peru_coalesced_purpose_name, values='commitment_amount_usd_constant', names='coalesced_purpose_name', title='Distribution of commitment_amount_usd_constant among coalesced_purpose_name')


# In[ ]:




