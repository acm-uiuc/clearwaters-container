#Just testing the docker-py SDK
import docker

client = docker.from_env()

def create_container(cmd):
    c = client.containers.run('registry.gitlab.com/acm-uiuc/sigops/clearwaters-docker/ubuntu-mpich-arm64', cmd, detach=True)
    return c.id
    
def get_container_logs(cid):
    c = client.containers.get(cid)
    return c.logs()

def stop_container(cid):
    c = client.containers.get(cid)
    c.stop()

def start_container(cid):
    c = client.containers.get(cid)
    c.start()
    
def start_all_containers():
    for c in client.containers.list():
        c.start()
        
def stop_all_containers():    
    for c in client.containers.list():
        c.stop()

def run_cmd(cid, cmd):
    c = client.containers.get(cid)
    print(c.exec_run(cmd))

    
#print('create 3 new docker containers')
#for i in range(3):
#    cmd = 'tail -f /dev/null'
#    id = create_container(cmd)
#    print('New Container_ID= ' + id)


#print('Testing the run command')
#for c in client.containers.list():
#    run_cmd(c.id, 'echo hello world from '+c.id)

stop_all_containers()
