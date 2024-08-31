
# extract zip file to a directory
def extract_zip_file(zip_file_path: str, extract_to_path: str):
    import zipfile
    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)
    print(f"Extracted all files to {extract_to_path}")

def download_raw_file(repository: str, file_name: str, vc_id: str, branch: str):
    url = f"https://raw.githubusercontent.com/{vc_id}/{repository}/{branch}/{file_name}"

    # download file from url
    import requests

    response = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(response.content)

    print(f"File {file_name} downloaded successfully")


