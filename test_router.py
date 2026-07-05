from agents.router_agent import generate_route

location = "Sector 4 Stadium"

constraints = [
    "Avoid Main St bridge"
]

result = generate_route(location, constraints)

print(result)