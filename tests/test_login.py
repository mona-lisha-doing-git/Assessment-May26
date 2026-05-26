from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger
from time import sleep


def test_valid_login(setup_and_teardown):
    driver = setup_and_teardown
    lp = LoginPage(driver)

    config = ConfigReader.read_config()
    env = config['qa']

    BASE_URL = env['base_url']
    EMAIL = env['email']
    PASSWORD = env['password']

    driver.get(BASE_URL)
    get_logger().info("Trying to Log In")

    sleep(5)
    lp.close_popup()

    lp.click_login()
    sleep(5)

    lp.switch_to_iframe((By.XPATH, "//iframe[contains(@src,'accounts.google.com/gsi/button')]"))
    lp.find((By.TAG_NAME, "div")).click()
    sleep(3)

    # switch to new google popup window
    main_window = driver.current_window_handle
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    for window in driver.window_handles:
        if window != main_window:
            driver.switch_to.window(window)
            break

    # enter email
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "identifierId")))
    driver.find_element(By.ID, "identifierId").send_keys(EMAIL)
    driver.find_element(By.ID, "identifierNext").click()
    sleep(3)

    # enter password
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Passwd")))
    driver.find_element(By.NAME, "Passwd").send_keys(PASSWORD)
    driver.find_element(By.ID, "passwordNext").click()
    sleep(5)

    # switch back to main window
    driver.switch_to.window(main_window)
    sleep(10)
    get_logger().info("Login Successful")