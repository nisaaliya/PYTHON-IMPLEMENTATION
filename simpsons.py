import math

g = 9.8  # gravitational constant (m/s^2)
m = 68.1  # mass of the parachutist (kg)
c = 12.5  # drag coefficient (kg/s)

def v(t):
    return g * m / c * (1 - math.exp(-(c / m) * t))

# Single-application Simpson's 1/3 rule
def simp13(h, f0, f1, f2):
    return 2 * h * (f0 + 4 * f1 + f2) / 6

# Single-application Simpson's 3/8 rule
def simp38(h, f0, f1, f2, f3):
    return 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8

# Multiple-application Simpson's 1/3 rule
def simp13m(h, n, f):
    result = f[0]
    for i in range(1, n, 2):
        result += 4 * f[i] + 2 * f[i + 1]
    result += 4 * f[n - 1] + f[n]
    return h * result / 3

# Multiple-application Simpson's rule for both odd and even number of segments
def simp_int(a, b, n, f):
    h = (b - a) / n

    if n == 1:
        return h * (f[0] + f[1]) / 2
    else:
        m = n
        odd = n // 2 * 2 != n  # Check if the number of segments is odd

        # Using Simpson's 3/8 rule for the first part (even number of segments)
        if not odd and n > 1:
            result = simp38(h, f[0], f[1], f[2], f[3])
            m = n - 3
        else:
            result = 0.0

        # Using multiple-application 1/3 rule for the remaining part
        result += simp13(h, f[m - 1], f[m], f[m + 1])
        for i in range(m + 2, n, 2):
            result += 4 * f[i] + 2 * f[i + 1]
        result += 4 * f[n - 1] + f[n]

        return h * result / 3

analytical_result = 289.43515
total_time = 10  # seconds

for segments in [2, 4, 8, 16, 32]:
    h = total_time / segments
    time_values = [i * h for i in range(segments + 1)]  # time values for each segment
    velocity_values = [v(time) for time in time_values]  # velocity values for each segment

    if len(velocity_values) < 4:
        print(f"Error: Not enough data points for {segments} segments.")
        continue

    simp13_result = simp13(h, velocity_values[0], velocity_values[1], velocity_values[2])
    simp38_result = simp38(h, velocity_values[0], velocity_values[1], velocity_values[2], velocity_values[3])
    simp13m_result = simp13m(h, segments, velocity_values)
    simp_int_result = simp_int(0, total_time, segments, velocity_values)

    simp13_error_percentage = abs((simp13_result - analytical_result) / analytical_result) * 100
    simp38_error_percentage = abs((simp38_result - analytical_result) / analytical_result) * 100
    simp13m_error_percentage = abs((simp13m_result - analytical_result) / analytical_result) * 100
    simp_int_error_percentage = abs((simp_int_result - analytical_result) / analytical_result) * 100

    print(f"Segments: {segments}")
    print(f"Simpson's 1/3 Distance: {simp13_result:.4f}, Error: {simp13_error_percentage:.4f}%")
    print(f"Simpson's 3/8 Distance: {simp38_result:.4f}, Error: {simp38_error_percentage:.4f}%")
    print(f"Simpson's 1/3 Multiple Distance: {simp13m_result:.4f}, Error: {simp13m_error_percentage:.4f}%")
    print(f"Simpson's Integral Distance: {simp_int_result:.4f}, Error: {simp_int_error_percentage:.4f}%")
    print("-" * 50)