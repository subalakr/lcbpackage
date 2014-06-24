from jinja2 import Template
buf = open("template.html", "r").read()

from collections import namedtuple
VersionInfo = namedtuple('VersionInfo', 'verstr display')
VERSIONS = [
        VersionInfo('lcb_207', '2.0.7'),
        VersionInfo('lcb_210', '2.1.0'),
        VersionInfo('lcb_211', '2.1.1'),
        VersionInfo('lcb_212', '2.1.2'),
        VersionInfo('lcb_213', '2.1.3'),
        VersionInfo('lcb_220', '2.2.0'),
        VersionInfo('lcb_230', '2.3.0'),
        VersionInfo('lcb_231', '2.3.1'),
        VersionInfo('lcb_240dp1', '2.4.0-dp1')
]

VERSIONS = list(reversed(VERSIONS))

class UbuntuTarget(object):
    def __init__(self, version, display_version):
        self.version = version
        self.display_version = display_version

    def get_filename(self, lcbvers, arch):
        if int(lcbvers[2]) < 4 and self.version == '1404':
            return "N/A";

        if arch == 'x86':
            arch = 'i386'
        else:
            arch = 'amd64'

        return "libcouchbase-{0}_ubuntu{1}_{2}.tar".format(
                lcbvers, self.version, arch)

class WindowsTarget(object):
    def __init__(self, version, display_version):
        self.version = version
        self.display_version = display_version

    def get_filename(self, lcbvers, arch):
        if arch == 'x64':
            arch = 'amd64'
        return "libcouchbase-{0}_{1}_{2}.zip".format(lcbvers, arch, self.version)

class RedhatTarget(object):
    def __init__(self, version, display_version):
        self.version = version
        self.display_version = display_version

    def get_filename(self, lcbvers, arch):
        if arch == 'x86':
            if self.version.startswith('centos5'):
                arch = 'i386'
            else:
                arch = 'i686'
        return "libcouchbase-{0}_{1}_{2}.tar".format(lcbvers, self.version, arch)

class SourceTarget(object):
    def __init__(self):
        self.display_version = "Source Archive"

    def get_filename(self, lcbvers, arch):
        lcbvers = lcbvers.replace("-", "_")
        return "libcouchbase-{0}.tar.gz".format(lcbvers)

TARGETS = (
        UbuntuTarget('1004', 'Ubuntu 10.04'),
        UbuntuTarget('1204', 'Ubuntu 12.04'),
        UbuntuTarget('1404', 'Ubuntu 14.04'),
        RedhatTarget('centos55', 'Enterprise Linux 5'),
        RedhatTarget('centos62', 'Enterprise Linux 6'),
        WindowsTarget('vc9', 'Visual Studio 2008'),
        WindowsTarget('vc10', 'Visual Studio 2010'),
        WindowsTarget('vc11', 'Visual Studio 2012'),
    )

tmpl = Template(buf)
print tmpl.render(versions=VERSIONS, targets=TARGETS, tarball=SourceTarget())
