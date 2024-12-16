# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
      # Regra 1  
        # Verificando linhas e colunas vitoria
        somal=0 
        for l in range (0,3):
         for c in range (0,3):
           somal += self.matriz[l][c]
         if somal == 2:
            for c in range (0,3):
               if self.matriz[l][c] == Tabuleiro.DESCONHECIDO: 
                return (l,c)
         somal=0    
        for c in range (0,3):
         for l in range (0,3):
           somal += self.matriz[l][c]
         if somal == 2 :
            for l in range (0,3):
               if self.matriz[l][c] == Tabuleiro.DESCONHECIDO: 
                return (l,c)
         somal=0
        # Verificando linhas e colunas bloqueio
        for l in range (0,3):
         for c in range (0,3):
           somal += self.matriz[l][c]
         if somal == 8:
            for c in range (0,3):
               if self.matriz[l][c] == Tabuleiro.DESCONHECIDO: 
                return (l,c)
         somal=0
        for c in range (0,3):
         for l in range (0,3):
           somal += self.matriz[l][c]
         if somal == 8 :
            for l in range (0,3):
               if self.matriz[l][c] == Tabuleiro.DESCONHECIDO: 
                return (l,c)
         somal=0
        # Verificando diagonais
        somad = 0
        somads = 0
        for d in range(0, 3):
         somad += self.matriz[d][d]
         somads += self.matriz[d][2 - d]

        if somad == 2:
         for d in range(0, 3):
          if self.matriz[d][d] == Tabuleiro.DESCONHECIDO: 
            return (d, d)

        if somads == 2:
         for d in range(0, 3):
          if self.matriz[d][2 - d] == Tabuleiro.DESCONHECIDO:
            return (d, 2 - d)

        if somad == 8:
         for d in range(0, 3):
          if self.matriz[d][d] == Tabuleiro.DESCONHECIDO: 
            return (d, d)

        if somads == 8:
         for d in range(0, 3):
          if self.matriz[d][2 - d] == Tabuleiro.DESCONHECIDO:  
            return (d, 2 - d)
          
      
        # Regra 2
        for l in range(3):
            for c in range(3):
                somal = somal + self.matriz[l][c]
            if somal == 1:
                somal = 0
                for a in range(3):
                    for b in range(3):
                        somal = somal + self.matriz[b][a]
                    if somal == 1:
                        if self.matriz[l][a] == Tabuleiro.DESCONHECIDO:
                            return (l, a)
                    somal=0
            somal=0
               
       
        # Regra 3 
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO: 
            return (1, 1)
        
        # Regra 4
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto in cantos:
          l, c = canto
          if self.matriz[l][c] != Tabuleiro.DESCONHECIDO:
             l_oposto, c_oposto = 2 - l, 2 - c
             if self.matriz[l_oposto][c_oposto] == Tabuleiro.DESCONHECIDO:
                return (l_oposto, c_oposto)
             
        # Regra 5
        aleatorio = []
        for l, c in cantos:
         if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
           aleatorio.append((l,c))
        if(len(aleatorio) > 0):
            p = randint(0, len(aleatorio)-1)
            return aleatorio[p]
        
        # Regra 6
        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
                    
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        
      