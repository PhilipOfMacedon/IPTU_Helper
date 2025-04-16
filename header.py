def read_even_lines(filepath, starting_line):

    even_lines_data = {}
    try:
        with open(filepath, 'r') as file:
            for index, line in enumerate(file):
                if (index + 1) % 2 == 0 and (index + 1) >= starting_line:
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
        return None
    return even_lines_data

# Example usage:
file_path = 'test.txt'  # Replace with the actual path to your file
data_dictionary = read_even_lines(file_path, 4)

if data_dictionary:
    print("Data stored in a dictionary:")
    for key, values in data_dictionary.items():
        print(f"Key: {key}, Values: {values}")
else:
    print("No data read or file could not be processed.")