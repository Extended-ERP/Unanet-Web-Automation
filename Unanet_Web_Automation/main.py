import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# starts google chrome in either headless (export) or standard (import) mode.
def hello(name):
	print("My name is " + name)


def init_brwsr(downloadDir, headless=True, driver_path=''):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": downloadDir}
    chromeOptions.add_experimental_option("prefs", prefs)
    if headless:
       chromeOptions.add_argument("--headless")
    chromeDriver = chromeDir
    if not driver_path:
        driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chromeOptions)
    else:
        driver = webdriver.Chrome(chrome_options=chromeOptions)
    print("browser opened")
    return driver


# logs into the browser with credentials provided in settings.py

def login(driver, URL, username, password):
    '''Logs into unanet. Takes four arguments: driver, URL, username, password'''

    driver.get(URL + "/home")

    id_box = driver.find_element_by_name('username')
    id_box.send_keys(username)

    pass_box = driver.find_element_by_name('password')
    pass_box.send_keys(password)

    login_button = driver.find_element_by_name('button_ok')
    login_button.click()
    print("Logging in...")


print("loaded")

def mkRefFile(tbody, ref_file, clmPadding):

    """ Creates csv from Unanet table
        Fields:
            tbody - html table
            ref_file - save file name
            clmPadding - column padding in case headers don't line up to values
    """

    head = tbody.find_element_by_tag_name('thead')
    body = tbody.find_element_by_tag_name('tbody')

    file_data = []

    head_line = head.find_element_by_tag_name("tr")
    file_header = [header.text for header in head_line.find_elements_by_tag_name('td')]
    for x in range(clmPadding):
        file_header.insert(0, '')
    file_header.insert(0,'key')
    file_data.append(",".join(file_header))

    body_rows = body.find_elements_by_tag_name('tr')
    for row in body_rows:
        data = row.find_elements_by_tag_name('td')
        key = row.get_attribute("id").strip("k_").strip("r")
        file_row = []
        for datum in data:
            datum_text = datum.text
            file_row.append(datum_text)
            print(datum_text)
        file_row.insert(0, key)
        file_data.append(",".join(file_row))

    with open(ref_file, "w") as f:
        f.write("\n".join(file_data))
