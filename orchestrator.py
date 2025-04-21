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


def save_full_report_to_html(violations, explanation, output_file="report.html"):
    violations_html = ""
    for v in violations:
        violations_html += f"<h3>{v['help']} ({v['impact']})</h3>"
        violations_html += f"<p><strong>Description:</strong> {v['description']}</p>"
        violations_html += "<ul>"
        for node in v['nodes'][:2]:  # show a couple examples max
            violations_html += f"<li><code>{node['html']}</code></li>"
        violations_html += "</ul><hr>"

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Accessibility Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #4CAF50; }}
            code {{ background-color: #f9f9f9; padding: 2px 4px; border-radius: 4px; }}
            pre {{ background-color: #f4f4f4; padding: 15px; border-radius: 8px; white-space: pre-wrap; }}
            hr {{ margin: 25px 0; }}
        </style>
    </head>
    <body>
        <h1>🧪 Accessibility Report</h1>

        <h2>🚫 Axe-core Violations</h2>
        {violations_html}

        <h2>💡 ChatGPT Suggestions</h2>
        <pre>{explanation}</pre>
    </body>
    </html>
    """
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_template.strip())
    print(f"✅ Full HTML report saved to {output_file}")
