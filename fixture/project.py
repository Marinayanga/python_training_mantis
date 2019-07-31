from selenium.webdriver.support.select import Select
from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        wd = self.app.wd
        self.app.open_home_page()
        self.return_to_ptoject_page()
        self.click_create_project()
        self.fill_project_name(project)

    def return_to_ptoject_page(self):
        wd = self.app.wd
        # Перейти на страницу Manage
        wd.find_element_by_link_text("Manage").click()
        # Перейти на страницу проектов
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_name(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def click_create_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def delete_project_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]")[index].click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def delete_first_project(self):
        wd = self.app.wd
        self.delete_project_by_index(0)

    list=[]

    def get_project_list(self):
        self.list=[]
        wd=self.app.wd
        for element in wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]/../.."):
            name = element.text
            cells = element.find_elements_by_tag_name("td")
            status = cells[1].text
            view_state = cells[3]
            description = cells[4]
            #id = element.find_element_by_name("selected[]").get_attribute("value")
            self.list.append(Project(name=name, status=status, view_state=view_state,description=description))
        return self.list

    def return_to_ptoject_page(self):
        wd = self.app.wd
        # Перейти на страницу Manage
        wd.find_element_by_link_text("Manage").click()
        # Перейти на страницу проектов
        wd.find_element_by_link_text("Manage Projects").click()


    def fill_project_name(self, project):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

# def delete_project_by_index(self,index):
#     wd=self.wd
#     wd.find_elements_by_css_selector("table.width100 > tr > td > a")[index].click()
#     wd.find_element_by_xpath("//input[@value='Delete Project']").click()
#     wd.find_element_by_xpath("//input[@value='Delete Project']").click()
#
# def delete_first_project(self):
#     wd=self.wd
#     self.delete_project_by_index(0)

    def select_first_project(self):
        wd=self.wd
        wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=')]").click()
