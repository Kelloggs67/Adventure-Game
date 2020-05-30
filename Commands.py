
from Map import *
from nltk.corpus import wordnet as wn
all_items

all_statics


list_of_commands = { }




    


def command(room, object=None):
    key = input("> ")
    full_sentence = key
    words = key.split()
    action_string = " "
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
    # for command in list_of_commands:
    #    if command in key:
    #       action = list_of_commands[command]


















