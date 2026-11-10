LOCATIONS = ["Beach", "Jungle", "Cave", "Old Bridge", "Lighthouse"]


def create_game_state(player_name):
    """Create and return the player's starting game information."""
    return {
        "name": player_name,
        "energy": 5,
        "location": "Beach",
        "inventory": [],
        "cave_clue": False,
        "bridge_crossed": False,
        "beacon_lit": False,
        "game_over": False,
        "won": False
    }


def move_to_location(state, destination):
    """Move the player to a valid location."""
    if destination not in LOCATIONS:
        return "That location does not exist."

    if destination == "Lighthouse" and not state["bridge_crossed"]:
        return "You must cross the Old Bridge before reaching the Lighthouse."

    state["location"] = destination
    return f"You are now at the {destination}."


def collect_item(state, item):
    """Add a useful object to the player's inventory."""
    available_items = {
        "Beach": "Rope",
        "Jungle": "Lantern"
    }

    location = state["location"]

    if location not in available_items:
        return "There is no useful object to collect here."

    if available_items[location] != item:
        return "That item cannot be collected here."

    if item in state["inventory"]:
        return f"You already collected the {item}."

    state["inventory"].append(item)
    return f"You collected the {item}!"


def spend_energy(state, amount):
    """Reduce the player's energy and check whether they have lost."""
    state["energy"] -= amount

    if state["energy"] <= 0:
        state["energy"] = 0
        state["game_over"] = True
        state["won"] = False
        return False

    return True


def explore_cave(state):
    """Explore the Cave to discover the clue needed for the bridge."""
    if state["location"] != "Cave":
        return "You must be in the Cave to explore it."

    if state["cave_clue"]:
        return "You have already discovered the cave clue."

    if not spend_energy(state, 1):
        return "You ran out of energy while exploring the Cave."

    state["cave_clue"] = True
    return "You discovered an ancient clue! It reveals how to cross the bridge."


def cross_bridge(state):
    """Cross the Old Bridge if the player has the required items and clue."""
    if state["location"] != "Old Bridge":
        return "You must be at the Old Bridge."

    if "Rope" not in state["inventory"]:
        return "You need a Rope to cross the bridge."

    if not state["cave_clue"]:
        return "You need to discover the clue in the Cave first."

    if not spend_energy(state, 1):
        return "You ran out of energy trying to cross the bridge."

    state["bridge_crossed"] = True
    return "You safely crossed the Old Bridge!"


def light_beacon(state):
    """Light the lighthouse beacon and win the game."""
    if state["location"] != "Lighthouse":
        return "You must be inside the Lighthouse."

    if not state["bridge_crossed"]:
        return "You must cross the Old Bridge first."

    if "Lantern" not in state["inventory"]:
        return "You need a Lantern to light the beacon."

    if not spend_energy(state, 1):
        return "You ran out of energy before lighting the beacon."

    state["beacon_lit"] = True
    state["game_over"] = True
    state["won"] = True

    return "The lighthouse beacon is shining! The rescue boat has spotted you!"


def take_risk(state):
    """Search a dangerous area, losing two energy points."""
    if not spend_energy(state, 2):
        return "The dangerous search exhausted your energy!"

    return "You searched the dangerous area. You lost 2 energy points."