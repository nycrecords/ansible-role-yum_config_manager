Ansible Role: Yum Config Manager
=========

[![License](https://img.shields.io/badge/license-Apache-green.svg?style=flat)](https://raw.githubusercontent.com/nycrecords/ansible-role-nginx/master/LICENSE)
[![Build Status](https://travis-ci.org/nycrecords/ansible-role-yum_config_manager.svg?branch=master)](https://travis-ci.org/nycrecords/ansible-role-yum_config_manager)
[![Build Status](https://gitlab.com/nycrecords/ansible-role-yum_config_manager/badges/master/build.svg)](https://gitlab.com/nycrecords/ansible-role-yum_config_manager)
[![Galaxy](https://img.shields.io/badge/galaxy-nycrecords.yum_config_manager-blue.svg)](https://galaxy.ansible.com/nycrecords/yum_config_manager)
![Ansible](https://img.shields.io/ansible/role/d/44625.svg)
![Ansible](https://img.shields.io/badge/dynamic/json.svg?label=min_ansible_version&url=https%3A%2F%2Fgalaxy.ansible.com%2Fapi%2Fv1%2Froles%2F44625%2F&query=$.min_ansible_version)

Role to use yum-config-manager to manage repositories on RHEL.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ansible-role-yum_config_manager, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
