FROM geerlingguy/docker-debian9-ansible

# This is to override Testinfra issue with Debian 9 Docker image
RUN touch /tmp/systemd
RUN ln -s /tmp/systemd /sbin/init

RUN ansible-galaxy install idealista.java-role
COPY playbook.yml /home/playbook.yml
RUN ansible-playbook /home/playbook.yml
