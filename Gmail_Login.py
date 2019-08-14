from selenium import webdriver
import os
driver = webdriver.Chrome(executable_path='C:\\Users\\Downloads\\chromedriver_win32\\chromedriver.exe')  #your path
driver.get("https://www.gmail.com")
driver.maximize_window()
driver.find_element_by_name("identifier").send_keys("youremail@gmail.com")                       #enter your email address 
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()                      #using xpath
driver.implicitly_wait(4)
driver.find_element_by_name("password").send_keys("yourpassword")                                #enter your password
driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
