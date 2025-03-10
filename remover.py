import os

def clean_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    cleaned_lines = [line.replace('(ಜೈನ)', '') for line in lines]
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            clean_text_file(file_path)
            print(f"Processed: {filename}")

# Change this to your target directory
directory_path = "refined"
process_directory(directory_path)
