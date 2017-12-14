class projecthelper:


    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@href='/mantisbt-1.2.20/manage_overview_page.php']").click()
        wd.find_elements_by_xpath("//*[contains(text() , 'Manage Projects')]")[-1].click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        for element in wd.find_element_by_xpath