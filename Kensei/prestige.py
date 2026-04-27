#Kensei higashi Prestige functions 
import pygame
import csv
from math import *

"""Open CSV and read
when game starts
	load life time rocks from csv
	load prestige level from csv
	load strange matter from csv

	Prestige bonus= 1 + (prestige level * 0.01)
end"""


def prestige_start():
    pass


"""function fro get prestige level( life time rocks)
	prestige level = floor( cube_root( life time rocks /1,000,000,000,000) )
	return prestige level
end"""

def load_level():
    prestige_level = floor(#cube root (lifetimerocks /1,000,000,000,000))