import re

def funfc(DIC,FCL,RES):
    FILEFC = open(FCL,"r")

    FRS = re.compile(".+[^\n|^\r]")     ## Expresion Regular que reconoce Cualquier Frase
    FRN = re.compile("[0-9]+")          ## Expresion Regular que reconoce Todos los Numeros
    ac = 0                              ## Acumulardor de Frases Claves
    nc = 0                              ## Numero de Frases Claves
    
    AOR = []                            ## Lista a Ordenar
    
    ## Aqui se utiliza la estructura de datos Lista,
    ## para guardar la frase clave seguida
    ## de la cantidad de ocurrencias de esta

    ## LEE EL RESUMEN
    for LINEA in FILEFC:
        
        fg = FRS.search(LINEA).group()  ## Expresion regular que reconoce la frase Clave
        fg = "(?<=^)"+ fg +"(?=\s|$)"+"|"+"(?<=\s)"+ fg +"(?=\s|$)"
        FC = re.compile(fg)
        nc = nc + 1  ## Guarda el numero de frases Claves
        
        FILERE = open(RES,"r")
        for LINEAR in FILERE:
            if re.match("[\n|\r]",LINEAR):
                AOR.append(FRS.search(LINEA).group()+" : "+str(ac))  
                ac = 0
            else:
                ac = ac + (len(FC.findall(LINEAR)))

    ## se divide la longitud de la lista solucion anterior entre la cantidad de Frases Clave
    NR = len(AOR)/nc

    ## Ordena en el orden correcto para la impresion
    REX1 = "\S{1}"          ## Expresion Regular que separa las letras
    LK = re.compile(REX1)   ## Se compila la Expresion Regular


    fin = 0                 ## Variable para iterar en la cantidad de resumenes
    while fin < NR:        
        i=fin
        
        ## Se utiliza BubbleSort, para el ordenamiento de la lista
        
        while i<len(AOR):
            j=i+NR
            C = i
            while j<len(AOR):
                if int(FRN.search(AOR[C]).group())<int(FRN.search(AOR[j]).group()):
                    C = j
                elif int(FRN.search(AOR[C]).group()) == int(FRN.search(AOR[j]).group()):
                    ##rompo empate por orden lexicografico
                    ii = len(LK.findall(AOR[C]))
                    jj = len(LK.findall(AOR[j]))

                    p = ii-jj
                    if p<0:
                        p = ii
                    else:
                        p = jj

                    k = 0
                    bool =True
                    while (k < p) and bool:
                        if str(LK.search(AOR[C],k).group())>str(LK.search(AOR[j],k).group()):
                            C = j
                            bool = False
                        elif str(LK.search(AOR[C],k).group())<str(LK.search(AOR[j],k).group()):
                            bool = False
                        else:
                            k = k + 1

                    if bool:
                        if p == jj:
                            C = j

                j=j+NR

            AUX = AOR[i]
            AOR[i]=AOR[C]
            AOR[C]=AUX
            i= i + NR

        fin = fin + 1     ## Avansamos al siguiente Resumen
        

    ## Imprime
    k=0
    i=0
    j=0
    FILERE = open(RES,"r")
    for LINEA in FILERE:
        if i==0:
            print FRS.search(LINEA).group()
            i=i+1
        if re.match("\n",LINEA):
            j = k
            while j < len(AOR):
                print AOR[j]
                j=j+NR
            i=0
            k=k+1