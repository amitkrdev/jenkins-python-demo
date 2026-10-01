from app import list_credentials, load_credentials

def test_list_credentials():
    """Test that credential files with 'amt' in the name can be listed"""
    files = list_credentials()
    assert len(files) > 0
    # Verify all returned files have 'amt' in the name
    for file in files:
        assert 'amt' in file.name.lower()

def test_load_credentials():
    """Test that credentials with 'amt' in filename can be loaded"""
    username, password = load_credentials()
    assert username is not None
    assert password is not None
    assert len(password) > 0
    print(f"✓ Test passed - loaded credentials for {username}")