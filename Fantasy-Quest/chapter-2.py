# Chapter 2: The Journey Continues

# Lesson 1
player_health = 1000
# don't touch below this line
print(player_health)

# Lesson 2
player_health = 1000

# reduce by 100 here
player_health -= 100
print(player_health)

# and here
player_health -= 100
print(player_health)

# and here
player_health -= 100
print(player_health)

# and here
player_health -= 100
print(player_health)

# Lesson 3
player_health = 1000
armor_multiplier = 2
armored_health = player_health * armor_multiplier

print(armored_health)

# Lesson 4
player_health = 100
poison_damage = -10

player_poison_health = player_health + poison_damage

print(player_poison_health)

# Lesson 5
# the best_sword variable holds the value of the best sword in the game
best_sword = "scimitar"
print(best_sword)

# Lesson 6
player_health = 100

player_has_magic = True

# don't touch below this line
print("player_health is a/an ", type(player_health).__name__)
print("player_has_magic is a/an ", type(player_has_magic).__name__)

# Lesson 7
name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print(f"{name} is a {race} who is {age} years old.")

# Lesson 8
# create the empty "enemy" variable here

enemy = None

# don't touch below this line
print(enemy is None)

# Lesson 9
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(f"{sentence_start}{player1_health}{sentence_end}")
print(f"{sentence_start}{player2_health}{sentence_end}")

# Lesson 10
quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

# don't touch above this line
print(f"{quest_start}\n{quest_middle}\n{quest_end}{space}{quest_objective}")

# Lesson 11
game_one_score = 97
game_two_score = 92
game_three_score = 106
game_four_score = 105

# Don't touch above this line

average_score = (game_one_score + game_two_score + game_three_score + game_four_score) / 4

# Don't touch below this line

print(round(average_score))

# Lesson 12
name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 15.0
account_active = True

# Don't edit below this line

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")

# End of Chapter 2