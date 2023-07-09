#Adventure Time
#Main Story Line
# As you settle into your chosen character, you embark on to journey in the village of Treasure Coast. The village is known for its harmonious collaboration among the six main occupations: the Blacksmith, the Miner, The Leatherworker, the Carpenter, the Farmer, and the Butcher. Together, they form the foundation of this beautiful village.
print("# As you settle into your chosen character, you embark on a journey in the village of Treasure Coast. The village is known for its harmonious collaboration among the six main occupations: \nThe Blacksmith, \nthe Miner, \nthe Leatherworker, \nthe Carpenter, \nthe Farmer, and \nthe Butcher. Together, they form the foundation of this beautiful village.")
print("Choose the character you wish to play as: \na.The Blacksmith \nb.The Miner \nc.The Leather worker \nd.The Carpenter \ne.The Farmer \nf.The Bucher \n")
character=input("###")

characters ={}
#Each Character has their own speacail Abilities/Skills
if character.lower() == "a":
  print("You choose the Blacksmith \nAblities: \n.Ability to forge weapons or amour \n.Ability to melt down items made of metal to form to items. \n.Ability to Repair broken items")
elif character.lower() == "b":
    print("You choose the Miner \nAbilies: \n.Ability to blast into rocks to create tunnels deep into the ground. \n.Practical and mechenical skills. \n.Exellent stamina.")
elif character.lower() == "c":
    print("You choose the Leather worker \nAbilies: \nAbility to produce clothes, shoes and bags for other occupations. \nability to Dye leather and Skiving. \nGluing")
elif character.lower() == "d":
    print("You choose the Carpenter \nAbilities: \n.Sanding sawing & General Woodworking \n.Furniture building \n.installation and remodeling")
elif character.lower() == "e":
    print("You choose the Farmer \nAbilities: \n.Plant growth(in planting, fertilising, watering and harvesting) \n.Managing Farming operations(Spraying, irrigating and pruning)")
elif character.lower() == "f":
    ("You choose the Buchern \nAbilities: \n.Cutting, Grinding and Preparing meat \nAbility to use knifes and other cutting tools \nMeat identification")
else:
    print()


#Each character has their own unique storyline based on their Abilities/Skills
print("\nYou begin your day, eager to utilize your unique abilities and contribute to the community. \nThe sun rises over the panoramic valley, casting a warm glow upon the village. \nThe sound of hammers, machinery, and the bustling of villagers fills the air.")
if character.lower() == "a":
  print("\nAs the Blacksmith, you enter your workshop, surrounded by tools and the fiery glow of the forge. \nYour abilities allow you to forge magnificent weapons and armour, melt down metal items to create new ones and repair broken equipment. \nYou take pride in your craft and the vital role you play in ensuring the village's defence and prosperity.")
  print("Together, the six occupations form an intricate web of support, fostering a thriving community in Treasure Coast. \nAs you continue your journey, you will encounter challenges, forge relationships, and contribute to the village's growth. \nThe future of this hidden valley rests in your capable hands, and the adventure has only just begun.")
elif character.lower() == "b":
    print("\nIf you chose to be the Miner, you find yourself equipped with practical and mechanical skills. \nYour task is to blast into rocks and create tunnels deep into the ground. \nYour tireless work provides valuable resources to the village, such as ores and precious minerals. With your excellent stamina, you delve into the depths, uncovering treasures that lay hidden within the earth.\n")
    print("Together, the six occupations form an intricate web of support, fostering a thriving community in Treasure Coast. \nAs you continue your journey, you will encounter challenges, forge relationships, and contribute to the village's growth. \nThe future of this hidden valley rests in your capable hands, and the adventure has only just begun.")
elif character.lower() == "c":
    print("\nAs the Leatherworker, you possess the skills to produce clothes, shoes, and bags for the villagers. \nYour craftsmanship is impeccable, and you have mastered the art of dyeing leather and skiving. \nWhether it's creating garments or accessories, you play a crucial role in enhancing the aesthetics and functionality of the village.")
    print("Together, the six occupations form an intricate web of support, fostering a thriving community in Treasure Coast. \nAs you continue your journey, you will encounter challenges, forge relationships, and contribute to the village's growth. \nThe future of this hidden valley rests in your capable hands, and the adventure has only just begun.")
elif character.lower() == "d":
    print("\nIf you chose to be the Carpenter, your abilities lie in woodworking. You are skilled in sanding, sawing, and general woodworking tasks. \nYour craftsmanship shines through as you build and repair furniture for the villagers. \nFrom creating beautiful wooden structures to remodelling existing ones, your work brings comfort and elegance to the homes and buildings of the Treasure Coast.\n")
    print("Together, the six occupations form an intricate web of support, fostering a thriving community in Treasure Coast. \nAs you continue your journey, you will encounter challenges, forge relationships, and contribute to the village's growth. \nThe future of this hidden valley rests in your capable hands, and the adventure has only just begun.")
elif character.lower() == "e":
    print("\nAs the Farmer, you possess a deep understanding of plant growth and farming operations. \nYour days are filled with planting, fertilizing, watering, and harvesting crops. \nYou manage the farming operations, ensuring proper care through spraying, irrigating, and pruning. \nThe village relies on your expertise to provide a bountiful harvest, sustaining the community with fresh food.\n")
    print("Together, the six occupations form an intricate web of support, fostering a thriving community in Treasure Coast. \nAs you continue your journey, you will encounter challenges, forge relationships, and contribute to the village's growth. \nThe future of this hidden valley rests in your capable hands, and the adventure has only just begun.")
elif character.lower() == "f":
    print("\nIf you chose to be the Butcher, your skills revolve around cutting, grinding, and preparing meat. \nYou wield knives and cutting tools with precision, ensuring the village has a steady supply of meat products. \nYour ability to identify different cuts of meat and utilize every part of an animal is highly valued. \nThe villagers appreciate your expertise in providing nourishment and culinary delights.\n")
    print("Together, the six occupations form an intricate web of support, fostering a thriving community in Treasure Coast. \nAs you continue your journey, you will encounter challenges, forge relationships, and contribute to the village's growth. \nThe future of this hidden valley rests in your capable hands, and the adventure has only just begun.")

if character.lower() == "a":
  print("\nOn one late evening, as you venture out to fetch coal for your smelters, you find yourself in an unfortunate situation. \nWhile gathering coal, you suddenly hear the sound of footsteps approaching from behind. \nStartled, you turn around to find a group of bandits, their eyes filled with greed and mischief.\n")
  print("Realizing that you're outnumbered and outmatched, you put up a valiant fight, but the bandits overpower you with their sheer strength. \nThey capture you and bind your hands, rendering you helpless.\n")
  print("Struggling against your restraints, you manage to free yourself after hours of determined effort. \nWith newfound freedom, you stand up and assess your surroundings. \nYou see four paths leading in different directions: east, west, north, and south.\n")
  print("With no clear sense of which path leads back to Treasure Coast, you must rely on your instincts and survival skills to navigate through the treacherous forest. \nAs you venture deeper into the unknown, you encounter mysterious creatures, hidden dangers, and unexpected allies, all while hoping to find your way back home.\nYour journey as the Blacksmith takes an unexpected turn, filled with challenges that test your mettle and resourcefulness. \nAlong the way, you uncover secrets, forge new friendships, and confront the bandits who captured you, seeking both justice and a way to secure the safety of your village.\nThe path back to Treasure Coast may be treacherous, but as the Blacksmith, you possess the resilience and determination to overcome any obstacle. \nThe fate of the village rests on your shoulders, and your journey is just beginning.\n")
elif character.lower() == "b":
    print("The Miner, equipped with practical and mechanical skills, ventures deep into the mines to extract valuable resources for the village of Treasure Coast. \nHowever, during one expedition, the Miner is ambushed and captured by a group of bandits. \nThey bind the miners and take them away from the village.\n")
    print("As a prisoner, the Miner is forced to work in treacherous mines under the bandits' control. \nEnduring harsh conditions, the Miner bides their time, looking for an opportunity to escape. \nAfter weeks of captivity, a chance to break free arises, and the Miner seizes it.\n")
    print("Navigating through labyrinthine tunnels and facing various obstacles, the Miner embarks on a perilous journey back to Treasure Coast. \nAlong the way, they forge alliances with other outcasts and victims of the bandits, forming a group united in their goal to protect the village.\n")
    print("The Miner's path is filled with danger, but their resilience, ingenuity, and practical skills help them overcome challenges. \nTheir ultimate objective is not only to secure their freedom but also to safeguard Treasure Coast from the menacing bandits.\n")
    print("Through perilous encounters and strategic planning, the Miner and their newfound allies work together to expose the bandits' plans and bring justice to the village. \nThe journey becomes a test of determination, resourcefulness, and unwavering spirit as they strive to restore peace and protect the community they hold dear.\n")
elif character.lower() == "c":
    print("\nHowever, your peaceful routine is disrupted when they stumble upon a group of bandits in the forest. \nDespite Yor attempts to escape, the Leatherworker is captured and forced to create specialized gear for the bandits. \nDetermined to regain their freedom, you study Your captors and plan a daring escape. \nWith the help of newfound allies, you navigate treacherous terrain, using their resourcefulness and knowledge of the forest to overcome obstacles. \nUpon returning to Treasure Coast, they share their insights and contribute to fortifying the village's defenses, ensuring the bandits' threat is eliminated.\n")
elif character.lower() =="d":
    print("However, Your tranquil existence is disrupted when a group of bandits infiltrates the village. \nDespite your efforts to protect their fellow villagers, the Carpenter is outnumbered and captured. \nBound and taken away from your beloved workshop, you are forced to use your carpentry skills for the bandits' nefarious purposes. \nDetermined to escape and protect their community, the Carpenter patiently observes their captors, analyzing their strengths and weaknesses. \nWhen an opportunity arises, they seize it, using their woodworking expertise to fashion makeshift tools and create diversions. With their ingenuity and resilience, the Carpenter manages to break free and embark on a perilous journey back to Treasure Coast. \nAlong the way, they encounter various challenges, relying on their woodworking skills to overcome obstacles and seek allies. \nUpon their long-awaited return, the Carpenter shares their knowledge, contributing to the village's fortification and rebuilding efforts. \nThrough your craftsmanship and unwavering spirit, the Carpenter becomes an instrumental part of the village's resilience and renewal.\n")
elif character.lower() == "e":
    print("However, your peaceful life is disrupted when a group of bandits launches a surprise attack on the village. \nDespite your best efforts to protect your crops and livestock, you find yourself overpowered and captured by the bandits. \nStripped away from your fields and animals, you are forced to witness the bandits' plunder and destruction.\n")
    print("Determined to find a way to escape and save your community, you carefully observe your captors, seeking any opportunity to break free. \nDrawing upon your knowledge of nature and resourcefulness, you find ways to sow seeds of rebellion among the other captives and sow chaos within the bandit camp.\n")
    print("Through your ingenuity and ability to navigate the natural environment, you manage to escape and begin your journey back to Treasure Coast. \nAlong the way, you encounter challenges such as harsh weather, predatory animals, and limited resources. \nHowever, your farming skills prove invaluable as you cultivate makeshift shelters, forage for food, and navigate treacherous terrains.\n")
    print("When you finally return to the village, you bring with you newfound wisdom and determination. \nUtilizing your expertise, you contribute to the village's recovery efforts, replanting crops and rearing livestock. \nThe community recognizes your resilience and dependability, and together, you work towards restoring Treasure Coast to its former glory.\n")
elif character.lower() == "f":
    print("However, the tranquility of your occupation is abruptly shattered when a notorious group of bandits descends upon Treasure Coast. \nDespite your efforts to defend the village, you find yourself outnumbered and captured by the bandits. \nStripped of your tools and separated from your beloved butchery, you are forced into captivity, witnessing the bandits' reign of terror.\n")
    print("Despite the dire circumstances, you remain vigilant, carefully observing your captors for any potential weaknesses or opportunities for escape. \nYour expertise in meat identification becomes a valuable asset as you use your knowledge to gather information and navigate the bandit camp discreetly.\n")
    print("After weeks of captivity, an opportunity for liberation presents itself. \nWith your swift and precise knife skills, you free yourself from your restraints and stealthily incapacitate the guards. \nWith every move calculated and every strike precise, you make your daring escape from the bandit camp, determined to bring justice to the village.\n")
    print("Navigating through treacherous terrain, you utilize your expertise to hunt for food and survive in the wilderness. \nAlong the way, you encounter fellow villagers who have also fallen victim to the bandits' tyranny. \nUnited by a common cause, you form a small resistance group, leveraging your butcher skills to provide sustenance and nourishment while strategizing a plan to reclaim Treasure Coast.\n")
    print("With your knowledge of the bandits' vulnerabilities and your ability to manipulate their desires for a hearty meal, you lead your fellow villagers in a covert operation to undermine the bandits' power. \nUsing your knife skills and resourcefulness, you disable their supply lines and disrupt their operations, weakening their grip on the village.\n")
    print("As the tide turns in favor of the villagers, you emerge as a symbol of resilience and determination.\nYour expertise in cutting and preparing meat becomes a source of unity and celebration as the community gathers to enjoy well-deserved feasts, reaffirming the strength and spirit of Treasure Coast.\n")
else:
    print()


#Introduction
if character.lower() == "a":
    print("After escaping, you see a path leading east, west, and another leading south and north\n")
    print("Which path do you choose?\n")
    # User input for the path choice
    path = input("#####(north, south, east, west/none)")

    if path.lower() == "none":
        print("You choose not to follow a path")
        print("As you sit down to catch your breath, you spot the bandits trying to find you")
        print("Do you hide away from the bandits or run out of the forest?")
        nonechoice = input("####(hide/run)")

        if nonechoice.lower() == "hide":
           print("You choose to hide away from the bandits")
           print("As you hide in a tree, you see the bandits searching for you")
           print("As they leave and you remain in a tree, you spot an Eagle. Before you have time to react, the Eagle grabs you and kills you!!!")

        elif nonechoice.lower() == "run":
            print("You choose to run out of the forest")
            print("As you run out of the forest you find a river with a rickety old bridge")
            print("Do you cross the bridge or follow the riverbank?")
            north_choice=input("####(bridge/riverbank)")
    else:
        print("Choose a different path")


#North Choice.
if path.lower() == "north":
  print("You follow the path north.")
  print("You come across a river with a rickety old bridge.")
  print("Do you cross the bridge or follow the riverbank?")
  north_choice=input("####(bridge/riverbank)")
#Crossing the bridge
  if north_choice.lower() == "bridge":
    print("You follow rickety old bridge.")
    print("As you follow(waliking on) the bidge it begins to shake, then the bridge collapses and you fall into the river")
    print("As the river carries you away a family of crocodiles eat you up.")
#Following the riverbank
  elif north_choice.lower() == "riverbank":
    print("You follow the riverbank.")
    print("You come across a waterfall.")
    print("Do you climb along the waterfall or continue along the riverbank")
    riverbankchoice=input("####(waterfall / riverbank):")



    if riverbankchoice.lower() == "rivevrbank":
      print("As you continue along the riverbank you decide to settle beside the river where you live the remainder of your days")

#Climbing up the waterfall
    if riverbankchoice.lower() == "waterfall":
       print("You climb up the waterfall.")
       print("At the top, you find a small cave.")
       print("Inside the cave, you find a treasure chest filled with gold coins.")
       print("As you leave the  little cave behind the waterfall you see a pawn shop and a forge beside it")
       print("Do you go to the pawn shop to sell the gold coins or forge an item using the forge")
    waterfallchoice = input("####(pawn shop / forge):")

#Heading towards the Pawn shop
    if waterfallchoice.lower() == "pawn shop":
      print("As you enter the pawn shop, you see the owner who offers you a deal of 50 Gold coins for 5,000 copper coins")
      pawn_shopchoice = input("Do you take the deal? (Yes/No):")

      if pawn_shopchoice.lower() == "Yes":
        print("You give the shop owner 50 Gold coins in exchange for 5,000 copper coins")
        print("Now what do you do with 5,000 copper coins?")

      elif pawn_shopchoice.lower() == "No":
          print("You decline the offer and leave the shop")
          print("What do you do next?")

    elif waterfallchoice.lower() == "forge":
          print("You choose to forge an item")
          print("Choose an item you wish to forge.\na.pickaxe \nb.sword \nc.shovel \nd.axe")
          forgechoice = input("####:")

    else:
        print("")
#East path
if path.lower() == "east":
  print("You follow the path east.")
  print("You see a small village in the distance.")
  print("Do you head towards the village or continue down the path?")
  east_choice1=input("####(village / path)") #

#Heading towards the villagers
  if east_choice1.lower() == "village":
    print("You head towards the village.")
    print("As you get closer, you notice that the village is surrounded by a high wall.")
    print("Do you try to climb over the wall or search for a way around it?")
    Villagechoice = input("####(climb / around):")

#Climbing the wall
    if Villagechoice.lower() == "climb":
      print("You choose to climb up the wall ")
      print("Choose an item you wish to use to climb the wall (Rope/Grapple hock)")
      climbchoice = input("####(Rope /Grappel):")

#Finding a way around the village
    if Villagechoice.lower() == "around":
      print("You choose to find a way around the wall")
      print("As you try to find a way around the wall the village find you, beat you and arrest you.")

#Following the path
  if east_choice1.lower() == "path":
    print("You choose to continue along the path")
    print("As you are walking along the along the path you see a group of terrorists, as you try to run away they spot you, capture you and sell you to slavery")
    print("The end")


#West Choice
if path.lower() == "west":
  print("You follow the path west.")
  print("You see a wooden cabin with people living inside")
  print("Do you form an alliance(be-friend them) or attack them.")
  westchoice=input("####(alliance / attack):")
#Attacking the cabin
  if westchoice.lower() == "attack":
    print("You choose to attack the people in the caben")
    print("As you involve youself in combat the group from the cabin quickly overpower you and force you to work as their slave")
    print("You loose!!!")
#Forming an alliance with the cabin inhabitants/darwfs
  if westchoice.lower() == "alliance":
    print("you choose to form an alliance")
    print("As you enter into the cabin you form an alliance with the darwfs and settle in and live with them forever ")

#South Choice
if path.lower() == "south":
  print("You follow the south path")
  print("You see an abandoned camp")
  print("Do you enter the camp or leave the camp?")
  southchoice=input("####(enter camp / leave):")
#Leaving the camp
  if southchoice.lower() == "leave":
    print("As you leave the camp you spot a village in which you seek refuge and live the remainder of your days")
    print("Try again!!!!!")
# Enertering the camp
  if southchoice.lower() == "enter camp":
    print("As you enter the camp you quickly realize that it was a trap a slowly fall to your doom(demise).")
