import math

# Given constants
g = 9.8  # gravitational constant (m/s^2)
m = 68.1  # mass of the parachutist (kg)
c = 12.5  # drag coefficient (kg/s)

# Function for velocity v(t)
def v(t):
    return g * m / c * (1 - math.exp(-c / m * t))

# Function for single application of Simpson’s 1/3 rule
def simp13(h, f0, f1, f2):
    return 2 * h * (f0 + 4 * f1 + f2) / 6

# Function for single application of Simpson’s 3/8 rule
def simp38(h, f0, f1, f2, f3):
    return 3 * h * (f0 + 3 * (f1 + f2) + f3) / 8

# Function for trapezoidal rule
def trap(h, f0, f1):
    return h * (f0 + f1) / 2

# Function for unequally spaced data using a combination of Simpson’s and trapezoidal rules
def uneven(x, f):
    n = len(x) - 1
    h = x[1] - x[0]
    k = 1
    sum_result = 0.0

    for j in range(1, n + 1):
        hf = x[j - 1] - x[j]
        
        if abs(h * hf) <= 0.000001:
            if k == 3:
                result = simp13(h, f[j - 3], f[j - 2], f[j - 1])
                sum_result += result
                truncation_error = calculate_truncation_error(exact_value, sum_result)
                print(f"Segment {j-2}-{j-1}: Result: {result:.4f}, Truncation Error: {truncation_error:.4f}%")
                k = 1
            else:
                k += 1
        else:
            if k == 1:
                result = trap(h, f[j - 1], f[j])
                sum_result += result
                truncation_error = calculate_truncation_error(exact_value, sum_result)
                print(f"Segment {j-1}-{j}: Result: {result:.4f}, Truncation Error: {truncation_error:.4f}%")
            elif k == 2:
                result = simp13(h, f[j - 2], f[j - 1], f[j])
                sum_result += result
                truncation_error = calculate_truncation_error(exact_value, sum_result)
                print(f"Segment {j-2}-{j-1}-{j}: Result: {result:.4f}, Truncation Error: {truncation_error:.4f}%")
            else:
                result = simp38(h, f[j - 3], f[j - 2], f[j - 1], f[j])
                sum_result += result
                truncation_error = calculate_truncation_error(exact_value, sum_result)
                print(f"Segment {j-3}-{j-2}-{j-1}-{j}: Result: {result:.4f}, Truncation Error: {truncation_error:.4f}%")
                k = 1

        h = hf

    return sum_result

# Function to calculate truncation error
def calculate_truncation_error(exact, approx):
    return abs((exact - approx) / exact) * 100

# Example data
x_values = [0, 0.5, 1, 1.5, 2, 2.5, 3]  # More segments
# Replace v(t) with the actual function for v(t) based on your provided formula
f_values = [v(t) for t in x_values]

# Truncation Error Calculation
exact_value = 289.43515
truncation_error_exact = calculate_truncation_error(exact_value, 0)

# Calculate results
print("(a) Trapezoidal Rule Result:")
trap_result = trap(x_values[1] - x_values[0], f_values[0], f_values[1])
truncation_error_trap = calculate_truncation_error(exact_value, trap_result)
print(f"Segment 0-1: Result: {trap_result:.4f}, Truncation Error: {truncation_error_trap:.4f}%\n")

print("(b) Combination of Simpson’s and Trapezoidal Rules Result:")
uneven_result = uneven(x_values, f_values)
truncation_error_uneven = calculate_truncation_error(exact_value, uneven_result)
print(f"Total Result: {uneven_result:.4f}, Truncation Error: {truncation_error_uneven:.4f}%")
