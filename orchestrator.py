from drive import launch_browser, run_axe_scan
from openai_agent import analyze_violations

def analyze_page(url):
    driver = launch_browser()
    try:
        violations = run_axe_scan(driver, url)
        explanation = analyze_violations(violations, site_url=url)
        return explanation
    finally:
        driver.quit()
