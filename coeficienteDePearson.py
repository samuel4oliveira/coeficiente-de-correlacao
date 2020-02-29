def coeficiente_de_correlacao(dado1, dado2):
    
    mediaX = 0.0
    mediaY = 0.0
    for i in range(len(dado1)):
        
        mediaX += float(dado1[i] / len(dado1))
        mediaY += float(dado2[i] / len(dado2))
    resultado = 0.0
    for i in range(len(dado1)):
        resultado += (dado1[i] - mediaX) * (dado2[i] - mediaY)
        resultado /= ((dado1[i] - mediaX)**2 * (dado2[i] - mediaY)**2) ** (1/2)
    return resultado