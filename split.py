import re
import grapheme  # Importing grapheme to handle multi-codepoint characters

def process_line(line):
    # Match pattern where (X) is present before '–'
    match = re.search(r'([^\s(]+)\(([^)]+)\)(\S*)\s*–', line)
    if match:
        base_word = match.group(1)
        suffix = match.group(2)
        extra_part = match.group(3)
        rest_of_line = line[match.end():].strip()
        
        # Convert iterator to list and extract the last grapheme properly
        grapheme_list = list(grapheme.graphemes(base_word))
        base_word_trimmed = "".join(grapheme_list[:-1])
        
        # Construct new lines
        new_line_1 = f"{base_word}{extra_part} – {rest_of_line}\n"
        new_line_2 = f"{base_word_trimmed}{suffix}{extra_part} – {rest_of_line}\n"
        
        return new_line_1 + new_line_2
    
    return line  # Return unchanged if no match found

def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            modified_line = process_line(line)
            outfile.write(modified_line)

import re
import grapheme  # Importing grapheme to handle multi-codepoint characters
import os

def process_line(line):
    # Match pattern where (X) is present before '–'
    match = re.search(r'([^\s(]+)\(([^)]+)\)(\S*)\s*–', line)
    if match:
        base_word = match.group(1)
        suffix = match.group(2)
        extra_part = match.group(3)
        rest_of_line = line[match.end():].strip()
        
        # Convert iterator to list and extract the last grapheme properly
        grapheme_list = list(grapheme.graphemes(base_word))
        base_word_trimmed = "".join(grapheme_list[:-1])
        
        # Construct new lines
        new_line_1 = f"{base_word}{extra_part} – {rest_of_line}\n"
        new_line_2 = f"{base_word_trimmed}{suffix}{extra_part} – {rest_of_line}\n"
        
        return new_line_1 + new_line_2
    
    return line  # Return unchanged if no match found

def process_file(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            modified_line = process_line(line)
            outfile.write(modified_line)

def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            process_file(input_path, output_path)

# Example usage
input_directory = "cleaned"  # Directory containing input .txt files
output_directory = "refined"  # Directory to save processed .txt files
process_directory(input_directory, output_directory)
