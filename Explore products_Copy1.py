#!/usr/bin/env python
# coding: utf-8

# ## Explore products_Copy1
# 
# 
# 

# In[3]:


df_counts = df.groupby(df.Category).count()
display(df_counts)


# In[2]:


get_ipython().run_cell_magic('pyspark', '', "df = spark.read.load('abfss://files@datalakedtu9yfm.dfs.core.windows.net/product_data/products.csv', format='csv'\r\n## If\u202fheader\u202fexists\u202funcomment\u202fline\u202fbelow\r\n, header=True\r\n)\r\ndisplay(df.limit(10))\n")

