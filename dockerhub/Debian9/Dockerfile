FROM debian:stretch-slim
ENV DEBIAN_FRONTEND noninteractive 

RUN mkdir -p /usr/share/man/man1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-pip python-dev \    
    && apt-get clean

CMD ["tail", "-f", "/dev/null"]

LABEL maintainer="idealista <labs@idealista.com>"
