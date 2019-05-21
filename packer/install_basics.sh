#!/bin/bash -eux

mkdir -p /usr/share/man/man1

if [ -x "$(command -v apt-get)" ]; then
    apt-get update
    apt-get upgrade -y
    apt-get install -y python ca-certificates
fi

if [ -x "$(command -v yum)" ]; then
    yum update -y
    yum install -y initscripts
fi
