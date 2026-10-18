#!/usr/bin/env python3

def print_last_digit(number):
    ultimo_digito = abs(number) % 10
    print("{}".format(ultimo_digito))
    return ultimo_digito