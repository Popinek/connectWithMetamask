from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

import time
import pyautogui

PASSWORD = '123pasworD321'
def press_left_alt_p():
    pyautogui.hotkey('altleft', 'p')


def press_left_alt_o():
    pyautogui.hotkey('altleft', 'o')


def open_firefox(extension):
    option = Options()
    option.headless = False

    service = Service('C:\\Users\\lukas\\Desktop\\python\\geckodriver.exe')

    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.get(extension)

    # Locate and click download button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div/div/div[2]/div[1]/section[1]/div/header/div[4]/div/div/a'))
    )
    button.click()

    # Wait for the page to load before performing actions
    time.sleep(10)

    # Perform actions after the page has loaded
    press_left_alt_p()

    time.sleep(3)
    press_left_alt_o()
    driver.switch_to.window(driver.window_handles[1])

    return driver


def input_mnemonic(driver, word, index):
    input_id = f'import-srp__srp-word-{index}'
    input_element = driver.find_element(By.ID, input_id)
    input_element.send_keys(word)


def move_to_next_input(driver):
    for i in range(2):
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB)


def connect_metamask(driver):
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)


    # Locate and click I Agree Checkbox button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="onboarding__terms-checkbox"]'))
    )
    button.click()

    # Locate and click Import Existing Wallet button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]'))
    )
    button.click()

    # Locate and click I Agree button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div/button[1]'))
    )
    button.click()

    # Locate and click First word button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="import-srp__srp-word-0"]'))
    )

    for i in range(3):
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB)  # locate mnemonic box

    with open('passphrase.txt', 'r') as file:
        mnemonic = file.read().split()

    for index, word in enumerate(mnemonic):
        input_mnemonic(driver, word, index)
        move_to_next_input(driver)

    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click()  # confirm
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(
        PASSWORD)  # enter password
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(
        PASSWORD)  # enter password twice
    time.sleep(1)
    driver.find_element('xpath',
                        '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click()  # I understand
    time.sleep(1)
    driver.find_element('xpath',
                        '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click()  # import my wallet
    time.sleep(2)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click()  # got it
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click()  # next page
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click()  # done
    time.sleep(1)
    driver.find_element('xpath', '/html/body/div[2]/div/div/section/div[1]/div/button/span').click()  # close

def connect_to_web3(driver):
    url = "https://app.uniswap.org/"
    driver.get(url)

    # Locate and click Connect button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[1]/nav/div/div[3]/div/div[3]/div/button'))
    )
    button.click()

    # Locate and click Metamask button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[3]/div[3]/div/div/div/div[2]/div[1]/div/div[2]/button/div/div[2]'))
    )
    button.click()

    time.sleep(1)
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)

    # Locate and click Metamask Next button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]'))
    )
    button.click()

    # Locate and click Metamask Connect button
    button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div[2]/footer/button[2]'))
    )
    button.click()

    print("You are connected with your MetaMask to ", url)

if __name__ == '__main__':
    extension = "https://addons.mozilla.org/cs/firefox/addon/ether-metamask/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search"

    driver = open_firefox(extension)
    connect_metamask(driver)
    connect_to_web3(driver)
