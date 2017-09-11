#Just testing the docker-py SDK

import docker

client = docker.from_env()
clearwaters_containers = []

def create_container():
    c = client.containers.run('registry.gitlab.com/acm-uiuc/sigops/clearwaters-docker/ubuntu-mpich-arm64', detach=True)
    clearwaters_containers.append(c)

for i in range(3):
    create_container(cmd)
    clearwaters_containers[i].logs()
