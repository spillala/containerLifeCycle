# Running Container Life Cycle Tests
Testing basic container life cycle operations

project is implemented in Python

## Prerequisites
- Install all Modules required mentioned in requirements.txt file
- Docker should be running on local machine
- Clone repository containerLifeCycle in one of the avilable ways
   Lear more about cloning a repo https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
## How to run tests
- Go to tests folder of the repository - containerLifeCycle/tests
- run containertest.py with test and container to be tested
```
python containertest.py -c <imageName> -t <testName>
```

- For help
```
python containertest.py -h
usage:  container life cycle test [-h] [-i image] -t testname

optional arguments:
  -h, --help            show this help message and exit
  --image , -i          container image name
  --testname {setup,run,teardown}, -t {setup,run,teardown}
                        Enter one of the testname
```
- Examples - Executing tests
```
$python containertest.py -i nginx -t setup
Already logged into container registry
About to execute test: setup
Started downloading image........: nginx
Downloaded image: nginx successful
```

```
$python containertest.py -i nginx -t run
Already logged into container registry
About to execute test: run
container: nginx started
Connecting to container.....http://localhost:8080
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

nginx is running
```
```
$python containertest.py -i nginx -t teardown
Already logged into container registry
About to execute test: teardown
Container: nginx stop successful
Container: nginx remove successful
Image: nginx remove successful
```
# Author Name
Sreekanth

