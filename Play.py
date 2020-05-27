from Player import *
from Items import *
from Map import *
from Commands import *
import sys,time,random

typing_speed = 120

def delay_print(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)


class Command:
    def __init__(self, key):
        self.key = key
        self.list_of_commands = list_of_commands

    def find_action(self):
        self.key



def command():
    key = input("> ")
    command = Command(key)
    command.find_action()



def create_character():
    delay_print("What is your name?\n")
    name_input = input("> ").strip().capitalize()
    player1.name = name_input
    delay_print("Hello " + player1.name + "\n")
    time.sleep(2)
    return player1

def play_game():
    player1 = create_character()
    house = build_house()
    house.set_starting_room(bedroom)
    delay_print("You wake up in your bedroom and there is an Axe and a Sword next to you.\n")
    delay_print("What would you like to do?\n")
    playing = True
    while playing:
       command()


play_game()
