from Commands import *




def play_game():
    create_character()
    world_map.set_starting_room(bedroom)
    player1.state = "in bed"
    delay_print("You wake up in your bed.")
    delay_print("What would you like to do?")
    count = 0
    while bed.state == "in bed":
        action = command()
        if bed.state == "in bed":
            if count <= 2:
                delay_print("Why don't you try getting out of bed.")
            else:
                continue
        count += 1
    in_house = True
    while in_house:
        command()



play_game()
