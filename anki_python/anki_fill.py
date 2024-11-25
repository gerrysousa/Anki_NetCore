from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.txtEmail = (By.XPATH, "//input[@placeholder='Email']")
        self.txtSenha = (By.XPATH, "//input[@placeholder='Password']")
        self.btnLogin = (By.XPATH, "//button[@class='btn btn-primary btn-lg']")
    
    def fill_email(self, email):
        self.driver.find_element(*self.txtEmail).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.txtSenha).send_keys(password)

    def click_btn_login(self):
        self.driver.find_element(*self.btnLogin).click()

class LoggedAreaPage:
    def __init__(self, driver):
        self.driver = driver
        self.txt_front = (By.XPATH, "//div[span='Front']/div/div")
        self.txt_back = (By.XPATH, "//div[span='Back']/div/div")
        self.txt_tag = (By.XPATH, "//div[span='Tags']/div/input")
        self.btn_save = (By.XPATH, "//button[text()='Add']")
        self.btn_add = (By.XPATH, "//a[text()='Add']")

    def fill_front_card(self, front):
        self.driver.find_element(*self.txt_front).send_keys(front)

    def fill_back_card(self, back):
        self.driver.find_element(*self.txt_back).send_keys(back)

    def fill_tag_card(self, tag):
        element = self.driver.find_element(*self.txt_tag)
        element.clear()  # clear
        element.send_keys(tag)

    def click_btn_save(self):
        self.driver.find_element(*self.btn_save).click()

    def click_btn_add(self):
        self.driver.find_element(*self.btn_add).click()

# Main function
def run_automation():
    # Config WebDriver
    driver = webdriver.Chrome()
    driver.get("https://ankiweb.net/account/login")    
    driver.maximize_window()
    time.sleep(2)
    
    # Login
    login_page = LoginPage(driver)
    login_page.fill_email("seu_email@exemplo.com")  # Fill your email
    login_page.fill_password("password")  # Fill your password
    login_page.click_btn_login()
    time.sleep(3)

    # Navigate to Deck cards
    logged_area_page = LoggedAreaPage(driver)
    logged_area_page.click_btn_add()
    time.sleep(3)

    # Read CSV file
    df = pd.read_csv("anki_data.csv", sep=";", header=0)  # header=0 if first line of csv is header

    # Add cards on Deck
    for index, row in df.iterrows():
        front = row[0]
        back = row[1]
        logged_area_page.fill_front_card(front)
        time.sleep(0.5)
        logged_area_page.fill_back_card(back)
        time.sleep(0.5)
        logged_area_page.fill_tag_card("Automatico_Sem_audio")
        logged_area_page.click_btn_save()
        time.sleep(1)

    # Finish
    print("++++++++++++++++++ Completed!!! ++++++++++++++++++")
    driver.quit()

if __name__ == "__main__":
    run_automation()
