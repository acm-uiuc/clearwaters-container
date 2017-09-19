import lib/clearwaters_docker as cwd

docker_client = cwd.CWDockerClient()

docker_client.create_container('echo hello world')

containers = docker_client.get_all_container_ids()

for c in containers:
    print(docker_client.get_container_logs(c.id))
