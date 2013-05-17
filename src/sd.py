import re

def funsd(DIC,FCL,RES):

    REXPSG = "[A-Z]+[\.|\-|_|A-Z]+"    ## Expresion Regular que reconoce las Siglas
    REXPSG = "(?<=[^|\s])"+REXPSG+"(?=\s|$)" 
    SGLS = re.compile(REXPSG)
    REXPAL = "(\w+\S*)"                ## Expresion Regular que reconoce las Palabras
    PAL  = re.compile(REXPAL)
    EXPRENULi= "\n|\r"                 ## Expresion regular que reconoce la siguiente linea
    CNLi= re.compile(EXPRENULi)

    FILDIC = open(DIC,"r") ## Abre el Diccionario
    FILFCL = open(FCL,"r") ## Abre las Frases Clave

    LIN =""  ## En LIN guarda la expresion Regular que reconoce todas las palabras conocidas

    DF = 0
    for LINEAC in FILDIC:  ## Guarda todas las palabras del Diccionario
        while PAL.search(LINEAC,DF):
            a = PAL.search(LINEAC,DF)
            DF = a.end()
            LIN = LIN + "|" + a.group()
        DF = 0

    for LINEAC in FILFCL: ## Guarda todas las palabras de las Frases Clave
        while PAL.search(LINEAC,DF): 
            a = PAL.search(LINEAC,DF)    
            DF = a.end()                 
            LIN = LIN + "|" + a.group()  
        DF = 0


    LIN = re.sub("\A[|]","",LIN)  
    LIN = "(?<=[\s|^])"+ LIN +"(?=[\s|\r|\n])"
    
    REGEXP = re.compile(LIN)


    ## Revisa en los resumenes


    s = 0       ## Contador de Siglas del resumen
    c = 0       ## Contador de palabras conocidas de la linea
    d = 0       ## Contador de palabras desconocidas del resumen
    i = 0       ## Contador de lineas del resumen
    FILRES = open(RES,"r")
    for LINEA in FILRES:
        if i==0: ## Imprime El Titulo
            print LINEA,
            i=i+1

        c = c + len (REGEXP.findall(LINEA)) ## acumula la cantidad de palabras conocidas
        d = d + len (PAL.findall(LINEA))    ## acumula la cantidad total de palabras
        s = s + len (SGLS.findall(LINEA))   ## acumula la cantidad de Siglas
        
        if CNLi.match(LINEA,0):
            ## Imprime las Estadisticas
            d = d - s - c
            print "#Siglas: ",
            print s
            print "#Desconocidas: ",
            print d
            s=0
            d=0
            c=0
            i=0


