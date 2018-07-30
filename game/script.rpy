# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define a = Character ("Mee6")
define b = Character ("Discord")
define c = Character("[name]")

# The game starts here.

label start:

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.



# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory.

show discord

# These display lines of dialogue.

b "Hey welcome to Discord, you must first choose a name for your account."

python:
    name = renpy.input('What would you like your name to be?')
    name = name.strip() or "Guy Shy"

b "Brace yourselves, [name] Just join the server!"
    
show mee6

a "Welcome to Affray Studios, Be sure to help us by following these steps below!"

a "• Check out our #links and consider supporting us"

a "• Checking out and giving some love to our #partners"

# This ends the game.

return
