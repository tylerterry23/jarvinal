import random
import termcolor 
from termcolor import colored, cprint
from pyfiglet import Figlet
import os
from py_imessage import imessage
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
import itertools
import threading
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

print_green = lambda x: cprint(x, 'green')
print_red = lambda x: cprint(x, 'red')

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

def intro():
    # Intro TODO: check if pip installed if not then install windows / mac
    i=0
    print("\n")
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if i == 70:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    

    print_green("\rLoad Successful\n")
    time.sleep(1)
    print("running script...")
    time.sleep(1)

    

    # TODO: make red
    # os.system('color')
    # print(termcolor.colored("I want to help", "red"))
    nums = [1,2,3,4,5,6,7,8,9,0]
    tm = 0
    while tm < 50:
        print(random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),random.randrange(1,5)* " ",
        random.choice(nums),)

        tm += 1

        time.sleep(0.1)



    f = Figlet(font="standard")
    print("----------------------------------------------------------------")
    print(f.renderText('WELCOME MR. TERRY'))
    print("----------------------------------------------------------------")
    time.sleep(2)
    
def internet():

    print("\n\n ----- INTERNET/WEB ----- \n")

    browser = input("\nSelect Browser (f)irefox, (s)afari, (c)hrome: ")
    if browser == 'f':
        browser = 'firefox'
    if browser == 's':
        browser = 'safari'
    if browser == 'c':
        browser = 'Google Chrome'
    if browser == 'home':
        main()
            


    path = f"/Applications/{browser}.app"
    os.system(f"open {path}")

def characterManipulation():

    print("\n\n ----- CHARACTER MANIPULATION ----- \n")

    quickResponses = {
        1: "---------------------------------------------------------------------------------------",

        2: "             ------------------------------------------------------\n \
            |   COMPUTER                                         |\n \
            ------------------------------------------------------",

        3: "hey"
        }

    for i in range(1, len(quickResponses)+1):
        print(quickResponses[i])
        
    character = input('Enter character(s) or Quick Response: ')
    if character == 'home':
        main()

    try:
        if int(character) in range(1,4):
            print(quickResponses[int(character)])  
            main()

    except:
        repeat = input('repeat how many times?: ')
        if repeat == 'home':
            main()
        
    

        product = []
        i = 0

        while i != int(repeat):
            product.append(character)
            i+=1

        print(f"\nCharacter(s): '{character}' // Repeated: {repeat}")
        [print(i, end='') for i in product] 
        print("\n")
        main()

def phoneConnect():

    # phone = "12484977128"
    # guid = imessage.send(phone, "Hello World!")
    # time.sleep(5)
    # esp = imessage.status(guid)

    print("\n\n ----- PHONE CONNECT ----- \n")

    quickResponses = {1:'heyy', 2:'my bad i was sleep', 3:'watchu up to'}

    [print(f"{i}) {quickResponses[i]}") for i in range(1, len(quickResponses)+1)]
    message = input("Quick Response or Message: ")

    if message == 'home':
        main()


    os.system("open -a Messages")

    time.sleep(1) 
    keyboard = Controller()

    # New Message (cmd + n)
    # press cmd / n
    keyboard.press(Key.cmd.value)
    keyboard.press('n')

    # release
    keyboard.release('n')
    keyboard.release(Key.cmd.value)

    time.sleep(1) 
    
    keyboard.type("2484977128")
    keyboard.press(Key.enter)
    time.sleep(1)


    try:
        if int(message) in range(1, 10):
            send = quickResponses[int(message)]
            keyboard.type(send)
            time.sleep(2)

    except:
        keyboard.type(f"{message}")
        time.sleep(2)

    
    
    
    # re open terminal
    os.system("open -a Terminal")

    # close messages
    os.system("pkill -x Messages")

def definition():

    print("\n\n ----- DEFINITIONS ----- \n")

    def webstersDictionary():
        term = input("\nenter term: ")

        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)
        driver.get("https://www.merriam-webster.com/")
        # assert "Python" in driver.title
        
        
        # locate Search bar > Clear > Enter Term > Click Return (search)
        elem = driver.find_element(By.NAME, "s")
        elem.clear()
        elem.send_keys(term)
        elem.send_keys(Keys.RETURN)

        # Formatting
        print("\n")

        # give time for page to load before pulling text
        time.sleep(2)
    
        try:
            print(driver.find_element(By.CLASS_NAME, "vg").text)
            print("\n")
        except:
            print("error")


        driver.close()
        driver.quit()

        # TODO: database implementation
        add = input("Add word to personal vocabulary database (y/n)?: ")

    def urbanDictionary(): 

        term = input("\nenter term: ")

        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)
        driver.get("https://www.urbandictionary.com/")
        # assert "Python" in driver.title
        
        
        # locate Search bar > Clear > Enter Term > Click Return (search)
        elem = driver.find_element(By.NAME, "term")
        elem.clear()
        elem.send_keys(term)
        elem.send_keys(Keys.RETURN)

        # Formatting
        print("\n")

        # give time for page to load before pulling text
        time.sleep(2)
    
        try:
            print(driver.find_element(By.CLASS_NAME, "break-words").text)
            print("\n")
        except:
            print("error")


        driver.close()
        driver.quit()

        # TODO: database implementation
        add = input("Add word to personal vocabulary database (y/n)?: ")
    
    
    print("SELECT DICTIONARY\n")
    print("1. Merriam-Webster Dictionary")
    print("2. Urban Dictionary\n")
    dic = input("Enter Choice: ")

    if dic == "1":
        webstersDictionary()
    if dic == "2":
        urbanDictionary()

def admin():
    print("\nWelcome, Mr. Terry")   
    password = input("Enter Password: ")

    if password == "terrytyler23":
        print_green("\nAdmin Mode Granted\n")
    else:
        print_red("\nIncorrect! Returning to Main...\n")
        time.sleep(1)
        main()

    # TODO: database implementation
    learn = ['Quick Sort', 'Merge Sort', 'Insertion Sort', 'Selection Sort',
            'Bubble Sort', 'Shell Sort']

    print(random.choice(learn))




def main():

    # intro()


    # Nav Menu
    # TODO: lifting database, separate app?
    print("\nNAVIGATION MENU\n")

    # Open Firefox, safari, chrome(not working)
    # TODO: Fix chrome
    print("1. Web Interaction")

    # TODO: quick actions like txt file box
    print("2. Character Manipulation")

    # TODO: connect contacts in order to use name as number 
    print("3. Send iMessage")

    # search urban or websters for definition
    print("4. Search Definition")


    print("5. Quit")

    


    # Nav Option Selection: 
    option = input("\nSelect Option (1-5): ")

    if option == '1':
        internet()

    if option == '2':
        characterManipulation()

    if option == '3':
        phoneConnect()
        
    if option == '4':
        definition()

    if option == '5':
        exit()

    if option == "//":
        admin()
        

        





    




    



main()