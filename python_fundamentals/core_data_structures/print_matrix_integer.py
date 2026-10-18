#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        print(" ".join("{:d}".format(numero) for numero in fila))
