import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
# Function to check if a character is Kannada or belongs to common Kannada symbols
def is_kannada(char):
    # Kannada Unicode range
    return '\u0C80' <= char <= '\u0CFF'

# List of allowed characters to exclude
excluded_chars = {"–", ";", ",",":"," ","\n","+","=","`","’",'“'," ","  ","?",".","(",")"}

# Open the input file
with open("ಸ.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# To store the line numbers and non-Kannada characters
non_kannada_info = []

# Iterate through each line and check for non-Kannada characters
for line_number, line in enumerate(lines, start=1):
    for char in line:
        # Check if the character is neither Kannada nor one of the excluded characters
        if not is_kannada(char) and char not in excluded_chars:
            non_kannada_info.append((line_number, char))

# Output the results
if non_kannada_info:
    print("Non-Kannada characters found (excluding specified ones):")
    for line_number, char in non_kannada_info:
        print(f"Line {line_number}: {char}")
else:
    print("No non-Kannada characters found (excluding specified ones).")
