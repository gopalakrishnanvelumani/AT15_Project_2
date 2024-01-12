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

    def test_login(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()


        # Login into the OrangeHRM site

        username_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, datas.TestSelectors.input_box_username))
        )
        username_input.send_keys(datas.TestData.username)

        password_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, datas.TestSelectors.input_box_password))
        )
        password_input.send_keys(datas.TestData.password)

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, datas.TestSelectors.login_xpath))
        )
        login_button.click()

# Validation of MENU options in the admin page

        # Getting of MENU options into the list
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, datas.TestSelectors.menu_path))
        )
        current_list = []
        for new_list in elements:
            current_list.append(new_list.text)

        del current_list[10]

        # Assertion of new list to the MENU Options list

        assert (datas.list.menu_list == current_list)

        print("Validation of MENU Options in Admin page is successfully completed")



