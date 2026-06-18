"""
Nexgensis Technologies Assignment

Author: Kajal Lavhe

Assumptions:
1. Agent positions remain fixed.
2. Packages are assigned independently.
3. In case of equal distances, first matching agent is selected.
4. Euclidean distance is used.
"""
import json
import math


def euclidean_distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


with open("base_case.json", "r") as file:
    data = json.load(file)

warehouses = data["warehouses"]
agents = data["agents"]
packages = data["packages"]

report = {}

for agent_id in agents:
    report[agent_id] = {
        "packages_delivered": 0,
        "total_distance": 0
    }

for package in packages:

    warehouse_id = package["warehouse"]
    warehouse_location = warehouses[warehouse_id]

    nearest_agent = None
    shortest_distance = float("inf")

    for agent_id, agent_location in agents.items():

        distance = euclidean_distance(
            agent_location,
            warehouse_location
        )

        if distance < shortest_distance:
            shortest_distance = distance
            nearest_agent = agent_id

    delivery_distance = euclidean_distance(
        warehouse_location,
        package["destination"]
    )

    total_trip = shortest_distance + delivery_distance

    report[nearest_agent]["packages_delivered"] += 1
    report[nearest_agent]["total_distance"] += total_trip

for agent_id in report:

    delivered = report[agent_id]["packages_delivered"]
    distance = report[agent_id]["total_distance"]

    report[agent_id]["total_distance"] = round(distance, 2)

    if delivered > 0:
        report[agent_id]["efficiency"] = round(
            distance / delivered,
            2
        )
    else:
        report[agent_id]["efficiency"] = 0

active_agents = {
    agent: info
    for agent, info in report.items()
    if info["packages_delivered"] > 0
}

best_agent = min(
    active_agents,
    key=lambda x: active_agents[x]["efficiency"]
)

report["best_agent"] = best_agent

with open("report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Report generated successfully.")
print(json.dumps(report, indent=4))
