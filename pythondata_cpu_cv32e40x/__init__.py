import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.2.0.post148"
version_tuple = (0, 2, 0, 148)
try:
    from packaging.version import Version as V
    pversion = V("0.2.0.post148")
except ImportError:
    pass

# Data version info
data_version_str = "0.2.0.post22"
data_version_tuple = (0, 2, 0, 22)
try:
    from packaging.version import Version as V
    pdata_version = V("0.2.0.post22")
except ImportError:
    pass
data_git_hash = "b84f137aa02f59df1be43e48ff3569ecb9de30cd"
data_git_describe = "0.2.0-22-gb84f137"
data_git_msg = """\
commit b84f137aa02f59df1be43e48ff3569ecb9de30cd
Merge: 2140bb5 174dcfa
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Mon Mar 28 15:15:55 2022 +0200

    Merge pull request #491 from Silabs-ArjanB/ArjanB_warlu3
    
    Updated WARL behavior of pmpxcfg

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
