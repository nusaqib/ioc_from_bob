import xml.etree.ElementTree as ET
import argparse

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

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract PV names from a .bob XML file.')
    parser.add_argument('xml_file', help='Path to the .bob XML file')
    parser.add_argument('-o', '--output', default='pv_names.txt', help='Output file to save PV names')

    args = parser.parse_args()

    # Extract and save PV names
    pv_names = extract_pv_names(args.xml_file)
    save_pv_names_to_file(pv_names, args.output)
    print(f'PV names have been saved to {args.output}')

if __name__ == '__main__':
    main()
