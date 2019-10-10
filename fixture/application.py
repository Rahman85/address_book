#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.chrome.webdriver import WebDriver
#from selenium.webdriver.safari.webdriver import WebDriver
from selenium import webdriver
from fixture.session_helper import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper



class Application:

    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd= webdriver.Firefox()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" + browser)
        #self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False



    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy(self):
        self.wd.quit()
