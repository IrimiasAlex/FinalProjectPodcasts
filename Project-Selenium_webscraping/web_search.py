import csv
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def browser_function():
    driver_path = "path/to/chromedriver"
    chr_options = Options()
    chr_options.add_experimental_option("detach", True)
    chr_driver = webdriver.Chrome(driver_path, options=chr_options)
    chr_driver.get("https://target_website.com")



first_question = input("In which store do you want to look? [emag/amazon/ebay/allthree]? ").lower()
second_question = input("What exactly do you want to look for? ").lower()
third_question = input("Do you want to see the prices sorted by something? ")

if first_question == 'emag' and not third_question:
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get("https://www.emag.ro/#opensearch")
    get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
    get_element.send_keys(second_question)
    get_element.submit()
    # search_element = browser.find_element(by=By.ID, value='card_grid')


elif first_question == 'amazon' and third_question == 'No':
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get("https://www.amazon.com/")
    get_element1 = browser.find_element(by=By.ID, value='twotabsearchtextbox')
    get_element1.send_keys(second_question)
    get_element1.submit()

elif first_question == 'ebay' and third_question == 'No':
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.get("https://www.ebay.com/")
    get_element2 = browser.find_element(by=By.CLASS_NAME, value='ui-autocomplete-input')
    get_element2.send_keys(second_question)
    get_element2.submit()

elif first_question == "allthree" and third_question == 'No':
    browser = webdriver.Chrome(ChromeDriverManager().install())

    browser.execute_script("window.open('');")  # opens new tab
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://www.emag.ro/#opensearch")
    get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
    get_element.send_keys(second_question)
    get_element.submit()

    browser.execute_script("window.open('');")  # opens new tab
    browser.switch_to.window(browser.window_handles[2])
    browser.get("https://www.amazon.com/")
    get_element1 = browser.find_element(by=By.ID, value='twotabsearchtextbox')
    get_element1.send_keys(second_question)
    get_element1.submit()

    browser.execute_script("window.open('');")  # opens new tab
    browser.switch_to.window(browser.window_handles[3])
    browser.get("https://www.ebay.com/")
    get_element2 = browser.find_element(by=By.CLASS_NAME, value='ui-autocomplete-input')
    get_element2.send_keys(second_question)
    get_element2.submit()

elif first_question == 'emag' and third_question == 'Yes':
    result = ['Price: Low to High', 'Price: High to Low']
    result1 = input(f"Sort by: 1 :{result[0]} or 2 :{result[1]} --> ")

    if result1 == "1":
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.emag.ro/#opensearch")
        get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
        get_element.send_keys(second_question)
        get_element.submit()
        get_element = browser.find_element(by=By.CLASS_NAME, value='sort-control-btn-dropdown')
        get_element.click()
        get_element = browser.find_element(by=By.LINK_TEXT, value='Pret crescator')
        get_element.click()
    elif result1 == "2":
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.emag.ro/#opensearch")
        get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
        get_element.send_keys(second_question)
        get_element.submit()
        get_element = browser.find_element(by=By.CLASS_NAME, value='sort-control-btn-dropdown')
        get_element.click()
        get_element = browser.find_element(by=By.LINK_TEXT, value='Pret descrescator')
        get_element.click()

elif first_question == 'amazon' and third_question == 'Yes':
    result = ['Price: Low to High', 'Price: High to Low']
    result1 = input(f"Sort by: 1 :{result[0]} or 2 :{result[1]} --> ")

    if result1 == "1":
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.amazon.com/")
        get_element1 = browser.find_element(by=By.ID, value='twotabsearchtextbox')
        get_element1.send_keys(second_question)
        get_element1.submit()
        get_element1 = browser.find_element(by=By.ID, value='a-autoid-0-announce')
        get_element1.click()
        get_element1 = browser.find_element(by=By.ID, value='s-result-sort-select_1')
        get_element1.click()

    elif result1 == '2':
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.amazon.com/")
        get_element1 = browser.find_element(by=By.ID, value='twotabsearchtextbox')
        get_element1.send_keys(second_question)
        get_element1.submit()
        get_element1 = browser.find_element(by=By.ID, value='a-autoid-0-announce')
        get_element1.click()
        get_element1 = browser.find_element(by=By.ID, value='s-result-sort-select_2')
        get_element1.click()

elif first_question == 'ebay' and third_question == 'Yes':
    result = ['Price: Low to High', 'Price: High to Low']
    result1 = input(f"Sort by: 1 :{result[0]} or 2 :{result[1]} --> ")

    if result1 == "1":
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.ebay.com/")
        get_element2 = browser.find_element(by=By.CLASS_NAME, value='ui-autocomplete-input')
        get_element2.send_keys(second_question)
        get_element2.submit()
        get_element1 = browser.find_element(by=By.CLASS_NAME, value='expand-btn__cell')
        get_element1.click()
        get_element1 = browser.find_element(by=By.LINK_TEXT, value='Price + Shipping: lowest first')
        get_element1.click()

    elif result1 == '2':
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.ebay.com/")
        get_element2 = browser.find_element(by=By.CLASS_NAME, value='ui-autocomplete-input')
        get_element2.send_keys(second_question)
        get_element2.submit()
        get_element1 = browser.find_element(by=By.CLASS_NAME, value='expand-btn__cell')
        get_element1.click()
        get_element1 = browser.find_element(by=By.LINK_TEXT, value='Price + Shipping: highest first')
        get_element1.click()

elif first_question == 'allthree' and third_question == 'Yes':
    result = ['Price: Low to High', 'Price: High to Low']
    result1 = input(f"Sort by: 1 :{result[0]} or 2 :{result[1]} --> ")

    if result1 == "1":
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get("https://www.emag.ro/#opensearch")
        get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
        get_element.send_keys(second_question)
        get_element.submit()
        get_element = browser.find_element(by=By.CLASS_NAME, value='sort-control-btn-dropdown')
        get_element.click()
        get_element = browser.find_element(by=By.LINK_TEXT, value='Pret crescator')
        get_element.click()

        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[2])
        browser.get("https://www.amazon.com/")
        get_element1 = browser.find_element(by=By.ID, value='twotabsearchtextbox')
        get_element1.send_keys(second_question)
        get_element1.submit()
        get_element1 = browser.find_element(by=By.ID, value='a-autoid-0-announce')
        get_element1.click()
        get_element1 = browser.find_element(by=By.ID, value='s-result-sort-select_1')
        get_element1.click()

        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[3])
        browser.get("https://www.ebay.com/")
        get_element2 = browser.find_element(by=By.CLASS_NAME, value='ui-autocomplete-input')
        get_element2.send_keys(second_question)
        get_element2.submit()
        get_element1 = browser.find_element(by=By.CLASS_NAME, value='expand-btn__cell')
        get_element1.click()
        get_element1 = browser.find_element(by=By.LINK_TEXT, value='Price + Shipping: lowest first')
        get_element1.click()

    elif result1 == '2':
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get("https://www.emag.ro/#opensearch")
        get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
        get_element.send_keys(second_question)
        get_element.submit()
        get_element = browser.find_element(by=By.CLASS_NAME, value='sort-control-btn-dropdown')
        get_element.click()
        get_element = browser.find_element(by=By.LINK_TEXT, value='Pret descrescator')
        get_element.click()

        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[2])
        browser.get("https://www.amazon.com/")
        get_element1 = browser.find_element(by=By.ID, value='twotabsearchtextbox')
        get_element1.send_keys(second_question)
        get_element1.submit()
        get_element1 = browser.find_element(by=By.ID, value='a-autoid-0-announce')
        get_element1.click()
        get_element1 = browser.find_element(by=By.ID, value='s-result-sort-select_2')
        get_element1.click()

        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[3])
        browser.get("https://www.ebay.com/")
        get_element2 = browser.find_element(by=By.CLASS_NAME, value='ui-autocomplete-input')
        get_element2.send_keys(second_question)
        get_element2.submit()
        get_element1 = browser.find_element(by=By.CLASS_NAME, value='expand-btn__cell')
        get_element1.click()
        get_element1 = browser.find_element(by=By.LINK_TEXT, value='Price + Shipping: highest first')
        get_element1.click()







