# 🧪 a11y-checker

An automated accessibility validation tool that uses `axe-core` in Selenium to detect issues on any web page and sends the violations to OpenAI GPT-4 Turbo for analysis and remediation suggestions.

## Features
- Injects `axe-core` into any webpage
- Captures accessibility violations
- Uses GPT-4 to explain and suggest fixes
- Modular code (browser, GPT, orchestrator)

## How to Run

```bash
# Clone the repo
git clone https://github.com/your-username/a11y-gpt-checker.git
cd a11y-gpt-checker

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI key in .env
echo "OPENAI_API_KEY=your-key-here" > .env

# Run
python main.py
# a11y-checker

```

## Analysis
![Screenshot 2025-04-21 at 10 37 40 PM](https://github.com/user-attachments/assets/1681e77a-bbb9-4b87-83f9-3f36b94258b9)
