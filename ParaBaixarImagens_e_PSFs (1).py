#!/usr/bin/env python
# coding: utf-8

# In[22]:


#################################################################################################
################## Cria tabela para fazer download das imagens e PSFs da HSC ####################
#################################################################################################
###################################### Carol Santiago ###########################################
#################################################################################################

import pandas as pd

coord = pd.read_csv("/home/carol/IC/InitialSamples/SF.csv")

coord = coord.drop(['z','sigma_e','logM','concentracao','class','i', 'logSFR'], axis='columns') #Exclui as colunas que eu nao preciso!

coord["rerun"]    = len(coord)*["pdr3_wide"] #Adiciona a coluna "rerun"
coord["filter"]   = len(coord)*["HSC-G"]
coord["image"]    = len(coord)*["true"]
coord["mask"]     = len(coord)*["true"]
coord["variance"] = len(coord)*["true"]
coord["type"]     = len(coord)*["coadd"]

coord["sw"] = (coord["petroR90_r"] * 5)/2    # (petroRad_r * 5)/2
coord["sh"] = (coord["petroR90_r"] * 5)/2
coord["sw"] = coord["sw"].astype(int).astype(str) + "asec"  #Converte para tipo inteiro, depois para string e adiciona "asec"
coord["sh"] = coord["sh"].astype(int).astype(str) + "asec"

coord = coord.drop(['petroR90_r'], axis='columns')          #Exclui a coluna 'petroR90_r'

coord.to_csv('coordSF.csv', sep = " ", index=False)         #Salva em .csv
coord


# In[ ]:




