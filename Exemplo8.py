#Exemplo 8: Exemplo de jogo

from BaseParaJogo import *

CORFUNDOJANELA = (89, 106, 108)
LARGURAJANELA = 896
ALTURAJANELA = 480
FPS = 60
ICONE = "Recursos/Imagens/python-logo.png"
#Direção do movimento
PARADO = 0
CIMA = 1
BAIXO = 2
ESQUERDA = 3
DIREITA = 4

MAPA = [[1,1,2,2,1,1,1,1,1,1],
        [1,0,1,0,0,0,0,0,0,1],
        [1,3,1,0,0,0,0,3,0,1],
        [1,3,0,0,0,0,0,0,0,1],
        [1,3,2,0,0,1,0,0,0,1],
        [1,3,2,0,0,0,0,0,0,1],
        [1,3,1,0,0,1,0,3,0,1],
        [1,3,1,0,0,1,0,0,0,1],
        [1,3,0,0,0,1,0,0,0,0],
        [1,1,1,1,1,1,1,2,2,2],
       ]

DESLOCAMENTO_ESQ = 288
DESLOCAMENTO_BAIXO = 90

def desenhaMapa(bloco1, bloco2, fundo, moeda):
    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c] == 0:
                desenhaFigura(fundo, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)
            elif MAPA[l][c] == 1:
                desenhaFigura(bloco1, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)
            elif MAPA[l][c] == 2:
                desenhaFigura(bloco2, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)
            elif MAPA[l][c] == 3:
                desenhaFigura(fundo, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)
                desenhaFigura(moeda, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Oitavo Exemplo", CORFUNDOJANELA, ICONE)

    bloco1 = carregaFigura("Recursos/Imagens/Exemplo8/bloco1.png", (32, 32))
    bloco2 = carregaFigura("Recursos/Imagens/Exemplo8/bloco2.png", (32, 32))
    fundo = carregaFigura("Recursos/Imagens/Exemplo8/fundo.png", (32, 32))
    moeda = carregaFigura("Recursos/Imagens/Exemplo8/moeda.png", (32, 32))

    jogador_baixo = [carregaFigura("Recursos/Imagens/Exemplo8/jogador_baixo1.png", (32, 32)),
                     carregaFigura("Recursos/Imagens/Exemplo8/jogador_baixo2.png", (32, 32)),
                     carregaFigura("Recursos/Imagens/Exemplo8/jogador_baixo3.png", (32, 32))]
    jogador_cima = [carregaFigura("Recursos/Imagens/Exemplo8/jogador_cima1.png", (32, 32)),
                     carregaFigura("Recursos/Imagens/Exemplo8/jogador_cima2.png", (32, 32)),
                     carregaFigura("Recursos/Imagens/Exemplo8/jogador_cima3.png", (32, 32))]
    jogador_esquerda = [carregaFigura("Recursos/Imagens/Exemplo8/jogador_esquerda1.png", (32, 32)),
                     carregaFigura("Recursos/Imagens/Exemplo8/jogador_esquerda2.png", (32, 32)),
                     carregaFigura("Recursos/Imagens/Exemplo8/jogador_esquerda3.png", (32, 32))]
    jogador_direita = [carregaFigura("Recursos/Imagens/Exemplo8/jogador_direita1.png", (32, 32)),
                     carregaFigura("Recursos/Imagens/Exemplo8/jogador_direita2.png", (32, 32)),
                     carregaFigura("Recursos/Imagens/Exemplo8/jogador_direita3.png", (32, 32))]
    imagemJogador = jogador_baixo
    frameJogador = 0
    direcao = PARADO
    yJogador = 122
    xJogador = 320
    velocidadeAnimacaoJogador = 0.1
    moedas = 0
    while True:      
        
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi pressionada
        #Se sim, atualiza a posição do retângulo
        if teclaPressionada(K_UP):
            direcao = CIMA
        elif teclaPressionada(K_DOWN):
            direcao = BAIXO
        elif teclaPressionada(K_LEFT):
            direcao = ESQUERDA
        elif teclaPressionada(K_RIGHT):
            direcao = DIREITA

        if direcao == CIMA:
            yJogador -= 2
            imagemJogador = jogador_cima
        elif direcao == BAIXO:
            yJogador += 2
            imagemJogador = jogador_baixo
        elif direcao == ESQUERDA:
            xJogador -= 2
            imagemJogador = jogador_esquerda
        elif direcao == DIREITA:
            xJogador += 2
            imagemJogador = jogador_direita
        direcao = PARADO

        #Desenha o mapa
        desenhaMapa(bloco1, bloco2, fundo, moeda)

        #Desenha o jogador
        frameJogador += velocidadeAnimacaoJogador
        if frameJogador >= 3:
            frameJogador = 0
        desenhaFigura(imagemJogador[int(frameJogador)], xJogador, yJogador)

        #Verifica se a posição possui moeda
        l = (yJogador - DESLOCAMENTO_BAIXO) // 32
        c = (xJogador - DESLOCAMENTO_ESQ) // 32
        print(l, c)
        if 0 <= l < 10 and 0 <= c < 10:
            if MAPA[l][c] == 3:
                MAPA[l][c] = 0
                moedas += 1

        #Desenha pontuação
        desenhaTexto(f"Pontos: {moedas:2d}", 400, 50, 15, (0, 0, 0), "Recursos/Fontes/FiraCode-Regular.ttf")

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

