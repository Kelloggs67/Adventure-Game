from Commands import *



def play_game():
    player1 = create_character()
    house.set_starting_room(bedroom)
    delay_print("You wake up in {0}.\n".format(house.current_room.name))
    delay_print("What would you like to do?\n")
    count = 0
    while bed.state == "in bed":
        current_room = house.current_room
        action = command(current_room)
        if bed.state == "in bed":
            if count <= 2:
                delay_print("Why don't you try getting out of bed.\n")
            else:
                continue
        count += 1
    delay_print("You get out of bed\n")
    in_house = True
    while in_house:
        current_room = house.current_room
        command(current_room)



play_game()
