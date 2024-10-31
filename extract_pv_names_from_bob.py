import xml.etree.ElementTree as ET

def extract_pv_names(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find all <pv_name> tags and extract their text, excluding those with $(pv_name)
    pv_names = [elem.text for elem in root.findall('.//pv_name') if elem.text and '$(pv_name)' not in elem.text]

    return pv_names

def save_pv_names_to_file(pv_names, output_file):
    # Write the list of PV names to a file
    with open(output_file, 'w') as f:
        for name in pv_names:
            f.write(name + ',')

# Example usage
xml_file = 'GTLView.bob'  # Replace with your XML file path
output_file = 'pv_names.txt'  # Replace with your desired output file path

pv_names = extract_pv_names(xml_file)
save_pv_names_to_file(pv_names, output_file)
print(f'PV names have been saved to {output_file}')
