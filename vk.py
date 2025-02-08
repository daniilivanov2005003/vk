import selenium.webdriver.common.by
import seleniumwire.webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import get_user


proxy_username = "modeler_NQo1GM"
proxy_password = "tiABEsHseXyV"
proxy_address = "86.104.75.67"
proxy_port = "13522"


seleniumwire_options = {
    'proxy': {
        'http': f'http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}',
        'https': f'http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

options = seleniumwire.webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = seleniumwire.webdriver.Chrome(options=options, seleniumwire_options=seleniumwire_options)
driver.get("https://vk.com/")

wait = WebDriverWait(driver, 10)

button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div/button[1]/span')))
button.click()

label = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div[1]/div[1]/div/label[2]')))
label.click()

user = get_user.get_user(0)
print(user[0])

input_login = wait.until(EC.presence_of_element_located((By.XPATH, '//form/div[1]/span/div/div/input')))
input_login.send_keys(user[0])

button_login = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/button[1]/span')))
button_login.click()


val = '//*[@id="root"]/div/div/div/div/div[1]/div/div/div/div/div/form/div[1]/div[3]/div/div/input'

input_password = wait.until(EC.presence_of_element_located((By.XPATH, val)))
input_password.send_keys(user[1])

button_pass = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/div/form/div[2]/button/span")))
button_pass.click()

int = input()