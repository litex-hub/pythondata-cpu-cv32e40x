import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.4.0.post151"
version_tuple = (0, 4, 0, 151)
try:
    from packaging.version import Version as V
    pversion = V("0.4.0.post151")
except ImportError:
    pass

# Data version info
data_version_str = "0.4.0.post9"
data_version_tuple = (0, 4, 0, 9)
try:
    from packaging.version import Version as V
    pdata_version = V("0.4.0.post9")
except ImportError:
    pass
data_git_hash = "cace6ec2f19537db0771f0d38a02f58ef4ef04b4"
data_git_describe = "0.4.0-9-gcace6ec2"
data_git_msg = """\
commit cace6ec2f19537db0771f0d38a02f58ef4ef04b4
Merge: cee7c0f4 0964f569
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Jun 8 09:49:30 2022 +0200

    Merge pull request #577 from openhwgroup/revert-576-ArjanB_t0
    
    Revert "Table experiment 0"

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
