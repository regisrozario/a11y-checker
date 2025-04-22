from browser import launch_browser, get_dom
from openai_agent import analyze_dom


if __name__ == "__main__":
    url = "https://www.meta.ai/"
    print(f"\n🔍 Analyzing: {url}")

    driver = launch_browser(url)
    try:
        dom = get_dom(driver)
        result = analyze_dom(dom, url)
        print("\n📋 ChatGPT Accessibility Suggestions:\n")
        print(result)
    finally:
        driver.quit()
