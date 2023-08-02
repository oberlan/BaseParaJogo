#Exemplo 1: Desenha dois retângulos na janela

from BaseParaJogo import *

def main():
    criaJanela(930, 600, "Primeiro Exemplo", (255, 255, 255))

    while True:
        #Verifica se a tecla ESC foi pressionada
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Desenha um retângulo
        desenhaRetangulo(400, 300, 25, 50, (255, 0, 255))

        desenhaRetangulo(0, 0, 100, 250, (0, 0, 255))

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

