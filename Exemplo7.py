#Exemplo 7: Exemplo de animação

from BaseParaJogo import *

CORFUNDOJANELA = (255, 255, 255)
LARGURAJANELA = 930
ALTURAJANELA = 600
FPS = 60
ICONE = "Recursos/Imagens/python-logo.png"
#Direção do movimento
PARADO = 0
CIMA = 1
BAIXO = 2
ESQUERDA = 3
DIREITA = 4

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Sexto Exemplo", CORFUNDOJANELA, ICONE)
    numImagensAsteroides = 16
    imagemAsteroides = []
    
    for i in range(numImagensAsteroides):
        imagemAsteroides += [carregaFigura(f"Recursos/Imagens/Asteroides/{i+1}.png", (100, 100))]

    idAsteroide = 0
    asteroideSpeed = 0.25
    xImagem = 0
    yImagem = 300
    direcao = PARADO
    while True:   
        
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição do retângulo
        if teclaPressionada(K_UP):
            direcao = CIMA
        elif teclaPressionada(K_DOWN):
            direcao = BAIXO
        elif teclaPressionada(K_LEFT):
            direcao = ESQUERDA
        elif teclaPressionada(K_RIGHT):
            direcao = DIREITA

        if direcao == CIMA:
            yImagem -= 5
        elif direcao == BAIXO:
            yImagem += 5
        elif direcao == ESQUERDA:
            xImagem -= 5
        elif direcao == DIREITA:
            xImagem += 5

        if xImagem <= 0 or xImagem >= LARGURAJANELA - 75 or yImagem <= 0 or yImagem >= ALTURAJANELA - 75:
            direcao = PARADO

        #Desenha a animação do asteroide
        idAsteroide += asteroideSpeed
        if idAsteroide >= len(imagemAsteroides):
            idAsteroide = 0
        desenhaFigura(imagemAsteroides[int(idAsteroide)], xImagem, yImagem)

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

