#!/usr/bin/env python
# -*- coding: utf-8 -*-

# "THE BEER-WARE LICENSE" (Revision 42):
# <jbc.develop@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Juan BC


#===============================================================================
# DOCS
#===============================================================================

"""Solucion al problema del buscaminas para la competencia de programación de la
UTN-FRC.

Objetivo: Ser legible y servir de instroduccion a python

Problema originalmente propuesto: 
    http://www.programming-challenges.com/pg.php?page=downloadproblem&probid=110102&format=html

Nota se simplifico para trabajar solo con matrices cuadradas

"""

#===============================================================================
# META
#===============================================================================

__author__ = "Juan BC"
__license__ = "BeerWare"
__date__ = "2011/10/26"
__version__ = "0.1"
__email__ = "jbc.develop@gmail.com"
__homepage__ = "http://jbcabral.wordpress.com/"
__twitter__ = "@juanbcabral"


#===============================================================================
# FUNCTIONS
#===============================================================================

def read_n_lines(n):
    """Esta funcion lee las siguientes n linea de la entrada y las retorna
    como una lista de listas.
    
    """
    lines = []
    for _ in range(n):
        line = list(raw_input())
        lines.append(line)
    return lines
    
    
def increment(board, row, col):
    """Funcion de soporte para resolve que incrementa en uno todas los vecinoa
    a una mina
    
    """
    for row_d in (-1, 0, 1):
        for col_d in (-1, 0, 1):
            rowp = row + row_d
            colp = col + col_d
            if rowp < 0 or colp < 0 \
               or rowp >= len(board) or colp >= len(board[rowp]) \
               or board[rowp][colp] == "*":
                continue
            if board[rowp][colp] == ".":
               board[rowp][colp] = 0
            board[rowp][colp] += 1
    
    
def resolve(board):
    """Itera sobre cada celda y si encuentra una mina (*) incrementa todos
    sus cacilleros vacios en 1
    
    """
    for idx_row, row in enumerate(board):
        for idx_col, cell in enumerate(row):
            if cell == "*":
                increment(board, idx_row, idx_col)
    

def main():
    field = 0;
    while True:
        
        # leemos el tamaño de nuestro board
        n = int(raw_input())
        
        # si el tamaño de nuestro board es 0 salimos
        if n == 0:
            break
        
        # incrementamos el numero de field
        field += 1
        
        # leemos el tablero
        board = read_n_lines(n)
        
        # resolvemos el tablero
        resolve(board)
        
        # armamos la salida
        out = "\n".join(["".join([str(c) for c in row]) for row in board])
        
        # imprimimos la salida con su decoradores
        # y si queda algun "." lo reemplazamos por un cero
        print "Field #{0}:".format(field)
        print out.replace(".", "0")
        print ""


#===============================================================================
# MAIN
#===============================================================================

if __name__ == "__main__":
    main()
