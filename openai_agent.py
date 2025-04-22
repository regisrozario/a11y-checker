import os
from openai import OpenAI
from dotenv import load_dotenv
import textwrap

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_dom(dom: str, site_url: str) -> str:
    report = []
    dom = dom[:10000]
    prompt = f"""
            You are an expert in web accessibility and HTML semantics.
            Below is the DOM structure from the webpage at {site_url}.
            Analyze the DOM for accessibility issues such as:
            - Missing alt attributes
            - Improper use of ARIA roles
            - Missing labels on form elements
            - Poor heading structure
            - Keyboard navigation concerns
            Provide a clear and structured report of your findings and suggested fixes. While providing fixes, please include the current code snippets. All issues should be returned only in list and no conclusion is required.
            DOM Content:
            {dom}
            """
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )
    return response.choices[0].message.content

