#!/usr/bin/env python
# coding: utf-8

#################################################################################################
##################################### Imfit - MakeImage #########################################
#################################################################################################
################################## Santiago-Menezes, A. C. ######################################
#################################################################################################

import subprocess
 
# Makeimage
# Filtro R
for i in range(2, 60):
    nome_fits = f"{i}r.fits"
    nome_txt = f"{i}r.txt"
    #nome_mascara = f"{i}_MASCARA_r.fits"
    #nome_psf = f"{i}psfR.fits"
    #nome_noise = f"{i}r.fits[3]"
    #nome_modelo = f"{i}r_mod.fits"
    #nome_residual = f"{i}R_res.fits"
    nome_flux = f"{i}r_fluxos.txt"
    nome_params = f"{i}R_bestfit_parameters_imfit.dat"

    
    comando = f"./makeimage {nome_params} --refimage {nome_fits}[1] --save-fluxes {nome_flux}"
    #comando = f"./imfit ../GV/{nome_fits}[1] --config ../GV/{nome_txt} --mask=../GV/{nome_mascara}[1] --psf ../GV/{nome_psf} --noise ../GV/{nome_noise} --save-model=../GV/{nome_modelo} --save-residual=../GV/{nome_residual} --save-params ../GV/{nome_params} --errors-are-variances --nm"

    subprocess.run(comando, shell=True)

