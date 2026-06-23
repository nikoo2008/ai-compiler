import google.generativeai as genai

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def design_system(ir):

    prompt = f"""
Design architecture from:

{ir}

Return JSON only:

{{
"entities": {{}},
"flows": [],
"roles": {{}}
}}
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

    import json

    return json.loads(text)