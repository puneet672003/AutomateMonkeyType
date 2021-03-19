from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

seconds = int(input("Choose timer : 15, 30 or 60: "))

if seconds not in [15, 30, 60]: 
    seconds = 30

driver = webdriver.Chrome("./chromedriver")

driver.get("https://monkeytype.com")
actions = ActionChains(driver)

timer = driver.find_element_by_xpath(f'//div[@class="buttons"]/div[@timeconfig="{seconds}"]')
timer.click()

sleep(2)

while True : 
    try : 
        letters = driver.find_elements_by_xpath('//div[@id="wordsWrapper"]/div[@id="words"]/div[@class="word active"]/letter')
        inputWords = driver.find_element_by_xpath('//div[@id="typingTest"]/input[@id="wordsInput"]')

        word = ''.join([_.text for _ in letters]) + ' '
        inputWords.send_keys(word)

    except: 
        break

