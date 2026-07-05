def generate_route(location, constraints):

    blocked_routes = []

    if constraints:

        for item in constraints:

            blocked_routes.append(item)

    recommended_route = (
        f"Primary relief route activated towards {location}"
    )

    avoid_route = ", ".join(blocked_routes)

    if avoid_route == "":
        avoid_route = "No blocked routes detected"

    return {

        "recommended_route": recommended_route,

        "avoid_route": avoid_route
    }
