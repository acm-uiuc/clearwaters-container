import docker
client = docker.from_env()
#go to tanishq next time and ask about the conditions for the containers
def morePrivilage(cmd):
    c = client.containers.cap_add()
    return c.id

