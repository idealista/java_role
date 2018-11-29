![Logo](https://raw.githubusercontent.com/idealista/java-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/java-role.png)](https://travis-ci.org/idealista/java-role)
[![Docker Hub pulls](https://img.shields.io/docker/pulls/idealista/java-debian-ansible.svg)](https://hub.docker.com/r/idealista/java-debian-ansible/)

# Java Ansible role

This Ansible Role installs java ([OpenJDK](http://openjdk.java.net/) or [Oracle JDK](http://www.oracle.com/technetwork/java/javase/overview/index.html)) in a [Debian/Ubuntu environment](https://github.com/idealista/java-role/blob/master/meta/main.yml#L7).

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

These instructions will get you a copy of the role for your Ansible playbook.

Once launched, it will install Java using APT Packages (default) or downloading fresh version of Oracle Technology Network.

**DISCLAIMER:** Usage of any version of Oracle JDK in this role implies you have accepted the
[Oracle Binary Code License Agreement for Java SE](http://www.oracle.com/technetwork/java/javase/terms/license/index.html).

### Prerequisities

Ansible 2.4.5.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Docker](https://www.docker.com/) as driver.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```yml
- src: http://github.com/idealista/java-role.git
  scm: git
  version: 3.1.1
  name: java
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/java-role/) as origin if you prefer:

```yml
- src: idealista.java-role
  version: 3.1.1
  name: java
```

Alternatively you could find tagged Docker images for Debian Jessie, Wheezy and Ubuntu Xenial in [Docker Hub](https://hub.docker.com/r/idealista/java-debian-ansible/).

Install the role with ansible-galaxy command:

```sh
$ ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```yml
---
- hosts: someserver
  roles:
    - {
        role: java,
        java_open_jdk_set_version: '8'
      }
```

## Usage

### OpenJDK

To set multiple versions

```yml
java_open_jdk_version: ['6', '7', '8']
```

To set system defaults

```yml
java_open_jdk_set_version: '8'
```

## Testing

```sh
$ pipenv install -r test-requirements.txt --python 2.7
$ pipenv run molecule test
```

See [molecule directory](https://github.com/idealista/java-role/tree/master/molecule) to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.4.5.0-green.svg)

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
