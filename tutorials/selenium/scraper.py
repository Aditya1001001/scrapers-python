from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element_by_xpath("//*[@id='search-2']/form/label/input")
search.send_keys("test", Keys.RETURN)
# print(search.text)
# print(driver.page_source)

try:
    #wait a maximum of ten seconds until the element cane
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # print(main.text)
    atricles  = main.find_elements_by_name("article")
    for a in atricles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)


finally:
    # time.sleep(5)
    driver.quit()

# print(main.text)
