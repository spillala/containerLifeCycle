#!/usr/bin/env python3
"""
Executes container test suite
"""
import argparse
import sys
import docker
sys.path.append('../')
import containerlib
from apptest import testconnection

def setup(image):
    print(f"Started downloading image........: {image}")
    container = containerlib.Containerlifecycle()
    container.imageimport(image)

def run(image, hostname='localhost', port='8080'):
    container = containerlib.Containerlifecycle()
    container.runcontainer(image,port)
    status = testconnection(hostname, port)
    if status == 200:
        print(f"{image} is running")

def teardown(containername):
    container = containerlib.Containerlifecycle()
    container.stopcontainer(containername)
    container.removecontainer(containername)
    container.removeimage(containername)

if __name__ == '__main__':
    #parser = argparse.ArgumentParser(" container life cycle test", usage='%(prog)s [-h] [-i image] -t testname')
    parser = argparse.ArgumentParser(" container life cycle test", usage='%(prog)s [-h] [-i image] -t testname')
    parser.add_argument('--image', '-i', help='container image name', required=True, metavar='')
    parser.add_argument('--testname', '-t', help='Enter one of the testname' , choices=[ 'setup', 'run', 'teardown'], required=True)

    try:
        args = parser.parse_args()
        container = args.image
        testname  = args.testname
    except:
        sys.exit(0)
    try:
        dc = docker.from_env()
    except docker.errors.DockerException as error:
        print("Check for docker service")
        sys.exit(0)

    if dc.ping():
        print("Already logged into container registry")
    else:
        print("please enter username and password")
        username, password = input("Enter username and password for container registry: ").split()
        
        try:
            dc.login(username,password)
        except docker.errors.APIError as error:
            print(f"Login Failed with error : {error}")
            sys.exit(0)
    
    print(f"About to execute test: {testname}")
    eval(testname + "(container)")



    