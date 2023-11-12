import math

g = 9.8  # gravitational constant (m/s^2)
m = 68.1  # mass of the parachutist (kg)
c = 12.5  # drag coefficient (kg/s)

def v(t):
    return g * m / c * (1 - math.exp(-(c / m) * t))

def trap(h, f0, f1):
    return h * (f0 + f1) / 2

def calculate_single_segment_distance(t):
    return trap(t, v(0), v(t))

analytical_result = 289.43515
total_time = 10  # seconds

single_segment_distance = calculate_single_segment_distance(total_time)
single_segment_error_percentage = abs((single_segment_distance - analytical_result) / analytical_result) * 100
print(f"Single-Segment Distance: {single_segment_distance:.4f}, Error: {single_segment_error_percentage:.4f}%")
