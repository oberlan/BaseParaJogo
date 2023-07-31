#Exemplo 6: Exemplo de animação

from BaseParaJogo import *

CORFUNDOJANELA = (255, 255, 255)
LARGURAJANELA = 930
ALTURAJANELA = 600
FPS = 60
ICONE = "Recursos/Imagens/python-logo.png"

def main():
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Sexto Exemplo", CORFUNDOJANELA, ICONE)
    numImagensAsteroides = 16
    imagemAsteroides = []
    
    for i in range(numImagensAsteroides):
        imagemAsteroides += [carregaFigura(f"Recursos/Imagens/Asteroides/{i+1}.png")]

    idAsteroide = 0
    asteroideSpeed = 4
    frame = 0
    xImagem = 0
    yImagem = 300
    while True:
        frame = (frame + 1) % FPS       
        
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Verifica se uma das teclas foi precionada
        #Se sim, atualiza a posição do retângulo
        if teclaPressionada(K_UP):
            yImagem -= 5
        elif teclaPressionada(K_DOWN):
            yImagem += 5
        elif teclaPressionada(K_LEFT):
            xImagem -= 5
        elif teclaPressionada(K_RIGHT):
            xImagem += 5

        #Desenha a animação do asteroide
        if frame % asteroideSpeed == 0:
            idAsteroide = (idAsteroide + 1) % numImagensAsteroides

        desenhaFigura(imagemAsteroides[idAsteroide], xImagem, yImagem)

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()

