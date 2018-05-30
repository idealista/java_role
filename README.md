![Logo](https://raw.githubusercontent.com/idealista/java-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/java-role.png)](https://travis-ci.org/idealista/java-role)

# Java Ansible role

This ansible role installs java ([OpenJDK](http://openjdk.java.net/) or [Oracle JDK](http://www.oracle.com/technetwork/java/javase/overview/index.html)) in a debian environment.

**DISCLAIMER:** Usage of any version of Oracle JDK in this role implies you have accepted the
[Oracle Binary Code License Agreement for Java SE](http://www.oracle.com/technetwork/java/javase/terms/license/index.html).

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install Java on ubuntu via ppa and sets the same ppa on Debian using trusty version

### Prerequisities

Ansible 2.4.3.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: http://github.com/idealista/java-role.git
  scm: git
  version: 2.0.0
  name: java
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - { role: java,
        java_open_jdk_set_version: '8'
      }
```

## Usage

### OpenJDK

To set multiple versions

```
java_open_jdk_version: ['6', '7', '8']
```

To set system defaults

```
java_open_jdk_set_version: '8'
```

## Testing

```
molecule test --platform=Debian9
```

See molecule.yml to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.4.3.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/java-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/java/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
