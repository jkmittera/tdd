from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
browser = webdriver.Firefox(firefox_binary=binary)
#browser = webdriver.Chrome()
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title