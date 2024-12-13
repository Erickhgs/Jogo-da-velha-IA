# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
         # -*- Verificando linhas -*-
        for l in range (0,3):
         somal=0
         for c in range (0,3):
           somal += self.matriz[l][c]
         if somal == 12:
            return Tabuleiro.JOGADOR_X
         elif somal == 3:
            return Tabuleiro.JOGADOR_0
         
        # -*- Verificando colunas -*-
        for c in range (0,3):
         somal=0
         for l in range (0,3):
           somal += self.matriz[l][c]
         if somal == 12:
            return Tabuleiro.JOGADOR_X
         elif somal == 3:
            return Tabuleiro.JOGADOR_0
         
         # -*- Verificando diagonais -*-
        somad=0
        somads=0
        for d in range (0,3):
         somad += self.matriz[d][d]
         somads += self.matriz[d][2-d]
        if somad == 12 or somads == 12 :
            return Tabuleiro.JOGADOR_X
        elif somad == 3 or somads == 3:
            return Tabuleiro.JOGADOR_0