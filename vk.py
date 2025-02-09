from abc import ABC, abstractmethod

import seleniumwire.webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import multiprocessing

from user import get_user
from proxy import get_proxy

class Matka:
    def __init__(self):
        self.bots = []
        self.processes = []
        self.create_bots()

    def create_bots(self):
        proxy_counter = 0
        user_counter = 0
        while True:
            proxy, user = get_proxy(proxy_counter), get_user(user_counter)
            if not proxy or not user:
                with open('counters.txt', 'a') as f:
                    f.write(f'{proxy_counter}\n{user_counter}')
                break
            else:
                proxy_counter += 1
                user_counter += 1
                self.bots.append(Bot(proxy, user))

    def start_bots(self):
        for bot in self.bots:
            self.processes.append(multiprocessing.Process(target=bot.authorize))
            self.processes[-1].start()

class Bot:
    def __init__(self, proxy, user):
        seleniumwire_options = {
            'proxy': {
                'http': f'http://{proxy['username']}:{proxy['password']}@{proxy['adress']}:{proxy['port']}',
                'https': f'http://{proxy['username']}:{proxy['password']}@{proxy['adress']}:{proxy['port']}',
                'no_proxy': 'localhost,127.0.0.1'
            }
        }

        options = seleniumwire.webdriver.ChromeOptions()
        #удалить снизу
        options.add_experimental_option("detach", True)

        self.driver = seleniumwire.webdriver.Chrome(options=options, seleniumwire_options=seleniumwire_options)

        self.user = user

    def asd(self):
        self.driver.get("https://vk.com/")
    
    def authorize(self):
        actions = []
        actions.append({'action': 'click', 'xpath': '/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/div[2]/div/button[1]/span'})
        actions.append({'action': 'click', 'xpath': '//form/div[1]/div[1]/div/label[2]'})
        actions.append({'action': 'send_keys', 'xpath': '//form/div[1]/span/div/div/input', 'text': self.user['username']})

        actions.append({'action': 'click', 'xpath': '/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/button[1]/span'})
        actions.append({'action': 'eblan', 'xpath': '/html/body/div[14]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/section/div/div/div/div/div/form/button[1]'})

        actions.append({'action': 'send_keys', 'xpath': '//*[@id="root"]/div/div/div/div/div[1]/div/div/div/div/div/form/div[1]/div[3]/div/div/input', 'text': self.user['password']})
        actions.append({'action': 'click', 'xpath': '/html/body/div[1]/div/div/div/div/div[1]/div/div/div/div/div/form/div[2]/button/span'})

        self.driver.get("https://vk.com/")

        wait = WebDriverWait(self.driver, 20)
        
        for action in actions:
            element = wait.until(EC.presence_of_element_located((By.XPATH, action['xpath'])))
            if action['action'] == 'click':
                element.click()
            elif action['action'] == 'send_keys':
                element.send_keys(action['text'])

        lala = input()


if __name__ == '__main__':
    matka = Matka()
    for bot in matka.bots:
        bot.authorize()
    time.sleep(100)