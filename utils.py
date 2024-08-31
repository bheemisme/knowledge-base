
# extract zip file to a directory
def extract_zip_file(zip_file_path: str, extract_to_path: str):
    import zipfile
    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)
    print(f"Extracted all files to {extract_to_path}")

