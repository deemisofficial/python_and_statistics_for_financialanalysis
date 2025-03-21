
# coding: utf-8

# ## Build a simple trading strategy 

# In[31]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# ### 1. Munging the stock data and add two columns - MA10 and MA50

# In[32]:


#import FB's stock data, add two columns - MA10 and MA50
#use dropna to remove any "Not a Number" data
import pandas as pd
fb = pd.read_csv('../data/facebook.csv', index_col=0, parse_dates=True)
fb['MA10'] = fb['Close'].rolling(10).mean()
fb['MA50'] = fb['Close'].rolling(50).mean()
fb = fb.dropna()
fb.head()
print(fb.head())


# In[ ]:





# ### 2. Add "Shares" column to make decisions base on the strategy 

# In[33]:


#Add a new column "Shares", if MA10>MA50, denote as 1 (long one share of stock), otherwise, denote as 0 (do nothing)

fb['Shares'] = [1 if fb.loc[ei, 'MA10']>fb.loc[ei, 'MA50'] else 0 for ei in fb.index]
print(fb.head())


# In[34]:


#Add a new column "Profit" using List Comprehension, for any rows in fb, if Shares=1, the profit is calculated as the close price of 
#tomorrow - the close price of today. Otherwise the profit is 0.

#Plot a graph to show the Profit/Loss
import matplotlib.pyplot as plt
fb['Close1'] = fb['Close'].shift(-1)
fb['Profit'] = [fb.loc[ei, 'Close1'] - fb.loc[ei, 'Close'] if fb.loc[ei, 'Shares']==1 else 0 for ei in fb.index]
fb['Profit'].plot()
plt.axhline(y=0, color='red')
plt.show()
print(fb.head())


# ### 3. Use .cumsum() to display our model's performance if we follow the strategy 

# In[35]:


#Use .cumsum() to calculate the accumulated wealth over the period

fb['wealth'] = fb['Profit'].cumsum()
fb.tail()


# In[36]:


#plot the wealth to show the growth of profit over the period

fb['wealth'].plot()
plt.title('Total money you win is {}'.format(fb.loc[fb.index[-2],'wealth']))


# ## You can create your own simple trading strategy by copying the codes above and modify the codes accordingly using the data of Microsoft (microsoft.csv).

# In[37]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[38]:


#import MS's stock data, add two columns - MA10 and MA50
#use dropna to remove any "Not a Number" data
import pandas as pd
ms = pd.read_csv('../data/microsoft.csv', index_col=0, parse_dates=True)
ms['MA10'] = ms['Close'].rolling(10).mean()
ms['MA50'] = ms['Close'].rolling(50).mean()
ms = ms.dropna()
ms.head()
print(ms.head())


# In[39]:


#2. Add "Shares" column to make decisions base on the strategy


# In[40]:


#Add a new column "Shares", if MA10>MA50, denote as 1 (long one share of stock), otherwise, denote as 0 (do nothing)

ms['Shares'] = [1 if ms.loc[ei, 'MA10']>ms.loc[ei, 'MA50'] else 0 for ei in ms.index]
print(ms.head())


# In[41]:


#Add a new column "Profit" using List Comprehension, for any rows in ms, if Shares=1, the profit is calculated as the close price of 
#tomorrow - the close price of today. Otherwise the profit is 0.

#Plot a graph to show the Profit/Loss
import matplotlib.pyplot as plt
ms['Close1'] = ms['Close'].shift(-1)
ms['Profit'] = [ms.loc[ei, 'Close1'] - ms.loc[ei, 'Close'] if ms.loc[ei, 'Shares']==1 else 0 for ei in ms.index]
ms['Profit'].plot()
plt.axhline(y=0, color='red')
plt.show()
print(ms.head())


# In[42]:


#3. Use .cumsum() to display our model's performance if we follow the strategy


# In[43]:


#Use .cumsum() to calculate the accumulated wealth over the period

ms['wealth'] = ms['Profit'].cumsum()
ms.tail()


# In[44]:


#plot the wealth to show the growth of profit over the period

ms['wealth'].plot()
plt.title('Total money you win is {}'.format(ms.loc[ms.index[-2],'wealth']))

