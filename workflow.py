from agents.triage_agent import analyze_emergency
from agents.matcher_agent import allocate_resources
from agents.router_agent import generate_route
from agents.weather_agent import get_weather_data


def run_disaster_workflow(user_input):

    triage = analyze_emergency(user_input)

    resources, shortage = allocate_resources(
        triage["needs"]
    )

    weather = get_weather_data(
        triage["location"]
    )

    route = generate_route(
        triage["location"],
        triage["constraints"]
    )

    recommendation = (
        "Deploy emergency teams immediately. "
        "Monitor weather and coordinate logistics continuously."
    )

    return {

        "triage": triage,

        "resources": resources,

        "weather": weather,

        "route": route,

        "recommendation": recommendation,

        "shortage": shortage
    }
