from selenium import webdriver
import time
import unittest
# driver = webdriver.Chrome(executable_path='D:\\python3.7.7\\chromedriver_win32\\chromedriver.exe')
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get('http://localhost:8000')
        time.sleep(1)
        self.assertIn('To-Do' , self.browser.title) , "Browser title was:" + self.browser.title
        self.fail('Finish the test')

if __name__ == "__main__":
    unittest.main()

