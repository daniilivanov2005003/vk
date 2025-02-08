from abc import ABC, abstractmethod

import seleniumwire.webdriver
import time
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import get_user
import os


#class Auth(ABC):
#    def

class Browser:
    def __init__(self):
        load_dotenv()
        self.proxy_username = os.getenv('PROXY_USERNAME')
        self.proxy_password = os.getenv('PROXY_PASSWORD')
        self.proxy_address = os.getenv('PROXY_HOST')
        self.proxy_port = os.getenv('PROXY_PORT')

        self.seleniumwire_options = {
            'proxy': {
                'http': f'http://{self.proxy_username}:{self.proxy_password}@{self.proxy_address}:{self.proxy_port}',
                'https': f'http://{self.proxy_username}:{self.proxy_password}@{self.proxy_address}:{self.proxy_port}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }
        self.options = seleniumwire.webdriver.ChromeOptions()
        self.driver = seleniumwire.webdriver.Chrome(options=self.options, seleniumwire_options=self.seleniumwire_options)
        self.options.add_experimental_option("detach", True)
        self.wait = WebDriverWait(self.driver, 20)

    def auth(self):
        self.driver.get("https://vk.com/")

        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/div[2]/div/button[1]/span')))
        button.click()

        label = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div[1]/div[1]/div/label[2]')))
        label.click()

        user = get_user.get_user(0)

        input_login = self.wait.until(EC.presence_of_element_located((By.XPATH, '//form/div[1]/span/div/div/input')))
        input_login.send_keys(user[0])

        button_login = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//form/button[1]/span')))
        button_login.click()

        input_password = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div/div[1]/div/div/div/div/div/form/div[1]/div[3]/div/div/input')))
        input_password.send_keys(user[1])

        while True:
            try:
                but_pass = self.driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/div/form/div[2]/button/span')
                if but_pass.is_displayed():
                    but_pass.click()
                    break
            except Exception as e:
                print(e)
            time.sleep(1)

        lala = input()

#but_pass = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/div/form/div[2]/button/span')))
#while True:
#    try:
#        but_pass.click()
#        break
#    except Exception as e:
#        print(e)
#    time.sleep(1)


if __name__ == '__main__':
    browser = Browser()
    browser.auth()