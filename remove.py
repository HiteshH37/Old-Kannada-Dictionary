def process_file(input_path, output_path):
    # Read all lines from the file.
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        # Remove trailing newline characters.
        line = line.rstrip('\n')
        dash_count = line.count("–")
        
        if dash_count == 0:
            # No dash in this line:
            # If there's a previous line already processed, join this one to it.
            # (If it's the very first line, there's nothing to join with so we add it as-is.)
            if processed_lines:
                # Remove any trailing whitespace from the previous line and join with a space.
                processed_lines[-1] = processed_lines[-1].rstrip() + " " + line.lstrip()
            else:
                processed_lines.append(line)
        elif dash_count == 1:
            # Exactly one dash: add the line as-is.
            processed_lines.append(line)
        else:
            # More than one dash:
            # We keep the first dash and replace every subsequent dash with a space.
            # Split the line at each occurrence of "–".
            parts = line.split("–")
            # Reconstruct the line:
            #   parts[0] + "–" + (parts[1] replaced by space + parts[2] replaced by space, etc.)
            new_line = parts[0] + "–" + " ".join(parts[1:])
            processed_lines.append(new_line)

    # Write the processed lines to the output file.
    with open(output_path, 'w', encoding='utf-8') as f:
        for line in processed_lines:
            f.write(line + "\n")


if __name__ == '__main__':
    # Change these file names/path as needed.
    input_filename = "cleaned\ಸ.txt"
    output_filename = input_filename
    process_file(input_filename, output_filename)
    print(f"Processing complete. Check '{output_filename}' for results.")
