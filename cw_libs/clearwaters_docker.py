#Just testing the docker-py SDK
import docker


class CWDockerClient:
    client = None
    
    def __init__(self):
        self.client = docker.from_env()
        self.client.version = 'auto'
        
    def create_container(self, cmd):
        c = self.client.containers.run('registry.gitlab.com/acm-uiuc/sigops/clearwaters-docker/ubuntu-mpich-arm64', cmd, detach=True)
        return c.id

    def get_container_logs(self, cid):
        c = self.client.containers.get(cid)
        return c.logs()

    def get_all_container_ids(self):
        return self.client.containers.list()
    
    def stop_container(self, cid):
        c = self.client.containers.get(cid)
        c.stop()

    def start_container(self, cid):
        c = self.client.containers.get(cid)
        c.start()
    
    def start_all_containers(self):
        for c in self.client.containers.list():
            c.start()
        
    def stop_all_containers(self):    
        for c in self.client.containers.list():
            c.stop()

    def run_cmd(self, cid, cmd):
        c = self.client.containers.get(cid)
        print(c.exec_run(cmd))
    
