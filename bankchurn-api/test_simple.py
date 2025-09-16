def test_simple():
    """Simple test to verify pytest is working."""
    assert 1 + 1 == 2

def test_imports():
    """Test that basic imports work."""
    import sys
    import os
    assert sys.version_info >= (3, 8)
    assert os.path.exists("app")
