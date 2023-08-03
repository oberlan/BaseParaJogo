frameJogador += velocidadeAnimacaoJogador
        if frameJogador >= 3:
            frameJogador = 0
        desenhaFigura(imagemJogador[int(frameJogador)], xJogador, yJogador)