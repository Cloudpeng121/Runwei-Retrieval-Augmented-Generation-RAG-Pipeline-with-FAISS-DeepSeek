import requests
import os

# Load from environment
api_key = os.getenv("DEEPSEEK_API_KEY") or "sk-6b0e2ad3f50340b8b006865c5301cf4e"
if not api_key:
    raise ValueError("⚠️ DeepSeek API key not found in environment variable!")

# Prompt from earlier
prompt = """
You are a grant advisor. Based on the following retrieved opportunities, answer the user's question:

Context:
Title: Hello Alice Grants
Description:  Various grants for small businesses.
...
Question: Is there a grant available for women founders in tech?

Answer:
"""

# API request
url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
payload = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "system", "content": "You are a helpful grant advisor."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print("🤖 DeepSeek says:\n")
    print(response.json()["choices"][0]["message"]["content"])
else:
    print("❌ API call failed:", response.status_code)
    print(response.text)
