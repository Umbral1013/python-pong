#!/usr/bin/python3

"""Programmer: Umbral1013
Name: Atrapa a Limonagrio.
Description: A simple game in which you catch Limonagrio if you type a 
number that happens to be an exact divisor of the prime numbers I've 
chosen.
atrapas a Limonagrio.
Creation date: 10/02/2024.
"""

import time
import random
from PIL import Image
from os import system

limonagrio = Image.open('limonagrio.jpg')

run = "s"
while run != "n":
    system("clear")
    print("### ATRAPA A LIMONAGRIO ###")
    print("¡Rápido! Limonagrio se escapa.")
    guess = int(input(">>> Teclea un número para alcanzarlo: "))
    guess = abs(guess)  # We can only have divisors of integers.
    primes = (2, 3, 5, 7, 11, 13, 17)
    random_prime = random.choice(primes)
    if ((guess % random_prime) == 0):
        print("¡Genial! Has atrapado a Limonagrio")
        time.sleep(1)
        limonagrio.show()
    else:
        print("¡Oh no! Limonagrio se ha escapado.")
    run = input(">>> ¿Quieres jugar de nuevo? (s/n): ")
