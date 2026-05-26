from selenium.webdriver.common.by import By

from config.env import ConfigReader
from time import sleep

def test_search(setup_and_teardown):

    driver = setup_and_teardown
    config = ConfigReader.read_config()
    env = config['qa']

    BASE_URL = env['base_url']

    driver.get(BASE_URL)

    from selenium.webdriver.common.action_chains import ActionChains
    sleep(5)
    ActionChains(driver).move_by_offset(0, 0).click().perform()
    driver.find_element(By.XPATH, "(//span[@class='absolute top-20'])[1]").click()
    sleep(3)
    driver.find_element(By.XPATH, "(//div[@class ='flex flex-grow items-center']//input)[1]").send_keys("Ranchi")
    sleep(3)
    driver.find_element(By.XPATH, "//p[.='Birsa Munda Airport']").click()

    sleep(3)
    driver.find_element(By.XPATH, "(//div[@class ='flex flex-grow items-center']//input)[2]").send_keys("Delhi")
    sleep(3)
    driver.find_element(By.XPATH, "((//div[@class='overflow-y-scroll absolute top-[61px] bg-white w-[375px] min-h-[150px] max-h-[450px] shadow-500 z-20 rounded-20 !animate-none no-scrollbar block Autocompleter_animate__zqRDe'])//div)[4]").click()
    sleep(3)
    # ActionChains(driver).move_by_offset(0, 0).click().perform()

    driver.find_element(By.XPATH, "//button[.='Search']").click()

    sleep(5)