#! /usr/bin/env python


import pop    ## Modulo que se encarga de Calcular Palabras Oraciones y Parrafos
import fc     ## Modulo que se encarga de Calcular el numero de ocurrencia de Frases Clave
import sd     ## Modulo que se encarga de Calcular el numero de Siglas y Palabras Desconocidas
import sys    

##
## En el modulo sys viene el acceso a la linea de entrada de consola, con una lista argv
##
## argv[0] El nombre del Archivo
## argv[1] El comando para la estadistica que se desea correr
## argv[2] Archivo de Diccionario
## argv[3] Archivo de Frases Clave
## argv[4] Archivo de Resumenes

if __name__ == "__main__":
    if sys.argv[1]=="-pop":  ## Palabras, Oraciones y Parrafos
        pop.funpop(sys.argv[4])
    elif sys.argv[1]=="-fc": ## Frases Clave
        fc.funfc(sys.argv[2], sys.argv[3], sys.argv[4])
    elif sys.argv[1]=="-sd": ## Palabras Desconocidas
        sd.funsd(sys.argv[2], sys.argv[3], sys.argv[4])