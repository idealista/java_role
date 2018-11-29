FROM geerlingguy/docker-ubuntu1604-ansible
RUN ansible-galaxy install idealista.java-role
COPY playbook.yml /home/playbook.yml
RUN ansible-playbook /home/playbook.yml

LABEL maintainer="idealista <labs@idealista.com>"
