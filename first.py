#!/usr/bin/python
#coding=utf-8

from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
print "open first web page: ", browser.title
time.sleep(0.2)
browser.maximize_window()
print "web browser maxisimum"
time.sleep(0.2)
browser.set_window_size(1400, 800)
browser.find_element_by_id("kw").send_keys("selenium")
time.sleep(0.2)
browser.find_element_by_id("su").click()
time.sleep(0.2)
browser.back()
print "web page back."
time.sleep(0.2)
browser.forward()
print "web page forward."
time.sleep(1)
browser.close()
