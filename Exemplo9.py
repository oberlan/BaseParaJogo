#Exemplo 9: Exemplo de utilização da função 'teclaLiberada' que 
# a nave é movimenta pelas setinhas do teclado e um disparo é 
# feito sempre que a tecla 'espaço' é liberada.

from BaseParaJogo import *

CORFUNDOJANELA = (94, 63, 107)
LARGURAJANELA = 400
ALTURAJANELA = 600
ICONE = "Recursos/Imagens/nave.png"


def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Introdução à Programação", CORFUNDOJANELA, ICONE)
    nave = carregaImagem("Recursos/Imagens/nave.png", (50, 38))
    laser = carregaImagem("Recursos/Imagens/laser.png", (9, 33))
    somDisparo = carregaSom("Recursos/Sons/laser.ogg")
    musicaFundo = carregaMusica("Recursos/Sons/low-fi.mp3")
    tocaMusica(musicaFundo)
    disparos = []

    xNave = LARGURAJANELA // 2 - 25
    yNave = ALTURAJANELA - 45
    while True:

        if teclaPressionada(K_ESCAPE): 
            break

        if teclaLiberada(K_SPACE):
            disparos.append([xNave+21, yNave-15])
            tocaSom(somDisparo)

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição da nave
        if teclaPressionada(K_UP):
            yNave -= 4
        elif teclaPressionada(K_DOWN):
            yNave += 4
        elif teclaPressionada(K_LEFT):
            xNave -= 4
        elif teclaPressionada(K_RIGHT):
            xNave += 4
        elif teclaPressionada(K_p):
            paraMusica()

        #Desenha os disparos e atualiza a posição de cada um
        for i in range(len(disparos)):
            desenhaImagem(laser, disparos[i][0], disparos[i][1])
            disparos[i][1] -= 4

        #Desenha a nave
        desenhaImagem(nave, xNave, yNave)

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()


main()
