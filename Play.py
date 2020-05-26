def create_character():
    name_input = input("What is your name?").strip().capitalize()
    player1.name = name_input


def play_game():
    player1 = create_character()
    print("Hello " + player1.name)
    print("You wake up and there is an Axe and a Sword next to you.")
    print("What would you like to do?")
    playing = True
    while playing:
        action = input("> ")
play_game()
