import re

def funpop(ED):
    
    ## Archivo Diccionario
    
    FILE = open(ED,"r")  ## Abre el Archivo

    EXPREPAL = "(\w+\S*)"               ## esta es la Expresion Regular Palabra
    EXPREORA = "(\.{1}\s+|\.$)"         ## esta es la Expresion Regular Oraciones
    EXPREPAR = "(\.{1}[\n|\r]+|\.$)"    ## esta es la Expresion Regular Parrafos
    EXPRENULi= "\n|\r"                  ## esta es la Expresion Regular para nueva Linea

    CPL = re.compile(EXPREPAL)
    COA = re.compile(EXPREORA)
    CPR = re.compile(EXPREPAR)
    CNLi= re.compile(EXPRENULi)

    ## mientras existan resumenes
    ## si es la primera linea entonces => print LINEA
    ## cuenta palabras, cuenta oraciones, cuenta parrafos
    ## imprime los resultados
    ## Avansa al siguiente resumen

    ## Acumuladores
    A = 0
    B = 0
    C = 0

    i=0
    for LINEA in FILE:
        
        if i==0:
            print LINEA, ## Primera Linea
            i = i+1
        
        A = A + len(CPL.findall(LINEA)) ## Acumulador de Palabras
        B = B + len(COA.findall(LINEA)) ## Acumulador de Oraciones
        C = C + len(CPR.findall(LINEA)) ## Acumulador de Parrafos

        if CNLi.match(LINEA):
            ## Imprime estadisticas por pantalla
            print "# Palabras: " ,
            print A
            print "# Oraciones: ",
            print B
            print "# Parrafos: ",
            print C

            A=0
            B=0
            C=0
            i=0
