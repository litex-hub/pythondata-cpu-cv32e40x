import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post155"
version_tuple = (0, 4, 0, 155)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post155")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post13"
data_version_tuple = (0, 4, 0, 13)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post13")
except ImportError:
    pass
data_git_hash = "c3dd4246a461a0db2de58b9387ffbbdc7a07917d"
data_git_describe = "0.4.0-13-gc3dd4246"
data_git_msg = """\
commit c3dd4246a461a0db2de58b9387ffbbdc7a07917d
Merge: fa6c9645 2c8ca3b3
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Jun 8 12:01:47 2022 +0200

    Merge pull request #579 from Silabs-ArjanB/ArjanB_t2
    
    Table width change

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
