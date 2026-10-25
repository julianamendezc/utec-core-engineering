#!/usr/bin/env python3

from safe_print_list import safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print(f"nb_print: {nb_print}")

nb_print = safe_print_list(my_list, 10)
print(f"nb_print: {nb_print}")

from safe_print_integer import safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
print("Resultado:", has_been_print)

value = "89"
has_been_print = safe_print_integer(value)
print("Resultado:", has_been_print)

value = 4.5
has_been_print = safe_print_integer(value)
print("Resultado:", has_been_print)