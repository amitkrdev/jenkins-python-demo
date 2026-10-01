import os
from app import login_with_fallback

def test_credentials_from_xml_or_env():
    """Test that credentials can be loaded from XML or environment"""
    try:
        result = login_with_fallback()
        assert result is True
    except RuntimeError as e:
        print(f"Credentials test failed: {e}")
        raise