from Map import *
from nltk.corpus import wordnet as wn




def command():
    key = input("> ")
    full_sentence = key
    room = world_map.current_room
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
        return print("You're in " + world_map.current_room.name)
    for useless in words:
        if useless == "the" or useless == "of":
            words.pop(words.index(useless))
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
                    functionality = check_player_state(action)
                    if functionality == False:
                        return
                    else:
                        return action()
        for word in words:
            for room_name in world_map.map_dict.keys():
                if word in room_name:
                    room_to_go_to = world_map.map_dict[room_name]
                    words.pop(words.index(word))
                    for other_words in words:
                        for commands in change_room_commands:
                            if other_words in commands:
                                if other_words in action_string:
                                    continue
                                else:
                                    action_string += (" " + other_words)
                            else:
                                continue
                    if action_string.strip() in change_room_commands:
                        action = world_map.functions[change_room_commands]
                        functionality = check_player_state(action)
                        if functionality == False:
                            return
                        else:
                            return action(room_to_go_to, action_string.strip())


                




def check_player_state(action):
    if player1.state:
        if action.__name__ in player1.change_state:
            return True
        else:
            delay_print("You can't do that while " + player1.state)
            return False








