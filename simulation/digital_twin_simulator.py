import numpy as np

def simulate_machine(temp, vibration):

    failure_risk = 0.01*temp + 0.2*vibration

    if failure_risk > 0.8:
        return "Maintenance Required"

    return "Healthy"