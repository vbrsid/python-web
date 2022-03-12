# Build, Store and Deploy micro-services to a Kubernetes Cluster


## Pre-requsites:
1. Kubernetes Cluster where the micro-services can be deployed
2. An ansible-controller machine with ansible version 2.12+, where micro-service images are built and pushed to dockerhub account
3. A dockerhub.com account
4. Login into docker account from ansible-controller
5. Install ‘ansible-galaxy collection install community.docker’ on ansible-controller
6. Install ‘ansible-galaxy collection install community.kubernetes’ on ansible-controller


## Code:
The app consists of two micro-services built using Python. The code for these two micro-services is available in ‘micro-service-A’ and ‘micro-service-B’ directories, along with ‘Dockerfile’ and deployment / service YAMLs for each of them.


## Build & Store

To build docker images out of both the micro-services:

```
docker login -u <DOCKER_HUB_USERNAME> 		# and provide the password
```

Open build-store-images.yml and replace <docker-user-name> with your user docker hub account name.


```
cd deploy-on-k8s
ansible-playbook build-store-images.yml
```


## Deploy:

To deploy the docker images into a kubernetes cluster:

```
cd deploy-on-k8s
ansible-playbook deploy-pods-k8s.yml
```


## All-in-one:

To build, store (in dockerhub account) and deploy images into a kubernetes cluster - all in one go:



```
cd deploy-on-k8s
ansible-playbook all-in-one.yml
```
