import pytest


@pytest.fixture()
def AnsibleDefaultVars(Ansible):
    return Ansible("include_vars", "vars/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVarsOracle(Ansible):
    return Ansible("include_vars", "tests/group_vars/oracle.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVarsOpenjdk(Ansible):
    return Ansible("include_vars", "tests/group_vars/openjdk.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleDistribution(Ansible):
    return Ansible("setup")["ansible_facts"]["ansible_distribution"]


@pytest.fixture()
def Hostname(TestinfraBackend):
    return TestinfraBackend.get_hostname()


def test_java_resources(File, AnsibleDefaultVars, AnsibleDistribution, Hostname):
    if "oracle" in Hostname:
        if AnsibleDistribution == "Debian":
            java_resources = File("/etc/apt/sources.list.d/ppa_launchpad_net_webupd8team_java_ubuntu.list")
            assert java_resources.contains(AnsibleDefaultVars["java_repo_oracle"])
        elif AnsibleDistribution == "Ubuntu":
            java_resources = File("/etc/apt/sources.list.d/ppa_webupd8team_java_xenial.list")
            assert java_resources.contains("deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main")
        else:
            raise ValueError("Unsupported distribution: " + AnsibleDistribution)


def test_java_package(Package, AnsibleVarsOracle, AnsibleVarsOpenjdk, Hostname):
    if "oracle" in Hostname:
        for version in AnsibleVarsOracle["java_version"]:
            assert Package("oracle-java" + str(version) + "-installer").is_installed
    if "openjdk" in Hostname:
        for version in AnsibleVarsOpenjdk["java_version"]:
            assert Package("openjdk-" + str(version) + "-jdk").is_installed


def test_java_default(File, Package, Command, AnsibleVarsOracle, AnsibleVarsOpenjdk, Hostname):
    if "oracle" in Hostname:
        assert Package("oracle-java" + str(AnsibleVarsOracle["java_set_version"]) + "-set-default").is_installed
        assert File("/usr/lib/jvm/default-java").linked_to == "/usr/lib/jvm/java-" + str((AnsibleVarsOracle["java_set_version"])) + "-oracle"
        assert str(AnsibleVarsOracle["java_set_version"]) in Command("java -version").stderr
    if "openjdk" in Hostname:
        assert str(AnsibleVarsOpenjdk["java_set_version"]) in Command("java -version").stderr
    assert File("/usr/lib/jvm/default-java").is_symlink
