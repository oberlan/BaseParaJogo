#Exemplo 6: Exemplo de animação

from BaseParaJogo import *

CORFUNDOJANELA = (255, 255, 255)
LARGURAJANELA = 300
ALTURAJANELA = 300
ICONE = "Recursos/Imagens/python-logo.png"

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Introdução à Programação", CORFUNDOJANELA, ICONE)
    
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

    yJogador = ALTURAJANELA // 2 - 16
    xJogador = LARGURAJANELA //2 - 16
    velocidadeAnimacaoJogador = 0.2
    while True:   
        
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição do jogador
        caminhando = True
        if teclaPressionada(K_UP):
            yJogador -= 2
            imagemJogador = jogador_cima
        elif teclaPressionada(K_DOWN):
            yJogador += 2
            imagemJogador = jogador_baixo
        elif teclaPressionada(K_LEFT):
            xJogador -= 2
            imagemJogador = jogador_esquerda
        elif teclaPressionada(K_RIGHT):
            xJogador += 2
            imagemJogador = jogador_direita
        else:
            caminhando = False

        #Desenha o jogador
        if caminhando:
            frameJogador += velocidadeAnimacaoJogador
            if frameJogador >= 3:
                frameJogador = 0
            desenhaImagem(imagemJogador[int(frameJogador)], xJogador, yJogador)
        else:
            desenhaImagem(imagemJogador[0], xJogador, yJogador)

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

