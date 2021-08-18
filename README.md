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

Once launched, it will install Java using Debian or RHEL packages.

### Prerequisities

To use this role as dependency in your playbook, prerequisites below:

Ansible >=2.9.0 version installed.
Inventory destination should be a Debian/Ubuntu or CentOS environment.

For testing purposes you will need [Python 3.7+](https://www.python.org/downloads/release/python-377/), [Pipenv](https://github.com/pypa/pipenv).

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```yml
- src: http://github.com/idealista/java_role.git
  scm: git
  version: 7.0.0
  name: java
```

or using [Ansible Galaxy](https://galaxy.ansible.com/idealista/java_role/) as origin if you prefer:

```yml
- src: idealista.java_role
  version: 7.0.0
  name: java
```

Alternatively you could find tagged Docker images for Debian Stretch and Buster, Ubuntu Xenial, Bionic and Focal, and CentOS 7 and 8 in [Docker Hub](https://hub.docker.com/r/idealista/jdk/).

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
docker pull idealista/jdk:${JDK_VERSION}-${DOCKER_IMAGE_BASE}-${JDK_VENDOR}headless)
```

`JDK_VERSION:` Preferred JDK version.
`DOCKER_IMAGE`: Currently supporting: `stretch`/`buster/bullseye` to select between Debian versions, `xenial`/`bionic`/`focal` to select between Ubuntu versions, and `7`/`8` to select a CentOS version.
`JDK_VENDOR`: Currently supporting `openjdk`/ `adoptopenjdk`/`corretto`

For instance:

```bash
docker pull idealista/jdk:8u191-xenial-openjdk-headless
```

List of versions (tags) can be checked on [Docker Hub](https://cloud.docker.com/repository/docker/idealista/jdk/tags)

### Ansible

[defaults/main.yml](https://github.com/idealista/java_role/blob/master/defaults/main.yml)

#### OpenJDK

A specific OpenJDK version should be selected overriding `java_open_jdk_version_major` variable using group vars/host vars:

Operative System | OpenJDK major release
--- | ---
Debian Stretch | `8` (default)
Debian Stretch | `11`
Debian Buster | `11` (default)
Debian Bullseye | `17`
Debian Bullseye | `11` (default)
Ubuntu Xenial | `8`
Ubuntu Xenial | `9` (default)
Ubuntu Bionic | `8`
Ubuntu Bionic | `11` (default)
Ubuntu Focal | `8`
Ubuntu Focal | `11`
Ubuntu Focal | `13`
Ubuntu Focal | `14` (default)
CentOS 7 | `1.6.0`
CentOS 7 | `1.7.0`
CentOS 7 | `1.8.0`
CentOS 7 | `11` (default)
CentOS 8 | `1.8.0`
CentOS 8 | `11` (default)

Other OpenJDK implementations out of GNU/Linux distributions streams are not officially supported, but it's easy use this role too adding extra repositories (see vars/ in AdoptOpenJDK and Corretto directories).
## Testing

```sh
$ pipenv sync
$ DOCKER_IMAGE_BASE=(debian:stretch-slim|debian:buster-slim|debian_bullseye-slim|amd64/ubuntu:xenial|amd64/ubuntu:bionic|amd64/ubuntu:focal|centos:7|centos:8) JDK_VENDOR=(`java_jdk_version` openjdk|adoptopenjdk|corretto) JDK_MAJOR=(`java_open_jdk_version_major` see [.travis.yml](.travis.yml) file to check supported versions) JDK_VERSION=(`java_open_jdk_version` see [.travis.yml](.travis.yml) file to check supported versions) pipenv run molecule test
```
**Note:** JDK_VENDOR is an optional parameter, if not defined this role will use openjdk.
**Note:** JDK_VERSION is an optional parameter, if not defined this role will install the latest available package for the selected Java major release.
**Note:** debian9 (Debian Stretch) will be used as default linux distro if none is provided.

See [molecule directory](https://github.com/idealista/java_role/tree/master/molecule) to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-4.4.0-green.svg)
![Molecule](https://img.shields.io/badge/molecule-3.4.0-green.svg)
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
