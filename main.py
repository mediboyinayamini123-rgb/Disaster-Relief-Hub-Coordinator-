from orchestration.workflow import run_disaster_workflow

message = """
Flash flooding at Sector 4 stadium.
Over 150 people stranded.
Need 200 blankets and medical kits urgently.
Avoid Main St bridge.
"""

result = run_disaster_workflow(message)

print(result)