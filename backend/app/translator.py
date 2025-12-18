from openai import OpenAI
import os
import json
import re

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# print("OPENAI_API_KEY loaded:", bool(os.getenv("OPENAI_API_KEY")))

def extract_json(text: str):
    text = re.sub(r"```json|```", "", text).strip()
    return json.loads(text)

def translate_batch(sections):
    valid = [
        s for s in sections
        if len(s.get("section_body_text", "").strip()) > 50
    ]

    if not valid:
        return {"translated_sections": []}
    
    payload = []
    for s in valid:
        payload.append({
            "id": s["section"],
            "text": s["section_body_text"]
        })
    
    prompt = f"""
    Translate the following zoning bylaw sections into structured JSON.

    Return ONLY valid JSON (no markdown, no explanation).
    {{
        "translated_sections": [
        {{
            "id": "2.2.1",
            "description": "...",
            "condition_english": "...",
            "requirement_english": "...",
            "exception": {{
                "condition_english": "...",
                "requirement_english": "...",
            }} | null
        }}]
    }}

    Sections:
    {json.dumps(payload, indent=2)}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a zoning bylaw expert."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3000,
        temperature=0
    )

    return extract_json(response.choices[0].message.content)   


# SYSTEM_PROMPT = """
# You are a zoning bylaw expert.
# Translate legal zoning text into structured plain
# English fields.
# Be precise. Do not invent rules.
# """

# def translate_section(section):
#     if not section["section_body_text"]:
#         return None
    
#     prompt = f"""
# Section ID: {section['section']}
# Text:
# {section['section_body_text']}

# Return JSON with:
# - description
# - condition_english
# - requirement_english
# - exception (or null)
# """
    
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {"role": "user", "content": prompt}
#         ]
#     )

#     return {
#         "id": section["section"],
#         **eval(response.choices[0].message.content)
#     }