from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def register_mailtm_account():
    chrome_options = Options()
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://mail.tm/en/")
    time.sleep(3)


    try:
        account_button = driver.find_element(By.ID, "reka-dropdown-menu-trigger-v-1-4")
        account_button.click()
        time.sleep(2)
    except:
        print("Не удалось найти кнопку 'Аккаунт'!")
        driver.quit()
        return


    try:
        email_element = driver.find_element(By.XPATH, "//p[contains(@class, 'cursor-pointer select-all')]")
        email = email_element.text
    except:
        print("Не удалось найти email!")
        driver.quit()
        return


    try:
        password_element = driver.find_element(By.XPATH, "//span[contains(@class, 'cursor-pointer select-all account-blur')]")
        password = password_element.text
        if not password:
            password = password_element.get_attribute("innerText")
    except:
        print("Не удалось найти пароль!")
        driver.quit()
        return


    with open("mailtm_accounts.txt", "a") as f:
        f.write(f"лог: {email} пас: {password}\n")
    print(f"Сохранено: лог: {email} пас: {password}")

    driver.quit()


if __name__ == "__main__":
    for _ in range(5):
        try:
            register_mailtm_account()
            time.sleep(5)
        except Exception as e:
            print(f"ошибка: {e}")
