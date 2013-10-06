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

Problema originalmente propuesto: http://acm.tju.edu.cn/toj/showp1330.html

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
    """Esta funcion lee las siguientes n lineas del file pointer
    
    """
    lines = []
    for _ in range(n):
        line = list(raw_input())
        lines.append(line)
    return lines
    
    
def touch2coordinates(touch):
    """Combierte los "toques" a una lista de coordenadas (fila, columna)
    donde se toco.
    
    """
    coords = []
    for idx_row, row in enumerate(touch):
        for idx_col, cell in enumerate(row):
            if cell == ".":
                continue
            coords.append((idx_row, idx_col))
    return coords
            

def coord2mine(row, col, board):
    """Retorna un "*" si el lugar donde indica la cordenada tiene una mina
    en caso contrario retorna cuantas minas rodean a ese lugar.
    
    """
    # primero nos fijamos en el lugar
    if board[row][col] == "*":
        return "*"
    # sino exploramos
    mines = 0
    for row_d in (-1, 0, 1):
        for col_d in (-1, 0, 1):
            rowp = row + row_d
            colp = col + col_d
            if rowp < 0 or colp < 0 \
               or rowp >= len(board) or colp >= len(board[rowp]):
                continue
            if board[rowp][colp] == "*":
                mines += 1
    return str(mines)


def main():
    """Lee desde un archivo un tablero y toques del buscaminas. Por defecto
    usa la salida estandar.
    
    """
    # leemos
    n = int(raw_input())
    board = read_n_lines(n)
    touchs = read_n_lines(n)

    # resolvemos
    for row, col in touch2coordinates(touchs):
        symbol = coord2mine(row, col, board)
        touchs[row][col] = symbol

    # convertimos a string para imprimir por pantalla
    print "\n".join(["".join([c for c in row]) for row in touchs])


#===============================================================================
# MAIN
#===============================================================================

if __name__ == "__main__":
    main()


