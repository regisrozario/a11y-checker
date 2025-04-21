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
```terminal
🔍 Analyzing: https://www.instagram.com

📋 ChatGPT Accessibility Suggestions:

The accessibility issues identified by the axe-core tool on https://www.instagram.com highlight two main concerns: text scalability and the absence of a level-one heading. Let's discuss each issue in detail and suggest improvements.

### 1. Text Scalability Issue

**Issue Explained:**
The `<meta name="viewport">` tag controls how a web page is displayed on mobile devices. In the current configuration:

```html
<meta id="viewport" name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=2, viewport-fit=cover">
```

The `maximum-scale=2` attribute restricts users from scaling the text beyond 200%. This limitation can be problematic for users with visual impairments who need to zoom in further to read text comfortably.

**Suggested Fix:**
Modify the `maximum-scale` attribute in the viewport meta tag to allow scaling up to 500%. This change will enhance the text readability for users requiring larger scale adjustments.

```html
<meta id="viewport" name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=5, viewport-fit=cover">
```

**Improvement:**
By allowing a maximum scale of 500%, the website will be more accessible to users with visual impairments, as they can zoom in on the text up to five times the original size without losing content usability.

### 2. Absence of a Level-One Heading

**Issue Explained:**
The absence of a level-one heading (`<h1>`) on a webpage can make it difficult for screen reader users to understand the overall context of the page. Headings are used to structure content hierarchically and provide cues about the importance of various sections, with `<h1>` typically representing the most significant content or main topic.

**Suggested Fix:**
Identify the core topic or main feature of the page and encapsulate this in an `<h1>` tag. This tag should be placed prominently where it logically makes sense, often at the top of the page. For Instagram, this could be something like "Instagram Feed" or "Welcome to Instagram," depending on the page context.

Example:

```html
<h1>Welcome to Instagram</h1>
```

**Improvement:**
Incorporating a level-one heading will significantly enhance the navigational experience for users relying on assistive technologies. It provides a clear starting point and helps in understanding the page layout and content hierarchy, making the website more navigable and comprehensible.

### Summary of Improvements
- **Text Scalability:** Users with visual impairments can now scale text up to 500%, improving readability and accessibility.
- **Presence of a Level-One Heading:** Introducing a clear, descriptive `<h1>` tag improves the structural navigation for screen reader users and enhances the overall user experience by clearly defining the page's main focus.

Implementing these changes will help in making Instagram more inclusive and accessible to a broader range of users, complying with best practices and accessibility standards.

Process finished with exit code 0
```
