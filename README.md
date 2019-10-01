![Logo](https://raw.githubusercontent.com/idealista/java_role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/java_role.png)](https://travis-ci.org/idealista/java_role)
[![Docker Hub pulls](https://img.shields.io/docker/pulls/idealista/jdk.svg)](https://hub.docker.com/r/idealista/jdk/)

# Java Ansible role

This Ansible Role installs java ([OpenJDK](http://openjdk.java.net/) in a [Debian/Ubuntu or CentOS environment](https://github.com/idealista/java_role/blob/master/meta/main.yml#L7).

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

**DISCLAIMER:** Because a [issue in Debian Jessie/backport repositories](https://www.lucas-nussbaum.net/blog/?p=947) we decided to follow the workaround of adding **Acquire::Check-Valid-Until no** to Debian Jessie configuration while the issue is not solved, with concerns about security it implies. The other option was removing Debian 8 support. Proceed with caution. 

### Prerequisities

To use this role as dependency in your playbook, prerequisites below:

Ansible 2.8.4.0 version installed.
Inventory destination should be a Debian/Ubuntu or CentOS environment.

For testing purposes you will need [Python 3.6+](https://www.python.org/downloads/release/python-368/) and [Pipenv](https://github.com/pypa/pipenv)

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```yml
- src: http://github.com/idealista/java_role.git
  scm: git
  version: 5.0.0
  name: java
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/java_role/) as origin if you prefer:

```yml
- src: idealista.java_role
  version: 5.0.0
  name: java
```

Alternatively you could find tagged Docker images for Debian Jessie, Debian Stretch, Ubuntu Xenial, Ubuntu Bionic and CentOS 7 in [Docker Hub](https://hub.docker.com/r/idealista/jdk/).

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

### Docker Hub

We publish every role version as a Docker image in Docker Hub: https://hub.docker.com/r/idealista/jdk.

You can pull our images by executing:

```bash
docker pull idealista/jdk:${JDK_VERSION}-${DOCKER_IMAGE_BASE}-(openjdk-headless)
```

`JDK_VERSION:` Preferred JDK version.
`DOCKER_IMAGE`: Currently supporting: `jessie`/`stretch` to select between Debian versions, `xenial`/`bionic` to select between Ubuntu versions, and `7` to select a CentOS version. 

For instance:

```bash
docker pull idealista/jdk:8u191-xenial-openjdk-headless
```

List of versions (tags) can be checked on [Docker Hub](https://cloud.docker.com/repository/docker/idealista/jdk/tags)

### Ansible

[defaults/main.yml](https://github.com/idealista/java_role/blob/master/defaults/main.yml)

#### OpenJDK

A specific OpenJDK version should be selected overriding `java_open_jdk_version` variable using group vars/host vars:

Operative System | OpenJDK version
--- | ---
Debian Jessie | `8u171-b11-1~bpo8+1` (default)
Debian Stretch | `8u222-b10-1~deb9u1` (default)
Debian Stretch | `11.0.4+11-1~deb10u1`
Ubuntu Xenial | `8u222-b10-1ubuntu1~16.04.1`
Ubuntu Xenial | `9~b114-0ubuntu1` (default)
Ubuntu Bionic | `8u222-b10-1ubuntu1~18.04.1`
Ubuntu Bionic | `11.0.4+11-1ubuntu2~18.04.3` (default)
CentOS 7 | `11.0.3.7` (default)

## Testing

```sh
$ pipenv install -r test-requirements.txt --python 3.6
$ DOCKER_IMAGE_BASE=(debian:jessie-slim|debian:stretch-slim|amd64/ubuntu:xenial|amd64/ubuntu:bionic|centos:7) JDK_VERSION=(`selected_jdk_version` see [.travis.yml](.travis.yml) file to check supported versions) pipenv run molecule test
```

**Note:** debian9 (Debian Stretch) will be used as default linux distro if none is provided.

See [molecule directory](https://github.com/idealista/java_role/tree/master/molecule) to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.8.4.0-green.svg)
![Packer](https://img.shields.io/badge/packer-1.3.4.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/java_role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/java_role/contributors) who participated in this project.

## License

![Apache 2.0 License](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE](LICENSE) file for details.

## Contributing

Please read [CONTRIBUTING.md](.github/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
