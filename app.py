import os
from pathlib import Path

def list_credentials():
    """
    List all credential files in C:\app\jenkins\conf\
    """
    conf_dir = Path("C:\\app\\jenkins\\conf\\")
    
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