
from room import Room
from player import Player

print("""
*************************************      
*         Let's Play A GAME         *
*************************************
      """)

player_name = input('Enter your name: ')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(player_name, current_room=room['outside'])


print(player)
# Write a loop that:
while True:

    direction = input('Well you made it caption odvice the mansion on the permantly raining hilltop is not "where the baddie is". Go inside now ITs RAining and I am wet')

    if direction == 'q':
        break
    elif direction == 'n':
        player.current_room = room['oustide'].n_to
        print(player)
    else:
        print("where are you going i said inside im WET")


    foyer_stop = input('okay were in the foyer. which way are we going glorified steed?')

    if foyer_stop == 'q'
        break
    elif foyer_stop == 'n':
        player.current_room = room['foyer'].n_to
        print(player)
    elif foyer_stop == 's':
        player.current_room = room['foyer'].s_to
        print(player)
    elif foyer_stop == 'e':
        player.current_room = room['foyer'].e_to
        print(player)
    else:
        print("really your going to run at the wall full speed?")

    overlook_stop = input("Why is this overlook a cliff is this where they go to take off? ")

    if overlook_stop == 'q'
        break
    elif overlook_stop == 's':
        player.current_room = room['foyer']
        print(player)
    else:
        print(" You cannot fly like a vampire. go back inside ")

    foyer_stop2 = input('So deeper into the house?')

    if foyer_stop2 == 'q':
        break
    elif foyer_stop2 == 'n':
        player.current_room = room['overlook']
        print(player)
    elif foyer_stop2 == 's'
        player.current_room = room['outside']
        print(player)
    elif foyer_stop2 == 'e':
        player.current_room = room['narrow']
        print(player)
    else:
        print("really your going to run at the wall full speed?")

    if narrow_stop == 'q':
        break
    elif narrow_stop == 'n':
        player.current_room = room['treasure']
        print(player)
    elif narrow_stop == 'w'
        player.current_room = room['foyer']
        print(player)
    else:
        print("what are you bumping into for real?")

    if player.current_room == room['treasure']:

                print("""
***************************************************************
    CONGRATULATIONS YOU FOUND THE TREASURE ROOM YOU WIN!!!
***************************************************************
          """)
    break




    #
    # * Prints the current room name
    print(player.location)
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    #
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.

    comand = input("> ").split(',')
    
    if command[0] == 'q':
        break
    
    elif command[0] == 'n':
    
    elif command[0] == 'e':

    elif command[0] == 's':

    elif command[0] == 'w':
