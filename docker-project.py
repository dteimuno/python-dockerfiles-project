import docker
client = docker.from_env()
#Get containers
docker_containers = client.containers.list()
print(docker_containers)

nginx_container = client.containers.run('nginx',
                                      detach=True, ports={'80/tcp': 8081}, name='nginx8081')

