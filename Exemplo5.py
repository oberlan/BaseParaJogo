#Exemplo 5: Executa som

from BaseParaJogo import *

CORFUNDOJANELA = (255, 255, 255)
LARGURAJANELA = 930
ALTURAJANELA = 600
ICONE = "Recursos/Imagens/python-logo.png"

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Quinto Exemplo", CORFUNDOJANELA, ICONE)
    imagem = carregaFigura("Recursos/Imagens/nave.png")
    musica = carregaMusica("Recursos/Sons/magic_space.mp3")
    som = carregaSom("Recursos/Sons/laser.ogg")
    iniciaMusica(musica)
    xImagem = 0
    yImagem = 300
    while True:
        #Verifica se a tecla ESC foi precionada
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição da figura
        if teclaPressionada(K_UP):
            yImagem -= 5
            tocaSom(som)
        elif teclaPressionada(K_DOWN):
            yImagem += 5
        elif teclaPressionada(K_LEFT):
            xImagem -= 5
        elif teclaPressionada(K_RIGHT):
            xImagem += 5
        elif teclaPressionada(K_p):
            paraMusica()

        #Desenha imagem
        desenhaFigura(imagem, xImagem, yImagem)

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

