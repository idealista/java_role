import pytest


@pytest.fixture()
def ExecutingUnderOracleJDK(Ansible):
    return "oraclejdk" in Ansible.get_variables()["inventory_hostname_short"]


@pytest.fixture()
def AnsibleVarsOpenjdk(Ansible):
    return Ansible("include_vars", "tests/group_vars/openjdk.yml")["ansible_facts"]


def test_java_package(ExecutingUnderOracleJDK, Package, AnsibleVarsOpenjdk):
    if(ExecutingUnderOracleJDK): pytest.skip('skipped due to run under oracleJDK installation')

    for version in AnsibleVarsOpenjdk["java_open_jdk_version"]:
        assert Package("openjdk-" + str(version) + "-jdk").is_installed


def test_java_default(ExecutingUnderOracleJDK, File, Command, AnsibleVarsOpenjdk):
    if(ExecutingUnderOracleJDK): pytest.skip('skipped due to run under oracleJDK installation')

    assert str(AnsibleVarsOpenjdk["java_open_jdk_set_version"]) in Command("java -version").stderr
    assert File("/usr/lib/jvm/default-java").is_symlink


def test_java_home(ExecutingUnderOracleJDK, Command):
    if(ExecutingUnderOracleJDK): pytest.skip('skipped due to run under oracleJDK installation')

    assert "/usr/lib/jvm/default-java" in Command(". /etc/profile && echo $JAVA_HOME").stdout
