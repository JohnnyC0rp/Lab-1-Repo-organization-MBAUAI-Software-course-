# file_io.py
import base64
import os

def encode_file(path):
    """Encode a file's bytes as a base64 UTF-8 string.

    Args:
        path: Path to the file on disk.

    Returns:
        The base64-encoded contents of the file as a UTF-8 string.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """Yield filenames and absolute paths for files in a directory.

    Args:
        dirpath: Directory to scan.

    Yields:
        Tuples of (filename, full_path) for each file in the directory.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path
