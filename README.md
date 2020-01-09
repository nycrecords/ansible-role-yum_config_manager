Ansible Role: Yum Config Manager
=========

![GitHub](https://img.shields.io/github/license/nycrecords/ansible-role-yum_config_manager)
[![Build Status](https://travis-ci.com/nycrecords/ansible-role-yum_config_manager.svg?branch=master)](https://travis-ci.com/nycrecords/ansible-role-yum_config_manager)
[![Galaxy](https://img.shields.io/badge/galaxy-nycrecords.yum_config_manager-blue.svg)](https://galaxy.ansible.com/nycrecords/yum_config_manager)
![Ansible](https://img.shields.io/ansible/role/d/44917)
![Ansible](https://img.shields.io/ansible/quality/44917)

Role to use yum-config-manager to manage repositories on RHEL.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

* `rhui_config_path` - The path to the repository configuration files. Defaults to `/etc/yum.repos.d`
* `rhui_config_name` - The name of the file to edit for repository management. Defaults to `redhat-rhui.repo`
* `repositories` - Specifies which repositories to enable/disable, details below

To enable/disable specific repositories:

```yaml
rhsm_repositories:
  enabled:
    - enabled-repository
  disabled:
    - disabled-repository
```

The list of repositories in `disabled` is processed before `enabled`.

Dependencies
------------

Privilege escalation (sudo) is required for this role to function.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  roles:
     - role: ansible-role-yum_config_manager
  vars:
    repositories:
      enabled:
        - rhui-REGION-rhel-server-rhscl
        - rhui-REGION-rhel-server-debug-rhscl
      disabled:
        - rhui-REGION-rhel-server-source-rh-common
```

License
-------

Apache-2.0

Author Information
------------------

Joel Castillo ([@joelbcastillo](https://github.com/joelbcastillo)) for the NYC Department of Records Dev Team ([@nycrecords](https://github.com/nycrecords)
