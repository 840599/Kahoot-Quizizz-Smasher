from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading


class KahootBot:
    def __init__(self, pin, name):
        print("\nConnecting to game at " + pin + " as " + name)

        self.driver = webdriver.Chrome(executable_path='webDrivers\chromedriver.exe')
        self.driver.get('http://www.kahoot.it')

        self.driver.implicitly_wait(2)

        self.pin = pin

        # now find the key input box and pass it the key
        self.driver.find_element_by_id('inputSession').send_keys(pin)
        # now find the submit button and click it
        self.driver.find_element_by_xpath("//button[@type='submit']").click()

        # now wait for javascript
        self.driver.implicitly_wait(2)

        # now find the name input box and pass it the name
        self.nameIn = self.driver.find_element_by_id("username")
        self.nameIn.send_keys(name)
        # now hit enter to submit the username
        self.nameIn.send_keys(Keys.RETURN)

        while True:
            pass


def createBot(pin, name):
    bot = KahootBot(pin, name)


choice = int(input("Welcome to the Kahoot/Quizizz smasher.\nTo smash a Kahoot, press 1. To smash a Quizizz, press 2.\n"
                   "Chrome is required\nWARNING: Smashing Kahoots and Quizizzs takes a lot of chrome windows! Try to"
                   " free up as much ram as possible before smashing something"))

if choice == 1:
    pin = str(input("You have chosen to smash a Kahoot.\nInput the pin: "))
    botNum = int(input("How many bots? "))
    baseName = str(input("What should they be named? "))

    for x in range(botNum):
        name = str(baseName + str(x))
        botThread = threading.Thread(target=createBot, args=(pin, name))
        botThread.start()
