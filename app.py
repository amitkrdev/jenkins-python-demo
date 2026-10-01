import os
import xml.etree.ElementTree as ET
from pathlib import Path

def list_credentials():
    """
    List all credential files in C:\app\jenkins\conf\ that contain 'amt' in the filename
    """
    conf_dir = Path(r"C:\app\jenkins\conf")
    
    if not conf_dir.exists():
        print(f"Directory not found: {conf_dir}")
        return []
    
    # Look for files with 'amt' in the name
    cred_files = list(conf_dir.glob("*amt*_cred_*.cred.xml"))
    
    if not cred_files:
        print("No credential files with 'amt' in the name found in C:\\app\\jenkins\\conf\\")
        return []
    
    print(f"Found {len(cred_files)} credential file(s) with 'amt' in the name:")
    for file in cred_files:
        print(f"  - {file.name}")
    
    return cred_files

def load_credentials():
    """
    Load credentials from PowerShell encrypted XML format
    Match only files with 'amt' in the filename
    """
    username = os.environ.get("USERNAME", "unknown")
    computername = os.environ.get("COMPUTERNAME", "unknown")
    
    conf_dir = Path(r"C:\app\jenkins\conf")
    
    # Look for credential files with 'amt' in the name ONLY
    cred_files = list(conf_dir.glob("*amt*_cred_*.cred.xml"))
    
    if not cred_files:
        raise RuntimeError("No credential files with 'amt' in the name found in C:\\app\\jenkins\\conf\\")
    
    # Filter to match current user and computer
    matching_files = [f for f in cred_files if username in f.name and computername in f.name]
    
    if not matching_files:
        raise RuntimeError(f"No credential file with 'amt' in the name found for {username}@{computername}")
    
    cred_file = matching_files[0]
    print(f"\nLoading from: {cred_file.name}")
    
    try:
        tree = ET.parse(cred_file)
        root = tree.getroot()
        
        # Define namespace for PowerShell XML
        ns = {'ps': 'http://schemas.microsoft.com/powershell/2004/04'}
        
        # Find UserName and Password in PowerShell credential format
        username_elem = root.find(".//ps:S[@N='UserName']", ns)
        password_elem = root.find(".//ps:SS[@N='Password']", ns)
        
        if username_elem is None or password_elem is None:
            raise RuntimeError("Missing UserName or Password in credential file")
        
        username_value = username_elem.text
        password_value = password_elem.text
        
        if not username_value or not password_value:
            raise RuntimeError("UserName or Password is empty")
        
        # Print redacted
        print(f"[REDACTED] Username: {username_value[:2]}***")
        print(f"[REDACTED] Password: {password_value[:3]}***")
        
        return username_value, password_value
    
    except ET.ParseError as e:
        raise RuntimeError(f"Failed to parse XML: {e}")