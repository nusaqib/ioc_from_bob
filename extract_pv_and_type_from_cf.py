import pandas as pd

# Load the CSV file
df = pd.read_csv('channel_finder_data.csv')

# Extract the 'PV' and 'Type' columns
extracted_df = df[['PV', 'type']]

# Save the extracted data to a new CSV file
extracted_df.to_csv('extracted_pv_and_type.csv', index=False)

# Print the extracted data to verify
print(extracted_df)