from idlelib import browser

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from model.project import Project

class Application:
    def __init__(self,base_url, browser):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.project = ProjectHelper(self)

    # def is_valid(self):
    #     try:
    #         self.wd.current_url
    #         return True
    #     except:
    #         return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20/my_view_page.php")

    def destroy(self):
        self.wd.quit()
