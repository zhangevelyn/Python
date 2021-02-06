#!/usr/bin/env python
# coding: utf-8

# In[165]:


import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[2]:


name="anne" # Syntax -object.function_name() or function_name(object)
name.capitalize()


# In[4]:


name="boris"
name.endswith("s")


# In[11]:


import pandas as pd


# In[25]:


ls  #list all the documents


# In[61]:


pwd


# In[97]:


listings_df=pd.read_csv(r"C:\Users\JT\documents\AB_NYC_2019.csv",encoding="cp1252")


# In[98]:


listings_df.shape   #tuple,rows&columns


# In[100]:


listings_df.columns         #s in the end


# In[102]:


listings_df.dtypes          #s in the end, check to load the data correctly


# In[103]:


listings_df.head()     #first 5 rows by default


# In[104]:


listings_df.head(3)


# In[105]:


##clean the dataframe


# In[106]:


listings_df.isnull().sum()  #how many dont have a valid value


# In[115]:


columns_to_drop=['id','host_name','last_review']   #no need to know the persons name
listings_df.drop(columns_to_drop,axis="columns",inplace=True)  #removing columns,implement changes, without inplace original won't change, may result cookie


# In[108]:


listings_df.head()


# In[122]:


#let's remove 'NaN' from the reviews_per month column
listings_df.fillna({'reviews_per_months':0},inplace=True)
listings_df.head()


# In[129]:


listings_df['name']   #series


# In[130]:


listings_df[['name','neighbourhood_group','price']]   #dataframe [[]] 2 brackets


# In[131]:


#rows need index
listings_df[0:8]     #first 8 lines


# In[135]:


listings_df[0:8][['name','neighbourhood_group','price']]               #  combined both selection


# In[136]:


##boolean indexing
listings_df['price']<100


# In[137]:


listings_df[listings_df['price']<100]


# In[139]:


listings_df[listings_df['price']<10].shape


# In[141]:


##what are the 10 most reviewed listings
listings_df.nlargest(10,'number_of_reviews')


# In[143]:


##what are the NY neighbourhood groups with listing?
listings_df['neighbourhood_group'].unique()


# In[144]:


##HOW many listings per neighbourhood group?
listings_df['neighbourhood_group'].value_counts()  #automatic sort


# In[146]:


##what are the top 10 neighbourhoods with airbnb listings
listings_df['neighbourhood'].value_counts().head(10)


# In[147]:


listings_df['neighbourhood'].value_counts().head(10).plot(kind='bar')  #plot barchart with matplotlib calling .plot called directly on the dataframe


# In[148]:


# no need for value_counts() with seaborn, we can just use a countplot from seaborn library
sns.countplot(data=listings_df,x='neighbourhood_group')


# In[149]:


sns.countplot(data=listings_df,x='room_type')


# In[150]:


listings_df['neighbourhood_group'].value_counts().index


# In[151]:


order=listings_df['neighbourhood_group'].value_counts().index
sns.countplot(data=listings_df,x='neighbourhood_group',order=order)


# In[152]:


##what's the influence neighbourhood group on room type
listings_df['room_type'].unique()


# In[153]:


sns.countplot(data=listings_df,x='neighbourhood_group',hue='room_type')


# In[156]:


sns.distplot(listings_df['price'])         #distribution of the price


# In[158]:


listings_df[listings_df['price']>500].shape         #2% of the data


# In[160]:


affordable_df= listings_df[listings_df['price']<=500]
sns.distplot(affordable_df['price'])          #don't want to put integer, but put 199.5 like that 


# In[163]:


affordable_df['price'].mean()


# In[164]:


##what's the distribution of flat prices based on the neighbourhood group?
##violinplot
sns.violinplot(data=affordable_df,x="neighbourhood_group",y="price")


# In[170]:


##make the figure bigger  
#from matplotlib import pyplot as plt
plt.figure(figsize=(15,8))
sns.violinplot(data=affordable_df,x="neighbourhood_group",y="price")


# In[171]:


##can we plot the listing on a map?
affordable_df.head()      #latitude as y, longitude as x, use scatterplot


# In[177]:


affordable_df.plot(
    kind='scatter',
    x='longitude',
    y='latitude',
    c='price',
    cmap='inferno',              #colormap
    colorbar=True,
    alpha=0.8,
    figsize=(12,8))


# In[180]:


import urllib
i=urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/e/ec/Neighbourhoods_New_York_City_Map.PNG')
plt.imshow(plt.imread(i),zorder=0,extent=[-74.258,73.7,40.49,40.92])
ax=plt.gca()
affordable_df.plot(
    kind='scatter',
    x='longitude',
    y='latitude',
    c='price',
    cmap='inferno',              #colormap
    colorbar=True,
    alpha=0.8,
    figsize=(12,8))


# In[183]:


import urllib
i=urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/e/ec/Neighbourhoods_New_York_City_Map.PNG')
nyc_img=plt.imread(i)
plt.imshow(nyc_img,zorder=0,extent=[-74.258, -73.7, 40.49,40.92])
ax=plt.gca()
affordable_df.plot(
    ax=ax,                      #add
    zorder=1,                   #add
    kind='scatter',
    x='longitude',
    y='latitude',
    c='price',
    cmap='inferno',              #colormap
    colorbar=True,
    alpha=0.8,
    figsize=(12,8))


# In[ ]:




