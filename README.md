# mystery_island
# The Lost Lighthouse

A Python text-adventure game set on Mystery Island.

## Requirements

- Python 3 installed.
- No external packages are required.

## Setup

1. Clone or download the project.
2. Open the project folder in your terminal.
3. Run the game:

   python main.py

## Game Rules

- You start with 5 energy points.
- You begin at the Beach.
- Collect the Rope at the Beach.
- Collect the Lantern in the Jungle.
- Explore the Cave to discover the bridge clue.
- Use the Rope and cave clue to cross the Old Bridge.
- Reach the Lighthouse and use the Lantern to light the beacon.
- You win when the lighthouse beacon is restored.
- You lose when your energy reaches zero.
- Searching a dangerous area costs 2 energy points.
- You can quit or replay the game.

## Locations

1. Beach
2. Jungle
3. Cave
4. Old Bridge
5. Lighthouse

## Running Tests

From the project root, run:

python -m unittest discover -s tests -v

## Known Limits

- The game does not save progress after exiting.
- The game uses text-based menus only.
- The game has no graphical interface.
- The player can revisit locations.
- The game uses simple predefined puzzles and decisions.

## Project Files

- main.py: Interactive game menu and player interaction.
- game.py: Game rules, energy, inventory and progression.
- tests/test_game.py: Automated tests.