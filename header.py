def read_even_lines(filepath, starting_line):

    even_lines_data = {}
    try:
        with open(filepath, 'r') as file:
            for index, line in enumerate(file):
                if (index + 1) % 2 == 0:
                    parts = line.strip().split('|')
                    if len(parts) > 4:
                        key = parts[1].strip()
                        start = parts[2].strip()
                        end = parts[3].strip()
                        size = parts[4].strip()
                        even_lines_data[key] = [start, end, size]
                    elif line.strip():
                        print(f"Warning: Skipping line due to incorrect format: '{line.strip()}'")
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    return even_lines_data

# Example usage:
file_path = 'your_structured_file.txt'  # Replace with the actual path to your file
data_from_even_lines = read_even_lines(file_path)

if data_from_even_lines:
    print("Data from even-numbered lines:")
    for item in data_from_even_lines:
        print(item)
else:
    print("No even-numbered lines found or file could not be read.")