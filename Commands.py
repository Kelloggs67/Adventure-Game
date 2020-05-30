
from Map import *
from nltk.corpus import wordnet as wn
all_items

all_statics


dict_of_commands = {"move": change_rooms, "go into": change_rooms, "enter": change_rooms}



def command_2(words, room):
    for command in dict_of_commands:
        if command in words:
            action = dict_of_commands[command]
            if action == change_rooms:
                for word in words:
                    if word in house.map_dict:
                        action(house.map_dict[word])
                        delay_print("Moving to " + house.map_dict[word.name])
                    else:
                        continue
            else:
                delay_print("No use for that yet.")
    


def command(room):
    key = input("> ")
    full_sentence = key
    words = key.split()
    action_string = " "
    if key == ("inventory" or "pockets"):
        if not player1.inventory:
            delay_print("You don't have anything on you.\n")
        else:
            return print(player1.inventory)
    elif key == ("stats" or "statistics"):
        return print(player1)
    elif key == ("room" or "current room"):
        return print(house.current_room.name)
    else:
        for word in words:
            if word in room.objects:
                object_to_take_action_on = room.objects[word]
                words.pop(words.index(word))
                if not words:
                    return delay_print(object_to_take_action_on.description + "\n")
                for other_words in words:
                    for interaction in object_to_take_action_on.interactions.keys():
                        if other_words in interaction:
                            if other_words in action_string:
                                continue
                            else:
                                action_string += (" " + other_words)
                        else:
                            continue
                if action_string.strip() in object_to_take_action_on.interactions.keys():
                    action = object_to_take_action_on.interactions[action_string.strip()]
                    if player1.state:
                        if action.__name__ in player1.change_state:
                            return action()
                        else:
                            return delay_print("You can't do that while " + player1.state + "\n")
                    return action()
            else:
                command_2(words, room)


















