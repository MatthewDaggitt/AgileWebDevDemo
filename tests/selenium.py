import multiprocessing
import time
from selenium import webdriver
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
   
        self.driver = webdriver.Chrome()
        self.driver.get(localHost)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        self.server_process.terminate()
        self.driver.close()


    def test_login_page(self):
        time.sleep(100)
        self.assertTrue(True)

        loginElement = self.driver.find_element(By.ID, "login")
        loginElement.send_keys("01349324")