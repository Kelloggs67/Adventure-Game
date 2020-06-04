from Commands import *




def play_game():
    create_character()
    world_map.set_starting_room(bedroom)
    player1.state = "in bed"
    delay_print("You wake up in your bed.")
    delay_print("What would you like to do?")
    count = 0
    compliance = False
    while bed.state == "in bed":
        action = command()
        if compliance == True:
            if action in confirm_commands:
                delay_print("Try typing: \"get out of bed\".")
                count += 1
                continue
            else:
                compliance = False
        if bed.state == "in bed":
            if count <= 2:
                delay_print("Why don't you try getting out of bed.")
                compliance = True
            elif count <= 4:
                delay_print("You won't be able to do anything until you get out of bed.")
                compliance = True
            elif count <= 5:
                delay_print("...")
                compliance = True
            elif count <= 6:
                delay_print("Jesus Christ, c'mon.")
                compliance = True
            elif count <= 7:
                delay_print("Okay, I'll stop bothering you about it then.\nWhen you're ready, try getting out of bed.")
                compliance = True
            else:
                continue
        count += 1
    in_house = True
    while in_house:
        command()



play_game()
