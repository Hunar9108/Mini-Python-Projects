from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]


print(item_ids)
end_time = time.time()+300.0
while time.time() < end_time:
    again = time.time()+5
    while time.time()<again:
        cookie = driver.find_element(By.ID,value="cookie")
        cookie.click()


    item = driver.find_elements(By.CSS_SELECTOR, value='#store b')
    item_price = []
    money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

    for price in item:
        element_text = price.text

        if element_text != "":
            cost = int(element_text.split("-")[1].strip().replace(",", ""))
            item_price.append(cost)

    cookie_functions = {}
    for n in range(len(item_price)):
        cookie_functions[item_price[n]] = item_ids[n]

    print(cookie_functions)

    affordable_functions = {}
    for cost, id in cookie_functions.items():
        if money > cost:
            affordable_functions[cost] = id
    print(affordable_functions)

    if affordable_functions:
        best_affordable_functions = max(affordable_functions)
        purchase_id = affordable_functions[best_affordable_functions]
        driver.find_element(By.ID,value=purchase_id).click()

driver.quit()
