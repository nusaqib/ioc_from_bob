import csv
import sys
import os

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

# Main script
if __name__ == "__main__":
    # Check if the CSV file and output file path are provided as command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py <csv_file> <output_file_path>")
        sys.exit(1)

    # Get the CSV file path and output file path from the command-line arguments
    csv_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    # Generate formatted data from the CSV file
    formatted_data = generate_formatted_data(csv_file_path)

    # Create the output directory if it doesn't exist
    output_directory = os.path.dirname(output_file_path)
    if output_directory:  # Only create if directory path is provided
        os.makedirs(output_directory, exist_ok=True)

    # Save the formatted data to the specified output file path
    save_to_file(formatted_data, output_file_path)
    print(f"Formatted data saved to {output_file_path}")
