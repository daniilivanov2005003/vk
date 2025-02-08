import selenium.webdriver.common.by
import seleniumwire.webdriver
import time
import get_user

proxy_username = "modeler_rOgCya"
proxy_password = "idVxnSDxf1Kv"
proxy_address = "86.104.75.67"
proxy_port = "13523"


seleniumwire_options = {
    'proxy': {
        'http': f'http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}',
        'https': f'http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}',
        'no_proxy': 'localhost,127.0.0.1'
    }
}

options = seleniumwire.webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = seleniumwire.webdriver.Chrome(options = options, seleniumwire_options = seleniumwire_options) 
driver.get("https://vk.com/")

element = driver.find_element(selenium.webdriver.common.by.By.XPATH, '/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/div[2]/div/button[1]/span')
element.click()

element = driver.find_element(selenium.webdriver.common.by.By.XPATH, '/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/div[1]/div[1]/div/label[2]')
element.click()

user = get_user.get_user(0)
print(user[0])

element = driver.find_element(selenium.webdriver.common.by.By.XPATH, '/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/div[1]/span/div/div/input')
element.send_keys(user[0])

element = driver.find_element(selenium.webdriver.common.by.By.XPATH, '/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/button[1]/span')
element.click()
