import pytest


@pytest.fixture()
def ExecutingUnderOpenJDK(Ansible):
    return "openjdk" in Ansible.get_variables()["inventory_hostname_short"]


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


def test_java_version(ExecutingUnderOpenJDK, File, Command, AnsibleDefaults):
    if(ExecutingUnderOpenJDK): pytest.skip('skipped due to run under openJDK installation')

    assert AnsibleDefaults["java_oracle_jdk_version"] in Command("java -version").stderr


def test_java_home(ExecutingUnderOpenJDK, Command, AnsibleDefaults):
    if(ExecutingUnderOpenJDK): pytest.skip('skipped due to run under openJDK installation')

    assert '/opt/jdk/' + AnsibleDefaults['java_oracle_jdk_version'] in Command(". /etc/profile && echo $JAVA_HOME").stdout
