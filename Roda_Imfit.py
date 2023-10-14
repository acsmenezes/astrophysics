#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#################################################################################################
########################################## Roda Imfit ###########################################
#################################################################################################
################################## Santiago-Menezes, A. C. ######################################
#################################################################################################



import subprocess

for i in range(2, 60):
    nome_fits = f"{i}r.fits"
    nome_txt = f"{i}r.txt"
    nome_mascara = f"{i}_MASCARA_r.fits"
    nome_psf = f"{i}psfR.fits"
    nome_noise = f"{i}r.fits[3]"
    nome_modelo = f"{i}r_mod.fits"
    nome_residual = f"{i}R_res.fits"
    nome_params = f"{i}R_bestfit_parameters_imfit.dat"

    comando = f"./imfit ../SF_morfo/{nome_fits}[1] --config ../SF_morfo/{nome_txt} --mask=../SF_morfo/{nome_mascara}[1] --psf ../SF_morfo/{nome_psf} --noise ../SF_morfo/{nome_noise} --save-model=../SF_morfo/{nome_modelo} --save-residual=../SF_morfo/{nome_residual} --save-params ../SF_morfo/{nome_params} --errors-are-variances --nm"

    subprocess.run(comando, shell=True)

