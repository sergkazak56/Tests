# Решение задания № 3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
import time

LOGIN = "*******"         # Здесь должен быть ваш логин от Яндекса
PASSWORD = "********"    # Здесь должен быть ваш пароль от Яндекса
DRIVER_PATH = r'C:\driver\chromedriver.exe' # драйвер для Chrome можно скачать здесь: https://sites.google.com/chromium.org/driver/downloads

if __name__ == '__main__':
    servise = Service(r'C:\driver\chromedriver.exe')
    options = Options()
    options.add_argument("start-maximized")
    # ua = UserAgent()
    # userAgent = ua.random # не все юзер-агенты подходят.
    # print(userAgent)
    ua = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.52 Safari/537.36"
    options.add_argument(f'user-agent={ua}')
    browser = webdriver.Chrome(service=servise, options=options)
    browser.get('https://passport.yandex.ru/auth')
    time.sleep(3)

    element = browser.find_element(By.ID, "passp-field-login")
    element.send_keys(LOGIN)
    time.sleep(2)

    element = browser.find_element(By.ID, 'passp:sign-in')
    element.click()
    time.sleep(2)

    window_next = browser.window_handles[0]
    browser.switch_to.window(window_next)

    element = browser.find_element(By.ID, 'passp-field-passwd')
    element.send_keys(PASSWORD)
    time.sleep(2)

    element = browser.find_element(By.ID, 'passp:sign-in')
    element.click()
    time.sleep(30)

    browser.quit()

# К сожалению похоже перевести браузер в ручной режим невозможно.
# Если у вас есть вариант - подскажите пожалуйста.