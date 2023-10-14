#!/usr/bin/env python
# coding: utf-8

#################################################################################################
#################################### Máscaras Sinal-Ruído #######################################
#################################################################################################
################################### Santiago-Menezes, A. C. #####################################
#################################################################################################

from astropy.io import fits
import numpy as np

hdulist = fits.open('53g.fits')  #Abre o arquivo .fits usando a função 'fits.open()'

hdulist.info()                   #Verifica as extensões disponíveis usando o método 'info()'

sinal = hdulist[1].data          #Acessa os dados das extensões 1
ruido = hdulist[3].data          #Acessa os dados das extensões 3

sr = sinal / ruido               #Faz a divisão das extensões

hdu_sr = fits.ImageHDU(data=sr)  #Cria uma nova extensão pra salvar a divisão

hdulist[1] = hdu_sr              #Salvei na extensão 1


#Criando uma máscara para o Sinal-Ruído
idx = np.where(sr<3)
sr[idx] = 1                 #Tudo que tiver valores menores que 3, ele substitui por 1, ou seja, fica branco

idx = np.where(sr>=3)
sr[idx] = 0                 #Tudo que tiver valores maiores ou iguais a 3, ele substitui por 0, ou seja, fica preto

hdulist.writeto('53g_sinalruido.fits', overwrite=True) #Salva em um novo .fits!


#Somando o Sinal-Ruído com a Máscara do SExtractor
maskSElist = fits.open('53_mask.fits')

maskSE = maskSElist[1].data               #Acessa os dados da extensão 1

mascara = maskSE + sr                     #Faz a soma das máscaras, criando uma nova!

hdu_mascara = fits.ImageHDU(data=mascara) #Cria uma nova extensão pra salvar a soma

maskSElist[1] = hdu_mascara               #Salvei na extensão 1

maskSElist.writeto('53_MASCARA.fits', overwrite=True) #Salvei em um novo .fits!

#Essa máscara que foi resultado da soma, é a que usa no IMFIT!!!!





# REPETINDO PARA 58 ARQUIVOS DE UMA VEZ!

for i in range(2, 60):
    filename = f"{i}r.fits"          # Gera o nome do arquivo baseado no número do loop
    
    hdulist = fits.open(filename)    # Abre o arquivo .fits usando a função 'fits.open()'
    
    hdulist.info()                   # Verifica as extensões disponíveis usando o método 'info()'
    
    sinal = hdulist[1].data          # Acessa os dados das extensões 1
    ruido = hdulist[3].data          # Acessa os dados das extensões 3
    
    sr = sinal / ruido               # Faz a divisão das extensões
    
    hdu_sr = fits.ImageHDU(data=sr)  # Cria uma nova extensão pra salvar a divisão
    
    hdulist[1] = hdu_sr              # Salva na extensão 1
    
    # Criando uma máscara para o Sinal-Ruído
    idx = np.where(sr < 3)
    sr[idx] = 1                 # Tudo que tiver valores menores que 3, ele substitui por 1, ou seja, fica branco
    
    idx = np.where(sr >= 3)
    sr[idx] = 0                 # Tudo que tiver valores maiores ou iguais a 3, ele substitui por 0, ou seja, fica preto
    
    new_filename_sr = f"{i}r_sinalruido.fits"
    hdulist.writeto(new_filename_sr, overwrite=True)  # Salva em um novo .fits!
    
    # Somando o Sinal-Ruído com a Máscara do SExtractor
    maskSElist = fits.open(f"{i}_mask.fits")
    
    maskSE = maskSElist[1].data               # Acessa os dados da extensão 1
    
    mascara = maskSE + sr                     # Faz a soma das máscaras, criando uma nova!
    
    hdu_mascara = fits.ImageHDU(data=mascara) # Cria uma nova extensão pra salvar a soma
    
    new_filename_mascara = f"{i}_MASCARA_r.fits"
    maskSElist[1] = hdu_mascara               # Salva na extensão 1
    
    maskSElist.writeto(new_filename_mascara, overwrite=True)  # Salva em um novo .fits!

