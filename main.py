from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}

driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=options)

def test_selenium():
    driver.get("https://www.python.org")
    print(driver.title)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_selenium()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
