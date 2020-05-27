from Commands import *



def play_game():
    create_character()
    env_house.map.set_starting_room(bedroom)
    delay_print("You wake up in your bedroom and there is an Axe and a Sword next to you.\n")
    delay_print("What would you like to do?\n")
    start_of_game.state = True
    while start_of_game.state:
        command()
    delay_print("You get out of bed\n")
    get_out_of_bed.state = True
    while get_out_of_bed.state:
        command()



play_game()
