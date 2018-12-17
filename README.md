![Logo](https://raw.githubusercontent.com/idealista/java-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/java-role.png)](https://travis-ci.org/idealista/java-role)
[![Docker Hub pulls](https://img.shields.io/docker/pulls/idealista/java-debian-ansible.svg)](https://hub.docker.com/r/idealista/jdk/)

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
  version: 3.2.0
  name: java
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/java-role/) as origin if you prefer:

```yml
- src: idealista.java-role
  version: 3.2.0
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
    - java
```

## Usage

### DockerHub

We publish every role version as a Docker image in Dockerhub: https://hub.docker.com/r/idealista/jdk.

You can pull our images by executing:
```bash
docker pull idealista/jdk:ROLE_VERSION-DISTRO_VERSION-JAVA_JDK
```

`ROLE_VERSION`: Starting from 3.2.1, is the tag published in GitHub
`DISTRO_VERSION`: Currently supporting: `ubuntu1604`, `debian8` and `debian9`
`JAVA_JDK`: `oraclejdk` or `openjdk`

For instance:
```bash
docker pull idealista/jdk:3.2.2-debian8-openjdk
```

List of versions can be checked on: https://cloud.docker.com/repository/docker/idealista/jdk/tags

### Ansible

You must choose between `openjdk` or `oraclejdk` implementation overriding `java_implementation` variable:

[defaults/main.yml](https://github.com/idealista/java-role/blob/master/defaults/main.yml)

Specific OpenJDK version should be selected using `java_open_jdk_version` variable under `vars/` specific OS variable files:

Operative System | OpenJDK version
--- | ---
Debian Jessie | `8u171-b11-1~bpo8+1`
Debian Stretch | `8u181-b13-2~deb9u1`
Ubuntu Xenial | `8u191-b12-0ubuntu0.16.04.1`

## Testing

```sh
$ pipenv install -r test-requirements.txt --python 2.7
$ MOLECULE_DISTRO=(debian8|debian9|ubuntu1604) pipenv run molecule test -s (openjdk|oraclejdk)
```

**Note:** debian9 (Debian Stretch) will be used as default linux distro if none is provided. It's mandatory to
define a scenario (openjdk or oraclejdk must be selected).

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

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
