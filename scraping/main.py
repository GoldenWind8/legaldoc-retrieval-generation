import os
import requests
from PyPDF2 import PdfMerger

base_url = "https://www.bop.gov/PublicInfo/execute/policysearch/index.jsp?todo=query&output=json&name=&series=5000&type=&sortBy=&sortDescending="
# Fetch the JSON response
response = requests.get(base_url)
json_data = response.json()

def download_pdf(url, name):
    # Ensure the base directory exists
    base_dir = "downloaded_files"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Process the download
    response = requests.get(url)
    if response.status_code == 200:
        # Set the PDF filename as the specified name
        pdf_filename = url.split("/")[-1]
        pdf_path = os.path.join(base_dir, pdf_filename)
        with open(pdf_path, "wb") as pdf_file:
            pdf_file.write(response.content)
        print(f"Downloaded: {pdf_filename}")
    else:
        print(f"Failed to download: {url}")


# Download PDFs based on the JSON response
for policy in json_data.get("Policies", []):
    pdf_url = "https://www.bop.gov" + policy.get("url")
    download_pdf(pdf_url, policy['name'])
