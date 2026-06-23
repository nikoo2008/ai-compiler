import google.generativeai as genai
import json

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_schema(system_design):

    prompt = f"""
Generate:

1 UI schema
2 API schema
3 DB schema
4 Auth schema

Return JSON:

{{
"ui": {{}},
"api": {{}},
"db": {{}},
"auth": {{}}
}}

Input:

{system_design}

JSON only.
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