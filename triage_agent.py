import json
import time
import os

from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv(".env")

API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)


def analyze_emergency(message):

    prompt = f"""
You are an intelligent disaster emergency analysis AI.

Analyze the emergency message carefully.

Rules:
- Estimate realistic quantities if not explicitly mentioned.
- If people count is available, estimate resources based on people count.
- Constraints should ONLY include blocked roads, damaged bridges, unsafe routes, or inaccessible paths.
- Do NOT include urgency words like "urgent", "immediately", or "critical" in constraints.
- Return ONLY valid JSON.
- No explanations.
- No markdown.

Emergency Message:
{message}

JSON Format:
{{
    "severity": "LOW/MEDIUM/HIGH/CRITICAL",
    "location": "location name",
    "people_affected": number,
    "needs": {{
        "blankets": number,
        "food": number,
        "medical_kits": number
    }},
    "constraints": ["blocked road"]
}}
"""

    for attempt in range(3):

        try:

            response = client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.3
            )

            text = response.choices[0].message.content.strip()

            print("\nRAW GROQ RESPONSE:\n")
            print(text)

            result = json.loads(text)

            return result

        except Exception as e:

            print(f"Attempt {attempt + 1} failed")
            print("FULL GROQ ERROR:")
            print(e)

            time.sleep(2)

    print("Using fallback mock response")

    return {

        "severity": "MEDIUM",

        "location": "Unknown",

        "people_affected": 0,

        "needs": {
            "blankets": 50,
            "food": 50,
            "medical_kits": 10
        },

        "constraints": []
    }
