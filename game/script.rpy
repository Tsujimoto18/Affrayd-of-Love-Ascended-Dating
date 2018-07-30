# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character ("Discord")
define f = Character("[name]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    d "Hey welcome to Discord, you must first choose a name for your account."
python:
    name = renpy.input('What would you like your name to be?')
    name = name.strip() or "Guy Shy"

    # This ends the game.

    return
