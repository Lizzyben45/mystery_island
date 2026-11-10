import unittest

from game import (
    create_game_state,
    move_to_location,
    collect_item,
    explore_cave,
    cross_bridge,
    light_beacon,
    take_risk
)


class TestLostLighthouse(unittest.TestCase):

    def setUp(self):
        self.state = create_game_state("Lizzy")

    def test_initial_game_state(self):
        self.assertEqual(self.state["energy"], 5)
        self.assertEqual(self.state["location"], "Beach")
        self.assertEqual(self.state["inventory"], [])

    def test_move_to_valid_location(self):
        move_to_location(self.state, "Jungle")
        self.assertEqual(self.state["location"], "Jungle")

    def test_invalid_location(self):
        move_to_location(self.state, "Desert")
        self.assertEqual(self.state["location"], "Beach")

    def test_collect_rope(self):
        collect_item(self.state, "Rope")
        self.assertIn("Rope", self.state["inventory"])

    def test_collect_item_only_once(self):
        collect_item(self.state, "Rope")
        collect_item(self.state, "Rope")
        self.assertEqual(self.state["inventory"].count("Rope"), 1)

    def test_collect_lantern(self):
        move_to_location(self.state, "Jungle")
        collect_item(self.state, "Lantern")
        self.assertIn("Lantern", self.state["inventory"])

    def test_cave_exploration(self):
        move_to_location(self.state, "Cave")
        explore_cave(self.state)

        self.assertTrue(self.state["cave_clue"])
        self.assertEqual(self.state["energy"], 4)

    def test_cannot_cross_without_rope(self):
        move_to_location(self.state, "Old Bridge")
        cross_bridge(self.state)

        self.assertFalse(self.state["bridge_crossed"])

    def test_cannot_cross_without_cave_clue(self):
        collect_item(self.state, "Rope")
        move_to_location(self.state, "Old Bridge")
        cross_bridge(self.state)

        self.assertFalse(self.state["bridge_crossed"])

    def test_successful_bridge_crossing(self):
        collect_item(self.state, "Rope")
        move_to_location(self.state, "Cave")
        explore_cave(self.state)
        move_to_location(self.state, "Old Bridge")

        cross_bridge(self.state)

        self.assertTrue(self.state["bridge_crossed"])
        self.assertEqual(self.state["energy"], 3)

    def test_cannot_reach_lighthouse_before_crossing(self):
        move_to_location(self.state, "Lighthouse")
        self.assertEqual(self.state["location"], "Beach")

    def test_successful_beacon_lighting(self):
        collect_item(self.state, "Rope")
        move_to_location(self.state, "Jungle")
        collect_item(self.state, "Lantern")
        move_to_location(self.state, "Cave")
        explore_cave(self.state)
        move_to_location(self.state, "Old Bridge")
        cross_bridge(self.state)
        move_to_location(self.state, "Lighthouse")

        light_beacon(self.state)

        self.assertTrue(self.state["beacon_lit"])
        self.assertTrue(self.state["won"])
        self.assertTrue(self.state["game_over"])

    def test_running_out_of_energy(self):
        take_risk(self.state)
        take_risk(self.state)
        take_risk(self.state)

        self.assertEqual(self.state["energy"], 0)
        self.assertTrue(self.state["game_over"])
        self.assertFalse(self.state["won"])


if __name__ == "__main__":
    unittest.main()