from selenium.webdriver.support.select import Select


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

def delete_project_by_index(self,index):
    wd=self.wd
    wd.find_elements_by_css_selector("table.width100 > tr > td > a")[index].click()
    wd.find_element_by_xpath("//input[@value='Delete Project']").click()
    wd.find_element_by_xpath("//input[@value='Delete Project']").click()

def delete_first_project(self):
    wd=self.wd
    self.delete_project_by_index(0)

# def select_project(self, name):
#     wd=self.wd
#     wd.find_element_by_link_text(name).click()
