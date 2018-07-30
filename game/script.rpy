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
define a = Character ("Mee6")
define b = Character ("Discord")
define c = Character("[name]")

label start:

show discord

b "Hey welcome to Discord, you must first choose a name for your account."

python:
    name = renpy.input('What would you like your name to be?')
    name = name.strip() or "Guy Shy"

b "Brace yourselves, [name] Just join the server!"
    
show mee6

a "Welcome to Affray Studios, Be sure to help us by following these steps below!"

a "• Check out our #links and consider supporting us"

a "• Checking out and giving some love to our #partners"

menu:
         "Hi.":
                jump choice1_hello

         "Fuck off, MEE6":
               jump choice2_fuckoff
         label choice1_hello
                a "Hi":
                   jump choice1_done
         label choice1_done
         label choice2_fuckoff
                     a "[name] has been warned for Profanity.":
                     jump choice2_done
         label choice2_done
return