# story function loops the game so player can play again
def story():

    import time
    # allows pause between each sentence
    import random
    # randomly selects which pebble is chosen

    def print_story(storyline):
        print(storyline)
        time.sleep(2)

    pebbles = ["green", "yellow", "blue", "red"]
    pebble_choice = random.choice(pebbles)

    no_list = ["N", "n", "no", "No", "NO"]
    yes_list = ["Y", "y", "yes", "Yes", "YES"]
    # list of possible valid answers

    def introduction():
        print_story("You find yourself lost at the zoo\n")
        print_story("Not only have you lost yourself but you've lost your "
                    "friends as well\n")
        print_story("You continue your search for them nonetheless\n")
        print_story("Suddenly, you trip over a twig, scraping your knee\n")
        print_story("Right where you've fallen are four shiny pebbles\n")
        print_story("The green, blue, red, and yellow stones shimmer in the "
                    "sunlight\n")

        print("A strong gust of wind blows the", pebble_choice, "pebble "
              "your way\n")
        time.sleep(3)

        if pebble_choice == pebbles[0]:
            path_green_pebble()
        elif pebble_choice == pebbles[1]:
            path_yellow_pebble()
        elif pebble_choice == pebbles[2]:
            path_blue_pebble()
        else:
            path_red_pebble()

    def path_green_pebble():

        path_options = ["1", "2"]
        choice = ""

        print_story("You pick up the shiny, green pebble without hesitation\n")
        print_story("Suddenly a small fairy dressed in green appears\n")
        print_story('"How cool! A fairy!" you thought to yourself\n')
        print_story("Before you had time to marvel at her presence\n")
        print_story("You hear fast, heavy footsteps coming your way\n")
        print_story("The fairy quickly summons you a sword for defense\n")

        print_story("Enter 1 to use the sword as your weapon\n")
        print_story("Enter 2 to use your fists as your weapon\n")

        while True:
            choice = input("What would you like to do?\n")
            if choice == path_options[0]:
                path_sword()
                break
            elif choice == path_options[1]:
                path_fists()
                break
            else:
                print("Please enter 1 or 2 to continue\n")

    def path_red_pebble():

        path_options = ["1", "2"]
        choice = ""

        print_story("You pick up the shiny, red pebble without hesitation\n")
        print_story("Suddenly a small fairy dressed in red appears\n")
        print_story('"How cool! A fairy!" you thought to yourself\n')
        print_story("But before you had time to marvel at her presence\n")
        print_story("Fast, heavy footsteps are quickly approaching from "
                    "behind\n")
        print_story("Inticipating danger, the fairy quickly summons you a "
                    "bow and arrows\n")
        print_story("Enter 1 to use the bow and arrows as your weapon\n")
        print_story("Enter 2 to use your fists as your weapon\n")

        while True:
            choice = input("What would you like to do?\n")
            if choice == path_options[0]:
                path_bow_arrow()
                break
            elif choice == path_options[1]:
                path_fists()
                break
            else:
                print("Please enter 1 or 2 to continue\n")

    def path_blue_pebble():

        path_options = ["1", "2"]
        choice = ""

        print_story("You pick up the shiny, blue pebble without hesitation\n")
        print_story("Suddenly, you hear a loud rumble up ahead\n")
        print_story("You look up to see a giant hill of pebbles rolling "
                    "your way\n")
        print_story("There's no way you can outrun this\n")
        print_story("You have to jump out the way!\n")

        print_story("Enter 1 to go right\n")
        print_story("Enter 2 to go left\n")

        while True:
            choice = input("What would you like to do?\n")
            if choice == path_options[0]:
                path_right()
                break
            elif choice == path_options[1]:
                path_left()
                break
            else:
                print("Please enter 1 or 2 to continue\n")

    def path_yellow_pebble():

        path_options = ["1", "2"]
        choice = ""

        print_story("You pick up the shiny, yellow pebble without "
                    "hesitation\n")
        print_story("Suddenly, you hear loud footsteps up ahead\n")
        print_story("You look up to see a stampede of elephants coming "
                    "your way\n")
        print_story("There's no way you can outrun this\n")
        print_story("You have to jump out the way!\n")

        print_story("Enter 1 to go right\n")
        print_story("Enter 2 to go left\n")

        while True:
            choice = input("What would you like to do?\n")
            if choice == path_options[0]:
                path_right()
                break
            elif choice == path_options[1]:
                path_left()
                break
            else:
                print("Please enter 1 or 2 to continue\n")

    def path_fists():
        print_story("Your fists it is\n")
        print_story("Right in front of you stands Big Foot!\n")
        print_story("You've only ever heard stories about him\n")
        print_story("Before you had time to position yourself for a fight\n")
        print_story("Big Foot gobbles you up\n")
        print_story("GAME OVER\n")

        while True:
            play_again = input("Would you like to play again? (Y/N)\n")
            if play_again in yes_list:
                story()
                break
            elif play_again in no_list:
                print_story("Thanks for playing!")
                exit()
                break
            else:
                print("Please enter Y/N to continue\n")

    def path_sword():
        path_options = ["1", "2"]
        choice = ""
        print_story("You decided the sword is best\n")
        print_story("Right in front of you stands Big Foot!\n")
        print_story("Despite the size, you're confident you can take "
                    "him down\n")
        print_story("You run towards him without hesitation striking "
                    "him in the knee\n")
        print_story("With a loud thud he hits the ground\n")
        print_story("But you know he's only temporarily disabled\n")
        print_story("From your peripheral you notice the opening to a "
                    "dimly lit cave\n")

        print_story("Enter 1 to keep fighting Big Foot\n")
        print_story("Enter 2 to hide in the cave\n")

        while True:
            choice = input("What would you like to do?\n")
            if choice == path_options[0]:
                path_fight()
                break
            elif choice == path_options[1]:
                path_cave()
                break
            else:
                print("Please enter 1 or 2 to continue\n")

    def path_bow_arrow():
        path_options = ["1", "2"]
        choice = ""
        print_story("You decided bow and arrows are best")
        print_story("Right in front of you stands Big Foot!\n")
        print_story("Despite the size, you're confident you can take "
                    "him down\n")
        print_story("You run towards him without hesitation striking "
                    "him on his big toe\n")
        print_story("Oh no! You've only made him angrier\n")
        print_story("From your peripheral you spot the opening to a dimly "
                    "lit cave\n")

        print_story("Enter 1 to keep fighting Big Foot\n")
        print_story("Enter 2 to hide in the cave\n")

        while True:
            choice = input("What would you like to do?\n")
            if choice == path_options[0]:
                path_fight()
                break
            elif choice == path_options[1]:
                path_cave()
                break
            else:
                print("Please enter 1 or 2 to continue\n")

    def path_right():
        path_options = ["1", "2"]
        choice = ""

        print_story("You throw yourself to the right\n")
        print_story("Landing in a ditch full of poisonous snakes, you are "
                    "bitten and die\n")
        print_story("GAME OVER\n")

        while True:
            play_again = input("Would you like to play again? (Y/N)\n")
            if play_again in yes_list:
                story()
                break
            elif play_again in no_list:
                print_story("Thanks for playing!")
                exit()
                break
            else:
                print("Please enter Y/N to continue\n")

    def path_left():
        path_options = ["1", "2"]
        choice = ""

        print_story("You throw yourself to the left\n")
        print_story("Landing in a pile of leaves, your fall is soften\n")
        print_story("However, you've now awaken Big Foot who was sleeping "
                    "not too far\n")
        print_story("Despite being a couple feet away, you can see how angry "
                    "he is\n")
        print_story("You notice a dimly lit cave just a few feet to your "
                    "right\n")
        print_story("Maybe you can make it\n")

        print_story("Enter 1 to stay and fight\n")
        print_story("Enter 2 to enter the cave\n")

        while True:
            choice = input("What would you like to do?\n")
            if choice == path_options[0]:
                path_fight()
                break
            elif choice == path_options[1]:
                path_cave()
                break
            else:
                print("Please enter 1 or 2 to continue\n")

    def path_fight():
        path_options = ["1", "2"]
        choice = ""

        print_story("No, you're going to face Big Foot\n")
        print_story("You won't be bullied into backing down\n")
        print_story("You'll be the first person in history to challenge him\n")
        print_story("Big Foot is fast on his feet\n")
        print_story("Before you can throw a blow, you've been snatched up "
                    "and eaten\n")
        print_story("GAME OVER\n")

        while True:
            play_again = input("Would you like to play again? (Y/N)\n")
            if play_again in yes_list:
                story()
                break
            elif play_again in no_list:
                print_story("Thanks for playing!")
                exit()
                break
            else:
                print("Please enter Y/N to continue\n")

    def path_cave():
        path_options = ["1", "2"]
        choice = ""

        print_story("Not wanting to take your chances, you run for the cave\n")
        print_story("You look around and see an exit near the end of "
                    "the cave\n")
        print_story("Maybe this is the way out of this horrible mess\n")
        print_story("You suddenly hear heavy footsteps behind you\n")
        print_story("On the wall, you see a cantation that promises to make "
                    "you invisible\n")

        print_story("Enter 1 to try and outrun Big Foot\n")
        print_story("Enter 2 to go invisible\n")

        while True:
            choice = input("What would you like to do?\n")
            if choice == path_options[0]:
                path_outrun()
                break
            elif choice == path_options[1]:
                path_invisible()
                break
            else:
                print("Please enter 1 or 2 to continue\n")

    def path_outrun():
        path_options = ["1", "2"]
        choice = ""

        print_story("Oh no, you're no match for Big Foot!\n")
        print_story("You been snatched up and eaten\n")
        print_story("GAME OVER\n")

        while True:
            play_again = input("Would you like to play again? (Y/N)\n")
            if play_again in yes_list:
                story()
                break
            elif play_again in no_list:
                print_story("Thanks for playing!")
                exit()
                break
            else:
                print("Please enter Y/N to continue\n")

    def path_invisible():
        path_options = ["1", "2"]
        choice = ""

        print_story("With your trust in the ancient spell, you close your eyes"
                    " after reciting it\n")
        print_story("You open them as you see Big Foot coming your way\n")
        print_story("You panic but stay pressed against the wall\n")
        print_story("To your surprise, he didn't see you!\n")
        print_story("Out of frustration, he walks out the cave the same way"
                    " he came in\n")
        print_story("You quickly run for the exit\n")
        print_story("You made it!\n")
        print_story("Right outside the cave are your friends who were also "
                    "searching for you\n")
        print_story("YOU WIN!\n")

        while True:
            play_again = input("Would you like to play again? (Y/N)\n")
            if play_again in yes_list:
                story()
                break
            elif play_again in no_list:
                print_story("Thanks for playing!")
                exit()
                break
            else:
                print("Please enter Y/N to continue\n")

    introduction()


story()
# python3 adventure_game.py
