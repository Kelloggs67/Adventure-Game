from Player import *
from Items import *
from Map import *
from Rooms import *
from Commands import *

def create_character():
    print("What is your name?")
    name_input = input("> ").strip().capitalize()
    player1.name = name_input
    return player1


def play_game():
    player1 = create_character()
    print("Hello " + player1.name)
    house = build_house()
    house.set_starting_room(bedroom)
    print("You wake up in your bedroom and there is an Axe and a Sword next to you.")
    print("What would you like to do?")
    playing = True
    while playing:
        action = input("> ")



play_game()
