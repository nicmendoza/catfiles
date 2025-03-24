#!/usr/bin/env python3

import sys
import os
from pathlib import Path
import pyperclip

DELIMITER = "---"


def find_common_root(paths):
    """Find the lowest common ancestor of all the given paths."""
    common_path = os.path.commonpath(paths)
    return Path(common_path)


def main():
    args = sys.argv[1:]
    write_file = False

    # Check if the first argument is the --write flag
    if args and args[0] == "--write":
        write_file = True
        args = args[1:]

    # Validate argument count based on whether file-writing is enabled
    if write_file:
        if len(args) < 2:
            print("Usage: python script.py --write <output_file> <input_file1> <input_file2> ...")
            sys.exit(1)
        output_path = Path(args[0])
        input_paths = [Path(p) for p in args[1:]]
    else:
        if len(args) < 1:
            print("Usage: python script.py <input_file1> <input_file2> ...")
            sys.exit(1)
        input_paths = [Path(p) for p in args]

    # Validate input files
    for path in input_paths:
        if not path.is_file():
            print(f"Error: '{path}' is not a valid file.")
            sys.exit(1)

    # Find the lowest common ancestor of the input files
    common_root = find_common_root([str(p.resolve()) for p in input_paths])
    output_content = ""

    # Build the output content
    for path in input_paths:
        rel_path = path.resolve().relative_to(common_root)
        output_content += f"{DELIMITER}\n{rel_path}\n"
        with path.open('r', encoding='utf-8') as infile:
            output_content += infile.read()

    # Write to file if flag is provided
    if write_file:
        try:
            with output_path.open('w', encoding='utf-8') as outfile:
                outfile.write(output_content)
            print(f"Output successfully written to {output_path} and copied to clipboard.")
        except Exception as e:
            print(f"An error occurred while writing to file: {e}")
            sys.exit(1)
    else:
        print("Output copied to clipboard.")

    # Copy the output to the clipboard
    try:
        pyperclip.copy(output_content)
    except Exception as e:
        print(f"An error occurred while copying to clipboard: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()