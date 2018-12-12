#!/bin/bash
set -e

echo $DOCKER_USERNAME

if [[ -n $1 ]]; then
    TAG_VERSION=$1
else
    echo "No tag version specified"
    exit 1
fi

if [[ -n $2 ]]; then
    DISTRO=$2
else
    echo "No distribution specified"
    exit 1
fi

cd dockerhub
docker build . -f $DISTRO/Dockerfile -t idealista/java-debian-ansible:${TAG_VERSION}-${DISTRO}
pipenv run ansible-playbook -i inventory -e "image_tag=${TAG_VERSION}-${DISTRO}" provision_docker_image.yml

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

docker logout