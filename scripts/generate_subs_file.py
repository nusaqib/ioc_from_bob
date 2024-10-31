import csv

def generate_formatted_data(csv_file):
    formatted_data = []

    # Open the CSV file
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)

        # Skip the header if present
        next(reader, None)

        # Process each row
        for row in reader:
            # Assuming 'PV' is in the first column and 'type' is in the second column
            pv = row[0]  # First column
            type_ = row[1]  # Second column

            # Append the formatted string to the list
            formatted_data.append(f'{{"{pv}", "{type_}"}}')

    return formatted_data

def save_to_file(formatted_data, output_file):
    with open(output_file, mode='w') as file:
        for item in formatted_data:
            file.write(f"{item}\n")

# Example usage
if __name__ == "__main__":
    csv_file_path = 'extracted_pv_and_type.csv'  # Update this to your CSV file path
    output_file_path = 'substitution_file.txt'  # Specify the output file name
    result = generate_formatted_data(csv_file_path)

    # Print the formatted output
    for item in result:
        print(item)

    # Save the output to a text file
    save_to_file(result, output_file_path)
    print(f"Formatted data saved to {output_file_path}")
