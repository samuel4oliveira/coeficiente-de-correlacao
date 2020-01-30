def coeficiente_de_correlacao(x, y):

    paresConcordantes = 0
    paresDiscordantes = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if float(x[i]) < float(x[j]) and float(y[i]) < float(y[j]):
                paresConcordantes += 1
            else:
                paresDiscordantes += 1  

    resultado = paresConcordantes - paresDiscordantes
    resultado /= len(x) * (len(x) - 1) / 2
    return resultado