from sys import exit
import re, sys

def name():
    print("You hear a whisper...")
    print("What is your name?")
    user = input("> ")
    start(user)
    
def approve(user):
    print(f"Count Doom does not approve...{user}.")
    roomE(user)
    
def start(user):
    print("You are standing in a forest... the rain bellows down on you and thunder rolls.")
    print("You see flashes of lightning everywhere.. and you forgot how you got to be here...")
    print("It doesn't matter you tell yourself, and you wonder what to do next...")
    print(f"Watch your feet {user}, AS YOU ARE ABOUT TO FALL!")
    print("You feel yourself fall into a sliding hole, and you are filled with fear as you don't know when it ends.")
    print("You find yourself with sore knees as you fall into the ground.")
    print(f"You hear someone say {user}.... menacingly")
    roomE(user)
    
def roomE(user):
    print("The room has completely encapsuled you in darkness.. until you see a small flame start in the centre of the room.")
    print("There is nothing of note inside the room except the bare moss covered stone walls...")
    print("And 4 doors made of iron and wood. You are facing north. Which room do you go into?")
    
    choice = input("> ")
    
    if re.search("[Nn][oO][Rr]", choice):
        roomB(user)
    elif re.search("[Ww][eE][sS]", choice):
        roomD(user)
    elif re.search("[Ee][aA][Ss]", choice):
        roomF(user)
    elif re.search("[Ss][oO][Uu]", choice):
        roomH(user)
    else: 
        print("What are you doing?")
        
def roomB(user):
    print("As you enter the room, there is a dim blue light..")
    print("It makes the walls look wavy, and everything appears to be made of water.")
    print("There are three doors, but something smells odd.")
    print("Where do you go?")
    room_2 = False
    
    while True:
        choice = input("> ")
    
        if re.search("[Nn][oO][Rr]", choice) and not room_2:
            print("Count Doom laughs at you menacingly.")
            print("Want to feel crazy?")
            roomE(user)
        elif choice == "Slap you with a trout" and not room_2:
            print("You hear a rumbling in the room.")
            print("You hear a menacing whisper right inside your head.")
            print("'I approve....,', Count Doom says, 'You are doing well....'")
            room_2 = True
        elif re.search("[Nn][oO][Rr]", choice) and room_2:
            print("There might be a way out of here!")
            room_2(user)
        
        
def roomC(user):
    print("Hmmm")
    choice = input("> ")
    
    if re.search("[Ww][eE][sS]", choice):
        roomB(user)
    elif re.search("[Ss][oO][Uu]", choice):
        roomF(user)
    else: 
        print("What are you doing?")
    
  
def roomA(user):
    print("hmmm2")
    room_1: False
    
    while True:
        choice = input("> ")
    
        if re.search("[Ww][eE][sS]", choice) and not room_2:
            print("Count Doom laughs at you menacingly.")
            print("Want to feel crazy?")
            roomE(user)
        elif choice == "Slap you with a Salmon" and not room_2:
            print("You hear a rumbling in the room.")
            print("You hear a menacing whisper right inside your head.")
            print("'I approve....,', Count Doom says, 'You are doing well....'")
            room_1 = True
        elif re.search("[Ww][eE][sS]", choice) and room_2:
            print("There might be a way out of here!")
            room_1(user)
        elif re.search("[Ee][aA][Ss]", choice):
            roomB(user)
        elif re.search("[Nn][oO][Rr]", choice):
            roomD(user)
        else: 
            print("What are you doing?")
            
def roomG(user):
    print("hmmm2")
    room_3: False
    
    while True:
        choice = input("> ")
    
        if re.search("[Ss][oO][Uu]", choice) and not room_3:
            print("Count Doom laughs at you menacingly.")
            print(f"Want to feel crazy, {user}?")
            roomE(user)
        elif choice == "Slap you with a Salmon" and not room_3:
            print("You hear a rumbling in the room.")
            print("You hear a menacing whisper right inside your head.")
            print("'I approve....,', Count Doom says, 'You are doing well....'")
            room_1 = True
        elif re.search("[Ss][oO][Uu]", choice) and room_3:
            print("There might be a way out of here!")
            room_3(user)
        elif re.search("[Ee][aA][Ss]", choice):
            roomH(user)
        elif re.search("[Ss][oO][Uu]", choice):
            roomD(user)
        else: 
            print("What are you doing?")
            
def roomH(user):
    print("Hmmm")
    choice = input("> ")
    
    if re.search("[Ww][eE][sS]", choice):
        roomG(user)
    elif re.search("[Ee][aA][Ss]", choice):
        roomI(user)
    elif re.search("[Nn][oO][Rr]", choice):
        roomE(user)
    else: 
        print("What are you doing?")
        
def roomI(user):
    print("Hmmm")
    choice = input("> ")
    
    if re.search("[Ww][eE][sS]", choice):
        roomH(user)
    elif re.search("[Nn][oO][Rr]", choice):
        roomF(user)
    else: 
        print("What are you doing?")
        
def roomF(user):
    print("Hmmm")
    choice = input("> ")
    
    if re.search("[Ww][eE][sS]", choice):
        roomE(user)
    elif re.search("[Ee][aA][Ss]", choice):
        roomI(user)
    elif re.search("[Ss][oO][Uu]", choice):
        roomI(user)
    else: 
        print("What are you doing?")
        
def roomD(user):
    print("Hmmm")
    choice = input("> ")
    
    if re.search("[Nn][oO][Rr]", choice):
        roomA(user)
    elif re.search("[Ee][aA][Ss]", choice):
        roomE(user)
    elif re.search("[Ss][oO][Uu]", choice):
        roomG(user)
    else: 
        print("What are you doing?")



def room_1(user):
    print("Congratulations!")
    
def room_2(user):
    print("Congratulations!")
    
def room_3(user):
    print("Congratulations!")
  
name()
        
    
        
    
    
