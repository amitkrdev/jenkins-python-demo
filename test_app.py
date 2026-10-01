from app import list_credentials, load_credentials

def test_list_credentials():
    """Test that credential files can be listed"""
    files = list_credentials()
    assert len(files) > 0

def test_load_credentials():
    """Test that credentials can be loaded from test_cred_*.cred.xml"""
    username, password = load_credentials()
    assert username == 'testuser'
    assert password == 'test-api-key-12345'
    print(f"✓ Test passed - loaded credentials for {username}")