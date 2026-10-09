"""Project Two starter for the student's text-based adventure game."""

# Full-name comment required by Project Two directions.
# Loriel Marissa Armstrong-Fraser

def show_instructions():
    """Display the game objective and available commands."""
    print("Welcome to the Castle Adventure Game!")
    print("Collect all 6 items to win the game, or be defeated by Randy!")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get [item name]")
    print("Type 'exit' to leave the game.")
    print("-" * 25)


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {inventory}")
    
    # Show the current-room item when one is available.
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("-" * 25)


def main():
    """Run the main gameplay loop."""
    # Create the full room/item dictionary from your Project One map.
    rooms = {
        'Entrance Hall': {'north': 'Boss Chamber', 'west': 'Armor Room'},
        'Armor Room': {'east': 'Entrance Hall', 'north': 'Laboratory', 'item': 'Shield'},
        'Laboratory': {'south': 'Armor Room', 'north': 'Treasury', 'item': 'Potion'},
        'Treasury': {'south': 'Laboratory', 'east': 'Observatory', 'item': 'Amulet'},
        'Observatory': {'west': 'Treasury', 'east': 'Armory', 'item': 'Key'},
        'Armory': {'west': 'Observatory', 'south': 'Library', 'item': 'Sword'},
        'Library': {'north': 'Armory', 'west': 'Boss Chamber', 'item': 'Spell Book'},
        'Boss Chamber': {'south': 'Entrance Hall', 'east': 'Library', 'item': 'Randy'}
    }

    # Set the player's starting room.
    current_room = 'Entrance Hall'

    # Create the player's inventory.
    inventory = []

    # Call the instruction function at the appropriate time.
    show_instructions()

    # Create the gameplay loop.
    while True:
        # Show player status.
        show_status(current_room, inventory, rooms)

        # Check for win/loss conditions if entering the Boss Chamber
        if current_room == 'Boss Chamber':
            if len(inventory) == 6:
                print("Congratulations! You have collected all items and defeated Randy! You win!")
            else:
                print("NOM NOM... GAME OVER!")
                print("You were defeated by Randy because you didn't have all 6 items.")
            break # Ends the game

        # Prompt for the player's next command.
        # .split(" ", 1) splits the input into two parts: the action (go/get) and the target (direction/item)
        user_input = input("Enter your move: ").strip().lower().split(" ", 1)
        
        # Branching for the "exit" command
        if user_input[0] == 'exit':
            print("Thanks for playing! Exiting game...")
            break
            
        # Error handling if the user types a single word that isn't 'exit'
        if len(user_input) != 2:
            print("Invalid command! Please use 'go [direction]' or 'get [item]'.")
            continue
            
        action = user_input[0]
        target = user_input[1]

        # Branching for movement
        if action == 'go':
            if target in rooms[current_room]:
                current_room = rooms[current_room][target]
            else:
                print("You can't go that way!")
                
        # Branching for getting items
        elif action == 'get':
            # Check if the room has an item and if the typed item matches the room's item
            if "item" in rooms[current_room] and target == rooms[current_room]["item"].lower():
                inventory.append(rooms[current_room]["item"])
                print(f"{rooms[current_room]['item']} retrieved!")
                # Remove the item from the room's dictionary once it's picked up
                del rooms[current_room]["item"]
            else:
                print(f"Can't get {target}! It is not in this room.")
                
        # Error handling for invalid actions (like typing 'run north' instead of 'go north')
        else:
            print("Invalid command! Please use 'go [direction]' or 'get [item]'.")


# This executes the main function when the script is run
if __name__ == "__main__":
    main()
