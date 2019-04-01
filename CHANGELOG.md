# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [4.1.0](https://github.com/idealista/java_role/tree/4.1.0) (2019-02-01)
[Full Changelog](https://github.com/idealista/java_role/compare/4.0.0...4.1.0)

### Added
- *[#92](https://github.com/idealista/java_role/issues/92) Added CentOS support @apolloclark
### Fixed
- *[#94](https://github.com/idealista/java_role/issues/94) Fix Debian 9 OpenJDK package version and Debian 8 repositories problem* @jnogol
- *[#86](https://github.com/idealista/java_role/issues/86) Fixing Docker Hub image badge url* @dortegau

## [Unreleased](https://github.com/idealista/java_role/tree/develop)

## [4.0.0](https://github.com/idealista/java_role/tree/4.0.0) (2019-02-08)
[Full Changelog](https://github.com/idealista/java_role/compare/3.4.3...4.0.0)

### Added
- *[#82](https://github.com/idealista/java_role/issues/82) Adding support to OpenJDK 11 in Debian Stretch* @dortegau
- Testing all supported platforms in Travis @dortegau
### Changed
- *[#80](https://github.com/idealista/java_role/issues/80) Installing OpenJDK headless by default* @dortegau
- Using Packer to deploy images to Docker Hub @dortegau
- Upgrading to molecule 2.19 @dortegau
- Simplifying containers for testing with molecule (without unneeded systemd) @dortegau

## [3.4.3](https://github.com/idealista/java_role/tree/3.4.3) (2019-01-21)
[Full Changelog](https://github.com/idealista/java_role/compare/3.4.2...3.4.3)
### Fixed
- *[#64](https://github.com/idealista/java_role/issues/64) Fix Travis deployment to Docker Hub* @jnogol

## [3.4.2](https://github.com/idealista/java_role/tree/3.4.2) (2019-01-17)
[Full Changelog](https://github.com/idealista/java_role/compare/3.4.1...3.4.2)
### Added
- *[#65](https://github.com/idealista/java_role/issues/65) Add Travis deployment for Ubuntu 18.04 Bionic* @jnogol
### Changed
- *Delete travis_wait in .travis.yml* @jnogol
- *[#56](https://github.com/idealista/java_role/issues/56) Add java version to docker image tag name* @jnogol
- *[#70](https://github.com/idealista/java_role/issues/70) New available Oracle Java versions added. Default Oracle JDK is now 1.8.0_201* @mmolinac

## [3.4.1](https://github.com/idealista/java_role/tree/3.4.1) (2019-01-17)
[Full Changelog](https://github.com/idealista/java_role/compare/3.4.0...3.4.1)
### Fixed
- *[#69](https://github.com/idealista/java_role/issues/69) Undefined variable java_open_jdk_version* @sorobon

## [3.4.0](https://github.com/idealista/java_role/tree/3.4.0) (2019-01-08)
[Full Changelog](https://github.com/idealista/java_role/compare/3.3.0...3.4.0)
### Changed
- *[#57](https://github.com/idealista/java_role/issues/57) Specifying explicitly OpenJDK version* @dortegau
### Added
- *[#52](https://github.com/idealista/java_role/issues/52) Add Support for Ubuntu 18.04 Bionic, Ubuntu 16.04 Xenial. Add Support for OpenJDK 11* @apolloclark

## [3.3.0](https://github.com/idealista/java_role/tree/3.3.0) (2018-12-17)
[Full Changelog](https://github.com/idealista/java_role/compare/3.2.0...3.3.0)
### Changed
- *[#53](https://github.com/idealista/java_role/issues/53) New way to deploy to DockerHub* @jnogol

## [3.2.0](https://github.com/idealista/java_role/tree/3.2.0) (2018-12-05)
[Full Changelog](https://github.com/idealista/java_role/compare/3.1.1...3.2.0)
### Changed
- *[#47](https://github.com/idealista/java_role/issues/47) Avoiding duplicated files to define specific Linux distros in Molecule* @dortegau

## [3.1.1](https://github.com/idealista/java_role/tree/3.1.1) (2018-11-29)
[Full Changelog](https://github.com/idealista/java_role/compare/3.1.0...3.1.1)
### Fixed
- *[#41](https://github.com/idealista/java_role/issues/41) Splitting vars by OS to avoid unnecessary library installation under Debian Stretch and creating a scenario per OS/JDK type pair* @dortegau
- *[#42](https://github.com/idealista/java_role/issues/42) Fixing tests for Debian Jessie in Molecule* @dortegau

## [3.1.0](https://github.com/idealista/java_role/tree/3.1.0) (2018-11-20)
[Full Changelog](https://github.com/idealista/java_role/compare/3.0.2...3.1.0)
### Changed
- *[#37](https://github.com/idealista/java_role/issues/37) Upgrade role (Ansible 2.5.3.x, Molecule 2.0, Pipenv, Goss 0.36.0...)* @dortegau
- *[#36](https://github.com/idealista/java_role/issues/36) Use new apt syntax for installing packages* @sklirg

## [3.0.2](https://github.com/idealista/java_role/tree/3.0.2) (2018-10-18)
[Full Changelog](https://github.com/idealista/java_role/compare/3.0.1...3.0.2)
### Changed
- *Oracle Java 8 update version outdated* @jnogol

## [3.0.1](https://github.com/idealista/java_role/tree/3.0.1) (2018-07-19)
[Full Changelog](https://github.com/idealista/java_role/compare/3.0.0...3.0.1)
### Changed
- *[#31](https://github.com/idealista/java_role/issues/31) update oracle java versions* @eskabetxe

## [3.0.0](https://github.com/idealista/java_role/tree/3.0.0) (2018-05-30)
[Full Changelog](https://github.com/idealista/java_role/compare/2.0.2...3.0.0)
### Changed
- *[#26](https://github.com/idealista/java_role/issues/26) Update imports (deprecation warnings)* @jmonterrubio

## [2.0.2](https://github.com/idealista/java_role/tree/2.0.2)
### Fixed
- *[#21](https://github.com/idealista/java_role/issues/21) Defined Ansible 2.3.x.x as min version* @dortegau
- *[#23](https://github.com/idealista/java_role/issues/23) Oracle Java 8 update version outdated* @jnogol

## [2.0.1](https://github.com/idealista/java_role/tree/2.0.1)
### Fixed
- *[#18](https://github.com/idealista/java_role/issues/18) OracleJDK 8 URL is not working* @jnogol

## [2.0.0](https://github.com/idealista/java_role/tree/2.0.0)
### Added
- *Fixing OracleJDK installation (now without webupd8 PPA)* @dortegau
- *Using OpenJDK as default implementation* @dortegau

## [1.2.0](https://github.com/idealista/java_role/tree/1.2.0)
### Added
- *Enable debian stretch platform* @jmonterrubio

## [1.1.0](https://github.com/idealista/java_role/tree/1.1.0)
### Added
- *Enable openjdk* @jmonterrubio

## [1.0.0](https://github.com/idealista/java_role/tree/1.0.0)
### Added
- *First commit* @agarcia
