def coeficiente_de_correlacao(dado1, dado2):
    
    somaX = 0.0
    somaY = 0.0
    somaXY = 0.0
    somaXQuad = 0.0
    somaYQuad = 0.0
    for i in range(len(dado1)):
        
        somaX += float(dado1[i])
        somaY += float(dado2[i])
        somaXY += float(dado1[i]) * float(dado2[i])
        somaXQuad += float(dado1[i]) ** 2
        somaYQuad += float(dado2[i]) ** 2

    #aplicando fórmula do Coeficiente de Correlação de Postos de Pearson
    resultado = somaXY - (somaX * somaY / (len(dado1)))
    resultado /= ((somaXQuad - ((somaX ** 2.0) / len(dado1))) * (somaYQuad - ((somaY ** 2.0) / len(dado1)))) ** (1/2)
    return resultado