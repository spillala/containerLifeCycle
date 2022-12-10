import docker
import sys
import random
import string
import re

class Containerlifecycle():
    """
    Container management
    Life cycle management of containers
    """
    def __init__(self):
        try:
            self.docker_client = docker.from_env()
        except docker.errors.DockerException as error:
            print("Check for docker service")
            sys.exit(0)
        
        self.containerPrefix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

    def imageimport(self, imagename):
        try:
            image = self.docker_client.images.pull(imagename)
            print(f"Downloaded image: {imagename} successful")
            return image
        except docker.errors.ImageNotFound as error:
            print(f"Image not found : {imagename} :, failed with: {error}")
        except docker.errors.APIError as error:
            print (f"Check for docker status or docker login, failed with error {error} ")

    def runcontainer(self, imagename, port):
        try:
            images = self.docker_client.images.get(imagename)
            if images:
                container = self.docker_client.containers.run(images, \
                    name=imagename+self.containerPrefix, ports = {'80/tcp': port}, detach=True)
            if container:
                print(f"container: {imagename} started ")
        except (docker.errors.ContainerError, docker.errors.ImageNotFound, docker.errors.APIError) as error:
            print(f"Container start failed with erorr : {error}")
    
    def stopcontainer(self, containername):
        try:
            containers = self.docker_client.containers.list('all')
            for container in containers:
                if re.search(f"^{containername}*", container.name):
                    container.stop()
                    print(f"Container: {containername} stop successful")
        except docker.errors.APIError as error:
            print(f"Stop container failed : {error}, check if it is running")

    def removecontainer(self, containername):
        try:
            containers = self.docker_client.containers.list(all)
            for container in containers:
                if re.search(f"^{containername}*", container.name):
                    container.remove()
                    print(f"Container: {containername} remove successful")
        except docker.errors.APIError as error:
            print(f"Remove container failed : {error}")

    def removeimage(self, imagename):
        try:
            image = self.docker_client.images.get(imagename)
            if image:
                image.remove()
                print(f"Image: {imagename} remove successful")
            else:
                print(f"Image not {imagename} not available")
        except docker.errors.APIError as error:
            print(f"Clean-up image failed : {error}")