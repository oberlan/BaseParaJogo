#Exemplo 10: Exemplo de utilização das funções 'posicaoCursorMouse'

from BaseParaJogo import *


def main():
    criaJanela(640, 480, "Introdução à Programação", (255, 255, 255))

    while True:
        #Verifica se a tecla ESC foi precionada
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Captura a posição do cursor do mouse
        xMouse, yMouse = posicaoCursorMouse() 

        desenhaTexto("Posicao do cursor", 320, 20, 20, (255, 0, 0), "Recursos/Fontes/FiraCode-Regular.ttf")
        desenhaTexto(f"({xMouse}, {yMouse})", 320, 40, 20, (255, 0, 0), "Recursos/Fontes/FiraCode-Regular.ttf")

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()


main()
