import pandas as pd
import sys
import os

# Check if the file name and output file path are provided as command-line arguments
if len(sys.argv) < 3:
    print("Usage: python script.py <csv_file_name> <output_file_path>")
    sys.exit(1)

# Get the CSV file name and output file path from the command-line arguments
file_name = sys.argv[1]
output_file_path = sys.argv[2]

# Load the CSV file
df = pd.read_csv(file_name)

# Extract the 'PV' and 'Type' columns
extracted_df = df[['PV', 'type']]

# Create the output directory if it doesn't exist
output_directory = os.path.dirname(output_file_path)
os.makedirs(output_directory, exist_ok=True)

# Save the extracted data to the specified output file path
extracted_df.to_csv(output_file_path, index=False)

# Print the extracted data to verify
print(extracted_df)
print(f"Extracted data saved to: {output_file_path}")
