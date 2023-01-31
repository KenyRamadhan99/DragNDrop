import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObject.Locator.locators import elementLocators
from TestData.data import dataTest

class elementObject():

     def __init__(self,driver):
        self.driver = driver
        self.Get_Box_A = elementLocators.BOX_A
        self.Get_Box_B = elementLocators.BOX_B
    

     def Box_A_To_B(self):
        source = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Get_Box_A)))
        target = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Get_Box_B)))
        
        # By Pass Bug Selenium Method ActionChains
        # Seharus nya bisa dengan function berikut :
        # action = ActionChains(self)
        # action.click_and_hold(source).move_to_element(target).release(target).perform()
        # #ActionChains(self).drag_and_drop(source,target).perform()
        
        f = open("script.js",  "r")
        javascript = f.read()
        f.close()
        time.sleep(3)
        self.execute_script(javascript, source, target)
        time.sleep(3)

     def Verify_Box_A_To_B(self):
        if self.find_element(By.CSS_SELECTOR,self.Get_Box_B).text == "A":
            print(dataTest.MessageSuccess)
        else:
            print(dataTest.MessageFailed)
        
        self.get_screenshot_as_file("A_To_B.png")

     def Box_B_To_A(self):
        source = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Get_Box_B)))
        target = WebDriverWait(self, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.Get_Box_A)))
        time.sleep(2)
        

        # By Pass Bug Selenium Method ActionChains
        # Seharus nya bisa dengan function berikut :
        # action = ActionChains(self)
        # action.click_and_hold(source).move_to_element(target).release(target).perform()
        # #ActionChains(self).drag_and_drop(source,target).perform()


        f = open("script.js",  "r")
        javascript = f.read()
        f.close()
        time.sleep(3)
        self.execute_script(javascript, source, target)
        time.sleep(3)

     def Verify_Box_B_To_A(self):   
        if self.find_element(By.CSS_SELECTOR,self.Get_Box_A).text == "B":
            print(dataTest.MessageSuccess)
        else:
            print(dataTest.MessageSuccess)
        
        self.get_screenshot_as_file("B_To_A.png")

        

        # action = ActionChains(self)
        # action.click_and_hold(source).move_to_element(target).release(target).perform()
        # #ActionChains(self).drag_and_drop(source,target).perform()