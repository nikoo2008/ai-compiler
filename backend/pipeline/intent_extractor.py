import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def extract_intent(user_prompt):

    prompt = f"""
Convert the user request into JSON.

User request:

{user_prompt}

Return ONLY:

{{
"app_type":"",
"features":[],
"roles":[],
"entities":[]
}}

No explanation.
"""

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0
        }
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")
        text = text.replace("```", "")

    return json.loads(text)