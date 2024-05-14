from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
# Driver path
paths = r"E:\PyCharm\chromedriver.exe"

# importing options
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Getting the Web page URL
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# locating the Elements and passing values
user=driver.find_element(By.ID,"user-name")
user.send_keys("standard_user")
pwd=driver.find_element(By.ID,"password")
pwd.send_keys("secret_sauce")

# Authorising the login
driver.find_element(By.ID, "login-button").click()

# Fetching the Title and Url
title=driver.title
print(title)
url=driver.current_url
print(url)

pr=(driver.find_element(By.XPATH, "/html/body").text)

# printing the Webpage text content to text file
file=open(r"webpage_task_11.txt","w")
file.write(pr)
file.close()

# Closing the webdriver
driver.close()