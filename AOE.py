def transposta(m):
    t=[]
    for j in range(len(m[0])):
        L=[]
        for i in range(len(m)):
            L.append(m[i][j])
        t.append(L)
    return t

def copia_matriz(m):
    c=[]
    for L in m:
        c.append(L[:])
    return c

def AOE(m):
    """Recebe uma matriz de incidencia onde as linhas sao as equacoes e as colunas as variaveis
    Retorna uma matriz no formato [[equação,variável]] ordenada e uma lista de variáveis que sobraram
    'F' significa 'final'"""
    #linhas - equacoes
    #colunas - variaveis
    e=len(m)
    v=len(m[0])
    L=[None]*e
    s=[]
    first_pos=0
    last_pos=-1
    copia=copia_matriz(m)
    mt=transposta(m)

    #enquanto tiver equacoes de incognita unica
    inc_unica=True
    while inc_unica:
        mod=0
        for i in range(e):
            n_inc=copia[i].count(1)
            if n_inc==1:
                inc=copia[i].index(1) #preferencia para a primeira variável
                L[first_pos]=[i+1,inc+1]
                first_pos+=1
                mt[inc]=[None]*len(mt[inc])
                copia=transposta(mt)
                mod+=1
        if mod==0:
            inc_unica=False
        

    #enquanto tiver equacoes
    while L.count(None)!=0:
        #enquanto tiver equacoes de variavel unitaria
        var_unit=True
        while var_unit:
            mod=0
            for j in range(v):
                freq=mt[j].count(1)
                if freq==1:
                    eq=mt[j].index(1) #preferencia para a primeira equação
                    L[last_pos]=[eq+1,j+1]
                    last_pos-=1
                    copia[eq]=[None]*len(copia[eq])
                    mt=transposta(copia)
                    mod+=1
            if mod==0:
                var_unit=False

        #se tiver equacoes (ciclo)
        if L.count(None)!=0:
            freq=[]
            for j in range(v):
                if mt[j].count(1) !=0:
                    freq.append(mt[j].count(1))
                else:
                    freq.append(v)

            var = freq.index(min(freq)) #preferencia para a primeira variável de menor frequência
            eq=mt[var].index(1) #preferencia para a primeira equação
            L[last_pos]=[eq+1,'F']
            last_pos-=1
            copia[eq]=[None]*len(copia[eq])
            mt=transposta(copia)

    #sobrando
    for i in range(1,v+1):
        if i not in transposta(L)[1]:
            s.append(i)

    return L, s

#exercicio master 3
a=[0]*14
m=[]
for i in range(14):
    m.append(a[:])

m[0][0]=1
m[0][2]=1
m[1][1]=1
m[2][2]=1
m[2][3]=1
m[3][2]=1
m[3][3]=1
m[4][3]=1
m[4][4]=1
m[4][5]=1
m[5][4]=1
m[5][5]=1
m[6][5]=1
m[6][6]=1
m[6][7]=1
m[6][8]=1
m[7][9]=1
m[8][7]=1
m[8][10]=1
m[9][7]=1
m[9][10]=1
m[10][10]=1
m[10][11]=1
m[10][12]=1
m[11][11]=1
m[11][12]=1
m[12][6]=1
m[12][11]=1
m[12][13]=1
m[13][6]=1
m[13][13]=1

a,b=AOE(m)
print("Ordenamento")
print("Eq, Var")
print("Obs: 'F' significa 'final'")
for x in a:
    print(x)
print()
print("Sobra")
print(b)
