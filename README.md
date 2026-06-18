# python-assignment-nexgensis
Python Developer Assignment Submission for Nexgensis Technologies. Implements package delivery simulation, agent assignment, distance calculation, and report generation.
# Python Assignment – Mystery Delivery System

## Objective

Simulate a logistics delivery system where packages are assigned to the nearest delivery agent.

## Features

* Reads JSON input data
* Calculates Euclidean distance
* Assigns packages to nearest agents
* Simulates delivery process
* Generates report.json
* Finds most efficient agent

## Assumptions

1. Agent location remains fixed throughout the simulation.
2. Each package is assigned independently.
3. If two agents are at equal distance, the first encountered agent is selected.
4. Efficiency = Total Distance / Packages Delivered.
5. Lower efficiency value indicates better performance.

## How to Run

```bash
python main.py
```

## Output

Generates:

```text
report.json
```

containing:

* Packages delivered
* Total distance traveled
* Efficiency score
* Best performing agent
