# Grafton Brown - TextBasedGame
def main():  # Main function containing gameplay loop and dict of rooms
    rooms = {  # dict containing key:value pairs for directions and item handling
        'Prison Cell': {
            'North': 'Great Hall',
            'East': 'Sewers',
            'Exit': 'Exit',
            'Item': 'Placeholder'
        },
        'Sewers': {
            'West': 'Prison Cell',
            'North': 'Basement',
            'Item': 'Poison',
            'Exit': 'Exit'
        },
        'Basement': {
            'West': 'Great Hall',
            'North': 'Kitchen',
            'South': 'Sewers',
            'Item': 'Torch',
            'Exit': 'Exit'
        },
        'Kitchen': {
            'North': 'Living Quarters',
            'South': 'Basement',
            'Item': 'Food',
            'Exit': 'Exit'
        },
        'Living Quarters': {
            'West': 'Throne Room',
            'South': 'Kitchen',
            'Item': 'Diary',
            'Exit': 'Exit'
        },
        'Great Hall': {
            'North': 'Throne Room',
            'West': 'Guard Tower',
            'East': 'Basement',
            'South': 'Prison Cell',
            'Item': 'Mead',
            'Exit': 'Exit'
        },
        'Guard Tower': {
            'North': 'Training Arena',
            'East': 'Great Hall',
            'Item': 'Armor',
            'Exit': 'Exit'
        },
        'Training Arena': {
            'North': 'Wizard Tower',
            'South': 'Guard Tower',
            'Item': 'Sword',
            'Exit': 'Exit'
        },
        'Wizard Tower': {
            'South': 'Training Arena',
            'Item': 'Spellbook',
            'Exit': 'Exit'
        },
        'Throne Room': {
            'South': 'Great Hall',
            'East': 'Living Quarters',
            'Item': 'Evil King'
        }
    }

    player = {'room': 'Prison Cell', 'items': []}  # Declare player dict with Key:value pairs/starting room/item array
    directions = {'North', 'South', 'East', 'West', 'Exit'}  # Inputs accepted while navigating rooms
    items = ['Poison', 'Torch', 'Food', 'Diary', 'Mead', 'Armor', 'Sword', 'Spellbook']  # Input validation for items
    command = ""
    show_instructions()  # function call for instructions
    while command != 'Exit':  # Loop for gameplay
        player_status(player, rooms, items)  # Returns player status
        player_input = [input.capitalize() for input in input('Enter a command:\n').split()]  # Capitalizes split input
        if len(player_input) == 1:  # input validation for input of [0] length with accepted inputs
            command = player_input[0]
            if command == 'Help':
                help_me()  # function call for help
            elif command == 'Exit':
                print('Thanks for playing!')
            else:
                print('Invalid Command')
                error_line()  # function call for formatting
        elif len(player_input) == 2:  # input validation for input of [1] length with accepted inputs
            command, argument = player_input
            if command == 'Go':  # if input length == 2 and [0] value is Go, function call on player_movement
                player_movement(argument, player, rooms, directions)
            elif command == 'Get':  # if input length == 2 and [0] value is Go, function call on item_handling
                item_handling(argument, player, items, rooms)
            else:
                print('Invalid Command')
                error_line()
        else:
            print("Invalid Command")
            error_line()


def error_line():  # function for formatting
    print('--------------------------------------------')


def victory_message():  # function for completion of game message, for readability
    error_line()
    print('You heroically throw open the door to the Evil King: Dom\'s Throne Room.')
    print('Equipped with weapons, armor, a magical staff, and the Evil King: Dom\'s secrets you read in his Diary.')
    print('You easily defeat the Evil King in combat and free the Kingdom.')
    print('Thanks for playing! I hope you had fun!')
    error_line()


def show_instructions():  # function containing instructions
    error_line()
    print("Welcome to the Evil Kingdom Text Adventure Game")
    print("Collect 8 items to win the game, or be killed by the Evil King: Dom.")
    print('Enter Go North, Go South, Go East, or Go West to move to a new room!\nEnter Exit to quit!')
    print("To add an item to inventory enter: get 'item name'")
    error_line()


def help_me():  # function that takes input during gameplay to provide valid commands
    error_line()
    print('Enter: Go North, Go South, Go East, or Go West to move to a new room.')
    print("To add an item to your inventory Enter: get 'item name'\nEnter: 'Exit' to quit!")
    error_line()


def player_movement(direction, player, rooms, directions): # function that manages room movement
    player_room_name = player["room"]
    player_room = rooms[player_room_name]
    if direction in directions:  # checks if input is in accepted list of inputs
        if direction in player_room:  # assigns player to new room if input is valid
            player["room"] = player_room[direction]
        else:
            print('You can\'t go that way from this room')  # Valid input, but invalid direction from current room
            error_line()
    else:
        print('Invalid Direction, Enter help for valid commands!')  # Invalid input, returns help command


def item_handling(item, player, items, rooms):  # function for item handling
    player_room_name = player["room"]
    player_room = rooms[player_room_name]
    room_item = player_room["Item"]
    if item in items:  # input validation for items
        if room_item in player["items"]:
            print('You already have the item from this room.')
        elif item == room_item and room_item not in player["items"]:  # checks item array for various outputs
            player['items'].append(room_item)
            print(f'Your inventory now has {player["items"]} in it!')
            if len(player["items"]) >= 7:
                print('Congratulations you found all the items! Now find the Evil King!')
        else:
            print('That item isn???t in this room!')
    else:
        print('Invalid Item!')
    error_line()


def player_status(player, rooms, items):  # player status function that loops in main gameplay
    player_room_name = player["room"]
    player_room = rooms[player_room_name]
    room_item = player_room["Item"]
    if player_room_name == 'Throne Room' and len(player["items"]) >= 7:  # if item array >= 7 the game is won.
        victory_message()  # function call for victory message
        exit()
    elif player_room_name == 'Throne Room' and len(player["items"]) < 7: # if item array < 7 the game is lost
        print('You entered the Throne Room unprepared! The Evil King: Dom kills you instantly!\nGAME OVER')
        exit()
    elif room_item in items and room_item not in player['items']:  # input validation and various outputs
        print(f'You are in the {player_room_name}')  # Returns updated player room
        print(f'The rooms item is {room_item}')
        print(f'Your inventory is {player["items"]}')
    elif room_item in player_room and room_item in player["items"]:  # various outputs depending on current player value
        print(f'You are in the {player_room_name}')  # Returns updated player room
        print(f'You already have the item from this room!')
        print(f'Your inventory is {player["items"]}')
    else:
        print(f'You are in the {player_room_name}')  # Returns updated player room
        print('The current room has no item!')
        print(f'Your inventory is {player["items"]}')
    error_line()


if __name__ == '__main__':  # main function call
    main()

