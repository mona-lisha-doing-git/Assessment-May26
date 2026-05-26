from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # login_link = (By.LINK_TEXT, 'Log in/Sign up')
    login_link = (By.XPATH, "//button[text()='Log in/Sign up']")
    email = (By.ID, 'Email')
    password = (By.ID, 'Password')
    login_button = (By.XPATH, "//input[@value='Log in']")
    close_popup_button = (By.XPATH, "//button[@id='closeButton']")

    def __init__(self, driver):
        super().__init__(driver)

    # def close_popup(self):
    #     try:
    #         self.wait_and_click(self.close_popup_button, 15)
    #     except TimeoutException:
    #         pass
    def close_popup(self):
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        except:
            pass

    def click_login(self):
        self.click(self.login_link)

    def enter_email(self, email):
        self.enter_text(self.email, email)

    def enter_password(self, password):
        self.enter_text(self.password, password)

    def click_login_button(self):
        self.click(self.login_button)
