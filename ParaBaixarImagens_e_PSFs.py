#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

coord = pd.read_csv("/home/carol/IC/InitialSamples/SF.csv")

coord = coord.drop(['z','sigma_e','logM','logSFR','concentracao','class','i'], axis='columns') #exclui as colunas que eu nao preciso!

coord["rerun"] = 58*["pdr3_wide"] #adiciona a coluna "rerun"
coord["filter"] = 58*["HSC-G"]
coord["image"] = 58*["true"]
coord["mask"] = 58*["true"]
coord["variance"] = 58*["true"]
coord["type"] = 58*["coadd"]

coord["sw"] = (coord["petroR90_r"] * 5)/2 # (petroRad_r * 5)/2
coord["sh"] = (coord["petroR90_r"] * 5)/2

coord = coord.drop(['petroR90_r'], axis='columns')

coord.to_csv('coordSF.csv', sep = ",")


# In[8]:


coord_G = pd.read_csv("/home/carol/IC/InitialSamples/coordSF_G.csv")

coord_G = coord_G.drop(['logSFR'], axis='columns')

coord_G.to_csv('coordSF__G.csv', sep = " ")


# In[ ]:




