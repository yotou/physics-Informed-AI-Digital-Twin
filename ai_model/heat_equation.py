import numpy as np

def heat_equation(u, alpha, dx, dt):
    return u + alpha * dt / dx**2 * (
        np.roll(u, -1) - 2*u + np.roll(u, 1)
    )