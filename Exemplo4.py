#Exemplo 4: Carrega e desenha uma imagem

from BaseParaJogo import *

CORFUNDOJANELA = (255, 255, 255)
LARGURAJANELA = 930
ALTURAJANELA = 600
ICONE = "Recursos/Imagens/python-logo.png"

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Quarto Exemplo", CORFUNDOJANELA, ICONE)
    imagem = carregaFigura("Recursos/Imagens/python-logo.png")
    xImagem = 0
    yImagem = 300
    while True:
        #Verifica se a tecla ESC foi pressionada
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi pressionada
        #Se sim, atualiza a posição do retângulo
        if teclaPressionada(K_UP):
            yImagem -= 10
        elif teclaPressionada(K_DOWN):
            yImagem += 10
        elif teclaPressionada(K_LEFT):
            xImagem -= 10
        elif teclaPressionada(K_RIGHT):
            xImagem += 10

        #Desenha imagem
        desenhaFigura(imagem, xImagem, yImagem)

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

