def check_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            # Remove trailing newline characters for cleaner output
            line = line.rstrip('\n')
            dash_count = line.count("–")
            # If the line does not contain exactly one dash, print it.
            if dash_count != 1:
                print(f"Line {line_number}: {line}")

if __name__ == "__main__":
    # Replace 'example.txt' with the path to your text file.
    file_path = "cleaned\ಸ.txt"
    check_lines(file_path)
