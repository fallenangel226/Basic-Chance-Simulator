"""
This Class is used to run all the background calculation determined by chance.
Chance rules are based loosely on D&D die rules.


"""

# Imported Modules
from random import randint


# This class controls all probability counters and actions associated with combat.
# These functions are to be used by both users and their opponents to reduce excess
# coding and to create a more balanced combat gameplay.
class Combat:
    # Initializes chance dice
    def __init__(self):
        self.d20 = randint(1, 20)
        self.d12 = randint(1, 12)
        self.d10 = randint(0, 9)
        self.d08 = randint(1, 8)
        self.d06 = randint(1, 6)
        self.d04 = randint(1, 4)

    # Determines who has first strike
    def new_instance(self):
        self.d20 = randint(1, 20)
        return self.d20

    # Opponents action chance function
    def opponentchance(self):
        self.d20 = randint(1, 20)
        return self.d20

    # Chance function for defending against next opponents next turn
    # Returns player stat tree back to main
    def defend(self, player, opponent):
        # stat tree declarations
        stat_player = player
        stat_opp = opponent
        # Player defend chance dice roll
        self.d20 = randint(1, 20)
        # Successful attempt
        if self.d20 > stat_opp["defence"]:
            # Players defence counter to opponents next attack
            player_defence = int((self.d20 / 2) + stat_player["defence"])
            # Determines whether player has a shield equipped or not
            if stat_player["shield"]:
                print("3. not functional")
                return player_defence
            else:
                return player_defence
        # Unsuccessful attempt
        else:
            return None

    # Chance function for attacking with equipped weapon
    # Returns opponent stat tree back to main
    def attack(self, player, opponent):
        # Stat tree declarations
        stat_player = player
        stat_opp = opponent
        # Attack chance dice roll
        self.d20 = randint(1, 20)
        # Damage dealt calculator
        if self.d20 > stat_opp["defence"]:
            # successful attack
            print("weapon type: ", stat_player["weapon"])
            if stat_player["weapon"] == "sword":
                self.d08 = randint(1, 8)
                damage_counter = self.d20 + self.d08
                return damage_counter
            elif stat_player["weapon"] == "axe":
                self.d12 = randint(1, 12)
                damage_counter = self.d20 + self.d12
                return damage_counter
            else:
                print("Unknown weapon type.")
                return self.d20
        # Unsuccessful attack
        else:
            return None

    # Chance function for leaving combat
    def escape(self):
        # Die roll 1 determines a value between 0-9
        self.d10 = randint(1, 9)
        cast1 = self.d10
        # Die roll 2 determines a value between 0-9 then multiplies it by 10
        self.d10 = randint(1, 9)
        cast2 = self.d10
        castcorr = cast2 * 10
        # Combines roll1 and roll2 to create the chance percentage
        percentile = cast1 + castcorr
        if percentile >= 60:
            print("You successfully evaded your opponent.")
            return
        else:
            print("You failed to avoid capture.")
            return


