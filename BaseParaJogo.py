
import pygame
from pygame.locals import *
from typing import Tuple
import os

__tela = None
__clock = None
__listaFiguras = []
__numFiguraCarregada = 0
__listaMusicas = []
__numMusicaCarregada = 0
__listaSons = []
__numSomCarregado = 0
__corFundo = tuple()
__tempoInicio = 0

class Vetor2D:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y 
    
def criaJanela(largura: int, altura: int, titulo: str, corFundo: pygame.Color = (0, 0, 0), icone: str = None):
    global __tela, __clock, __corFundo
    pygame.init()
    __corFundo = corFundo
    __tela = pygame.display.set_mode((largura, altura))
    
    if icone != None:
        try:
            icone = f"{os.getcwd()}/{icone}"
        except FileNotFoundError:
            print(f"ERRO: Não foi possível carregar o arquivo '{icone}'")
            raise SystemExit
        pygame.display.set_caption(titulo, icone)
        imgIcone = pygame.image.load(icone)
        pygame.display.set_icon(imgIcone)
    else:
        pygame.display.set_caption(titulo)
    
    __tela.fill(corFundo)
    pygame.mixer.init()
    __clock = pygame.time.Clock()
    __tempoInicio = pygame.time.get_ticks()

def finalizaJogo():
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()
    exit()

def tempoExecutandoJogo() -> int:
    return pygame.time.get_ticks() - __tempoInicio

def atualizaTelaJogo() -> None:
    global __clock
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            finalizaJogo()

    pygame.display.update()
    __clock.tick(60)  # limits FPS to 60

def limpaTela() -> None:
    atualizaCorFundo(__corFundo)

def atualizaCorFundo(cor: pygame.Color) -> None:
    global __corFundo
    __corFundo = cor
    __tela.fill(cor)


def desenhaTexto(mensagem: str, x: int, y: int, tamFonte: int, cor: pygame.Color = "black", nomeFonte: str = None) -> None:
    if nomeFonte:
        nomeFonte = f"{os.getcwd()}/{nomeFonte}"
    fonte = pygame.font.Font(nomeFonte, tamFonte)
    texto = fonte.render(mensagem, True, cor)
    textoPos = texto.get_rect()
    textoPos.centerx = x
    textoPos.centery = y
    __tela.blit(texto, textoPos)


def desenhaRetangulo(x: int, y: int, largura: int, altura: int, corFundo: pygame.Color) -> None:
    pygame.draw.rect(__tela, corFundo, (x, y, largura, altura))


def carregaFigura(nomeArquivo: str, tamanho: tuple = (0, 0)) -> int:
    global __numFiguraCarregada
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
        __listaFiguras.append(imagem)
        __numFiguraCarregada += 1
    except FileNotFoundError:
        print(f"ERRO: Não foi possível carregar o arquivo '{nomeArquivoCompleto}'")
        raise SystemExit
    return __numFiguraCarregada


def desenhaFigura(numFigura: int, x: int, y: int) -> None:
    if numFigura <= 0 or numFigura > __numFiguraCarregada:
        print("ERRO - Número da figura inválido!")
        return  
    __tela.blit(__listaFiguras[numFigura - 1], (x, y))

def teclaPressionada(tecla: int) -> bool:
    return pygame.key.get_pressed()[tecla]

def teclaLiberada(tecla) -> bool:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            finalizaJogo()
        if evento.type == KEYUP and evento.key == tecla:
            return True
    return False

def posicaoCursorMouse() -> Tuple[int, int]:
    return pygame.mouse.get_pos()


def botaoMousePressionado() -> Tuple[bool, int, Tuple[int, int]]:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            finalizaJogo()
        if evento.type == MOUSEBUTTONDOWN:
            return True, evento.button, evento.pos
    return False, -1, (-1, -1)

def carregaSom(nomeArquivo: str) -> int:
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
    if numSom <= 0 or numSom > __numSomCarregado:
        print("ERRO - Número do som inválido!")
        return
    __listaSons[numSom - 1].play()

def carregaMusica(nomeArquivo: str) -> int:
    global __numMusicaCarregada
    nomeArquivoCompleto = f"{os.getcwd()}/{nomeArquivo}"
    if os.path.isfile(nomeArquivoCompleto):
        # pygame.mixer.music.load(nomeArquivoCompleto)
        # pygame.mixer.music.play()
        __listaMusicas.append(nomeArquivoCompleto)
        __numMusicaCarregada += 1
    else:
        print(f"ERRO: Não foi possível carregar o arquivo '{nomeArquivoCompleto}'")
        raise SystemExit
    return __numMusicaCarregada
    
def iniciaMusica(numMusica: int, loop: bool = True) -> None:
    if numMusica <= 0 or numMusica > __numMusicaCarregada:
        print("ERRO - Número da música invalido!")
        return
    pygame.mixer.music.load(__listaMusicas[numMusica - 1])
    if loop: 
        pygame.mixer.music.play(loops=-1)
    else: 
        pygame.mixer.music.play()

def paraMusica() -> None:
    pygame.mixer.music.stop()


