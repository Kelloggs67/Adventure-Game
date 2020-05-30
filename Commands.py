from Map import *
from nltk.corpus import wordnet as wn
all_items

all_statics


dict_of_commands = {"move": change_rooms, "go into": change_rooms, "enter": change_rooms, "leave": leave_room}
def get_keys(value):
    keys = []
    times_in_thing = []
    for thing in list(dict_of_commands.values()):
        if value in thing.__name__:
            times_in_thing.append(value)
            for values in times_in_thing:
                if values == value:
                    keys.append(dict_of_commands.keys())
                    return keys


def command_2(words):
    for command in dict_of_commands.keys():
        if command in words:
            action = dict_of_commands[command]
            if action in get_keys("change_rooms"):
                for word in words:
                    for room in house.map_dict.keys():
                        if word in room.name:
                            check_player_state(action)
                            action(room)
                            delay_print("Moving to " + house.map_dict[word.name])
                        else:
                            delay_print("That doesn't exist")
            else:
                continue





def command(room):
    key = input("> ")
    full_sentence = key
    room = house.current_room
    words_original = key.split()
    words = key.split()
    action_string = " "
    if key == ("inventory" or "pockets"):
        if not player1.inventory:
            delay_print("You don't have anything on you.")
        else:
            return print(player1.inventory)
    elif key == ("stats" or "statistics"):
        return print(player1)
    elif key == ("room" or "current room"):
        return print("You're in " + house.current_room.name)
    else:
        for word in words:
            if word in room.objects:
                object_to_take_action_on = room.objects[word]
                words.pop(words.index(word))
                if not words:
                    return delay_print(object_to_take_action_on.description)
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
                    check_player_state(action)
                    return action()
            else:
                command_2(words_original)






def check_player_state(action):
    if player1.state:
        if action.__name__ in player1.change_state:
            return action()
        else:
            return delay_print("You can't do that while " + player1.state)










