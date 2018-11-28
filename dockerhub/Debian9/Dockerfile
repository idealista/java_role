FROM geerlingguy/docker-debian9-ansible
RUN ansible-galaxy install idealista.java-role
COPY playbook.yml /home/playbook.yml
RUN ansible-playbook /home/playbook.yml

LABEL maintainer="idealista <labs@idealista.com>"
