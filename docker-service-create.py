import docker
from docker.types import EndpointSpec

#expose a port
endpoint_spec = EndpointSpec(ports={8257: 80})

#control replicas
from docker.types import ServiceMode
mode = ServiceMode('replicated', replicas=3)

client = docker.from_env()
#Initialize swarm
try:
    client.swarm.init()
except docker.errors.APIError:
    print("Trouble initializing swarm, look up debugging steps.")

#Create a service with a port mapping
try:
    service = client.services.create(
        name='nginx_service',
        image='nginx',
        endpoint_spec=endpoint_spec,
        mode=mode
    )
except docker.errors.APIError:
    print("Trouble creating service, look up debugging steps.")