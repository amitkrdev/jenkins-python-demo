from app import list_credentials

def test_list_credentials():
    """Test that credential files can be listed"""
    files = list_credentials()
    assert len(files) > 0