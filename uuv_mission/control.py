def PDcontroller(reference: float, position: float, error: float):
    Kp = 0.15   # Proportional Gain
    Kd = 0.6    # Derivative Gain

    error_past = error
    error_current = reference - position
    action = Kp * error_current + Kd * (error_current - error_past)
    return action, error_current