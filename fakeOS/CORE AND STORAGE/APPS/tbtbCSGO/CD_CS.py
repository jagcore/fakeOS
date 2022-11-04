import time
import random

# default settings:
# gun types: 1 = pistol | 2 = smg | 3 = ak | 4 = awp
yourGun = 1
enemyGun = 1
you = ""
them = ""
yourSkill = 10
enemySkill = 10
yourHP = 100
enemyHP = 100
roll = 0

def userCreate():
    # returns a random username from this list
    x = random.randint(1, 20)
    if x == 1:
        return("xX_ProGamer_Xx")
    elif x == 2:
        return("n00b123")
    elif x == 3:
        return("amongus")
    elif x == 4:
        return("Water Bottle 2.0")
    elif x == 5:
        return("Strafe.God")
    elif x == 6:
        return("GG_Gamer")
    elif x == 7:
        return("LEEEEEERRRROOOYYYY JEEEEEENNNNKIIINNNNNSSSS")
    elif x == 8:
        return("AK_Enjoyer")
    elif x == 9:
        return("AWP_Stan")
    elif x == 10:
        return("rain")
    elif x == 11:
        return("yoshi")
    elif x == 12:
        return("tax fraud")
    elif x == 13:
        return("UnluckyDuckie")
    elif x == 14:
        return("JohnDoe")
    elif x == 15:
        return("Scout from tf2")
    elif x == 16:
        return("Sosig")
    elif x == 17:
        return("CvC better")
    elif x == 18:
        return("3ds Master Race")
    elif x == 19:
        return("pikachu")
    elif x == 20:
        return("ovo")
    else:
        return("Wow! This username never gets used!")

def firefight(friendlySkill, enemySkill, friendlyHealth, enemyHealth, friendlyWeapon, enemyWeapon, friendlyUser, enemyUser):
    #IMPORTANT NOTE: due to technical limitations, after a firefight, alive players will return to 100 health. However, you can change the values to fit your own firefight scenarios.
    print("DUEL START")
    print(f"{friendlyUser} VS {enemyUser}")
    time.sleep(1)
    while friendlyHealth < 0 and enemyHealth < 0:
        
        roll = random.randint(1, 20)
        shots = 0
        dmg = 0
        
        print("Your Turn")
        print(f"You have {friendlyHealth} HP")
        time.sleep(2)
        
        # FRIENDLY TURN
        # friendly shoots first
        if roll == 20:
            # 20s mean headshots or instas
            # enemy still shoots, but he dies after the firing round
            enemyHealth = 0
            print(f"{friendlyUser} got a headshot!")
        elif roll == 1:
            # 1s mean chokes. You accidentally bait a shot, and are hit with a potshot. this does 10 dmg.
            print(f"{friendlyUser} choked and got potshot.")
            friendlyHealth -= 10
        elif roll >= friendlySkill:
            if friendlyWeapon == 1:
                # pistol
                shots = random.randint(1,2)
                enemyHealth -= 25 * shots
                dmg = 25 * shots
                print(f"{friendlyUser} successfully shot {enemyUser} with pistol. {dmg} damage. ({shots} shots hit)")
            elif friendlyWeapon == 2:
                # smg
                shots = random.randint(1,3)
                enemyHealth -= 20 * shots
                dmg = 20 * shots
                print(f"{friendlyUser} successfully shot {enemyUser} with smg. {dmg} damage. ({shots} shots hit)")
            elif friendlyWeapon == 3:
                # ak
                shots = random.randint(1,4)
                if shots == 1:
                    print(f"{friendlyUser} missed their shot due to the immense power of the ak.")
                else:
                    print(f"{friendlyUser} successfully shot {enemyUser} with ak. 75 damage.")
                    enemyHealth -= 75
            else:
                # awp
                shots = random.randint(1,2)
                if shots == 1:
                    print(f"{friendlyUser} hit {enemyUser} in the leg. 50 damage.")
                    enemyHealth -= 50
                else:
                    print(f"{friendlyUser} successfully shot {enemyUser}. 100 damage.")
                    enemyHealth -= 100
        elif roll < friendlySkill:
            # when the shot is less than your skill, it misses. this is why higher skill numbers mean more misses
            print(f"{friendlyUser} missed their shot.")
        
        roll = random.randint(1,20)
        print()
        time.sleep(1)
        print(f"{enemyUser}'s Turn ")
        print(f"{enemyUser} has {enemyHealth} HP")
        time.sleep(2)
        # ENEMY TURN
        # enemy shoots seceond
        if roll == 20:
            # 20s mean headshots or instas
            # enemy still shoots, but he dies after the firing round
            friendlyHealth = 0
            print(f"{enemyUser} got a headshot!")
        elif roll == 1:
            # 1s mean chokes and you take 10 damage
            print(f"{enemyUser} choked and got potshot.")
            enemyHealth -= 10
        elif roll >= enemySkill:
            if enemyWeapon == 1:
                # pistol
                shots = random.randint(1,2)
                friendlyHealth -= 25 * shots
                dmg = 25 * shots
                print(f"{enemyUser} successfully shot {friendlyUser} with pistol. {dmg} damage. ({shots} hit)")
            elif enemyWeapon == 2:
                # smg
                shots = random.randint(1,3)
                friendlyHealth -= 20 * shots
                dmg = 20 * shots
                print(f"{enemyUser} successfully shot {friendlyUser} with smg. {dmg} damage. ({shots} shots hit)")
            elif enemyWeapon == 3:
                # ak
                shots = random.randint(1,4)
                if shots == 1:
                    print(f"{enemyUser} missed their shot due to the immense power of the ak.")
                else:
                    print(f"{enemyUser} successfully shot {friendlyUser} with ak. 75 damage.")
                    enemyHealth -= 75
            else:
                # awp
                shots = random.randint(1,2)
                if shots == 1:
                    print(f"{enemyUser} hit {friendlyUser} in the leg. 50 damage.")
                    enemyHealth -= 50
                else:
                    print(f"{enemyUser} successfully shot {friendlyUser}. 100 damage.")
                    enemyHealth -= 100
        elif roll < enemySkill:
            print(f"{enemyUser} missed their shot.")
            
        time.sleep(1)
        print("---{ Shots Fired! }---")
        
        
    if friendlyHealth <= 0 and enemyHealth <= 0:
        # 3 means both sides died
        print("Draw.")
        return(3)
    elif friendlyHealth <= 0:
        # 1 means friendly lost
        print(f"{enemyUser} wins!")
        return(1)
    elif enemyHealth <= 0:
        # 2 means enemy lost
        print(f"{friendlyUser} wins!")
        return(2)
    else:
        print("This isn't supposed to happen! ERROR in def firefight()")
        exit()
        
# THIS CONCLUDES def firefight()

## init
print("Duels Modpack Enabled")
time.sleep(1)
print("CD_CS.py modpack for tb2CSGO")
print("tb2CSGO made by Michael 'jagcore'")
print("CD_CS.py made by Michael 'jagcore'")
time.sleep(1)
print("Relocating server...")
time.sleep(2)
print("Finalizing connection...")
time.sleep(3)
print("Welcome to the server!")
print("Enter a username.")
you = str(input("//:"))
time.sleep(1)
print("Regristration Complete! Welcome to the server.")
print("Do you want to play on an official preset? Or is a custom firefight more your style? Bot wars are still being worked on.")
time.sleep(1)
print("Enter either 1 for presets, 2 for custom, or 3 for bot wars (UNFINISHED).")
x = int(input("//: "))
if x == 1:
    print("Matching you to a presets lobby...")
    print("When you want to leave, say exit after a duel.")
    ## core presets loop
    time.sleep(1)
    print("Lobby found!")
    them = userCreate()
    print(f"You are matched with {them}.")
    time.sleep(1)
    print("The preset is:")
    time.sleep(1)
    # there are a lot of different presets, so Ill list em here
    # 200HP Skill 05 SMGs (SMG200)
    # 100HP Skill 10 Pistols (PistolSilver)
    # 200HP Skill 10 AKs (AK200)
    # 300HP Skill 05 AWPs (NoScopeSaturday)
    # And who could forget:
    # 010HP Skill 15 AKs (TheFunnyOne)
    # preset is chosen at random, except for TheFunnyOne, which has, since release, been incredibly rare.
    roll = random.randint(1,101)
    if roll == 101:
        print("WOW! It's... TheFunnyOne.")
        time.sleep(1)
        print("In TheFunnyOne, you have 10 HP, Skill 15, and an ak. Good luck. You'll need it. Did you know that TheFunnyOne is the rarest preset?")
        yourGun = 3
        enemyGun = 3
        yourHP = 10
        enemyHP = 10
        yourSkill = 15
        enemySkill = 15
    elif roll > 0 and roll <= 25:
        print("SMG200.")
        time.sleep(1)
        print("In SMG200, you have 200 HP, Skill 5, and an smg. Perfect for trigger happies.")
        yourGun = 2
        enemyGun = 2
        yourHP = 200
        enemyHP = 200
        yourSkill = 5
        enemySkill = 5
    elif roll > 25 and roll <= 50:
        print("PistolSilver.")
        time.sleep(1)
        print("In PistolSilver, you'll relive your first ranked defusal silver pistol round. You have 100 HP, Skill 10, and a pistol.")
        yourGun = 1
        enemyGun = 1
        yourHP = 100
        enemyHP = 100
        yourSkill = 10
        enemySkill = 10
    elif roll > 50 and roll <= 75:
        print("AK200.")
        time.sleep(1)
        print("In AK200, you have 200 HP, Skill 10, and an ak. Perfect if you want to learn how to use the ak.")
        yourGun = 3
        enemyGun = 3
        yourHP = 200
        enemyHP = 200
        yourSkill = 10
        enemySkill = 10
    elif roll > 75 and roll <= 100:
        print("NoScopeSaturday.")
        time.sleep(1)
        print("In NoScopeSaturday, you can unleash your inner trickshot. You have 300 HP, Skill 5, and an AWP.")
        yourGun = 4
        enemyGun = 4
        yourHP = 300
        enemyHP = 300
        yourSkill = 5
        enemySkill = 5
    else:
        print("I hope nobody sees this jagcore is dum ok baiiiiiiii")
        print("also bigbigbigbigbig BEEEEEEEEG error in presets lmao uhh kthx")
        
    time.sleep(2)
    print("Now that the preset is chosen, the duel may commence!")
    time.sleep(1)
    print("syncing connection...")
    time.sleep(3)
    print("synced.")
    firefight(yourSkill, enemySkill, yourHP, enemyHP, yourGun, enemyGun, you, them)
    time.sleep(2)
    print("GG! That was an amazing duel.")
    print("Do you want to keep playing presets? Or leave the server?")
    print("Keep playing (ok) | (exit) leave game")
    x = input("//: ")
    if x == "ok":
        print("Glad to hear it! We'll open up a presets lobby.")
        while True:
            print("Matching you to a presets lobby...")
            print("When you want to leave, say exit after a duel.")
            ## core presets loop
            time.sleep(1)
            print("Lobby found!")
            them = userCreate()
            print(f"You are matched with {them}.")
            time.sleep(1)
            print("The preset is:")
            time.sleep(1)
            # there are a lot of different presets, so Ill list em here
            # 200HP Skill 05 SMGs (SMG200)
            # 100HP Skill 10 Pistols (PistolSilver)
            # 200HP Skill 10 AKs (AK200)
            # 300HP Skill 05 AWPs (NoScopeSaturday)
            # And who could forget:
            # 010HP Skill 15 AKs (TheFunnyOne)
            # preset is chosen at random, except for TheFunnyOne, which has, since release, been incredibly rare.
            roll = random.randint(1,101)
            if roll == 101:
                print("WOW! It's... TheFunnyOne.")
                time.sleep(1)
                print("In TheFunnyOne, you have 10 HP, Skill 15, and an ak. Good luck. You'll need it. Did you know that TheFunnyOne is the rarest preset?")
                yourGun = 3
                enemyGun = 3
                yourHP = 10
                enemyHP = 10
                yourSkill = 15
                enemySkill = 15
            elif roll > 0 and roll <= 25:
                print("SMG200.")
                time.sleep(1)
                print("In SMG200, you have 200 HP, Skill 5, and an smg. Perfect for trigger happies.")
                yourGun = 2
                enemyGun = 2
                yourHP = 200
                enemyHP = 200
                yourSkill = 5
                enemySkill = 5
            elif roll > 25 and roll <= 50:
                print("PistolSilver.")
                time.sleep(1)
                print("In PistolSilver, you'll relive your first ranked defusal silver pistol round. You have 100 HP, Skill 10, and a pistol.")
                yourGun = 1
                enemyGun = 1
                yourHP = 100
                enemyHP = 100
                yourSkill = 10
                enemySkill = 10
            elif roll > 50 and roll <= 75:
                print("AK200.")
                time.sleep(1)
                print("In AK200, you have 200 HP, Skill 10, and an ak. Perfect if you want to learn how to use the ak.")
                yourGun = 3
                enemyGun = 3
                yourHP = 200
                enemyHP = 200
                yourSkill = 10
                enemySkill = 10
            elif roll > 75 and roll <= 100:
                print("NoScopeSaturday.")
                time.sleep(1)
                print("In NoScopeSaturday, you can unleash your inner trickshot. You have 300 HP, Skill 5, and an AWP.")
                yourGun = 4
                enemyGun = 4
                yourHP = 300
                enemyHP = 300
                yourSkill = 5
                enemySkill = 5
            else:
                print("'I hope nobody sees this jagcore is dumb ok byeee' - Adaptation of a quote by: carykh ")
                print("Kicking from server 'gcd_cs.s': error in 'presets.ss.gcd_cs.s'")
        
            time.sleep(2)
            print("Loading map...")
            time.sleep(1)
            print("syncing connection...")
            time.sleep(3)
            print("synced.")
            firefight(yourSkill, enemySkill, yourHP, enemyHP, yourGun, enemyGun, you, them)
        
        
    
    
elif x == 2:
    print("Creating a customs lobby...")
    print("When you want to leave, say exit after a duel.")
    ## core customs loop
    while True:
        time.sleep(1)
        print("First, set the health for both players. 100 is default.")
        yourHP = int(input("//: "))
        enemyHP = yourHP
        time.sleep(1)
        print("Next, set the weapon for both players. 1 is pistol, 2 is smg, 3 is ak, and 4 is awp.")
        yourGun = int(input("//: "))
        enemyGun = yourGun
        time.sleep(1)
        print("Finally, set your skill level. This is to match players similar in skill with you. 0 skill is deadeye (you will do damage every turn), while 20 is headshot or bust (also the worst possible accuracy).")
        yourSkill = int(input("//:"))
        enemySkill = yourSkill
        time.sleep(1)
        print("Settings complete! Finding player...")
        time.sleep(5)
        them = userCreate()
        print(f"Player {them} found! Starting Duel...")
        time.sleep(1)
        firefight(yourSkill, enemySkill, yourHP, enemyHP, yourGun, enemyGun, you, them)
        
        print("GG! Hope you both had fun. You want to play again? Or do you want to exit the server?")
        print("Play customs again (ok) OR (exit) Exit CD_CS server?")
        x = input("//: ")
        if x == "ok":
            print("Cool! We'll open another customs lobby for you.")
            print("Have fun!")
            while True:
                time.sleep(3)
                print("First, set the health for both players.")
                yourHP = int(input("//: "))
                enemyHP = yourHP
                time.sleep(1)
                print("Next, set the weapon for both players. 1 is pistol, 2 is smg, 3 is ak, and 4 is awp.")
                yourGun = int(input("//: "))
                enemyGun = yourGun
                time.sleep(1)
                print("Finally, set your skill level. This will match you with players similar in skill to you. Higher skill means more misses.")
                yourSkill = int(input("//:"))
                enemySkill = yourSkill
                time.sleep(1)
                print("Settings complete! Finding player...")
                time.sleep(5)
                them = userCreate()
                print(f"Player {them} found! Starting Duel...")
                time.sleep(2)
                firefight(yourSkill, enemySkill, yourHP, enemyHP, yourGun, enemyGun, you, them)
                print("Play customs again (ok) OR (exit) Exit CD_CS server?")
                x = input("//: ")
                if x == "ok":
                    pass
                elif x == "exit":
                    print("Thanks for playing with us! We hope to see you soon.")
                    exit()
                else:
                    print("Kicking from server 'gcd_cs.s': error in 'customs.ss.gcd_cs.s'")
                    exit()
                
        
        elif x == "exit":
            print("Thanks for playing with us! We hope to see you soon.")
            exit()
        else:
            print("Kicking from server 'gcd_cs.s': error in 'customs.ss.gcd_cs.s'")
            exit()
elif x == 3:
    print("Matching to bot wars lobby...")
    time.sleep(7)
    print("Matched!")
    print("ERROR: 'botwars is unfinished'")
    time.sleep(0.3)
    print("Kicking from server 'botwars01.ss.gcd_cs.s': error in 'botwars01.ss.gcd_cs.s'")
    time.sleep(0.2)
    print("Kicking from server 'gcd_cs.s': error in 'clientsideRender.svd', 'clientsideServerHandler.svd', 'serverHandler.svd', 'CD_CS.py'")