#!/bin/bash
set -e

if [[ -n $1 ]]; then
    DISTRO=$1
else
    echo "No distribution specified"
    exit 1
fi

declare -A distro_hash

distro_hash=( ["debian8"]="Debian-jessie" ["debian9"]="Debian-stretch" ["ubuntu1604"]="Ubuntu-xenial" ["ubuntu1804"]="Ubuntu-bionic" )

OPENJDK_VERSION="$(cat dockerhub/vars/${distro_hash[$DISTRO]}.yml | grep -w java_open_jdk_version_major | cut -d ' ' -f2)"
ORACLEJDK_VERSION="$(cat defaults/main.yml | grep -w java_oracle_jdk_version_major | cut -d ' ' -f2)"

DOCKERHUB_REPO_BASE=idealista/jdk:${DISTRO}

cd dockerhub
docker build . -f $DISTRO/Dockerfile -t ${DOCKERHUB_REPO_BASE}-test
pipenv run ansible-playbook -i inventory -e "image_tag=${DOCKERHUB_REPO_BASE}-test" provision_docker_image.yml

echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin

docker commit docker-test-openjdk ${DOCKERHUB_REPO_BASE}-java${OPENJDK_VERSION}-openjdk
docker push ${DOCKERHUB_REPO_BASE}-java${OPENJDK_VERSION}-openjdk

docker commit docker-test-oraclejdk ${DOCKERHUB_REPO_BASE}-java${ORACLEJDK_VERSION}-oraclejdk
docker push ${DOCKERHUB_REPO_BASE}-java${ORACLEJDK_VERSION}-oraclejdk

docker logout
