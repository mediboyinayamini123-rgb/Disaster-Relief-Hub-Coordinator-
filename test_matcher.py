from agents.matcher_agent import match_resources

needs = {
    "blankets": 200,
    "medical_kits": 5
}

result = match_resources(needs)

print(result)