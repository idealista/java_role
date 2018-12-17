FROM debian:stretch-slim
LABEL maintainer="idealista <labs@idealista.com>"
ENV DEBIAN_FRONTEND noninteractive 

RUN mkdir -p /usr/share/man/man1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python-pip python-dev \    
    && apt-get clean

CMD ["sleep", "infinity"]
