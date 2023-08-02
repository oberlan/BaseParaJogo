#Exemplo 2: Desenha um retângulo na janela e permite movimentá-lo usando as setinhas do teclado

from BaseParaJogo import *

CORFUNDOJANELA = (255, 255, 255)
LARGURAJANELA = 930
ALTURAJANELA = 600

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Segundo Exemplo", CORFUNDOJANELA)
    xRetangulo = 0
    yRetangulo = 300
    while True:
        #Verifica se a tecla ESC foi pressionada
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi pressionada
        #Se sim, atualiza a posição do retângulo
        if teclaPressionada(K_UP):
            yRetangulo -= 10
        elif teclaPressionada(K_DOWN):
            yRetangulo += 10
        elif teclaPressionada(K_LEFT):
            xRetangulo -= 10
        elif teclaPressionada(K_RIGHT):
            xRetangulo += 10

        #Desenha o retângulo
        desenhaRetangulo(xRetangulo, yRetangulo, 25, 50, (255, 0, 255))

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

