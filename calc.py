#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Vamos a programar una calculadora

import sys

def main():
    print("calculadora")

def suma(num1, num2):
    return num1 + num2


if __name__ == "__main__": 
    Operando1 = int(sys.argv[2])
    Operando2 = int(sys.argv[3])
    print(suma(Operando1,Operando2))
