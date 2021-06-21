from selenium import webdriver
browser = webdriver.Chrome('F:\windows tools\chromedriver')
browser.get('https://www.flipkart.com/')
closeButton = browser.find_element_by_css_selector('._2doB4z')
closeButton.click()

searchBox = browser.find_element_by_css_selector('._3704LK')
searchBox.send_keys('legion y540')
searchBox.submit()