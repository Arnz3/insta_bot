from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import sys

class InstaBot:

    def __init__(self, PATH, user, pasw, hashtag, freq=5, ber=3, pause=1):
        self.PATH = PATH
        self.user = user
        self.pasw = pasw
        self.hashtag = hashtag
        self.freq = freq
        self.ber = ber
        self.pause = pause
       

    def start(self):
        global driver
        driver = webdriver.Chrome(self.PATH)

        global run
        global comments
        comments = ["Wowwww, great job!!", "emmazing work!", "A real work of art!", "Awesome bro!", "oofff", "thats fire!!!"]

        def login():
            
            coockies = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@role="presentation"]//*[text()="Accepteren"]')))
            coockies.click()

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

            user_input = driver.find_element_by_name("username")
            user_input.send_keys(self.user)
            pasw_input = driver.find_element_by_name("password")
            pasw_input.send_keys(self.pasw)
            login_button = driver.find_element_by_xpath('//*[@id="loginForm"]//*[text()="Aanmelden"]')
            login_button.click()
            
            not_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@role="main"]//*[text()="Niet nu"]')))
            not_now.click() # no keep signed in 

            no_noti = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@role="presentation"]//*[text()="Niet nu"]')))
            no_noti.click() # no notifications


        def like(times):
            pictures = driver.find_elements_by_class_name("eLAPa")
            pictures[9].click()
            for i in range(times):
                like = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//article[@role="presentation"]//*[@aria-label="Vind ik leuk"]')))
                like.click() # like                                                         
                if random.randint(0, 5) == 2: # comment 1/6
                    comment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//article[@role="presentation"]//*[@aria-label="Een opmerking toevoegen..."]')))
                    comment.click()
                    comment2 = driver.find_element_by_xpath('//article[@role="presentation"]//*[@aria-label="Een opmerking toevoegen..."]')
                    comment2.send_keys(random.choice(comments)) 
                    comment2.send_keys(Keys.ENTER)
                right_arrow = driver.find_element_by_xpath('//div[@role="dialog"]//*[text()="Volgende"]') # next picture
                right_arrow.click()
            exit = driver.find_element_by_xpath('//div[@role="dialog"]//*[@aria-label="Sluiten"]')
            exit.click()

        driver.get("https://www.instagram.com/")
        driver.maximize_window()
        login()
        driver.get(f"https://www.instagram.com/explore/tags/{self.hashtag}/")
        run = True
        while run:
            for i in range(self.freq + 1):
                like(self.ber)
                time.sleep(self.ber)
                driver.refresh()
            for i in range(self.pause):
                time.sleep(60)

    def stop(self):
        global run
        driver.quit()
        run = False
