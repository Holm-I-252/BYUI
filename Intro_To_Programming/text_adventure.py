running = True

while running:

    print("Text Based Adventure Game")
    print("Enter one of the two options to have your character move on. Possible options are in all caps.")

    name = input("What is your character's name? ")

    print(f"Welcome, {name}! You find yourself in a dark room with two doors. One door is on the left and the other is on the right.")

    dark_room = input("Which door would you like to go through? (LEFT or RIGHT) ").lower()

    if dark_room == "left":
        print(f"{name} finds themselves in a long coridor with a door at the end. The door seems to be locked. There are 3 pots, a green one, a blue one and a red one. Which will you reach your hand into to look for the key?")

        pot = input("Which pot will you reach into? (GREEN, BLUE or RED) ").lower()

        if pot == "green":
            print(f"{name} reaches their hand into the green pot and suddenly, a bright green gas begins to fill the room! Will you try and hold your breath, or tray and flip the pot over?")
            gas = input("What will you do? (HOLD or FLIP) ").lower()
            if gas == "hold":
                print(f"{name} tries to hold their breath, and after a while, the gas clears and they find a key at the bottom of the pot! {name} unlocks the door and continues into the next room.")

                print(f"{name} opens the door and continiues into the next room, where they see a dragon sleeping on a pile of gold. You could probably sneek past it and take a little gold, or you could take a lot and risk waking the dragon. What will you do?")
                gold = input("How much gold will you take? (LITTLE or LOT) ").lower()

                if gold == "little":
                    print(f"{name} sneaks over to the dragon and takes just a little gold. They successfully grab a little bit and make it out without waking the dragon. {name} makes it out of the cave and spends the gold quickly. {name} runs out of money and has to spend the rest of their life in a dead end job. GAME OVER.")

                elif gold == "lot":
                    print(f"{name} sneaks over and fills all their bags with gold. The dragon is a heavy sleeper and doesn't hear a thing. {name} makes it out of the cave and is now rich! {name} lives the rest of their life in luxury. GAME OVER.")

                else:
                    print("Invalid input. Please try again.")


        elif pot == "red":
            print(f"{name} reaches their hand into the red pot and finds a key! {name} opens the door and continiues into the next room, where they see a dragon sleeping on a pile of gold. You could probably sneek past it and take a little gold, or you could take a lot and risk waking the dragon. What will you do?")
            gold = input("How much gold will you take? (LITTLE or LOT) ").lower()

            if gold == "little":
                print(f"{name} sneaks over to the dragon and takes just a little gold. They successfully grab a little bit and make it out without waking the dragon. {name} makes it out of the cave and spends the gold quickly. {name} runs out of money and has to spend the rest of their life in a dead end job. GAME OVER.")

            elif gold == "lot":
                print(f"{name} sneaks over and fills all their bags with gold. The dragon is a heavy sleeper and doesn't hear a thing. {name} makes it out of the cave and is now rich! {name} lives the rest of their life in luxury. GAME OVER.")

            else:
                print("Invalid input. Please try again.")

        elif pot == "blue":
            print(f"{name} reaches their hand into the blue pot and feels something cold and metal at the bottom. A key perchance?")

            pull_key = input("Will you pull out the object? (YES or NO) ").lower()

            if pull_key == "yes":
                print(f"{name} pulls out the object and realizes its the lid to a little box inisde the pot. Out of the box comes a blue mist that fills the room. The room gets colder and colder from the mist, until {name} is encased in a solid block of ice. GAME OVER.")

            elif pull_key == "no":
                print(f"{name} decides not to pull out the object and instead leaves the room. They abandon their quest and return home to wonder for the rest of their life, what if I pulled the out the key? GAME OVER.")
            
            else:
                print("Invalid input. Please try again.")

        else:
            print("Invalid input. Please try again.")

    elif dark_room == "right":
        print(f"{name} walks through the right door and finds themselves in a room with a river of lava! There is a old, rickety bridge that crosses the river, and there is also a little metal boat that looks like it might survive the lava. Which will you take?")

        bridge_or_boat = input("Which will you take? (BRIDGE or BOAT) ").lower()

        if bridge_or_boat == "bridge":
            print(f"{name} begins to cross the bridge. The bridge seems sturdy enough. About 2/3 of the way across, the brigshe begins to snap! {name} has 2 options they could try. You could try to jump across the rest of the way, or you could climb the ropes and try and tightrope walk the rest of the way. What will you do?")

            snap = input("What will you do? (JUMP or CLIMB) ").lower()

            if snap == "jump":
                print(f"While {name} is a remarkable athlete, they can't quite make it across all the way, and they fall into the river of lava and burn to a crisp. GAME OVER.")

            elif snap == "climb":
                print(f"{name} quickly scrambles up the ropes and carefully walks over to the end of the bridge. They successfully make it across and jump to safety. They continue into the room and find a huge pile of treasure, but as they fill their bags with gold, they realise they can't make it accross the river of lava again. {name} is stuck in the room forever and leaves a skeleton for the next adventurer to find. GAME OVER.")
            
            else:
                print("Invalid input. Please try again.")

        elif bridge_or_boat == "boat":
            print(f"As {name} approaches the boat, they feel a little bit uneasy about the condtion of the metal hull of the boat. Will you still take the boat?")
            take_boat = input("Will you take the boat? (YES or NO) ").lower()

            if take_boat == "yes": 
                print(f"{name} hops in the boat and begins sailing across the river. The boat floats across perfectly, but {name} didn't think about the fact that the lava would make the boat extremely hot. {name}'s shoes begin to melt, and eventually they burn away into just a pile of ash. GAME OVER.")
                
            elif take_boat == "no":
                print(f"{name} decides not to take the boat and instead turns around and takes the bridge.")
                print(f"{name} begins to cross the bridge. The bridge seems sturdy enough. About 2/3 of the way across, the brigshe begins to snap! {name} has 2 options they could try. You could try to jump across the rest of the way, or you could climb the ropes and try and tightrope walk the rest of the way. What will you do?")

                snap = input("What will you do? (JUMP or CLIMB) ").lower()

                if snap == "jump":
                    print(f"While {name} is a remarkable athlete, they can't quite make it across all the way, and they fall into the river of lava and burn to a crisp. GAME OVER.")

                elif snap == "climb":
                    print(f"{name} quickly scrambles up the ropes and carefully walks over to the end of the bridge. They successfully make it across and jump to safety. They continue into the room and find a huge pile of treasure, but as they fill their bags with gold, they realise they can't make it accross the river of lava again. {name} is stuck in the room forever and leaves a skeleton for the next adventurer to find. GAME OVER.")
                
                else:
                    print("Invalid input. Please try again.")
            else:
                print("Invalid input. Please try again.")

        else:
            print("Invalid input. Please try again.")


    else:
        print("Invalid input. Please try again.")

    play_again = input("Would you like to play again? (YES or NO) ").lower()

    if play_again == "no":
        running = False
        print("Thanks for playing!")