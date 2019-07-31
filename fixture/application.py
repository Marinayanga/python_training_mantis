from idlelib import browser

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from fixture.session import SessionHelper
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

    # def is_valid(self):
    #     try:
    #         self.wd.current_url
    #         return True
    #     except:
    #         return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20/my_view_page.php")

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

    def delete_project_by_index(self, index):
        wd = self.wd
        wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]")[index].click()
        #wd.find_elements_by_css_selector("tr.row-1 > td > a")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def delete_first_project(self):
        wd = self.wd
        self.delete_project_by_index(1)

    list=[]

    def get_project_list(self):
        self.list=[]
        wd=self.wd
        for element in wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]"):
            name = element.text
            cells = element.find_elements_by_tag_name("td")
            status = cells[1].text
            view_state = cells[3]
            description = cells[4]
            #id = element.find_element_by_name("selected[]").get_attribute("value")
            self.list.append(Project(name=name, status=status, view_state=view_state,description=description))
        return list

    #
    # def logout(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
