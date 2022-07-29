import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Resgistration():
    def register_account(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        driver.maximize_window()

        firstname = driver.find_element(By.ID,"input-firstname")
        firstname.send_keys("Tasmima")
        time.sleep(1)

        lastname = driver.find_element(By.ID, "input-lastname")
        lastname.send_keys("Akter")
        time.sleep(1)

        email = driver.find_element(By.ID, "input-email")
        email.send_keys("tas.rima99@gmail.com")
        time.sleep(1)

        password = driver.find_element(By.ID, "input-password")
        password.send_keys("ta12340@")
        time.sleep(1)
#radio button--newshelter
        driver.find_element(By.NAME,"newsletter").click()
        time.sleep(3)
        subscribe = driver.find_element(By.NAME,"newsletter").is_selected()
        print(subscribe)
#checkbox-- agreement policy
        driver.find_element(By.NAME, "agree").click()
        time.sleep(3)
        agree = driver.find_element(By.NAME, "agree").is_selected()
        print(agree)
#continue
        register_panel = driver.find_element(By.CSS_SELECTOR,"#form-register > div > div > button")
        register_panel.click()

        time.sleep(10)
        driver.close()

obj_register = Resgistration()
obj_register.register_account()














