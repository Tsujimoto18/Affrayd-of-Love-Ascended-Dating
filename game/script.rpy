label start:
    # Setup basic python variables first.
    python:
        # PlayerData will hold all data referring to the player.
        class PlayerData:
            # Initialization.
            def __init__(self, username, gender, strength, dexterity, intelligence, charisma):
                self.username = username
                self.gender = gender
                self.strength = strength
                self.dexterity = dexterity
                self.intelligence = intelligence
                self.charisma = charisma

    # Have Discord introduce the player to the new world they are in.
    "Discord" "Hello and welcome to Discord."
    "Discord" "Discord is a small group of passionate gamers whose mission is to bring people together around games."
    "Discord" "Diversity and inclusiveness are a critical part of how we get there."
    "Discord" "We believe that with diversity comes a better product, better decisions, and a better work environment."
    "Discord" "Everyone here is committed to making Discord representative of the world we want to live and play in."

    "Discord" "If you wish to use Discord you must first have a username for others to address you by."

    jump name_input

    return

label name_input
    python:
        # Make a global variable called temp_name as a temporary name holder.
        global temp_name = renpy.input("Please type in your username.")
        temp_name = temp_name.strip()

        if not temp_name:
            temp_name = "Guy Shy"

    "Your username will be [temp_name]. Are you sure?"

    # Check if the player made a mistake. If so, restart the label.
    menu:
        "Yes":
            jump gender_input

        "No":
            jump name_input

    return

label gender_input:
    "Are you male or female?"

    #Check the gender of the player's character.
    menu:
        "Male":
            $ global temp_gender = 'M'
            jump connect_to_affray_studios
        "Female":
            $ global temp_gender = 'F'
            jump connect_to_affray_studios
        "Other":
            $ global temp_gender = 'O'
            jump connect_to_affray_studios
    
    return

label connect_to_affray_studios:
    # Set default values.
    $ global player = Character(temp_name)
    $ global player_data = PlayerData(temp_name, temp_gender, 0, 0, 0, 0)

    # Remove temp_name and temp_gender from memory.
    $ temp_name = null
    $ temp_gender = null

    "Discord" "Great!"
    "Discord" "Now all we need to do is connect you to a server."
    "Discord" "Which server would you like to connect to?"
    menu:
        "Affray Studios":
            jump connect_to_affray_studios_second

label connect_to_affray_studios_second:
    "Discord" "Have fun!"