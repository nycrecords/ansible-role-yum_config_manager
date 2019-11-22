import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

@pytest.fixture(scope="module")
def enabled_repos(host):
    with host.sudo():
        stdout = host.check_output("yum repolist enabled")

    enabled_repos = []
    for line in stdout.splitlines():
        if line.lower().startswith("!"):
            enabled_repos.append(line.split()[0])
    return enabled_repos


def test_repos_enabled(expected_repos, enabled_repos):
    assert set(None) == set(enabled_repos)
