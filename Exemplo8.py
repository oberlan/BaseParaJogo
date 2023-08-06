#Exemplo 8: Exemplo de animação 

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
                desenhaImagem(fundo, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)
            elif MAPA[l][c] == 1:
                desenhaImagem(bloco1, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)
            elif MAPA[l][c] == 2:
                desenhaImagem(bloco2, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)
            elif MAPA[l][c] == 3:
                desenhaImagem(fundo, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)
                desenhaImagem(moeda, DESLOCAMENTO_ESQ + c*32, DESLOCAMENTO_BAIXO + l*32)

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Introdução à Programação", CORFUNDOJANELA, ICONE)

    bloco1 = carregaImagem("Recursos/Imagens/bloco1.png", (32, 32))
    bloco2 = carregaImagem("Recursos/Imagens/bloco2.png", (32, 32))
    fundo = carregaImagem("Recursos/Imagens/fundo.png", (32, 32))
    moeda = carregaImagem("Recursos/Imagens/moeda.png", (32, 32))

    jogador_baixo = [carregaImagem("Recursos/Imagens/jogador_baixo1.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_baixo2.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_baixo3.png", (32, 32))]
    jogador_cima = [carregaImagem("Recursos/Imagens/jogador_cima1.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_cima2.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_cima3.png", (32, 32))]
    jogador_esquerda = [carregaImagem("Recursos/Imagens/jogador_esquerda1.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_esquerda2.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_esquerda3.png", (32, 32))]
    jogador_direita = [carregaImagem("Recursos/Imagens/jogador_direita1.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_direita2.png", (32, 32)),
                     carregaImagem("Recursos/Imagens/jogador_direita3.png", (32, 32))]
    imagemJogador = jogador_baixo
    frameJogador = 0
    direcao = PARADO
    yJogador = 122
    xJogador = 320
    velocidadeAnimacaoJogador = 0.2
    moedas = 0
    while True:      
        
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição do retângulo
        caminhando = True
        if teclaPressionada(K_UP):
            direcao = CIMA
        elif teclaPressionada(K_DOWN):
            direcao = BAIXO
        elif teclaPressionada(K_LEFT):
            direcao = ESQUERDA
        elif teclaPressionada(K_RIGHT):
            direcao = DIREITA
        else:
            caminhando = False

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
        if caminhando:
            frameJogador += velocidadeAnimacaoJogador
            if frameJogador >= 3:
                frameJogador = 0
            desenhaImagem(imagemJogador[int(frameJogador)], xJogador, yJogador)
        else:
            desenhaImagem(imagemJogador[0], xJogador, yJogador)

        #Desenha pontuação
        desenhaTexto(f"Pontos: {moedas:2d}", 400, 50, 15, (0, 0, 0), "Recursos/Fontes/FiraCode-Regular.ttf")

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

