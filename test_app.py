from app import list_credentials, load_credentials

def test_list_credentials():
    """Test that credential files can be listed"""
    files = list_credentials()
    assert len(files) > 0

def test_load_credentials():
    """Test that credentials can be loaded and printed"""
    username, password = load_credentials()
    assert username is not None
    assert password is not None