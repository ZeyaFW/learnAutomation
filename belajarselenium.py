from curses import keyname
import selectors
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By (this is removed on the version Selenium 4.3.0)

def test_googling():
    driver = webdriver.Chrome()
    driver.get('https://google.co.id')
    driver.find_element('name','q').send_keys("Zeya Firdaus Widyaka" + Keys.ENTER)
    assert 'Zeya Firdaus Widyaka' in driver.find_elements('h3').text
    assert 'Zeya Firdaus Widyaka' in driver.title
    driver.quit()
