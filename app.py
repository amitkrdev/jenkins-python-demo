import os
import xml.etree.ElementTree as ET
from pathlib import Path

def load_credentials_from_xml():
    """
    Load credentials from XML file (similar to PowerShell Import-CliXml pattern)
    Expected file: C:\app\jenkins\conf\lm_api_token_cred_<USERNAME>_<COMPUTERNAME>.cred.xml
    """
    username = os.environ.get("USERNAME", "unknown")
    computername = os.environ.get("COMPUTERNAME", "unknown")
    
    cred_file = f"C:\\app\\jenkins\\conf\\lm_api_token_cred_{username}_{computername}.cred.xml"
    cred_path = Path(cred_file)
    
    if not cred_path.exists():
        raise RuntimeError(f"Credential file not found: {cred_file}")
    
    try:
        tree = ET.parse(cred_path)
        root = tree.getroot()
        
        # Parse XML to extract username and password
        # Adjust tag names based on your actual XML structure
        company = root.find(".//username")
        auth = root.find(".//password")
        
        if company is None or auth is None:
            raise RuntimeError("Missing username or password in credential file")
        
        company_value = company.text
        auth_value = auth.text
        
        return company_value, auth_value
    
    except ET.ParseError as e:
        raise RuntimeError(f"Failed to parse credential XML: {e}")

def login():
    """
    Load credentials from XML file and validate
    """
    try:
        company, auth = load_credentials_from_xml()
        
        if not company or not auth:
            raise RuntimeError("Missing credentials in XML file")
        
        # Print redacted credentials (for logging/debugging)
        print(f"[REDACTED] Company: {company[:2]}***")
        print(f"[REDACTED] Auth: {auth[:3]}***")
        
        # Fake "authentication" for demo purposes
        return len(auth) >= 6
    
    except RuntimeError as e:
        print(f"Error: {e}")
        raise

# Alternative: If you want to fallback to environment variables
def login_with_fallback():
    """
    Try XML file first, fall back to environment variables
    """
    try:
        return login()
    except RuntimeError:
        print("XML credential file not found, trying environment variables...")
        user = os.environ.get("APP_USER")
        password = os.environ.get("APP_PASS")
        
        if not user or not password:
            raise RuntimeError("Missing credentials: APP_USER / APP_PASS not set")
        
        print(f"[REDACTED] User: {user[:2]}***")
        print(f"[REDACTED] Pass: {password[:3]}***")
        
        return len(password) >= 6