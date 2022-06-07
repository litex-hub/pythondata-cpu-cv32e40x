import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post142"
version_tuple = (0, 4, 0, 142)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post142")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post0"
data_version_tuple = (0, 4, 0, 0)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post0")
except ImportError:
    pass
data_git_hash = "7d0e140f056bbba71db62a4996f66c02232db3fc"
data_git_describe = "0.4.0-0-g7d0e140f"
data_git_msg = """\
commit 7d0e140f056bbba71db62a4996f66c02232db3fc
Merge: 7882d20e a7fc7ca5
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Tue Jun 7 13:33:32 2022 +0200

    Merge pull request #574 from Silabs-ArjanB/ArjanB_table2
    
    Table width fixes

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn
