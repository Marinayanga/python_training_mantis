from idlelib import browser

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from fixture.james import JamesHelper
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from model.project import Project
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper

class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup =SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20/my_view_page.php")

    def destroy(self):
        self.wd.quit()
