from room import Room
from player import Player

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

newPlayer = Player(input("Please enter your name"), room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# def move():
#     direction = input("> ")
#     if direction != 'n' or 's' or 'e' or 'w':
#         print("Please enter a valid direction!")
#     else:
#         print("Go ahead!")

# move()

while True:
    currentLocation = newPlayer.location
    print(currentLocation.name)
    print(currentLocation.description)
    cmd = input("Where do you want to go? > ")

    if cmd == "q":
        break
    elif cmd == "n":
        newPlayer.current_room = newPlayer.current_room.n_to
    elif cmd == "s":
        newPlayer.current_room = newPlayer.current_room.s_to
    elif cmd == "w":
        newPlayer.current_room = newPlayer.current_room.w_to
    elif cmd == "e":
        newPlayer.current_room = newPlayer.current_room.e_to
    else:
        print('Please enter a valid direction: "n", "s", "w", "e", or "q" to quit.')