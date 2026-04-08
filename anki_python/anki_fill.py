from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    def __init__(self, driver, wait_timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_timeout)
        self.txt_front = (By.XPATH, "//div[span='Front']/div/div")
        self.txt_back = (By.XPATH, "//div[span='Back']/div/div")
        self.txt_tag = (By.XPATH, "//div[span='Tags']/div/input")
        self.btn_save = (
            By.XPATH,
            "//button[contains(@class,'btn-primary') and normalize-space()='Add']",
        )
        self.btn_add = (By.XPATH, "//a[text()='Add']")

    def _fill_contenteditable(self, locator, text):
        el = self.wait.until(EC.presence_of_element_located(locator))
        el.click()
        el.send_keys(Keys.CONTROL, "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(str(text))

    def fill_front_card(self, front):
        self._fill_contenteditable(self.txt_front, front)

    def fill_back_card(self, back):
        self._fill_contenteditable(self.txt_back, back)

    def fill_tag_card(self, tag):
        element = self.wait.until(EC.presence_of_element_located(self.txt_tag))
        element.clear()
        element.send_keys(tag)
        element.send_keys(Keys.TAB)

    def click_btn_save(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.btn_save))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
        btn.click()

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
    df = pd.read_csv("anki_data.csv", sep=";", header=0)

    col_front = "Inglês"
    col_back = "Português"
    if col_front not in df.columns or col_back not in df.columns:
        raise ValueError(
            f"CSV deve ter colunas '{col_front}' e '{col_back}'. Encontrado: {list(df.columns)}"
        )

    # Add cards on Deck
    for index, row in df.iterrows():
        front = row[col_front]
        back = row[col_back]
        if pd.isna(front) or pd.isna(back):
            print(f"Pulando índice {index}: célula vazia")
            continue
        logged_area_page.fill_front_card(front)
        time.sleep(0.5)
        logged_area_page.fill_back_card(back)
        time.sleep(0.5)
        logged_area_page.fill_tag_card("Automatico_Sem_audio")
        logged_area_page.click_btn_save()
        time.sleep(1)
        print(f"Adicionado! Índice: {index} ")

    # Finish
    print("++++++++++++++++++ Completed!!! ++++++++++++++++++")
    driver.quit()

if __name__ == "__main__":
    run_automation()
