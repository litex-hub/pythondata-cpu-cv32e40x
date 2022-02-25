import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.1.0.post156"
version_tuple = (0, 1, 0, 156)
try:
    from packaging.version import Version as V
    pversion = V("0.1.0.post156")
except ImportError:
    pass

# Data version info
data_version_str = "0.1.0.post30"
data_version_tuple = (0, 1, 0, 30)
try:
    from packaging.version import Version as V
    pdata_version = V("0.1.0.post30")
except ImportError:
    pass
data_git_hash = "7240216a9b4aa9892df767d436c105171fff9b76"
data_git_describe = "0.1.0-30-g7240216"
data_git_msg = """\
commit 7240216a9b4aa9892df767d436c105171fff9b76
Merge: 3575f67 a18191e
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Fri Feb 25 10:40:01 2022 +0100

    Merge pull request #456 from silabs-halfdan/rvfi_bugfix
    
    RVFI bugfixes

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
