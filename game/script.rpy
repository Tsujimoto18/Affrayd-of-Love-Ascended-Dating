# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.
# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.
# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory
# These display lines of dialogue.   
# Simple test code on choice-based conversations
# This ends the game.
define Mee6 = Character("Mee6")
define Discord = Character("Discord")
define Player = Character("[name]")

label start:
    show discord

    Discord "Hey welcome to Discord, you must first choose a name for your account."

    python:
        name = renpy.input('What would you like your name to be?')
        name = name.strip() or "Guy Shy"

    Discord "Brace yourselves, [name] Just join the server!"
    
    show mee6

    Mee6 "Welcome to Affray Studios, Be sure to help us by following these steps below!"

    Mee6 "• Check out our #links and consider supporting us"

    Mee6 "• Checking out and giving some love to our #partners"

    menu:
        "Hi.":
            jump choice1_first_mee6

        "Fuck off, MEE6":
            jump choice2_firstmee6

    return

label choice1_first_mee6:
    Mee6 "Hi"
    return

label choice2_first_mee6:
    Mee6 "[name] has been warned for Profanity."
    return