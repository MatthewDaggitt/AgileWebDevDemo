import multiprocessing
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from unittest import TestCase

from app import create_app, db
from app.config import TestConfig
from app.controllers import GroupCreationError, create_group


localHost = "http://localhost:5000/"

class SeleniumTestCase(TestCase):

    def setUp(self):
        self.testApp = create_app(TestConfig)
        self.app_context = self.testApp.app_context()
        self.app_context.push()
        db.create_all()

        self.server_process = multiprocessing.Process(target=self.testApp.run)
        self.server_process.start()

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        self.server_process.terminate()
        self.driver.close()


    def test_login_page_missing_student(self):
        student_id = "01349324"
        loginElement = self.driver.find_element(By.ID, "uwa_id")

        loginElement.send_keys(student_id)

        loginElement = self.driver.find_element(By.ID, "password")
        loginElement.send_keys("a-password")

        submitElement = self.driver.find_element(By.ID, "submit")
        submitElement.click()

        messages = self.driver.find_elements(By.CLASS_NAME, "message")
        self.assertEqual(len(messages), 1, "Expected there to be a single error message when trying to login as a non-existent student")
        self.assertEqual(messages[0].text, f"No student found with ID {student_id}")
