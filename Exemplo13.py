#Exemplo 13: Exemplo de menu para o usuário escolher uma opção. 
# Util para definir temas ou parâmetros (como, por exemplo, nível de dificuldade) do jogo.

from BaseParaJogo import *

def mouseDentroRetangulo(xRetangulo, yRetangulo, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
    """Verifica se o cursor do mouse está "dentro" do retângulo"""
    return xRetangulo <= xMouse <= larguraRetangulo + xRetangulo and yRetangulo <= yMouse <= yRetangulo + alturaRetangulo

def main():
    criaJanela(640, 480, "Introdução à Programação", (0, 0, 0))
    larguraRetangulo = 250
    alturaRetangulo = 50
    xRetangulo = 195
    yRetangulo1 = 150
    yRetangulo2 = 250
    yRetangulo3 = 350
    opcaoEscolhida = 0

    #Primeiro é desenhado o menu enquanto o usuário não clicar em uma das opções
    while True:
        #Verifica se a tecla ESC foi precionada
        if teclaPressionada(K_ESCAPE):
            break
        
        #Limpa a janela
        limpaTela()

        desenhaTexto("Escolha uma Opção", 320, 50, 30, (128, 128, 128), "Recursos/Fontes/Constance-7BLXE.otf")

        #Obtem as informções do clique do mouse
        xMouse, yMouse = posicaoCursorMouse() 
        opcaoEscolhida = 0

        #Define as cores dos retângulos
        corRetangulo1 = (128, 128, 128) 
        if mouseDentroRetangulo(xRetangulo, yRetangulo1, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
            corRetangulo1 = (255, 255, 255)
            opcaoEscolhida = 1

        corRetangulo2 = (128, 128, 128) 
        if mouseDentroRetangulo(xRetangulo, yRetangulo2, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
            corRetangulo2 = (255, 255, 255)
            opcaoEscolhida = 2

        corRetangulo3 = (128, 128, 128) 
        if mouseDentroRetangulo(xRetangulo, yRetangulo3, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
            corRetangulo3 = (255, 255, 255)
            opcaoEscolhida = 3

        botaoPressionado, botao, posicao = botaoMousePressionado()
        #Verifica se o botão esquerdo foi pressionado dentro de uma das opções
        if botaoPressionado and botao == 1 and opcaoEscolhida != 0: 
            break

        #Desenha os retângulos com os textos
        #Observe a estratégia que foi usada para desenhar as bordas dos retângulos
        borda = 3
        desenhaRetangulo(xRetangulo-borda, yRetangulo1-borda, larguraRetangulo+2*borda, alturaRetangulo+2*borda, corRetangulo1)
        desenhaRetangulo(xRetangulo, yRetangulo1, larguraRetangulo, alturaRetangulo, (0, 0, 0))
        desenhaTexto("Opção 1", 320, 175, 15, corRetangulo1, "Recursos/Fontes/Constance-7BLXE.otf")

        desenhaRetangulo(xRetangulo-borda, yRetangulo2-borda, larguraRetangulo+2*borda, alturaRetangulo+2*borda, corRetangulo2)
        desenhaRetangulo(xRetangulo, yRetangulo2, larguraRetangulo, alturaRetangulo, (0, 0, 0))
        desenhaTexto("Opção 2", 320, 275, 15, corRetangulo2, "Recursos/Fontes/Constance-7BLXE.otf")

        desenhaRetangulo(xRetangulo-borda, yRetangulo3-borda, larguraRetangulo+2*borda, alturaRetangulo+2*borda, corRetangulo3)
        desenhaRetangulo(xRetangulo, yRetangulo3, larguraRetangulo, alturaRetangulo, (0, 0, 0))
        desenhaTexto("Opção 3", 320, 375, 15, corRetangulo3, "Recursos/Fontes/Constance-7BLXE.otf")

        #Atualiza os objetos na janela
        atualizaTelaJogo()

    #Neste ponto o usuário já escolheu a opção
    #Perceba que as funções limpaTela() e atualizaTelaJogo() devem ser chamadas novamente.
    while True:
        #Verifica se a tecla ESC foi precionada
        if teclaPressionada(K_ESCAPE):
            break

        #Limpa a janela
        limpaTela()

        #Aqui poderia ser um if-elif-else de acordo com a esolha do usuário
        desenhaTexto(f"Opção Escolhida: {opcaoEscolhida}", 320, 240, 30, (128, 128, 128), "Recursos/Fontes/Constance-7BLXE.otf")
        
        #Atualiza os objetos na janela
        atualizaTelaJogo()

    finalizaJogo()

main()
