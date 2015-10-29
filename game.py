#!/usr/bin/env python
# coding: utf-8
from sys import exit
import random

print "\nWelcome to the Vocabulary Gauntlet!!!!!\n"
language_choice = False
language = " "

#------LANGUAGE SELECTION AND TYPING INSTRUCTIONS----
while language_choice == False:
    language = raw_input ("Please choose your target language. [Icelandic, Italian, or Turkish] >>   ")

    #------ICELANDIC----
    if language == "Icelandic":
        from icelandic_vocab import *
        language_choice = True

    #------ITALIAN----#
    elif language == "Italian":
        from italian_vocab import *
        language_choice = True

    #------TURKISH----#
    elif language == "Turkish":
        from turkish_vocab import *
        language_choice = True

    else:
        print "Choose again."
        language_choice = False



# --------CLASSES----------

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter."
        exit(1)


    def quiz(self):
        keys_list = self.quiz_dict.keys()
        # random sample from keys_list
        keys_list = random.sample(keys_list, 10)

        print "\nThere are 10 items in this quiz."
        print "After 7 wrong answers, the quiz will restart.\n"
        num_correct = 0
        num_wrong = 0
        for key in keys_list:
            print key + ":  "
            answer = raw_input(">> ")
            if answer == self.quiz_dict[key]:
                print "*****Good job!*****"
                num_correct += 1
                print "\tCorrect answers: " + str(num_correct)
                print "\tWrong answers: " + str(num_wrong) + "\n"
            else:
                num_wrong += 1
                print "*****Wrong answer!*****"
                print "(correct answer = " + self.quiz_dict[key] + ")"
                print "\tCorrect answers: " + str(num_correct)
                print "\tWrong answers: " + str(num_wrong) + "\n"

                if num_wrong > 6:
                    return False
        return True


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


# ----------------SCENE SUBCLASSES---------------------

# STARTING AREA
class Foyer(Scene):

    def enter(self):
        print "\n" + "-" * 80
        print "IMPORTANT: HOW TO TYPE ACCENTS AND NON-ENGLISH CHARACTERS IN THE COMMAND LINE"
        print "-" * 80
        print "You must activate the US-Extended (Mac) or Windows International (PC) Keyboard. "

        print "\nFor a grave accent(è):"
        print "\t[MAC]\t\ttype option + ` and then the letter you wish to accent"
        print "\t[WINDOWS]\ttype ` and then the letter you wish to accent\n"

        print "For an acute accent(é):"
        print "\t[MAC]\t\ttype option + e and then the vowel"
        print "\t[WINDOWS]\ttype single quote and then the vowel\n"

        print "For an umlaut(ö):"
        print "\t[MAC]\t\ttype option + u and then the vowel"
        print "\t[WINDOW]\ttype double quote and the vowel\n"

        print "It may be helpful to visit this site:"
        print "http://symbolcodes.tlt.psu.edu/bylanguage/icelandic.html#htmlcodes \n"


# --------instructions for special characters--------

        if language == "Icelandic":
            print "ICELANDIC-SPECIFIC characters:"
            print "\tæ (AE ligature):"
            print "\t\t [MAC]\t\toption + ' (apostrophe)"
            print " \t\t [WINDOWS]\tRightAlt"
            print "\tþ (thorn): "
            print "\t\t[MAC]\t\toption + t"
            print "\t\t[WINDOWS]\tRightAlt + t"
            print "\tð (eth):"
            print "\t\t[MAC]\t\toption + d"
            print "\t\t[WINDOWS]\tRightAlt + d\n"

        if language == "Turkish":
            print "You will need to use a Turkish-QWERTY keyboard instead of the US-Extended Keyboard"
            print "because ş, ı, and ğ are not coded into the US-Extended Keyboard. Sigh.\n "
            print "\t[MAC]\t\tuse option + i, s, c, o, u, or g for ı, ş, ç, ö, ü, or ğ"
            print "-" * 80

        print "GAME INSTRUCTIONS"
        print "-" * 80
        print "You are required to move through three rooms where your linguistic mettle"
        print "will be challenged. You must provide translations for colors, numbers,"
        print "and parts of the body in " + language + "."
        print "\nHit ENTER when you are ready. CTRL-C to quit."
        raw_input(">>" )
        return 'color_room'

# COLOR ROOM
class ColorRoom(Scene):
    quiz_dict = colors
    def enter(self):
        print "\nWelcome to the bedazzling Room of Colors. You will be given an English color word,"
        print "and you must provide the translation in order to proceed to the next room."
        finished = False
        while not finished:
            finished = self.quiz()
        print "\n" + "-" * 80
        print "Excellent work! You have completed the first trial. Onward!"
        print "-" * 80
        return 'number_room'

# NUMBER ROOM
class NumberRoom(Scene):
    quiz_dict = numbers
    def enter(self):
        print "\nYou have now entered the eerily pristine Hall of Numbers. You will be given an English number,"
        print "and you must provide the translation in order to proceed to the next room."
        finished = False
        while not finished:
            finished = self.quiz()
        print "\n" + "-" * 80
        print "Excellent work! You have completed the second trial. Onward!"
        print "-" * 80
        return 'body_room'

# PARTS OF THE BODY ROOM
class BodyRoom(Scene):
    quiz_dict = body_parts
    def enter(self):
        print "\nYou step into the final room: the Body Parts Basement."
        print "(It's not as grisly as it sounds, though this quiz is the hardest of the 3 challenges.)"
        print "You will now be quizzed on the parts of the body. Begin!\n"

        if language == 'Italian':
            print "NB: Be sure to use the definite article (la, il, l',  or lo) as appropriate.\n"
        else:
            print "NB: The definite or indefinite article is not required.\n"

        finished = False
        while not finished:
            finished = self.quiz()
        return 'finished'

class Finished(Scene):

    def enter(self):
        print "\n" + "-" * 80
        print "You completed the Vocabulary Gauntlet! Good job."
        print "!" * 80
        exit()


# MAP OBJECT
# The Map class has to come after the scenes because the dictionary storing the scenes
# refers to the scenes. They must exist for them to be referenced.
#
class Map(object):
    scenes = {
        'foyer': Foyer(),
        'color_room': ColorRoom(),
        'number_room': NumberRoom(),
        'body_room': BodyRoom(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('foyer')
a_game = Engine(a_map)
a_game.play()

