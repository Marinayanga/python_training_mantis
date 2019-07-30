from idlelib import browser

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from fixture.session import SessionHelper


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

        self.wd = WebDriver
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.base_url = base_url

    # def is_valid(self):
    #     try:
    #         self.wd.current_url
    #         return True
    #     except:
    #         return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20")

    def login(self, username, password):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20/login_page.php")
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def return_to_ptoject_page(self):
        wd = self.wd
        # Перейти на страницу Manage
        wd.find_element_by_link_text("Manage").click()
        # Перейти на страницу проектов
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_name(self, project):
        wd = self.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def click_create_project(self):
        wd = self.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
