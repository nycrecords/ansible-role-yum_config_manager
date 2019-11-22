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
        if line.lower().startswith("repo") or line.lower().startswith("loaded"):
            continue
        enabled_repos.append(line.split()[0])
    return enabled_repos


@pytest.fixture(scope="module")
def expected_repos():
    return (
        "rhui-REGION-client-config-server-7/x86_64",
        "rhui-REGION-rhel-server-debug-rhscl/7Server/x86_64",
        "rhui-REGION-rhel-server-releases/7Server/x86_64",
        "rhui-REGION-rhel-server-rh-common/7Server/x86_64",
        "rhui-REGION-rhel-server-rhscl/7Server/x86_64",
        "rhui-REGION-rhel-server-source-rhscl/7Server/x86_64",
    )


def test_repos_enabled(expected_repos, enabled_repos):
    assert set(expected_repos) == set(enabled_repos)
