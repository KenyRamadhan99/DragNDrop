from selenium import webdriver
import unittest
from TestData.data import dataTest
from PageObject.Page import object
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner


class TestCreate(unittest.TestCase): 

    def setUp(cls): 
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(dataTest.URL)
        
    def test_drag_and_drop_A_to_B(self): 
        driver = self.driver

        dragdrop = object.elementObject(driver)
        dragdrop.Box_A_To_B
        dragdrop.Verify_Box_A_To_B

    def test_drag_and_drop_B_to_A(self): 
        driver = self.driver

        dragdrop = object.elementObject(driver)
        dragdrop.Box_B_To_A
        dragdrop.Verify_Box_B_To_A

if __name__ == "__main__": 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Qoin/OneDrive - PT. Loyalty Program Indonesia/Documents/DragNDrop/Reports")          
          


    
