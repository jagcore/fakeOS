import time
import random

## config

wins = 0
losses = 0

## defaults:
# eSkill = 5
# fSkill = 5
# health starts at 100
# weapons starts as pistols
# both teams have 5 players (10 total)
# both teams start with 0g
# both teams start at their respective spawns. (They will be teleported there, but before the game you will see that they are in 0, the 'lobby')

# skill is a factor in firefights
# higher skill numbers mean more misses (weird, i know)
enemySkill = 5
friendlySkill = 5

# health is self explanatory
# if health goes to 0 team loses a player
enemyHealth = 100
friendlyHealth = 100

# 1 is pistol, 2 is smg, 3 is ak, and 4 is awp
# pistols do 25 damage and deal damage based on a multiplier representing 2 shots (max damage 50)
# smgs do 20 damage and deal damage based on a multiplier representing 3 shot bursts (max damage 60)
# aks do 75 damage but have 25% less accuracy
# awps do 100 damage but have a 50% to do 50
enemyWeapon = 1
friendlyWeapon = 1

# g is the currency used to buy weapons before a round
# g is earned by winning rounds or getting kills
friendlyG = 0
enemyG = 0

# team represents player count
# if bomb is planted, there is a 50% chance that CTside loses even if all of Tside dies
friendlyTeam = 5
enemyTeam = 5

# Pos represents location on the map.
# there are 6 positions:
# A site  - B site  - Mid (to B)  - Long (to A)  - Tspawn (connects Mid to Long)(not used) 5 - CTspawn (connects A site to B site)(not used) 6
# If Tside gets to a site without initiating a firefight, bomb is planted.
# This means that if Tside all dies there is still a 50% chance the bomb explodes resetting all weapons to pistols.
# Before a round, you can tell your team where to go. They can only go to A site or B site (if you are on ctside) or Long and mid (if you are on tside) in this way.

# Pos affects firefights. If all of Tside go to Mid and all of CTside are at B site, a firefight begins between one pair at a time.
# Splitting your team up is a smart idea as CTside, to at least weaken Tside before the plant the bomb, if not fully hold them off.
# On Tside, it is recommended that you keep your whole team together to protect the bomb carrier and get the highest chance of planting the bomb.
friendlyPos1 = 0
friendlyPos2 = 0
enemyPos1 = 0
enemyPos2 = 0


# bomb

## game funcs

def teamselector():
    x = random.randint(1,2)
    if x == 1:
        # this means player is on Tside
        return 1
    elif x == 2:
        # this means player is on CTside
        return 2
    else:
        pass

# THIS BEGINS def firefight(), possibly the most important func.

def firefight(friendlySkill, enemySkill, friendlyHealth, enemyHealth, friendlyWeapon, enemyWeapon):
    #IMPORTANT NOTE: due to technical limitations, after a firefight, alive players will return to 100 health. However, you can change the values to fit your own firefight scenarios.
    print()
    print("[|] FIREFIGHT START [|]")
    time.sleep(1)
    while friendlyHealth > 0 and enemyHealth > 0:
        roll = random.randint(1, 20)
        shots = 0
        dmg = 0
        
        print()
        print("FRIENDLY TURN (F|:]")
        time.sleep(1)
        print(f"Friendly has {friendlyHealth} HP.")
        time.sleep(1)
        
        # FRIENDLY TURN
        # friendly shoots first
        if roll == 20:
            # 20s mean headshots or instas
            # enemy still shoots, but he dies after the firing round
            enemyHealth = 0
            print("HEADSHOT by friendly.")
        elif roll == 1:
            # 1s mean guaranteed misses
            shots = random.randint(1,10)
            dmg = shots
            friendlyHealth -= shots
            print(f"Friendly choked and got potshot. {dmg} damage.")
        elif roll >= friendlySkill:
            if friendlyWeapon == 1:
                # pistol
                shots = random.randint(1,2)
                enemyHealth -= 25 * shots
                dmg = 25 * shots
                print(f"Friendly successfully shot enemy with pistol. {dmg} damage.")
            elif friendlyWeapon == 2:
                # smg
                shots = random.randint(1,3)
                enemyHealth -= 20 * shots
                dmg = 20 * shots
                print(f"Friendly successfully shot enemy with smg. {dmg} damage.")
            elif friendlyWeapon == 3:
                # ak
                shots = random.randint(1,4)
                if shots == 1:
                    pass
                else:
                    print("Friendly successfully shot enemy with ak. 75 damage.")
                    enemyHealth -= 75
            else:
                # awp
                shots = random.randint(1,2)
                if shots == 1:
                    print("Friendly hit enemy in the leg. 50 damage.")
                    enemyHealth -= 50
                else:
                    print("Friendly successfully shot enemy. 100 damage.")
                    enemyHealth -= 100
        elif roll < friendlySkill:
            print("Friendly missed.")
        
        roll = random.randint(1,20)
        time.sleep(1)
        print()
        print("ENEMY TURN (E|:]")
        time.sleep(1)
        print(f"Enemy has {enemyHealth} HP.")
        time.sleep(1)
        # ENEMY TURN
        # enemy shoots seceond
        if roll == 20:
            # 20s mean headshots or instas
            # enemy still shoots, but he dies after the firing round
            friendlyHealth = 0
            print("HEADSHOT by enemy.")
        elif roll == 1:
            # 1s mean guaranteed misses
            shots = random.randint(1,10)
            dmg = shots
            enemyHealth -= shots
            print(f"Enemy choked and got potshot. {dmg} damage.")
            pass
        elif roll >= enemySkill:
            if enemyWeapon == 1:
                # pistol
                shots = random.randint(1,2)
                friendlyHealth -= 25 * shots
                dmg = 25 * shots
                print(f"Enemy successfully shot friendly with pistol. {dmg} damage.")
            elif enemyWeapon == 2:
                # smg
                shots = random.randint(1,3)
                friendlyHealth -= 20 * shots
                dmg = 20 * shots
                print(f"Enemy successfully shot friendly with smg. {dmg} damage.")
            elif enemyWeapon == 3:
                # ak
                shots = random.randint(1,4)
                if shots == 1:
                    pass
                else:
                    print("Enemy successfully shot friendly with ak. 75 damage.")
                    enemyHealth -= 75
            else:
                # awp
                shots = random.randint(1,2)
                if shots == 1:
                    print("Enemy hit friendly in the leg. 50 damage.")
                    enemyHealth -= 50
                else:
                    print("Enemy successfully shot friendly. 100 damage.")
                    enemyHealth -= 100
        elif roll < enemySkill:
            print("Enemy missed.")
    time.sleep(1)
    print()
    if friendlyHealth <= 0 and enemyHealth <= 0:
        # 3 means both sides died
        print("Friendly and enemy both died.")
        return(3)
    elif friendlyHealth <= 0:
        # 1 means friendly lost
        print("Enemy gunned down friendly.")
        return(1)
    elif enemyHealth <= 0:
        # 2 means enemy lost
        print("Friendly gunned down enemy.")
        return(2)
    else:
        print("This isn't supposed to happen! ERROR in def firefight()")
        exit()
    time.sleep(1)
    print("[|] FIREFIGHT END [|]")
        
# THIS CONCLUDES def firefight()
            
                
        
## init
print("...TEXT BASED - TURN BASED CS:GO...")
print("         CREATED BY MICHAEL")
time.sleep(1)
print("inspired by xkcd 91 by Randall Munroe")
print("copyright lololol")
print("CS:GO originally made by Valve Studios")
print()

print("What gamemode would you like to play?")
print("RANKED DEFUSAL (1)|(2) SERVERS")
print("Please enter 1 or 2.")
x = int(input("{@input}:>> "))
if x == 1:
    print("Loading into ranked lobby...")
    time.sleep(4)
    print("Lobby connect successful. Finding open server...")
    time.sleep(10)
    print("Server found! Connecting")
    time.sleep(1)
elif x == 2:
    print("SERVERS")
    print("Please select a server.")
    print("Server calls can be found in servers.txt.")
    x = input("{@input}:>> ")
    if x == "gcd":
        exec(open("CD_CS.py").read())
        
    print("Server timeout. Program ending.")
    exit()
    
## load map de_dust2 for 'RANKED'
## The rest of this code is for RANKED. CUSTOM is in that if then.
print("PLEASE WAIT")
print("loading map de_dust2 ...")
time.sleep(3)
print("loaded.")
time.sleep(2)
print("loading players from lobby...")
print("loaded.")
print()
print()
time.sleep(1)

## team selection
x = teamselector()

# tside loop
if x == 1:
    while True:
        print("YOU CAN LEAVE GAME AFTER A ROUND. THE LOBBY WILL WAIT FOR MORE PLAYERS.")
        while True:
            time.sleep(2)
            print(f"Your Score: (wins | losses) {wins} | {losses}")
            friendlyPos1 = 5
            enemyPos1 = 5
            print("You are on Tside")
            print("You will have to plant a bomb at A site or B site. Once the bomb is planted, you will have to defend it.")
            print("Begin prep phase.")
            time.sleep(1)
            print("How many soldiers will you send to Long (to A site)? You have 5.")
            x = int(input("//: "))
            friendlyPos1 = x
            print(f"YOU: {x} go to Long. rest go Mid")
            friendlyPos2 = 5 - x
            time.sleep(1)
            print("FRIENDLY4: sounds good")
            time.sleep(2)
            print("FRIENDLY2: Gotcha")
            time.sleep(1)
            print(f"Buy a weapon? You have {friendlyG}g.")
            print("y/n")
            x = input("//:")
            if x == "y" and friendlyG < 100:
                print("You have no money to buy anything.")
            elif x == "y":
                print("Which weapon? 2 for SMG, 3 for AK, and 4 for AWP.")
                print("SMGs cost 100g. AKs cost 500g and AWPs cost 1000g.")
                x = input("//:")
                if x == "2" and friendlyG >= 100:
                    print("Buying SMGs.")
                    time.sleep(1)
                    friendlyG -= 100
                    print("YOU: buy smgs")
                    time.sleep(2)
                    print("FRIENDLY5: i like smgs")
                    time.sleep(1)
                    print("FRIENDLY3: ill buy 1")
                    friendlyWeapon = 2
                elif x == "3" and friendlyG >= 500:
                    print("Buying AKs.")
                    time.sleep(1)
                    friendlyG -= 500
                    print("YOU: buy aks")
                    time.sleep(2)
                    print("FRIENDLY2: done")
                    time.sleep(3)
                    print("FRIENDLY4: i got 2 anybody need 1?")
                    friendlyWeapon = 3
                elif x == "4" and friendlyG >= 1000:
                    print("Buying AWPS.")
                    time.sleep(1)
                    print("YOU: It's AWP time buy awps")
                    time.sleep(1)
                    print("FRIENDLY3: YEAHHHHH")
                    time.sleep(2)
                    print("FRIENDLY2: HECK YES")
                    time.sleep(1)
                    print("FRIENDLY5: AWP RUSH LETS GOOOO")
                    time.sleep(3)
                    print("FRIENDLY4: they dont stand a chance")
                    friendlyWeapon = 4
                else:
                    print("No money.")
            else:
                print("Pregame complete. GO!")
            ## enemy side buying
            if enemyG > 1000:
                enemyG -= 1000
                enemyWeapon = 4
            elif enemyG > 500:
                enemyG -= 500
                enemyWeapon = 3
            elif enemyG > 100:
                enemyG -= 100
                enemyWeapon = 2
            else:
                pass
            ## enemy side splitting
            enemyPos1 = random.randint(0,5)
            enemyPos2 = 5 - enemyPos1
            time.sleep(3)
            # game set
            print("LONG / B SITE | RESOLVING")
            while friendlyPos1 > 0 and enemyPos1 > 0:
                x = firefight(friendlySkill, enemySkill, friendlyHealth, enemyHealth, friendlyWeapon, enemyWeapon)
                if x == 3:
                    friendlyPos1 -= 1
                    enemyPos1 -= 1
                    friendlyG += 10
                    enemyG += 10
                elif x == 2:
                    enemyPos1 -= 1
                    friendlyG += 50
                elif x == 3:
                    friendlyPos1 -= 1
                    enemyG += 50
                else:
                    pass
            friendlyTeam = friendlyPos1 + friendlyPos2
            enemyTeam = enemyPos1 + enemyPos2
            print(f"You have a total of {friendlyTeam} players, and the enemy has {enemyTeam} players.")
            if friendlyPos1 == 0 and enemyPos1 == 0:
                print("YOU: Wow. Draw.")
                print("FRIENDLY3: yeesh.")
                time.sleep(1)
                print("ENEMY1: lol")
                time.sleep(2)
                print("FRIENDLY2: gg")
            elif enemyPos1 == 0:
                print("BOMB HAS BEEN PLANTED.")
                time.sleep(1)
                print("YOU: gj everyone")
                time.sleep(1)
                print("FRIENDLY5: yay :D")
                print("ENEMY4: gg")
            elif friendlyPos1 == 0:
                print("YOU: gg")
                time.sleep(1)
                print("ENEMY2: gg")
            elif friendlyTeam == 0:
                print("CTSIDE WINS")
                print("YOU: gg")
                print("3+ Others: gg")
                friendlyWeapon = 1
                losses += 1
                break
            elif enemyTeam == 0:
                print("TSIDE WINS")
                print("YOU: GG")
                print("3+ Others: gg")
                enemyWeapon = 1
                wins += 1
                break
            else:
                print("An error occured in your lobby. You will be kicked, and the game will not count.")
                exit()
            
                
            # next set    
            time.sleep(1)
            print("MID / A SITE | RESOLVING")
            while friendlyPos2 > 0 and enemyPos2 > 0:
                x = firefight(friendlySkill, enemySkill, friendlyHealth, enemyHealth, friendlyWeapon, enemyWeapon)
                if x == 3:
                    friendlyPos2 -= 1
                    enemyPos2 -= 1
                    friendlyG += 10
                    enemyG += 10
                elif x == 2:
                    enemyPos2 -= 1
                    friendlyG += 50
                elif x == 3:
                    friendlyPos2 -= 1
                    enemyG += 50
                else:
                    pass
            friendlyTeam = friendlyPos1 + friendlyPos2
            enemyTeam = enemyPos1 + enemyPos2
            print(f"You have a total of {friendlyTeam} players, and the enemy has {enemyTeam} players.")
            if friendlyPos2 == 0 and enemyPos2 == 0:
                print("YOU: Wow. Draw.")
                print("FRIENDLY3: yeesh.")
                time.sleep(1)
                print("ENEMY1: lol")
                time.sleep(2)
                print("FRIENDLY2: gg")
            elif enemyPos2 == 0:
                print("BOMB HAS BEEN PLANTED.")
                time.sleep(1)
                print("YOU: gj everyone")
                time.sleep(1)
                print("FRIENDLY5: yay :D")
                print("ENEMY4: gg")
            elif friendlyPos2 == 0:
                print("YOU: gg")
                time.sleep(1)
                print("ENEMY2: gg")
            elif friendlyTeam == 0:
                print("CTSIDE WINS")
                print("YOU: gg")
                print("3+ Others: gg")
                losses += 1
                friendlyWeapon = 1
                break
            elif enemyTeam == 0:
                print("TSIDE WINS")
                print("YOU: GG")
                print("3+ Others: gg")
                enemyWeapon = 1
                wins += 1
                break
            else:
                print("An error occured in your lobby. You will be kicked, and the game will not count.")
                exit()
                
            # final set 
            time.sleep(1)
            print(f"You have a total of {friendlyTeam} players, and the enemy has {enemyTeam} players.")
            time.sleep(1)
            print("HUNT/DEFUSE STAGE | RESOLVING")
            # everyone gets together and hunts the last players
            while friendlyTeam > 0 and enemyTeam > 0:
                x = firefight(friendlySkill, enemySkill, friendlyHealth, enemyHealth, friendlyWeapon, enemyWeapon)
                if x == 3:
                    friendlyTeam -= 1
                    enemyTeam -= 1
                    friendlyG += 10
                    enemyG += 10
                elif x == 2:
                    enemyTeam -= 1
                    friendlyG += 50
                elif x == 3:
                    friendlyTeam -= 1
                    enemyG += 50
                else:
                    pass
            roll = random.randint(1,2)
            if friendlyTeam == 0 and enemyTeam == 0:
                print("TSIDE WINS")
                time.sleep(1)
                print("YOU: gg")
                print("ENEMY3: GG")
                friendlyWeapon = 1
                enemyWeapon = 1
                wins += 1
            elif friendlyTeam == 0 and roll == 1:
                print("TSIDE WINS")
                time.sleep(1)
                print("YOU: gg")
                print("FRIENDLY3: lets gooo")
                time.sleep(1)
                print("ENEMY1: gg")
                time.sleep(2)
                print("ENEMY4: gg")
                friendlyWeapon = 1
                enemyWeapon = 1
                wins += 1
            elif friendlyTeam == 0 and roll == 2:
                print("BOMB HAS BEEN DEFUSED")
                print("CTSIDE WINS")
                time.sleep(1)
                print("YOU: gt team")
                time.sleep(1)
                print("FRIENDLY5: gg")
                print("ENEMY4: gg")
                time.sleep(1)
                print("ENEMY2: yeahhhh lets gooo")
                friendlyWeapon = 1
                losses += 1
            elif enemyTeam == 0:
                print("TSIDE WINS")
                print("YOU: gg")
                time.sleep(1)
                print("ENEMY2: gg")
                enemyWeapon = 1
                wins += 1
            else:
                print("An error occured in your lobby. You will be kicked, and the game will not count.")
                exit()
        
        
        
# ctside loop       
elif x == 2:
    while True:
            print("YOU CAN LEAVE GAME AFTER A ROUND. THE LOBBY WILL WAIT FOR MORE PLAYERS.")
            while True:
                time.sleep(2)
                print(f"Your Score: (wins | losses) {wins} | {losses}")
                friendlyPos1 = 5
                enemyPos1 = 5
                print("You are on CTside")
                print("You will have to defend the sites from Tside. If the bomb is planted, you will have to defuse it.")
                print("Begin prep phase.")
                time.sleep(1)
                print("How many soldiers will you send to A site (defend from long)? You have 5.")
                x = int(input("//: "))
                friendlyPos1 = x
                print(f"YOU: {x} defend A site. rest go to B")
                friendlyPos2 = 5 - x
                time.sleep(1)
                print("FRIENDLY3: ok")
                time.sleep(2)
                print("FRIENDLY2: alright")
                time.sleep(1)
                print(f"Buy a weapon? You have {friendlyG}g.")
                print("y/n")
                x = input("//:")
                if x == "y" and friendlyG < 100:
                    print("You have no money to buy anything.")
                elif x == "y":
                    print("Which weapon? 2 for SMG, 3 for AK, and 4 for AWP.")
                    print("SMGs cost 100g. AKs cost 500g and AWPs cost 1000g.")
                    x = input("//:")
                    if x == "2" and friendlyG >= 100:
                        print("Buying SMGs.")
                        time.sleep(1)
                        friendlyG -= 100
                        print("YOU: buy smgs")
                        time.sleep(2)
                        print("FRIENDLY4: sounds good")
                        time.sleep(1)
                        print("FRIENDLY5: sure")
                        friendlyWeapon = 2
                    elif x == "3" and friendlyG >= 500:
                        print("Buying AKs.")
                        time.sleep(1)
                        friendlyG -= 500
                        print("YOU: buy aks")
                        time.sleep(2)
                        print("FRIENDLY3: i like aks")
                        time.sleep(3)
                        print("FRIENDLY5: Ill buy 2 anybody need 1?")
                        friendlyWeapon = 3
                    elif x == "4" and friendlyG >= 1000:
                        print("Buying AWPS.")
                        time.sleep(1)
                        print("YOU: AWP defense buy awps")
                        time.sleep(1)
                        print("FRIENDLY4: Hold the line")
                        time.sleep(2)
                        print("FRIENDLY2: we will be victorious")
                        time.sleep(1)
                        print("FRIENDLY5: AWP more like AW man")
                        time.sleep(3)
                        print("FRIENDLY4: lets go")
                        friendlyWeapon = 4
                    else:
                        print("No money.")
                else:
                    print("Pregame complete. GO!")
                ## enemy side buying
                if enemyG > 1000:
                    enemyG -= 1000
                    enemyWeapon = 4
                elif enemyG > 500:
                    enemyG -= 500
                    enemyWeapon = 3
                elif enemyG > 100:
                    enemyG -= 100
                    enemyWeapon = 2
                else:
                    pass
                ## enemy side splitting
                enemyPos1 = random.randint(0,5)
                enemyPos2 = 5 - enemyPos1
                time.sleep(3)
                # game set
                print("LONG / B SITE | RESOLVING")
                while friendlyPos1 > 0 and enemyPos1 > 0:
                    x = firefight(friendlySkill, enemySkill, friendlyHealth, enemyHealth, friendlyWeapon, enemyWeapon)
                    if x == 3:
                        friendlyPos1 -= 1
                        enemyPos1 -= 1
                        friendlyG += 10
                        enemyG += 10
                    elif x == 2:
                        enemyPos1 -= 1
                        friendlyG += 50
                    elif x == 3:
                        friendlyPos1 -= 1
                        enemyG += 50
                    else:
                        pass
                friendlyTeam = friendlyPos1 + friendlyPos2
                enemyTeam = enemyPos1 + enemyPos2
                print(f"You have a total of {friendlyTeam} players, and the enemy has {enemyTeam} players.")
                if friendlyPos1 == 0 and enemyPos1 == 0:
                    print("YOU: gg")
                    print("FRIENDLY4: draw wow")
                    time.sleep(1)
                    print("ENEMY1: lol")
                    time.sleep(2)
                    print("FRIENDLY2: gg")
                elif friendlyPos1 == 0:
                    print("BOMB HAS BEEN PLANTED.")
                    time.sleep(1)
                    print("YOU: darn")
                    time.sleep(1)
                    print("FRIENDLY5: gg")
                    print("ENEMY4: ggs")
                elif enemyPos1 == 0:
                    print("YOU: nice gj everyone")
                    time.sleep(1)
                    print("ENEMY2: gg")
                    print("FRIENDLY2: gg")
                elif friendlyTeam == 0:
                    print("TSIDE WINS")
                    print("YOU: gg")
                    print("3+ Others: gg")
                    friendlyWeapon = 1
                    losses += 1
                    break
                elif enemyTeam == 0:
                    print("CTSIDE WINS")
                    print("YOU: GG")
                    print("3+ Others: gg")
                    enemyWeapon = 1
                    wins += 1
                    break
                else:
                    print("An error occured in your lobby. You will be kicked, and the game will not count.")
                    exit()
                
                    
                # next set    
                time.sleep(1)
                print("MID / A SITE | RESOLVING")
                while friendlyPos2 > 0 and enemyPos2 > 0:
                    x = firefight(friendlySkill, enemySkill, friendlyHealth, enemyHealth, friendlyWeapon, enemyWeapon)
                    if x == 3:
                        friendlyPos2 -= 1
                        enemyPos2 -= 1
                        friendlyG += 10
                        enemyG += 10
                    elif x == 2:
                        enemyPos2 -= 1
                        friendlyG += 50
                    elif x == 3:
                        friendlyPos2 -= 1
                        enemyG += 50
                    else:
                        pass
                friendlyTeam = friendlyPos1 + friendlyPos2
                enemyTeam = enemyPos1 + enemyPos2
                print(f"You have a total of {friendlyTeam} players, and the enemy has {enemyTeam} players.")
                if friendlyPos2 == 0 and enemyPos2 == 0:
                    print("YOU: draw")
                    print("FRIENDLY5: nice")
                    time.sleep(1)
                    print("ENEMY3: gg")
                    time.sleep(2)
                    print("ENEMY2: good game")
                elif friendlyPos2 == 0:
                    print("BOMB HAS BEEN PLANTED.")
                    time.sleep(1)
                    print("YOU: aw man")
                    print("ENEMY2: yeahhh")
                    time.sleep(1)
                    print("FRIENDLY5: ouch")
                    print("ENEMY4: gg")
                elif enemyPos2 == 0:
                    print("YOU: nice defense")
                    time.sleep(1)
                    print("FRIENDLY2: gg")
                    print("ENEMY2: gg")
                elif friendlyTeam == 0:
                    print("TSIDE WINS")
                    print("YOU: gg")
                    print("3+ Others: gg")
                    losses += 1
                    friendlyWeapon = 1
                    break
                elif enemyTeam == 0:
                    print("CTSIDE WINS")
                    print("YOU: GG")
                    print("3+ Others: gg")
                    enemyWeapon = 1
                    wins += 1
                    break
                else:
                    print("An error occured in your lobby. You will be kicked, and the game will not count.")
                    exit()
                    
                # final set 
                time.sleep(1)
                print(f"You have a total of {friendlyTeam} players, and the enemy has {enemyTeam} players.")
                time.sleep(1)
                print("HUNT/DEFUSE STAGE | RESOLVING")
                # everyone gets together and hunts the last players
                while friendlyTeam > 0 and enemyTeam > 0:
                    x = firefight(friendlySkill, enemySkill, friendlyHealth, enemyHealth, friendlyWeapon, enemyWeapon)
                    if x == 3:
                        friendlyTeam -= 1
                        enemyTeam -= 1
                        friendlyG += 10
                        enemyG += 10
                    elif x == 2:
                        enemyTeam -= 1
                        friendlyG += 50
                    elif x == 3:
                        friendlyTeam -= 1
                        enemyG += 50
                    else:
                        pass
                roll = random.randint(1,2)
                if friendlyTeam == 0 and enemyTeam == 0:
                    print("TSIDE WINS")
                    time.sleep(1)
                    print("YOU: gg")
                    print("ENEMY3: GG")
                    friendlyWeapon = 1
                    enemyWeapon = 1
                    losses += 1
                elif enemyTeam == 0 and roll == 1:
                    print("TSIDE WINS")
                    time.sleep(1)
                    print("YOU: gg")
                    print("FRIENDLY3: ughhh")
                    time.sleep(1)
                    print("ENEMY1: gg")
                    time.sleep(2)
                    print("ENEMY4: gg")
                    friendlyWeapon = 1
                    enemyWeapon = 1
                    losses += 1
                elif enemyTeam == 0 and roll == 2:
                    print("BOMB HAS BEEN DEFUSED")
                    print("CTSIDE WINS")
                    time.sleep(1)
                    print("YOU: nice defuse")
                    time.sleep(1)
                    print("FRIENDLY5: yeahhhh")
                    print("ENEMY4: gg")
                    time.sleep(1)
                    print("ENEMY2: gg")
                    enemyWeapon = 1
                    wins += 1
                elif friendlyTeam == 0:
                    print("TSIDE WINS")
                    print("YOU: darn")
                    time.sleep(1)
                    print("FRIENDLY5: gg")
                    print("ENEMY2: gg")
                    friendlyWeapon = 1
                    losses += 1
                else:
                    print("An error occured in your lobby. You will be kicked, and the game will not count.")
                    exit()
else:
    print("This shouldn't happen! ERROR! check def teamselector() or the team select init")

