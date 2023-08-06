#Exemplo 12: Exemplo de utilização da função 'botaoMousePressionado' em 
# que uma nave segue os movimentos do cursor do mouse.
# O disparo da nave é feito pelo clique do mouse.

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
        #Verifica se a tecla ESC foi precionada
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Obtem as informções do clique do mouse
        botaoPressionado, botao, posicao = botaoMousePressionado()
        if botaoPressionado and botao == 1:
            #Inclui um disparo na lista
            disparos.append([posicao[0]-5, yNave-15])
            print(f"Número de disparos: {len(disparos)}")
            tocaSom(somDisparo)

        xMouse, yMouse = posicaoCursorMouse()
        if xMouse + 50 <= LARGURAJANELA:
            xNave = xMouse - 25
        if yMouse + 38 <= ALTURAJANELA:
            yNave = yMouse - 19

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
