from orchestrator import analyze_page, save_full_report_to_html
from drive import launch_browser, run_axe_scan


if __name__ == "__main__":
    url = "https://www.facebook.com"
    print(f"\n🔍 Analyzing: {url}")

    driver = launch_browser()
    try:
        violations = run_axe_scan(driver, url)
        result = analyze_page(url)
        print("\n📋 ChatGPT Accessibility Suggestions:\n")
        print(result)

        # Save full report
        save_full_report_to_html(violations, result)
    finally:
        driver.quit()
