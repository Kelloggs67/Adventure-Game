from Commands import *



def play_game():
    create_character()
    house.set_starting_room(bedroom)
    player1.state = "in bed"
    delay_print("You wake up in your bed")
    delay_print("What would you like to do?")
    count = 0
    while bed.state == "in bed":
        current_room = house.current_room
        action = command(current_room)
        if bed.state == "in bed":
            if count <= 2:
                delay_print("Why don't you try getting out of bed.")
            else:
                continue
        count += 1
    delay_print("You get out of bed")
    in_house = True
    while in_house:
        current_room = house.current_room
        command(current_room)



play_game()
