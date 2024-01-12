import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import datas


class TestOrangeHRM:
    url = "https://opensource-demo.orangehrmlive.com"

    # Booting Method
    @pytest.fixture
    def booting_function(self):
        service_obj = Service("c:/NewDriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_obj)
        yield
        self.driver.close()

    # To get OrangeHRM site
    def test_login(self, booting_function):
        self.driver.get(self.url)

        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, datas.TestSelectors.input_box_username))
        )
        username_input.send_keys(datas.TestData.username)

        # Forgot Password
        forgot_link = WebDriverWait(self.driver, 10).until(
             EC.element_to_be_clickable((By.XPATH, datas.TestSelectors.forgot_password))
         )
        forgot_link.click()

        repeat_username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, datas.TestSelectors.reset_username))

        )
        repeat_username.send_keys(datas.TestData.username)

        # Reset Password

        reset_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, datas.TestSelectors.reset_button))
        )
        reset_link.click()

        print("Reset Password link sent successfully")


