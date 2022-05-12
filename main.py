# Necessary Imports
import sqlite3
import random
with sqlite3.connect("Game Idea\Death Chance.db") as db:
    cursor = db.cursor()

# Constant Values
skills = ["Logical", "Creative", "Handy"]
skill = random.choice(skills)
day_length = 24
primary_school_start = 4
secondary_school_start = 11
consent_age = 16
adult_age = 18

# Person
class Person:
    def __init__(self, name, age, alive, skill):
        self.skill = skill
        self.name = name
        self.age = age
        self.alive = alive

# Extract Death Rate from database
def death_chance(age):
    cursor.execute(f"""SELECT Death_Chance FROM Death WHERE Age = {age}""")
    x = cursor.fetchone()
    x = float(x[0])
    return x

# Player chooses their name and is created
print("Please choose a name: ")
name = input()
player = Person(name, 0, True, skill)

print(player.skill)
# Game
while player.alive:
    # Checks if you will die
    try:
        will_die = death_chance(player.age)
    except:
        will_die = 6
    if random.randint(1, will_die) == 1:
        print(f"You died at age {player.age}")
        break
    
    # Tells your age
    print(f"You are {player.age} years old")

    # School System
    if player.age == primary_school_start:
        print("You have started primary school\n")
    if player.age == secondary_school_start:
        print("You have ended primary school\n")
        print("You have started secondary school\n")

    # Age System
    print("Press enter to age!")
    input()
    player.age +=1





