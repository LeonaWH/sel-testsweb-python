from selenium import webdriver	 
import time 
from selenium.webdriver.common.by import By



# Creating an instance webdriver
browser = webdriver.Chrome() 
browser.get('https://dbit.acm.org/')

#Clicking on Teams in nav bar
teams_menu = browser.find_element(By.XPATH, '//*[@id="menuDropdown"]/ul/li[2]/a')
teams_menu.click()

#Clicking on Team 2022-2023
team2023 = browser.find_element(By.XPATH, '//*[@id="bg"]/div/div/div[3]/div[2]/div[2]/div[2]/a')
team2023.click()

#Open LinkedIn Profile
leona_varghese_linkedin = browser.find_element(By.XPATH, '//*[@id="bg"]/div/div/div[3]/div[1]/div[1]/div[2]/div[2]/div/a/div/div[2]/h4')
leona_varghese_linkedin.click()
time.sleep(2)


# Close the browser window
browser.close()


