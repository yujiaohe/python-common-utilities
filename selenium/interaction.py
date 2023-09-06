from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# click
# article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

# click
# community_portal = driver.find_element(by=By.LINK_TEXT, value="Community portal")
# community_portal.click()

# search for python
search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search_button = driver.find_element(by=By.CSS_SELECTOR, value="#searchform div .cdx-button")
search_button.click()

driver.close()
