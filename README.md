Ansible Role to install java
============================

## This role installs multiple or single java versions and set one of them as system defaults

It installs java on ubuntu via ppa and sets the same ppa on Debian using trusty version

To set multiple versions

```bash
java_version: ['6', '7', '8']
```

To set system defaults

```bash
java_set_version: '8'
```


To launch tests

```bash
molecule test
```

There is a pre_task with python2 to satisfy ubuntu vbox image dependencies

## Omit linter

[ANSIBLE0010] Line 28 tasks/main.yml      Omit linter as we usually want jdk on latest version within propper version
[ANSIBLE0010] Line 35 tasks/main.yml      Omit linter as we usually want this package on latest versions aswell as previous one
[ANSIBLE0012] Line 5  tests/playbook.yml  Omit linter as we dont care about syntax on this pre_tasks. Its just to allow testing on ubuntu
