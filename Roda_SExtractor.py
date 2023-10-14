#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#################################################################################################
################################# Máscaras SourceExtractor ######################################
#################################################################################################
################################## Santiago-Menezes, A. C. ######################################
#################################################################################################


import subprocess
import os
import fileinput
import shutil

# Diretório contendo os arquivos .fits
diretorio = "/home/carol/IC/imagens_PSFs_SamplesTCC/GV"

# Localização do executável do Source Extractor
#source_extractor_executavel = "/home/carol/IC/testeSEx/source-extractor"

# Nome do arquivo .sex original
nome_config_original = "config.sex"

# Loop através dos arquivos .fits
for i in range(2, 60):
    # Nome do arquivo .fits
    nome_fits = str(i) + "r.fits"

    # Caminho completo para o arquivo .fits
    caminho_fits = os.path.join(diretorio, nome_fits)

    # Nome do arquivo .sex modificado
    nome_config_modificado = "config_modificado.sex"

    # Copia o arquivo .sex original para o arquivo modificado
    shutil.copyfile(nome_config_original, nome_config_modificado)


    # Comando para executar o Source Extractor
    comando = ["source-extractor", caminho_fits, "-c", nome_config_modificado]

    # Modifica a linha desejada no arquivo de configuração
    with fileinput.FileInput(nome_config_modificado, inplace=True) as arquivo_config:
        for linha in arquivo_config:
            # Verifica a linha desejada
            if "CHECKIMAGE_NAME  teste.fits" in linha:
                # Modifica a linha para cada iteração do loop
                linha_alterada = linha.replace("CHECKIMAGE_NAME  teste.fits", f"CHECKIMAGE_NAME {nome_fits}mask\n")
                print(linha_alterada, end='')
            else:
                print(linha, end='')

    # Executa o comando no terminal
    subprocess.run(comando)

