from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("--headless")  # Run without opening browser window
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def get_all_text(url):
    driver = get_driver()
    driver.get(url)

    # Get all visible text on the page
    page_text = driver.find_element("tag name", "body").text

    driver.quit()
    return page_text

# Example usage
url = "https://guardeerfunding.com/"  # Change to any website you want
text = get_all_text(url)
print(text)
