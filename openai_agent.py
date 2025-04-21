import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_violations(violations, site_url="https://facebook.com"):
    summary = ""
    for v in violations[:25]:  # Limit to 25 violations
        summary += f"- {v['help']} ({v['impact']}): {v['description']}\n"
        for n in v['nodes'][:1]:
            summary += f"  Example HTML: {n['html']}\n"
        summary += "\n"

    prompt = f"""
    You are an AI accessibility expert. I ran axe-core on {site_url} and got the following accessibility violations:

    {summary}

    Please explain the issues and suggest how they can be fixed.
    """

    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=1000
    )

    return response.choices[0].message.content
