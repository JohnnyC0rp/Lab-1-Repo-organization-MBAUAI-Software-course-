# main.py
import argparse
import json

from . import file_io as io_mod
from . import gpt

def process_directory(dirpath):
    """Process all receipt images in a directory.

    Args:
        dirpath: Directory containing receipt images.

    Returns:
        A dictionary keyed by filename with extracted receipt details.
    """
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        results[name] = data
    return results

def main():
    """Parse CLI arguments and print extracted receipt data."""
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath")
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    data = process_directory(args.dirpath)
    if args.print:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
