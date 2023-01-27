from selenium import webdriver
import unittest
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
class TestCreate(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        
    def test_drag_and_drop_A_to_B(self): 
        browser = self.browser
        browser.get('http://the-internet.herokuapp.com/drag_and_drop')
        browser.implicitly_wait(10)
        # source = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[(@id='column-a')]")))
        # target = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[(@id='column-b')]")))
        source = browser.find_element(By.CSS_SELECTOR,  "#column-a")
        target = browser.find_element(By.CSS_SELECTOR,  "#column-b")
        time.sleep(2)
        
        f = open("script.js",  "r")
        javascript = f.read()
        f.close()
        time.sleep(3)
        browser.execute_script(javascript, source, target)
        time.sleep(3)

        # action = ActionChains(browser)
        # action.click_and_hold(source).move_to_element(target).release(target).perform()
        # #ActionChains(browser).drag_and_drop(source,target).perform()
        # time.sleep(2)
        
        verifyA = browser.find_element(By.CSS_SELECTOR,"#column-b").text
        if verifyA == 'A':
            print("Drag & Drop Sukses")
        else:
            print("Drag & Drop Gagal")
        
        browser.get_screenshot_as_file("A_To_B.png")
    

    def test_drag_and_drop_B_to_A(self): 
        browser = self.browser
        browser.get('http://the-internet.herokuapp.com/drag_and_drop')
        browser.implicitly_wait(10)
        # source = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[(@id='column-a')]")))
        # target = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[(@id='column-b')]")))
        source = browser.find_element(By.CSS_SELECTOR,  "#column-b")
        target = browser.find_element(By.CSS_SELECTOR,  "#column-a")
        time.sleep(2)
        
        f = open("script.js",  "r")
        javascript = f.read()
        f.close()
        time.sleep(3)
        browser.execute_script(javascript, source, target)
        time.sleep(3)

        # action = ActionChains(browser)
        # action.click_and_hold(source).move_to_element(target).release(target).perform()
        # #ActionChains(browser).drag_and_drop(source,target).perform()
        # time.sleep(2)
        
        verifyA = browser.find_element(By.CSS_SELECTOR,"#column-a").text
        if verifyA == 'B':
            print("Drag & Drop Sukses")
        else:
            print("Drag & Drop Gagal")
        
        browser.get_screenshot_as_file("B_To_A.png")  

if __name__ == "__main__": 
    unittest.main()          
          


    
