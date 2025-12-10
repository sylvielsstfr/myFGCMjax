import myfgcmjax


def test_version():
    """Check to see that we can get the package version"""
    assert myfgcmjax.__version__ is not None
