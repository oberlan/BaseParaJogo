#Exemplo 11: exemplo de utilização da função 'botaoMousePressionado'

from BaseParaJogo import *


def main():
    criaJanela(640, 480, "Introdução à Programação", (255, 255, 255))

    while True:
        #Verifica se a tecla ESC foi precionada
        if teclaPressionada(K_ESCAPE):
            break
        

        #Limpa a janela
        limpaTela()

        #Obtem as informções do clique do mouse
        botaoPressionado, botao, posicao = botaoMousePressionado()
        if botaoPressionado: #Verifica se algum botão foi pressionado
            print(f"Algum botão pressionado na posicao ({posicao[0]}, {posicao[1]})")
            if botao == 1:
                print("Botão esquerdo pressionado")
            elif botao == 2:
                print("Botão central pressionado")
            elif botao == 3:
                print("Botão direito pressionado")

        xMouse, yMouse = posicaoCursorMouse() 

        desenhaTexto("Posicao do cursor", 320, 20, 20, (255, 0, 0), "Recursos/Fontes/FiraCode-Regular.ttf")
        desenhaTexto(f"({xMouse}, {yMouse})", 320, 40, 20, (255, 0, 0), "Recursos/Fontes/FiraCode-Regular.ttf")

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()
