import time
import os
# Built-in funcs

def ERROR():
    print("---{}---")
    print("FATAL ERROR HAS OCCURRED")
    time.sleep(1)
    print("This may have been caused by:")
    print("UNFINISHED CONTENT or BUG IN MAIN LOOP")
    time.sleep(1)
    print("reload fakeOS and try again.")
    exit()

def init():
    print("initializing fakeOS...")
    time.sleep(1)
    print("init successful")
    print("Function 'init' ending...")
    
def START(program):
    print("Starting program...")
    time.sleep(2)
    print(f"Program '{program}' started successfully.")

def END(program):
    print("Ending program...")
    time.sleep(1)
    print(f"Program '{program}' ended successfully.")

def OSmain():
    print("---{}---")
    print("fakeOS")
    time.sleep(1)
    print("v1.0")
    print("Created by Michael 'jagcore'")
    time.sleep(1)
    print()

#SHELL
    
#SHELL HANDLER
def SHELL_HANDLER():
    SHELL_INIT()
    # Can't change variables with funcs so they are in the handler
    shellVAR01 = 0
    shellVAR02 = 0
    shellinput01 = 0
    shellinput02 = 0
    while True:
        # input area
        shell = input("//: ")
        
        # print command
        if shell == "SHELL_PRINT":
            shellinput01 = input("$PRINT$//:")
            # checks if input is a var and prints var val
            if shellinput01 == "01":
                SHELL_PRINT(shellVAR01)
            elif shellinput01 == "02":
                SHELL_PRINT(shellVAR02)
            # else, prints input    
            else:
                SHELL_PRINT(shellinput01)
        
        # shell end command
        elif shell == "SHELL_END":
            SHELL_END()
            break
        
        # resetVARS
        elif shell == "resetVARS":
            # resetting all vars, including inputs to int(0)
            shellVAR01 = 0
            shellVAR02 = 0
            shellinput01 = 0
            shellinput02 = 0
            print("All vars reset.")
            
        # setVAR
        elif shell == "setVAR":
            shellinput01 = input("$VARtoEDIT$//: ")
            # checks if var being changed is 01
            if shellinput01 == "01":
                shellinput02 = input("$TYPE$//: ")
                # makes the type of val str or int
                # then sets var to val
                if shellinput02 == "str":
                    shellinput01 = str(input("$VAL$//: "))
                elif shellinput02 == "int":
                    shellinput01 = int(input("$VAL$//:"))
                else:
                    print("INVALID TYPE")
                # var is now equal to the val
                # message is printed
                shellVAR01 = shellinput01
                print(f"shellVAR01 = '{shellVAR01}'")
            # the above happens here, but for var 02    
            elif shellinput01 == "02":
                shellinput02 = input("$TYPE$//: ")
                # checks val type and sets var to val
                if shellinput02 == "str":
                    shellinput01 = str(input("$VAL$//: "))
                elif shellinput02 == "int":
                    shellinput01 = int(input("$VAL$//:"))
                else:
                    print("INVALID TYPE")
                # var is now val
                # message printed
                shellVAR02 = shellinput01
                print(f"shellVAR02 = '{shellVAR02}'")
                
            else:
                print("INVALID VAR")

        else:
            print("COMMAND NOT RECOGNIZED")
# SHELL COMMANDS

def SHELL_INIT():
    print("SHELL TEST01")
    print("see more details in shell.txt")
    print("SHELL IS NOT COMPLETE")
    print("This is a primitive version for now, will be updated")

def SHELL_PRINT(toPrint):
    print("SHELL:")
    print(f"{toPrint}")

def SHELL_END():
    print("SHELL DEACTIVATED.")
    

# built-in tools
    
def TRYcalc():
    print("TRYcalc v1.0")
    time.sleep(1)
    print("commands can be found in TRY.txt in the BUILT-IN folder")
    while True:
        code2 = 0
        code3 = 0
        output = 0
        code = input("//: ")
        if code == "try":
            print("Be specific.")
            
        elif code == "don't try":
            print("Can't do that, it's my thing.")
            
        elif code == "try add":
            code2 = int(input(">?< + ? //: "))
            code3 = int(input(f"{code2} + >?< //: "))
            output = code2 + code3
            print(f"I tried and I got {output}")
            
        elif code == "try subtract":
            code2 = int(input(">?< - ? //: "))
            code3 = int(input(f"{code2} - >?< //: "))
            output = code2 - code3
            print(f"I tried and I got {output}")
            
        elif code == "try multiply":
            code2 = int(input(">?< * ? //: "))
            code3 = int(input(f"{code2} * >?< //:"))
            output = code2 * code3
            print(f"I tried and I got {output}")
            
        elif code == "try divide":
            code2 = int(input(">?< / ? //: "))
            code3 = int(input(f"{code2} / >?< //: "))
            output = code2 / code3
            print(f"I tried and I got {output}")
            
        elif code == "exit":
            print("Thanks for usage!")
            break

helpcounter = 0
username = os.getlogin()
with open("dir.txt", 'r+') as appdir:
    global filedir
    appdir.write(os.path.abspath(__file__))
    filedir = appdir.read()
    appdir.close()

#init sys
init()
time.sleep(1)
OSmain()
# test func
print("Please wait, testing software.")
START("test")
time.sleep(1)
print("testing all software...")
time.sleep(3)
print("No problems detected.")
END("test")
print("---{}---")
print(f"Hello, {username}.")
print("Is that your name? y/n")
x = input("//: ")
if x == "y":
    print(f"Name set to {username}.")
elif x == "n":
    print("Please enter new username.")
    username = input("//: ")
    print(f"Name set to {username}.")
else:
    print(f"Input not accepted, name set to {username}.")
print("fakeOS active. Enter commands.")

# CORE
print("use command 'help' for help")
while True:
    x = input("//: ")

    if x == "help":
        helpcounter += 1
        if helpcounter >= 10:
            print("---{}---")
            print("You don't need more help. Go ask your teacher or something.")
        elif helpcounter == 5:
            print("---{}---")
            print("COMMAND LIST:")
            print("help: displays this screen")
            print("runfile: runs a specified file from APPS")
            print("run: runs a tool or script built in")
            print("ls: shows all tools or scripts built in")
            print("brackets: prints '[]' to the SHELL")
            print("shell: activates the SHELL terminal")
            print("end: ends fakeOS safely")
            print()
            print("You've asked for help so many times.")
            
        elif helpcounter < 5:        
            print("---{}---")
            print("COMMAND LIST:")
            print("help: displays this screen")
            print("runfile: runs a specified file from APPS")
            print("run: runs a tool or script built in")
            print("ls: shows all tools or scripts built in")
            print("brackets: prints '[]' to the SHELL")
            print("shell: activates the SHELL terminal")
            print("end: ends fakeOS safely")
    
    elif x == "end":
        print("fakeOS ending...")
        print("fakeOS ended successfully")
        exit()
    
    elif x == "brackets":
        SHELL_PRINT("[]")
    
    
    elif x == "ls":
        print("Use the 'run' command to run built in tools and scripts.")
        print("TRYcalc: simple calculator that tries")
        
    elif x == "run":
        running = input("$RUN_BUILT_IN$//: ")
        if running == "TRYcalc":
            print("TRYcalc selected...")
            START("TRYcalc")
            TRYcalc()
            END("TRYcalc")
    
    elif x == "shell":
        START("SHELL TERMINAL")
        SHELL_HANDLER()
        END("SHELL TERMINAL")
    
    elif x == "runfile":
        running = str(input("$RUNFILE$//: "))
        os.chdir(filedir)
        exec(open(running).read())
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print(f"Program {running} seems to have ended.")
        print("Returning to core shell...")
        
    else:
        print("BAD COMMAND")
    
    print("---{}---")
        