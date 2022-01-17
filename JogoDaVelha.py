## EXERCÍCIO BASEADO NOS VÍDEOS DO CANAL "CODING SPOT"

import pygame, sys
import numpy as np

pygame.init()

### CONSTANTES

LARGURA = 600
ALTURA = 600
LARGURALINHA = 15
WIN_LARGURALINHA = 15
QUADRADOTAM = 200
RAIOCIRCULO = 60
LARGURACIRCULO = 15
LARGURAX = 20
ESPACO = 55
jogador = 1

# COORDENADAS
COORDLINHA = 3
COORDCOLUNA = 3
COORDENADAS = np.zeros((COORDLINHA, COORDCOLUNA))

## CORES RGB
BRANCO = (242, 235, 211)
CIANO = (20, 189, 172)
CIANOLINHA = (13, 161, 146)
CINZA = (84, 84, 84)

## ESTRUTURAS FRONT-END
ICONE = pygame.image.load('images/jogodavelha.png')
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Velha')
pygame.display.set_icon(ICONE)
tela.fill(CIANO)


def linha_tab():
    # 1 HORIZONTAL      #(angulo,distancia teto), (angulo,distancia chão), largura
    pygame.draw.line(tela, CIANOLINHA, (0, 200), (600, 200), 15)
    # 2 HORIZONTAL
    pygame.draw.line(tela, CIANOLINHA, (0, 400), (600, 400), 15)

    # 1 VERTICAL
    pygame.draw.line(tela, CIANOLINHA, (200, 0), (200, 600), 15)
    # 2 VERTICAL
    pygame.draw.line(tela, CIANOLINHA, (400, 0), (400, 600), 15)


def FORMAS():
    for linha in range(COORDLINHA):
        for coluna in range(COORDCOLUNA):
            if COORDENADAS[linha][coluna] == 1:
                pygame.draw.line(tela, CINZA,
                                 (coluna * QUADRADOTAM + ESPACO, linha * QUADRADOTAM + QUADRADOTAM - ESPACO),
                                 (coluna * QUADRADOTAM + QUADRADOTAM - ESPACO, linha * QUADRADOTAM + ESPACO), LARGURAX)
                pygame.draw.line(tela, CINZA, (coluna * QUADRADOTAM + ESPACO, linha * QUADRADOTAM + ESPACO), (
                    coluna * QUADRADOTAM + QUADRADOTAM - ESPACO, linha * QUADRADOTAM + QUADRADOTAM - ESPACO), LARGURAX)

            elif COORDENADAS[linha][coluna] == 2:  # (angulo,distancia teto), (angulo,distancia chão), largura
                pygame.draw.circle(tela, BRANCO, (
                    int(coluna * QUADRADOTAM + QUADRADOTAM // 2), int(linha * QUADRADOTAM + QUADRADOTAM // 2)),
                                   RAIOCIRCULO,
                                   LARGURACIRCULO)


def MARCA(linha, coluna, jogador):
    COORDENADAS[linha][coluna] = jogador


def LIVRE(linha, coluna):
    return COORDENADAS[linha][coluna] == 0


def OCUPADO():
    for linha in range(COORDLINHA):
        for coluna in range(COORDCOLUNA):
            if COORDENADAS[linha][coluna] == 0:
                return False
    return True


# RESULTADOS
def VENCEU(jogador):
    # VERTICAL
    for coluna in range(COORDCOLUNA):
        if COORDENADAS[0][coluna] == jogador and COORDENADAS[1][coluna] == jogador and COORDENADAS[2][
            coluna] == jogador:
            LINHAVERTICALVENCEDOR(coluna, jogador)
            return True
    # HORIZONTAL
    for linha in range(COORDLINHA):
        if COORDENADAS[linha][0] == jogador and COORDENADAS[linha][1] == jogador and COORDENADAS[linha][2] == jogador:
            LINHAHORIZONTALVENCEDOR(linha, jogador)
            return True

    # LINHA ASCENDENTE VENCEDOR
    if COORDENADAS[2][0] == jogador and COORDENADAS[1][1] == jogador and COORDENADAS[0][2] == jogador:
        LINHAASCENDENTEDIAGONAL(jogador)
        return True

    # LINHA DESCENDENTE VENCEDOR
    if COORDENADAS[0][0] == jogador and COORDENADAS[1][1] == jogador and COORDENADAS[2][2] == jogador:
        LINHADESCENDENTEDIAGONAL(jogador)
        return True

    return False


def LINHAVERTICALVENCEDOR(coluna, jogador):
    global cor
    posX = coluna * QUADRADOTAM + QUADRADOTAM // 2

    if jogador == 1:
        cor = CINZA
    elif jogador == 2:
        cor = BRANCO

    pygame.draw.line(tela, cor, (posX, 15), (posX, ALTURA - 15), LARGURALINHA - 5)


def LINHAHORIZONTALVENCEDOR(linha, jogador):
    global cor
    posY = linha * QUADRADOTAM + QUADRADOTAM // 2

    if jogador == 1:
        cor = CINZA
    elif jogador == 2:
        cor = BRANCO

    pygame.draw.line(tela, cor, (15,posY), (LARGURA - 15,posY), WIN_LARGURALINHA-5)


def LINHAASCENDENTEDIAGONAL(jogador):
    global cor
    if jogador == 1:
        cor = CINZA
    elif jogador == 2:
        cor = BRANCO

    pygame.draw.line(tela, cor, (15, ALTURA - 15), (LARGURA - 15, 15), WIN_LARGURALINHA - 5)


def LINHADESCENDENTEDIAGONAL(jogador):
    global cor
    if jogador == 1:
        cor = CINZA
    elif jogador == 2:
        cor = BRANCO

    pygame.draw.line(tela, cor, (15, 15), (LARGURA - 15, ALTURA - 15), WIN_LARGURALINHA - 5)


def RESTART():
    tela.fill(CIANO, )
    linha_tab()
    jogador = 1
    for linha in range(COORDLINHA):
        for coluna in range(COORDCOLUNA):
            COORDENADAS[linha][coluna] = 0


linha_tab()
FIM = False

while True:
    for event in pygame.event.get():

        # SAIDA
        if event.type == pygame.QUIT:
            sys.exit()

        # CLICK
        if event.type == pygame.MOUSEBUTTONDOWN and not FIM:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicklinha = int(mouseY // 200)
            clickcoluna = int(mouseX // 200)

            if LIVRE(clicklinha, clickcoluna):

                if jogador == 1:
                    MARCA(clicklinha, clickcoluna, 1)
                    if VENCEU(jogador):
                        pygame.display.update()
                        FIM = True
                    jogador = 2
                    FORMAS()

                elif jogador == 2:
                    MARCA(clicklinha, clickcoluna, 2)
                    if VENCEU(jogador):
                        pygame.display.update()
                        FIM = True
                    jogador = 1
                    FORMAS()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                RESTART()
                jogador = 1
                FIM = False

            pygame.display.update()

    pygame.display.update()
