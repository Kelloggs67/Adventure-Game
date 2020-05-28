from Commands import *



def play_game():
    create_character()
    current_room = env_house.map.set_starting_room(bedroom)
    delay_print("You wake up in your bedroom and there is an Axe and a Sword next to you.\n")
    delay_print("What would you like to do?\n")
    start_of_game.state = True
    while not get_out_of_bed:
        current_environment = env_house
        command(current_room, current_environment)
        current_room = env_house.map.current_room
    delay_print("You get out of bed\n")
    get_out_of_bed.state = True
    while not leave_room.state:
        command(current_room, current_environment)



play_game()
