#!/usr/bin/env python3
Square = __import__('2-square').Square

print(Square(3).__dict__)
print(Square().__dict__)

try:
    Square("3")
except Exception as e:
    print(e)

try:
    Square(-89)
except Exception as e:
    print(e)