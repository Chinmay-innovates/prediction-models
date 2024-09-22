def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculate_mode(data):
    frequency = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_count = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_count]

    if len(modes) == 1:
        return modes[0]
    else:
        return "No unique mode found"

def calculate_variance(data, mean):
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std_dev(variance):
    return variance ** 0.5

def central_tendency(data):
    if len(data) == 0:
        return "Data list is empty. Please provide valid data."

    # Calculate mean
    mean = calculate_mean(data)

    # Calculate median
    median = calculate_median(data)

    # Calculate mode
    mode = calculate_mode(data)

    # Calculate variance
    variance = calculate_variance(data, mean)

    # Calculate standard deviation
    std_dev = calculate_std_dev(variance)

    # Display the results
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")

# Example usage
data = [1, 2, 33, 4, 55, 55, 5, 6, 7, 8, 9]
central_tendency(data)
