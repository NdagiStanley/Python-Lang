# From CS50 lecture

from itertools import product
from string import ascii_letters, digits, punctuation
import cProfile

passcodes = []

with cProfile.Profile() as pr:
    for passcode in product((ascii_letters + digits + punctuation), repeat=4):
        passcodes.append(passcode)

pr.print_stats()
