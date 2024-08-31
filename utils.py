import zipfile
from pathlib import Path

# extract zip file to a directory
def extract_zip_file(zip_file_path: Path, extract_to_path: Path):
  zip_file_path = Path(zip_file_path)
  extract_to_path = Path('.')
  with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
      zip_ref.extractall(extract_to_path)
  print(f"Extracted all files to {extract_to_path}")

