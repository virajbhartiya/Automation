from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
from time import sleep


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def closeBrowser(self):
        sleep(3)
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://instagram.com")

        sleep(1)

        usernameEle = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        usernameEle.clear()
        usernameEle.send_keys(self.username)

        passwordEle = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        passwordEle.clear()
        passwordEle.send_keys(self.password)
        passwordEle.send_keys(Keys.RETURN)

        sleep(5)

        notNowEle = driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]')
        notNowEle.click()
        sleep(1)

        # //*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input       usernme
        # //*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input        pwd

    def likePhoto(self, hashtag):

        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        sleep(2)

        for i in range(1, 2):
            driver.execute_script(
                "window.scrollTo(0 , document.body.scrollHeight);")
            sleep(2)

        href = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')

        pichrefs = [elem.get_attribute('href') for elem in href]
        pichrefs = [href for href in pichrefs if hashtag in href]

        print(hashtag + 'photos : ' + str(len(pichrefs)))

        for pichref in range(2):
            driver.get(pichref)
            #driver.execute_script("window.scrollTo(0 , document.body.scrollHeight);")
            try:
                driver.find_element_by_link_text("Like").click()
                sleep(18)
            except Exception as e:
                sleep(2)

    def followPeople(self, people):
        driver = self.driver
        driver.get('https://www.instagram.com/'+people+'/')
        sleep(2)

        btn = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/button').click()

    def followPublic(self, people):
        driver = self.driver
        driver.get('https://www.instagram.com/'+people+'/')
        sleep(2)

        btn = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()

    def followTag(self, name):

        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+name+'/')
        sleep(2)

        btn = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/header/div[2]/div[1]/button').click()

    def like(self, name):
        driver = self.driver
        driver.get('https://www.instagram.com/'+name+'/')

        fphoto = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]')
        fphoto.click()

        heart = driver.find_element_by_link_text("Like")

        nxt = driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div/div/a')

        sleep(2)
        heart.click()
        sleep(2)
        nxt.click()
        sleep(2)


def main():

    username = input("Enter username : ")
    password = getpass("Enter Password : ")

    #username = 'bhartiya.viraj'
    #password = 'Vlbhartiya2205'

    instagram = Bot(username, password)
    instagram.login()

    # instagram.followPeople('smitabhartiya')
    # instagram.followPeople('dhruv.bhartiya')
    # instagram.followPeople('soumya_goyal_17')
    # instagram.followPeople('goyal_chaitanya_')

    instagram.followPublic('taylorswift')
    # instagram.followPublic('selenagomez')

    # instagram.followTag('taylorswift')

    # instagram.likePhoto('TaylorSwift')

    #instagram.followTag('taylorswift')

    instagram.closeBrowser()


main()
