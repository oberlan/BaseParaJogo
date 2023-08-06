#Exemplo 3: Desenha um texto na tela

from BaseParaJogo import *

CORFUNDOJANELA = (255, 255, 255)
LARGURAJANELA = 930
ALTURAJANELA = 600

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Introdução à Programação", CORFUNDOJANELA)

    while True:
        #Verifica se a tecla ESC foi precionada
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Desenha textos na tela
        desenhaTexto("Introdução à", LARGURAJANELA//2, 200, 50, (255, 0, 0), "Recursos/Fontes/FiraCode-Regular.ttf")
        desenhaTexto("Programação", LARGURAJANELA//2, 300, 50, (255, 0, 0), "Recursos/Fontes/FiraCode-Regular.ttf")

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

