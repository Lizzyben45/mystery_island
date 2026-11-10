# main.py

from game import (
    create_game_state,
    move_to_location,
    collect_item,
    explore_cave,
    cross_bridge,
    light_beacon,
    take_risk
)


def display_instructions():
    print("\n================================")
    print("       THE LOST LIGHTHOUSE")
    print("================================")
    print("Welcome to Mystery Island!")
    print("\nYour rescue boat will only find you")
    print("if you restore the lighthouse beacon.")
    print("\nExplore five locations:")
    print("Beach, Jungle, Cave, Old Bridge and Lighthouse.")
    print("\nCollect useful objects, solve the cave puzzle")
    print("and manage your energy carefully.")
    print("You start with 5 energy points.")
    print("\nGood luck, adventurer!")


def display_status(state):
    print("\n---------- PLAYER STATUS ----------")
    print("Player:", state["name"])
    print("Energy:", state["energy"])
    print("Location:", state["location"])
    print("Inventory:", state["inventory"])
    print("-----------------------------------")


def display_menu():
    print("\n========== MYSTERY ISLAND ==========")
    print("1. Explore Beach")
    print("2. Explore Jungle")
    print("3. Explore Cave")
    print("4. Visit Old Bridge")
    print("5. Visit Lighthouse")
    print("6. Search a dangerous area")
    print("7. Check Inventory")
    print("8. Check Energy")
    print("9. Quit Game")


def run_game():
    """Run one complete game session."""
    display_instructions()

    name = input("\nEnter your name: ").strip()

    if not name:
        name = "Adventurer"

    state = create_game_state(name)

    print(f"\nWelcome, {name}! Your adventure begins.")

    while not state["game_over"]:

        display_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            print(move_to_location(state, "Beach"))
            print(collect_item(state, "Rope"))

        elif choice == "2":
            print(move_to_location(state, "Jungle"))
            print(collect_item(state, "Lantern"))

        elif choice == "3":
            print(move_to_location(state, "Cave"))

            if state["location"] == "Cave":
                decision = input(
                    "Explore the Cave and spend 1 energy? (yes/no): "
                ).strip().lower()

                if decision == "yes":
                    print(explore_cave(state))
                elif decision == "no":
                    print("You decided not to explore the Cave.")
                else:
                    print("Invalid response. You remain in the Cave.")

        elif choice == "4":
            print(move_to_location(state, "Old Bridge"))

            if state["location"] == "Old Bridge":
                decision = input(
                    "Attempt to cross the bridge? (yes/no): "
                ).strip().lower()

                if decision == "yes":
                    print(cross_bridge(state))
                elif decision == "no":
                    print("You decided not to cross the bridge.")
                else:
                    print("Invalid response. You remain at the bridge.")

        elif choice == "5":
            print(move_to_location(state, "Lighthouse"))

            if state["location"] == "Lighthouse":
                decision = input(
                    "Use your Lantern to light the beacon? (yes/no): "
                ).strip().lower()

                if decision == "yes":
                    print(light_beacon(state))
                elif decision == "no":
                    print("You decided not to light the beacon.")
                else:
                    print("Invalid response. You remain in the Lighthouse.")

        elif choice == "6":
            print(take_risk(state))

        elif choice == "7":
            print("Your inventory:", state["inventory"])

        elif choice == "8":
            print("Your remaining energy:", state["energy"])

        elif choice == "9":
            print("You decided to leave Mystery Island.")
            state["game_over"] = True
            state["won"] = False

        else:
            print("Invalid menu choice. Please choose a number from 1 to 9.")

    if state["won"]:
        print("\nCONGRATULATIONS!")
        print(f"{name}, you restored the lighthouse and escaped Mystery Island!")
    elif state["energy"] == 0:
        print("\nGAME OVER!")
        print(f"{name}, you ran out of energy on Mystery Island.")
    else:
        print("\nYou quit the adventure. Better luck next time!")


def main():
    """Allow the player to replay the game."""
    while True:
        run_game()

        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()

        if replay != "yes":
            print("Thank you for playing The Lost Lighthouse!")
            break


if __name__ == "__main__":
    main()