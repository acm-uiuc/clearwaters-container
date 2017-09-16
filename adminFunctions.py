import docker
 client = docker.from_env()
 #go to tanishq next time and ask about the conditions for the containers
 def morePrivilage(cmd):
    c = client.containers.cap_add()
    return c.start
def lessPrivilage(cmd):
    c = client.containers.cap_drop()
    return c.stop
def howStrong():
    c = client.containers.cpu_shares()
    return c.id
def runOne(true):
    c = client.containers.detatch()
    return c
def whoami(cmd):
    c = client.containers.devices(cmd)
    return c.id
def limitTheMemore(10):
    c = client.containers.memlimit(10)
    return c
