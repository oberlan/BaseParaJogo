# BaseParaJogo - Biblioteca de desenvolvimento de jogos baseado no PyGame
# Copyright (C) 2023  Oberlan Romão
"""
BaseParaJogo é um conjunto de funções, baseado no PyGame, usado para o 
desenvolvimento de jogos na disciplina de "Introdução à Programação", que
segue o paradigma estruturado.  
Por ser uma disciplina introdutória, o objetivo desta biblioteca é 
facilitar a implementação de jogos pelos alunos, não sendo necessário 
conhecimento de Orientação à Objetos.
Para usar a biblioteca, certifique-se que o pygame está intalado.
"""
try:
    import pygame
    from pygame.locals import *
except:
    print("\033[1;31mBiblioteca PyGame não instalada\033[00m")
    raise SystemExit
from typing import Tuple
import os

#Variáveis globais
__tela = None
__clock = None
__listaImagens = []
__numImagemCarregada = 0
__listaMusicas = []
__numMusicaCarregada = 0
__listaSons = []
__numSomCarregado = 0
__corFundo = tuple()
__tempoInicio = 0
__eventos = []

def criaJanela(largura: int, altura: int, titulo: str, corFundo: pygame.Color = (0, 0, 0), icone: str = None):
    """Inicia o PyGame e cria a janela do jogo

    Parâmetros:
        - largura (int): Lagura da janela
        - altura (int): Altura da janela
        - titulo (str): Título da janela
        - corFundo (pygame.Color, opcional): Cor do fundo da janela. Valor padrão: (0, 0, 0)
        - icone (str, opcional): Arquivo de imagem para ser usando como ícone. Valor padrão: None
    """
    global __tela, __clock, __corFundo
    #Inicia o PyGame
    pygame.init()
    __corFundo = corFundo
    __tela = pygame.display.set_mode((largura, altura))
    if icone != None:
        try:
            icone = f"{os.getcwd()}/{icone}"
            pygame.display.set_caption(titulo, icone)
            imgIcone = pygame.image.load(icone)
            pygame.display.set_icon(imgIcone)
        except:
            print(f"ERRO: Não foi possível carregar o arquivo '{icone}'")
            raise SystemExit
    else:
        pygame.display.set_caption(titulo)
    
    __tela.fill(corFundo)
    pygame.mixer.init()
    __clock = pygame.time.Clock()
    __tempoInicio = pygame.time.get_ticks()

def finalizaJogo():
    """Finaliza as funções do PyGame
    """
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()
    exit()

def tempoExecutandoJogo() -> int:
    """Retorna o tempo de execução do jogo em milissegundos

    Retorno:
        int: tempo de execução do jogo
    """
    return pygame.time.get_ticks() - __tempoInicio

def tempoAtual() -> int:
    """Retorna o tempo em milissegundos

    Exemplo de uso:
        inicio = tempoAtual()\n
        #Sequencia de comandos\n
        fim = tempoAtual()\n
        print(f"Tempo gasto: {fim - inicio}ms")

    Retorno:
        int: retorna o tempo em milissegundos
    """
    return pygame.time.get_ticks()

def atualizaTelaJogo() -> None:
    """Atualiza a janela do jogo, redesenhando todos os objetos.
     Função também responsável por capturar os eventos ocorridos na janela. 
    """
    global __clock, __eventos
    __eventos = pygame.event.get()
    for evento in __eventos:# pygame.event.get():
        if evento.type == pygame.QUIT:
            finalizaJogo()

    pygame.display.update()
    __clock.tick(60)  # Frames por segundos


def limpaTela() -> None:
    """Apaga todas as "informações" da tela
    """
    atualizaCorFundo(__corFundo)
    

def atualizaCorFundo(cor: pygame.Color) -> None:
    """Atualiza a cor de fundo da tela

    Parâmetro:
        - cor (pygame.Color): Cor do fundo da tela
    """
    global __corFundo
    __corFundo = cor
    __tela.fill(cor)


def desenhaTexto(texto: str, x: int, y: int, tamFonte: int, cor: pygame.Color = "black", arquivoFonte: str = None) -> None:
    """Escreve texto na tela. Para facilitar, o texto é centralizado na posição (x, y) passados como parâmetros. 

    Parâmetros:
        - texto (str): Texto a ser escrito na tela
        - x (int): Posição x na tela que o texto deve ser escrito
        - y (int): Posição y na tela que o texto deve ser escrito
        - tamFonte (int): Tamanho da fonte do texto
        - cor (pygame.Color, optional): Cor da fonte. Valor padrão: "black".
        - arquivoFonte (str, optional): Arquivo com a fonte a ser usada. Valor padrão: None.
    """
    if arquivoFonte:
        arquivoFonte = f"{os.getcwd()}/{arquivoFonte}"
    fonte = pygame.font.Font(arquivoFonte, tamFonte)
    texto = fonte.render(texto, True, cor)
    textoPos = texto.get_rect()
    textoPos.centerx = x
    textoPos.centery = y
    __tela.blit(texto, textoPos)


def desenhaRetangulo(x: int, y: int, largura: int, altura: int, corFundo: pygame.Color) -> None:
    """Desenha um retângulo colorido na tela

    Parâmetros:
        - x (int): posição x do retângulo
        - y (int): posição y do retângulo
        - largura (int): largura do retângulo
        - altura (int): largura do retângulo
        - corFundo (pygame.Color): cor do retângulo
    """
    pygame.draw.rect(__tela, corFundo, (x, y, largura, altura))


def carregaImagem(nomeArquivo: str, tamanho: tuple = (0, 0)) -> int:
    """Responsável por carregar e armazenar uma imagem a partir de um arquivo

    Parâmetros:
        - nomeArquivo (str): arquivo com a imagem
        - tamanho (tuple, opcional): tamanho que a imagem deve ser desenhada. Este parâmetro é usado caso \
                                   seja necessário redimensionar a imagem. \
                                   Valor padrão (0, 0) indicando que deve ser mantida as dimensões originais da imagem.

    Returno:
        int: identificador da imagem
    """
    global __numImagemCarregada
    nomeArquivoCompleto = f"{os.getcwd()}/{nomeArquivo}"
    try:
        imagem = pygame.image.load(nomeArquivoCompleto)
        if imagem.get_alpha() is None:
            imagem = imagem.convert()
        else:
            imagem = imagem.convert_alpha()
        if type(tamanho) != tuple and type(tamanho) != list or len(tamanho) != 2 or tamanho[0] <= 0 or tamanho[1] <= 0:
            tamanho = imagem.get_size()
        if tamanho != (0, 0):
            imagem = pygame.transform.scale(imagem, tamanho)
        __listaImagens.append(imagem)
        __numImagemCarregada += 1
    except FileNotFoundError:
        print(f"ERRO: Não foi possível carregar o arquivo '{nomeArquivoCompleto}'")
        raise SystemExit
    return __numImagemCarregada


def desenhaImagem(idImagem: int, x: int, y: int) -> None:
    """Desenha imagem na posição (x, y) na tela

    Parâmetros:
        - idImagem (int): identificador da imagem
        - x (int): posição x que a imagem será desenhada
        - y (int): posição y que a imagem será desenhada
    """
    if idImagem <= 0 or idImagem > __numImagemCarregada:
        print("ERRO - Número da figura inválido!")
        return  
    __tela.blit(__listaImagens[idImagem - 1], (x, y))

def teclaPressionada(tecla: int) -> bool:
    """Verifica se a tecla foi pressionada

    Parâmetro:
        - tecla (int): tecla que se deseja verificar se foi pressionada

    Returno:
        bool: True se a tecla foi pressionada e False, caso contrário
    """
    return pygame.key.get_pressed()[tecla]

def teclaLiberada(tecla: int) -> bool:
    """Verifica se a tecla foi liberada

    Parâmetro:
        - tecla (int): tecla que se deseja verificar se foi liberada

    Returno:
        bool: True se a tecla foi liberada e False, caso contrário
    """
    for evento in __eventos: # pygame.event.get():
        if evento.type == pygame.QUIT:
            finalizaJogo()
        if evento.type == KEYUP and evento.key == tecla:
            return True
    return False

def posicaoCursorMouse() -> Tuple[int, int]:
    """Posição do curso do mouse na janela

    Returno:
        Tuple[int, int]: posição (x, y) que do curso na janela
    """
    return pygame.mouse.get_pos()


def botaoMousePressionado() -> Tuple[bool, int, Tuple[int, int]]:
    """Verifica se algum botão do mouse foi pressionado

    Returno:
        Tuple[bool, int, Tuple[int, int]]: retorna três informações: \n
            1. se algum botão foi pressionado;
            2. identificador do botão pressionado e;
            3. posição (x, y) onde o botão foi pressionado na janela.
    """
    for evento in __eventos: # pygame.event.get():
        if evento.type == pygame.QUIT:
            finalizaJogo()
        if evento.type == MOUSEBUTTONDOWN:
            return True, evento.button, evento.pos
    return False, -1, (-1, -1)

def carregaSom(nomeArquivo: str) -> int:
    """Carrega som a partir de um arquivo de áudio. 

    Parâmetro:
        - nomeArquivo (str): arquivo com o som

    Returno:
        int: identificador do som
    """
    global __numSomCarregado
    nomeArquivoCompleto = f"{os.getcwd()}/{nomeArquivo}"
    try:
        som = pygame.mixer.Sound(nomeArquivoCompleto)
        __listaSons.append(som)
        __numSomCarregado += 1
    except FileNotFoundError:
        print(
            f"ERRO: Não foi possível carregar o arquivo '{nomeArquivoCompleto}'")
        raise SystemExit
    return __numSomCarregado

def tocaSom(numSom: int) -> None:
    """Toca um som a partir do identificador

    Parâmetro:
        numSom (int): identificador do som a ser tocado
    """
    if numSom <= 0 or numSom > __numSomCarregado:
        print("ERRO - Número do som inválido!")
        return
    __listaSons[numSom - 1].play()

def carregaMusica(nomeArquivo: str) -> int:
    """Carrega música a partir de um arquivo. 

    Parâmetro:
        nomeArquivo (str): arquivo com a música

    Returno:
        int: identificador da música
    """
    global __numMusicaCarregada
    nomeArquivoCompleto = f"{os.getcwd()}/{nomeArquivo}"
    if os.path.isfile(nomeArquivoCompleto):
        __listaMusicas.append(nomeArquivoCompleto)
        __numMusicaCarregada += 1
    else:
        print(f"ERRO: Não foi possível carregar o arquivo '{nomeArquivoCompleto}'")
        raise SystemExit
    return __numMusicaCarregada
    
def tocaMusica(numMusica: int, loop: bool = True) -> None:
    """Inicia a execução da música de acordo com o identificador

    Parâmetros:
        - numMusica (int): identificador da música
        - loop (bool, opcional): True se a música deve ser tocada em loop e False, caso contrário. Valor padrão: True.
    """
    if numMusica <= 0 or numMusica > __numMusicaCarregada:
        print("ERRO - Número da música invalido!")
        return
    pygame.mixer.music.load(__listaMusicas[numMusica - 1])
    if loop: 
        pygame.mixer.music.play(loops=-1)
    else: 
        pygame.mixer.music.play()

def paraMusica() -> None:
    """Para a execução a música que está tocando
    """
    pygame.mixer.music.stop()


