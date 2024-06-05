from selenium import webdriver
import time
# driver = webdriver.Chrome(executable_path='D:\\python3.7.7\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome()
browser.get('http://localhost:8000')
time.sleep(1000)
assert 'Django' in browser.page_source