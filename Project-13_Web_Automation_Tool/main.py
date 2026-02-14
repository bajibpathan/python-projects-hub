from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os


class WebAutomation:
    """
    Handles browser automation using Selenium WebDriver.
    """

    def __init__(self):
        """
        Initialize Chrome driver with custom options.
        """
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        # Set download directory to current working directory
        download_path = os.getcwd()
        prefs = {"download.default_directory": download_path}
        chrome_options.add_experimental_option("prefs", prefs)

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def wait_for_element(self, by, value, timeout=10):
        """
        Reusable method to wait for an element to become visible.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

    def login(self, username, password):
        """
        Perform login on demo website.
        """
        self.driver.get("https://demoqa.com/login")

        username_field = self.wait_for_element(By.ID, "userName")
        password_field = self.wait_for_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

    def close(self):
        """
        Close the browser session.
        """
        self.driver.quit()
