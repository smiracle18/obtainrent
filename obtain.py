from selenium import webdriver
import time
driver = webdriver.Chrome("C:\\Users\\susha\\Desktop\\kncChain\\driver\\chromedriver.exe")

driver.get("https://kncchain.com/index/login/login.html")

driver.find_element_by_name("account").send_keys("9473113408")
driver.find_element_by_name("password").send_keys("Welcome2")
time.sleep(1)
driver.find_element_by_css_selector(".login-submit button").click()
time.sleep(1)
driver.find_element_by_css_selector(".mui-popup-button-bold").click()
time.sleep(1)
driver.get("https://kncchain.com/index/machine/mymachine.html")

