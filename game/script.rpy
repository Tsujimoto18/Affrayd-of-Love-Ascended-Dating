define Mee6 = Character("Mee6")
define Discord = Character("Discord")
define Player = Character("[name]")

label start:
    show discord

    Discord "Hey welcome to Discord, you must first choose a name for your account."

    python:
        name = renpy.input('What would you like your name to be?')
        name = name.strip() or "Guy Shy"

    Discord "Brace yourselves, [name] Just joined the server!"
    
    
    "You blink."
    "Colors rush by you as you are thrown violently in one direction and the next."
    "You limbs flail awkwardly around the place like a fleshy ragdoll as your body stings with odd sensations."
    "You blink three more times."
    "You are now standing in some sort of small town like area."
    "The sky is a cool sky-blue with an odd lattice of lines streaking across it."
    "The sun is bright yet doesn't pierce through your eyes, allowing you to stare directly at it without any side effect."
    "Small buildings litter the area with an occasional expanse of flora."
    "You made it."
    "Affray Studios..."
    
    
    
    show mee6

    Mee6 "Welcome to Affray Studios, Be sure to help us by following these steps below!"

    Mee6 "• Check out our #links and consider supporting us"

    Mee6 "• Checking out and giving some love to our #partners"

    menu:
        "Hi.":
            jump choice1_first_mee6

        "Fuck off, MEE6":
            jump choice2_first_mee6

    return

label choice1_first_mee6:
    Mee6 "Hi"
    return

label choice2_first_mee6:
    Mee6 "[name] has been warned for Profanity."
    Player "..."
    return