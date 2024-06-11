from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import unittest
from django.test import LiveServerTestCase

MAX_WAIT = 10
# driver = webdriver.Chrome(executable_path='D:\\python3.7.7\\chromedriver_win32\\chromedriver.exe')
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()

    # def check_for_row_in_list_table(self,row_text):
    #     table = self.browser.find_element(By.ID, 'id_list_table')
    #     rows = table.find_elements(By.TAG_NAME, 'tr')
    #     self.assertIn(row_text, [row.text for row in rows])

    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrive_it_later(self):
        self.browser.get(self.live_server_url)
        time.sleep(1)

        #检测标题和头部包含'To-Do'
        self.assertIn('To-Do' , self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text
        self.assertIn('To-Do', header_text)

        #检查有输入代办项的文本框
        inputbox = self.browser.find_element(By.ID,'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #文本框输入'Buy flowers'
        inputbox.send_keys('Buy flowers')
        #按回车，页面更新
        #待办事项显示'1：Buy flowers'
        inputbox.send_keys(Keys.ENTER)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to List')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table("1：Buy flowers")
        self.wait_for_row_in_list_table("2：Give a gift to List")
        self.fail("Finish the test!")

# if __name__ == "__main__":
#     # unittest.main()

