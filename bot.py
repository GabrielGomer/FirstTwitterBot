from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TwitterBot:
    # Launch webbrowser and set executable path for geckodriver
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # Download geckodriver and place in folder then webdriver.Firefox(executable_path= 'filepath/geckodriver.exe')
        self.bot = webdriver.Firefox(executable_path= 'C:/Users/Gabe Gomer/PycharmProjects/geckodriver.exe')

    # login to twitter
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        # places email in email-input
        email = bot.find_element_by_class_name('email-input')
        # places password in session[password]
        password = bot.find_element_by_name('session[password]')
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        # Delay to pass recaptcha
        time.sleep(3)

    def heart_tweet(self, hashtag):
        bot = self.bot
        # Takes any hashtag given below
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=typed_query')
        time.sleep(3)
        # Scrolls through full page then likes a tweet repeats 5 times
        for i in range(1, 5):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = bot.find_elements_by_class_name('tweet')
            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]
            for link in links:
                bot.get('https://twitter.com/' + link)
                try:
                    # Clicks the Heart Button
                    bot.find_element_by_class_name('HeartAnimation').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(60)


# input your twitter 'email/username', 'password'
gg = TwitterBot('', '')
gg.login()
# Calls out gaming hashtag
gg.like_tweet('gaming')
