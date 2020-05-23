from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import creds
import time

path = ('../driver/chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("test-type")
chrome_options.add_argument("enable-strict-powerful-feature-restrictions")
chrome_options.add_argument("--disable-geolocation")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("disable-notifications")

driver = webdriver.Chrome(executable_path=path, options=chrome_options)



driver.get('https://www.facebook.com')

element = driver.find_element_by_id("email")
element.send_keys(creds.EMAIL)

element = driver.find_element_by_id("pass")
element.send_keys(creds.PASSWORD)

element.send_keys(Keys.RETURN)

time.sleep(2)


post_element = driver.find_element_by_xpath('//*[@name="xhpc_message"]')

time.sleep(3)

post_element.send_keys('Hello everyone, this status is posted by a bot')

time.sleep(1)

buttons = driver.find_elements_by_tag_name("button")
time.sleep(5)
for button in buttons:
    if button.text == 'Post':
        button.click()


