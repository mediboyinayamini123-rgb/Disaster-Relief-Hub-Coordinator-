from agents.triage_agent import analyze_emergency

message = """
Flash flooding at Sector 4 stadium.
Over 150 people stranded.
Need 200 blankets and medical kits urgently.
Avoid Main St bridge.
"""

result = analyze_emergency(message)

print(result)