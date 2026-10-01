import os
import xml.etree.ElementTree as ET
from pathlib import Path

def list_credentials():
    """
    List all credential files in C:\app\jenkins\conf\
    """
    conf_dir = Path(r"C:\app\jenkins\conf")
    
    if not conf_dir.exists():
        print(f"Directory not found: {conf_dir}")
        return []
    
    cred_files = list(conf_dir.glob("lm_api_token_cred_*.cred.xml"))
    
    if not cred_files:
        print("No credential files found in C:\\app\\jenkins\\conf\\")
        return []
    
    print(f"Found {len(cred_files)} credential file(s):")
    for file in cred_files:
        print(f"  - {file.name}")
    
    return cred_files

def load_credentials():
    """
    Load credentials from the first credential file found
    """
    cred_files = list_credentials()
    
    if not cred_files:
        raise RuntimeError("No credential files found")
    
    # Use the first credential file
    cred_file = cred_files[0]
    print(f"\nLoading from: {cred_file.name}")
    
    try:
        tree = ET.parse(cred_file)
        root = tree.getroot()
        
        username = root.find(".//username")
        password = root.find(".//password")
        
        if username is None or password is None:
            raise RuntimeError("Missing username or password in credential file")
        
        username_value = username.text
        password_value = password.text
        
        # Print redacted
        print(f"[REDACTED] Username: {username_value[:2]}***")
        print(f"[REDACTED] Password: {password_value[:3]}***")
        
        return username_value, password_value
    
    except ET.ParseError as e:
        raise RuntimeError(f"Failed to parse XML: {e}")