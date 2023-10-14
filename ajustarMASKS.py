#!/usr/bin/env python
# coding: utf-8

#################################################################################################
################################### Ajustes nas máscaras do SE ##################################
#################################################################################################
################################## Santiago-Menezes, A. C. ######################################
#################################################################################################

from astropy.io import fits
import numpy as np

hdulist = fits.open('52r_mask.fits')  #Abre o arquivo .fits usando a função 'fits.open()'

hdulist.info()                   #Verifica as extensões disponíveis usando o método 'info()'

mask = hdulist[1].data          #Acessa os dados das extensões 1

hdu_mask = fits.ImageHDU(data=mask)  #Cria uma nova extensão pra salvar a divisão

hdulist[1] = hdu_mask              #Salvei na extensão 1


#Exclui o que eu não quero da máscara

values_to_replace = [3]   #Valores que quero excluir

idx = np.where(np.isin(mask, values_to_replace))
mask[idx] = 0                                      #Tudo que tiver valores iguais aos escolhidos, ele substitui por 0, ou seja, fica preto

hdulist.writeto('52r_mask.fits', overwrite=True) #Salva em um novo .fits!


