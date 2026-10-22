# -*- coding: utf-8 -*-
"""
This script downloads the data sets for examples in data subfolder of examples folder.

Created on Fri Aug 01 10:19:50 2026

@author: U.S. Securities and Exchange Commission.
"""

import requests
import zipfile
from io import BytesIO

def download_and_unzip(url, extract_to='.'):
    """
    Downloads a ZIP file from a URL and extracts its contents
    
    Parameters
    ----------
    url : str
        URL pointing to the ZIP file.
    extract_to : str, optional
        Directory path where the contents will be extracted. The default is 'data'.

    Returns
    -------
    None.

    """
    # Define headers with a User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 (Contact: your-email@example.com)'
    }
    
    # Send a GET request to the URL
    print(f"Downloading ZIP file from {url} ...")
    response = requests.get(url, headers=headers)
    
    # Raise an exception if the download fails
    response.raise_for_status()
    
    # Create a ZipFile object from the bytes of the ZIP file
    zip_file = zipfile.ZipFile(BytesIO(response.content))
    
    # Extract the contents of the Zip file
    print(f"Extracting the contents to {extract_to}...")
    zip_file.extractall(path=extract_to)
    zip_file.close()
    print("Extraction complete.")
    
    
download_and_unzip("https://www.sec.gov/files/dera/data/mutual-fund-prospectus-risk/return-summary-data-sets/2026q2_rr1.zip", extract_to="data/2026q2_rr1")
download_and_unzip("https://www.sec.gov/files/dera/data/mutual-fund-prospectus-risk/return-summary-data-sets/2025q1_rr1.zip", extract_to="data/2025q1_rr1")
download_and_unzip("https://www.sec.gov/files/dera/data/mutual-fund-prospectus-risk/return-summary-data-sets/2025q2_rr1.zip", extract_to="data/2025q2_rr1")
download_and_unzip("https://www.sec.gov/files/dera/data/mutual-fund-prospectus-risk/return-summary-data-sets/2025q3_rr1.zip", extract_to="data/2025q3_rr1")
download_and_unzip("https://www.sec.gov/files/dera/data/mutual-fund-prospectus-risk/return-summary-data-sets/2025q4_rr1.zip", extract_to="data/2025q4_rr1")

