"""
This program generates passages that are generated in mad-lib format for the user to create a wacky story.
Author: Andre S. Bamba
"""

# The template for the story

import time

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Welcome to Mad-Libs, the WaCkY sToRy MaKeR."


name = raw_input("Whats your name bro? ")
print "Hmmm... " + name + ". Has a nice ring to it."

time.sleep(1)


first = raw_input("Enter an adjective: ")
second = raw_input("Enter another adjective: ")
third = raw_input("And one more... ")

time.sleep(1)

print "Alright. We've got that down. On to the nouns... "

time.sleep(1)

noun1 = raw_input("Gimme a noun G ")
noun2 = raw_input("Give me one more... ")

time.sleep(1)

verb = raw_input("Ok and one more thing: I need a verb: ")


time.sleep(1)

animal = raw_input("Alright, this may sound weird, but give me an animal: ")

time.sleep(1)

food = raw_input("Gimme a foooood... :")

time.sleep(1)

fruit = raw_input("Ok... now give me a fruit: ")

time.sleep(1)

superhero = raw_input("And your favorite superhero: ")

time.sleep(1)

country = raw_input("What country do you wanna visit? ")

time.sleep(1)

dessert = raw_input("Whats your fav dessert")

time.sleep(1)

year = raw_input("Lastly, if you could visit any year, what would it be")

time.sleep(1)

print "Ok, creating..." 

time.sleep(3)


print STORY % (name, first, second, animal, food, verb, noun1, fruit, third, name, superhero, name, country, name, dessert, name, year, second)