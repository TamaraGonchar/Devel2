from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from selenium import webdriver

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
           self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
           self.wd = webdriver.Chrome("C:\Windows\SysWOW64\chromedriver.exe")
        elif browser == "ie":
           self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
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


