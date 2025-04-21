from orchestrator import analyze_page

if __name__ == "__main__":
    url = "https://www.instagram.com"
    print(f"\n🔍 Analyzing: {url}")
    result = analyze_page(url)
    print("\n📋 ChatGPT Accessibility Suggestions:\n")
    print(result)
