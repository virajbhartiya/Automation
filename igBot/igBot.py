from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


class InstagramBot:
    def __init__(self, username, password):
        """
        Initialises an instance of the class


        Args :
            username:str: Instagram useranme
            password:str: Instagram password

        Attributes:
            driver:selenium.webdriver.chrome : the web browser
        """

        self.username = username
        self.password = password

        self.base_url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.login()

    def login(self):
        self.driver.get(self.base_url)
        sleep(2)

        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
        sleep(3)

    def navUser(self, user):
        sleep(3)
        self.driver.get('{}{}'.format(self.base_url, user))

    def follow_user(self, user):
        self.navUser(user)

        follow_btn = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/a/button')
        follow_btn.click()

    def like_latest_posts(self, user, n_posts, like=True):
        """
        Likes a number of a users latest posts, specified by n_posts.
        Args:
            user:str: User whose posts to like or unlike
            n_posts:int: Number of most recent posts to like or unlike
            like:bool: If True, likes recent posts, else if False, unlikes recent posts
        TODO: Currently maxes out around 15.
        """

        action = 'Like' if like else 'Unlike'

        self.navUser(user)

        imgs = []
        imgs = self.driver.find_elements_by_class_name('_9AhH0')

        for img in imgs[:n_posts]:
            img.click()
            sleep(1)
            try:
                self.driver.find_element_by_xpath(
                    "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
            except Exception as e:
                print(e)

            #self.comment_post('beep boop testing bot')
            self.driver.find_elements_by_class_name('ckWGn')[0].click()
# /html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button


if __name__ == '__main__':

    ig_bot = InstagramBot('bhartiya.viraj', 'Vlbhartiya2205')
    # ig_bot.navUser('bhartiya.viraj')
    # ig_bot.follow_user('taylorswift')
    # ig_bot.login('bhartiya.viraj','Vlbh')
    ig_bot.like_latest_posts('tomholland2013', 2, like=True)
