from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

class InstaBot:

    def __init__(self, PATH, user, pasw, hashtag, freq=5, ber=3, pause=1):
        self.PATH = PATH
        self.user = user
        self.pasw = pasw
        self.hashtag = hashtag
        self.freq = freq
        self.ber = ber
        self.pause = pause

        global driver
        driver = webdriver.Chrome(self.PATH)
       

    def start(self):
        global run
        global comments
        comments = ["Wowwww, great job!!", "emmazing work!", "A real work of art!", "Awesome bro!", "oofff"]

        def login():

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

            user_input = driver.find_element_by_name("username")
            user_input.send_keys(self.user)
            pasw_input = driver.find_element_by_name("password")
            pasw_input.send_keys(self.pasw)
            login_button = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button")
            login_button.click()

            not_now = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button")))
            not_now.click() # no keep signed in 

            no_noti = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
            no_noti.click() # no notifications


        def like(times):
            pictures = driver.find_elements_by_class_name("eLAPa")
            pictures[9].click()
            for i in range(times):
                like = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")))
                like.click() # like
                comment = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
                comment.click()
                comment2 = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
                comment2.send_keys(random.choice(comments)) # comment
                comment2.send_keys(Keys.ENTER)
                right_arrow = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]") # next picture
                right_arrow.click()
            exit = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')
            exit.click()

        driver.get("https://www.instagram.com/")
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


bot = InstaBot("C:\Program Files (x86)\chromedriver.exe", "a.j__art", "AJart.Insta.TikTok", "doodle", 1, 3, 60)
bot.start()