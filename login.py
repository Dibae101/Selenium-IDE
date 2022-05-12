# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    # Test name: login
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://d2mhj3k1iqbtxz.cloudfront.net/")
    # 2 | setWindowSize | 945x1033 | 
    self.driver.set_window_size(945, 1033)
    # 3 | click | name=username | 
    self.driver.find_element(By.NAME, "username").click()
    # 4 | type | name=username | dib@gmail.cpm
    self.driver.find_element(By.NAME, "username").send_keys("dib@gmail.cpm")
    # 5 | click | name=password | 
    self.driver.find_element(By.NAME, "password").click()
    # 6 | type | name=password | test123
    self.driver.find_element(By.NAME, "password").send_keys("test123")
    # 7 | click | css=.login-button | Bad Credential
    # Failed
    self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()
    # 8 | mouseDownAt | css=html | -39,522
    element = self.driver.find_element(By.CSS_SELECTOR, "html")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 9 | mouseMoveAt | css=html | -39,522
    element = self.driver.find_element(By.CSS_SELECTOR, "html")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 10 | mouseUpAt | css=html | -39,522
    element = self.driver.find_element(By.CSS_SELECTOR, "html")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 11 | click | css=html | 
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    # 12 | type | name=username | tu@gmail.com
    self.driver.find_element(By.NAME, "username").send_keys("tu@gmail.com")
    # 13 | type | name=password | Dibae3663
    self.driver.find_element(By.NAME, "password").send_keys("Dibae3663")
    # 14 | click | css=form | 
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    # 15 | click | css=.login-button | Login Successful
    # Passed
    self.driver.find_element(By.CSS_SELECTOR, ".login-button").click()