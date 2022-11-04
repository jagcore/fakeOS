fakeOS
v1.0

by Michael 'jagcore'

!!!PLEASE READ THIS ENTIRE PAGE!!!
!!!   FULLSCREEN THIS WINDOW   !!!

ABOUT:
fakeOS is a simple script that can run other scripts in an easy way.
It also has a SHELL terminal and some built in tools.
There is a simple runfile command that can run other files,
and a way to manually download small programs or tools for ease of access.

PREP TO RUN:
fakeOS can run .py scripts in its APPS folder. However, this does not function immediately.
First, run the code. After it takes you to the console, stop the code.
Now, edit the code. Go to line 183, and delete it. This line of code sets your directory, and we don't need it anymore.
Finally, go to dir.txt, which should be in CORE AND STORAGE. Edit it, and you'll see a directory.
It should look something like this:
C:\Users\BLAUVMC\Desktop\fakeOS\CORE AND STORAGE\fakeOS.py
You can change the last part to look like this:
C:\Users\BLAUVMC\Desktop\fakeOS\CORE AND STORAGE\APPS  <- This part changes.


RUNNING OTHER SCRIPTS:
fakeOS has a command called 'runfile'.
When in the main screen, also called the core shell,
you can type 'runfile' and the shell will display a prompt.
You will be asked to enter the name of the file, which must be in python version 3.10.
It may take some time for the program to fully run, please be patient.

example:
//: runfile
$RUNFILE$//: example.py
---{example.py}---
Hello World!
...
...
...
Program 'example.py' seems to have ended.
Returning to core shell...
---{}---


CREATING SCRIPTS:
Any script can be run by 'runfile', but only those written in python.
However, if you want to make an application to be shared, there are several steps.

1. Create a folder named after your app.

2. Put the .py file of your app inside.

3. Make an about .txt and put contacts (optional) , how to use your app, version, who made it, etc.



HOW TO USE CORE SHELL:
The main way to interact with fakeOS is the core shell, a simple terminal.
If you ever need help using the terminal, you can use the 'help' command to display all commands.
However, if you don't know where to start, you can simply use this guide:

First things first, when you boot up fakeOS, after the boot up ends and runs, you should see this:

//:

This is the terminal input.
You type commands here. I'll use the 'help' command.

//: help
(press enter after typing!)
---{}---
COMMAND LIST:
help: displays this screen
runfile: runs a specified file from APPS
run: runs a tool or script built in
ls: shows all tools or scripts built in
brackets: prints '[]' to the SHELL
shell: activates the SHELL terminal
end: ends fakeOS safely
---{}---
//:

That should be all the help you need to get started. If you need more..

Email me on outlook with:

BLAUVMC@student.okaloosaschools.com

for help, bug reporting, and developer advice.



THANK YOU FOR READING THE README.
THANK YOU ALSO FOR USING fakeOS.