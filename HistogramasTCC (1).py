#!/usr/bin/env python
# coding: utf-8

# In[17]:


#################################################################################################
#################################### Teste KS + Histogramas #####################################
#################################################################################################
################################## Santiago-Menezes, A. C. ######################################
#################################################################################################


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Carregue suas três tabelas (substitua 'tabela1.csv', 'tabela2.csv' e 'tabela3.csv' pelos seus arquivos)
tabela1 = pd.read_csv('GV_tabela_COMPLETASSAAAAAsuperFINAL_colunasReduzidas_MassaReduct.csv')
tabela2 = pd.read_csv('SF_tabela_COMPLETASSAAAAAsuperFINAL_colunasReduzidas_MassaReduct.csv')
tabela3 = pd.read_csv('SFmorfo_tabela_COMPLETASSAAAAAsuperFINAL_colunasReduzidas_MassaReduct.csv')

# Especifique a coluna que você deseja usar para o histograma
#coluna_alvo = 'n_bojo'
#coluna_alvo = 'r_e_bojo_kpc'
#coluna_alvo = 'r_e_disco_kpc'
coluna_alvo = 'FraÃ§Ã£o'

# Combine os dados das três tabelas em um único array
dados_combinados = [tabela1[coluna_alvo], tabela2[coluna_alvo], tabela3[coluna_alvo]]

# Calcule os limites dos bins com base nos dados combinados
min_valor = min([min(dados) for dados in dados_combinados])
max_valor = max([max(dados) for dados in dados_combinados])
largura_bin = (max_valor - min_valor) / 10  #Divide o intervalo em 10 bins para cada tabela
bins = np.arange(min_valor, max_valor + largura_bin, largura_bin)

# p-value
ksstats, pvalue1 = stats.ks_2samp(tabela1[coluna_alvo], tabela2[coluna_alvo], mode = "asymp")
#print(pvalue1)
ksstats, pvalue2 = stats.ks_2samp(tabela1[coluna_alvo], tabela3[coluna_alvo], mode = "asymp")
#print(pvalue2)

# Crie o histograma para cada tabela
#plt.figure(figsize=(10, 6))  # Defina o tamanho da figura
plt.hist(tabela1[coluna_alvo], bins=bins, alpha=1, histtype='step', linewidth=3, label='Green Valley', color='green', density=True)
plt.hist(tabela2[coluna_alvo], bins=bins, alpha=1, histtype='step', linewidth=2, label='SF', hatch='\\', density=True)
plt.hist(tabela3[coluna_alvo], bins=bins, alpha=1, histtype='step', linewidth=1.5, label='SFmorfo', hatch='/', density=True)


#plt.xlabel('n')
#plt.title('Índice de Sérsic - Bojo')
plt.ylabel('Densidade')
#plt.xlabel('$r_e$ (kpc)')
#plt.title('Raio efetivo - Bojo')
#plt.xlabel('$r_e$')
#plt.title('Raio efetivo - Disco')
plt.xlabel('B/T')
plt.title('Fração de luz no bojo')

plt.text(0.75, 3.3, f'p-value = {pvalue1:.3f} (GV e SF)', ha='center', va='bottom')
plt.text(0.75, 3.0, f'p-value = {pvalue2:.3f} (GV e SFmorfo)', ha='center', va='bottom')
plt.legend()

#plt.savefig('histTCC_pvalue_n_bojo.png')
#plt.savefig('histTCC_pvalue_Re_bojo.png')
#plt.savefig('histTCC_pvalue_Re_disco.png')
plt.savefig('histTCC_pvalue_fracaoDeLuz_bojo.png')
plt.show()


# In[ ]:





# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

# Carregue suas três tabelas (substitua 'tabela1.csv', 'tabela2.csv' e 'tabela3.csv' pelos seus arquivos)
tabela1 = pd.read_csv('GV_BTreduct.csv')
tabela2 = pd.read_csv('SF_BTreduct.csv')
tabela3 = pd.read_csv('SFmorfo_BTreduct.csv')

# Especifique a coluna que você deseja usar para o histograma
coluna_alvo = 'n_bojo'
#coluna_alvo = 'r_e_bojo_kpc'
#coluna_alvo = 'r_e_disco_kpc'
#coluna_alvo = 'FraÃ§Ã£o'

# Combine os dados das três tabelas em um único array
dados_combinados = [tabela1[coluna_alvo], tabela2[coluna_alvo], tabela3[coluna_alvo]]

# Calcule os limites dos bins com base nos dados combinados
min_valor = min([min(dados) for dados in dados_combinados])
max_valor = max([max(dados) for dados in dados_combinados])
largura_bin = (max_valor - min_valor) / 10  #Divide o intervalo em 10 bins para cada tabela
bins = np.arange(min_valor, max_valor + largura_bin, largura_bin)

# p-value
ksstats, pvalue1 = stats.ks_2samp(tabela1[coluna_alvo], tabela2[coluna_alvo], mode = "asymp")
#print(pvalue1)
ksstats, pvalue2 = stats.ks_2samp(tabela1[coluna_alvo], tabela3[coluna_alvo], mode = "asymp")
#print(pvalue2)

# Crie o histograma para cada tabela
#plt.figure(figsize=(10, 6))  # Defina o tamanho da figura
plt.hist(tabela1[coluna_alvo], bins=bins, alpha=1, histtype='step', linewidth=3, label='Green Valley - 26 galáxias', color='green')
plt.hist(tabela2[coluna_alvo], bins=bins, alpha=1, histtype='step', linewidth=2, label='SF - 31 galáxias', hatch='\\')
plt.hist(tabela3[coluna_alvo], bins=bins, alpha=1, histtype='step', linewidth=1.5, label='SFmorfo - 21 galáxias', hatch='/')


plt.xlabel('$n_{bojo}$')
plt.ylabel('Número de galáxias')
plt.title('Índice de Sérsic - Bojo \n Galáxias com B/T < 0.3')


plt.text(6, 13, f'p-value = {pvalue1:.3f} (GV e SF)', ha='center', va='bottom')
plt.text(6, 12, f'p-value = {pvalue2:.3f} (GV e SFmorfo)', ha='center', va='bottom')
plt.legend()

#plt.savefig('histTCC_pvalue_n_bojo_BTreduct.png')

plt.show()


# In[ ]:




