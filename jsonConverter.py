import os
import json
import re

def process_file(filepath):
    dictionary = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if "–" in line:  # Check if the line contains "–"
                key, value = line.split("\u2013", 1)
                key = key.strip()
                values = [v.strip() for v in re.split(r'[;,]', value.strip())]
                dictionary[key] = values
    return dictionary

def process_directory(input_dir, output_file):
    final_dict = {}
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            final_dict.update(process_file(input_path))
    
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(final_dict, json_file, ensure_ascii=False, indent=4)

# Example usage
input_directory = "refined"  # Directory containing processed .txt files
output_json_file = "dictionary.json"  # Output JSON file
process_directory(input_directory, output_json_file)