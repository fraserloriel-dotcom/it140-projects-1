"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"}
}

current_room = "Great Hall"

while True:
    # 1. Display the current room.
    print(f"\nYou are currently in the {current_room}.")
    
    # 2. Prompt for a movement command or "exit".
    command = input("Enter a direction to move (north, south, east, west) or 'exit': ").strip().lower()
    
    # 3. Branch for a valid move, exit, or invalid input.
    if command == "exit":
        # 5. Continue until the required exit condition is reached.
        print("Thanks for playing! Exiting game...")
        break
        
    elif command in rooms[current_room]:
        # 4. Update the room only after a valid movement command.
        current_room = rooms[current_room][command]
        print(f"You moved {command}.")
        
    else:
        # Handling invalid input / walking into walls
        print("You can't go that way!")
