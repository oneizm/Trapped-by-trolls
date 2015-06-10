Game By Oneizm Studios
# Right side of room dialogue:
box_see = '\nI see a box. If there is anything in this box it is just further proof of the lack of troll intellect'
box_q = 'The top is loose enough for me to move...what if there is is something dangerous in here? Should I open it?'
box_open = '\n*box opening sounds*'
box_easy = 'I opened the box with ease.'
crowbar_get = '... Ok seriously? Really? Inside this box is a crowbar. Who leaves a crowbar in a cell? Trolls are so dumb.\n'
# Left side of room dialogue:
bookshelf = "\nThere's a bookshelf. As one would assume about a troll library, the bookshelf is empty making it rather light."
bookshelf_q = 'Should I move it?'
boarded_hole = '\nHuh! A boarded up hole...'
pry = "Let's try to pry this wood off with the crowbar."
mallet_get = 'I now have a mallet. The only possible explaination for a mallet AND a crowbar is that after the jail was built the trolls just left the tools sitting in the cell.\n'
# Back side of room dialogue:
crack = '\nI see something in a small crack in the wall.'
crack_q = 'Should I try to get it?'
crack_complementing = '\nI wonder if...'
crack_smash = 'I slam the mallet againt the wall and *crash*....the wall itself has crumbled to pieces. Gotta love troll quality. I can walk into the empty cell next to me!'
key_get = "I walk in and scan the room. On the ground is a key. What did I tell you. I called this early, trolls leave keys around like a king leaves spare change\n"
# General dialogue:
cant = "Nothing I can do here. What if I had a cinnamonbun...Wait, why would eating a cinnamonbun help? I guess I'm hungry. Whatever! Time to look somewhere else +hit enter+\n"
no_dice = '\nAbsolutly nothing useful. It looks like a troll did a drawing of his family. My brother Aio could do better and he is three years old.\n'
leave_alone = "\nI'd really rather not deal with this right now... I should take a nap... maybe later ... I should break out now.\n"
hand = 1
crowbar = 0
mallet = 0
key = 0

def main_adventure():
    beginning()
    main_hub()

def beginning():
    name = input('My name is...\n')
    if not name:
        name = 'Not important, I guess'
        name_line = ". . . {0}. (Press Enter to advance)".format(name)
    else:
        name_line = "it's. . . {0}. Yeah, that's right. (Press Enter to advance)".format(name)
    input(name_line)
    input('Hm, I have no idea how I got here.')
    input('Last thing I remember was going to')
    input("explore the temple of Raposo...I was fighting some trolls then I heard a laugh behind me..")
    input('My head hurts ... I guess I got knocked out')
    input("*tries to open the door*")
    input("Of course it's locked. I don't know what I really expected...I'm not that lucky")
    input('I am stuck in a troll jail... That is the bad news...The good news is trolls are quite dumb')
    input('This is definitely not the most secure jail I have had to escape from ...')
    input("Knowing how stupid trolls are I check the ground for a key... once again my luck is not that good")
    input("Damn, guess I really will have to break out of here. . .\n")

def main_hub():
    print('What to do. . .')
    inventory()
    print("(Input 'left' to look left,")
    print("'right' to look right,")
    print("'back' to look behind you,")
    look = input("or 'door' to go to the door.)\n")
    if not look:
        main_hub()
    elif look == 'left' or look == 'Left':
        room_sides(mallet, bookshelf, bookshelf_q, crowbar, boarded_hole, pry, mallet_get)
    elif look == 'right' or look == 'Right':
        room_sides(crowbar, box_see, box_q, hand, box_open, box_easy, crowbar_get)
    elif look == 'back' or look == 'Back':
        room_sides(key, crack, crack_q, mallet, crack_complementing, crack_smash, key_get )
    elif look == 'door' or look == 'Door':
        game_end()
    else:
        main_hub()

def inventory():
    if crowbar == 0:
        print('Inventory: empty')
    elif crowbar == 1 and mallet == 0:
        print('Inventory: crowbar')
    elif crowbar == 1 and mallet == 1 and key == 0:
        print('Inventory: crowbar, mallet')
    else:
        print('Inventory: crowbar, mallet, key')

def room_sides(item_get, string1, string2, item_use, string3, string4, string5):
    global crowbar
    global mallet
    global key
    if item_get == 1:
        input(no_dice)
        return main_hub()
    input(string1)
    print(string2)
    action = input('(y for yes, n for no)\n')
    if not action:
        input(leave_alone)
        main_hub()
    if action == 'y' and item_use == 0:
        input(string3)
        input(cant)
        main_hub()
    elif action == 'n':
        input(leave_alone)
        main_hub()
    elif action == 'y' and item_use == 1:
        input(string3)
        input(string4)
        input(string5)
        if item_get == crowbar:
            crowbar =+ 1
            return main_hub()
        elif item_get == mallet:
            mallet =+ 1
            return main_hub()
        elif item_get == key:
            key =+ 1
            return main_hub()

def game_end():
    global key
    if key == 1:
        input("\nIf the key doesn't work I'll just hit the door with the mallet. Apparently that's how things get done around here.")
        input('*key fits and turns perfectly, unlocking the door*')
        input("Well...I mean...just wow! This was basically just a nice break from my adventure.")
        input('I walk outside and see a two-foot statue of gold. I estimated the weight of the statue, grabbed a small sack of sand, and carefully switched it with the gold ')
        input("I wait for a boulder to fall and roll after me or darts to fly at me...nothing! I look around and see a door with an exit sign above it")
        input("I sigh and walk out of the unlocked door. There is a horse waiting with a cinnimonbun in the saddlebag. I ride off into the sunset wondering if all adventures are this easy.")
        input("I guess I just have great luck after all... ~_^")
        input(" THANK YOU FOR PLAYING 'TRAPPED BY TROLLS'")
        input("DEVELOPED BY ONEIZM STUDIOS")
    else:
        input("I've already tried the door but who knows maybe...Why am I even checking I know my luck is crap. Back to looking around\n")
        return main_hub()

main_adventure()
