# coding:UTF-8
from selenium import webdriver

#�u���E�U��yahoo���J��
driver = webdriver.Chrome("C:\work\chromedriver.exe")
driver.get("https://www.google.co.jp/")


elem_search_word = driver.find_element_by_name("q")
elem_search_word.send_keys("selenium")

#�����܂łł���
elem_search_btn = driver.find_element_by_name("btnI")
elem_search_btn.click()
