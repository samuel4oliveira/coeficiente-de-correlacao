def coeficiente_de_correlacao(dado1, dado2):
    
    dados1 = []
    dados2 = []
    for i in range(len(dado1)):
        dados1.append(float(dado1[i]))
        dados2.append(float(dado2[i]))

    import scipy.stats as ss
    numeroDeDados = len(dados1)
    rank1 = ss.rankdata(dados1)
    rank2 = ss.rankdata(dados2)

    dQuadrado =[]
    for i in range(len(rank1)):
        dQuadrado.append(((rank1[i] - rank2[i]) **2))

    somaDQuadrado = 0.0
    for i in range(len(dQuadrado)):
        somaDQuadrado += dQuadrado[i]

    #aplicando fórmula do Coeficiente de Correlação de Postos de Spearman
    coeficienteDeCorrelacao = 1 - ((6 * somaDQuadrado) / (numeroDeDados * (numeroDeDados **2 - 1)))

    return coeficienteDeCorrelacao