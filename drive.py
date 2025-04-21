import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def launch_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    return driver


def run_axe_scan(driver, url):
    driver.get(url)
    time.sleep(5)  # Let it load
    axe_script = requests.get("https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.8.0/axe.min.js").text
    driver.execute_script(axe_script)

    results = driver.execute_script("""
        return new Promise(resolve => {
            axe.run(function(err, results) {
                if (err) throw err;
                resolve(results);
            });
        });
    """)
    return results["violations"]
