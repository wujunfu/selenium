#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
import time
import os

browser = webdriver.Firefox()
print os.path.abspath("./frame.html")
filePath = 'file:///' + os.path.abspath("frame.html")
browser.get(filePath)

browser.implicitly_wait(30)
browser.switch_to_frame("f1")
browser.switch_to_frame("f2")
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(2)
