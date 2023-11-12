import math

g = 9.8  # gravitational constant (m/s^2)
m = 68.1  # mass of the parachutist (kg)
c = 12.5  # drag coefficient (kg/s)

def v(t):
    return g * m / c * (1 - math.exp(-(c / m) * t))

def trapm(h, n, f):
    result = f[0]  # f[0] is f0
    for i in range(1, n):
        result += 2 * f[i]
    result += f[n]  # f[n] is fn
    return h * result / 2

def calculate_multiple_segment_distance(t, segments):
    h = t / segments  # width of each segment
    time_values = [i * h for i in range(segments + 1)]  # time values for each segment
    velocity_values = [v(time) for time in time_values]  # velocity values for each segment
    return trapm(h, segments, velocity_values)

analytical_result = 289.43515
total_time = 10  # seconds

for segments in [1, 2, 5, 10, 100, 1000]:
    multiple_segment_distance = calculate_multiple_segment_distance(total_time, segments)
    multiple_segment_error_percentage = abs((multiple_segment_distance - analytical_result) / analytical_result) * 100
    print(f"Segments: {segments}, Multiple-Segment Distance: {multiple_segment_distance:.4f}, Error: {multiple_segment_error_percentage:.4f}%")
    print("-" * 50)
