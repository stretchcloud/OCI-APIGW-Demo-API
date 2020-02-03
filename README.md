# APIApp


This instruction is to show, how to run the developed API App in either inside a Docker Container or inside a Kubernetes Cluster.
  
This is split in two buckets. Firstly we will see how to deploy it in Docker Container and the second part will focus on Kubernetes.

  

### 1. Fork this repository & Deploy the build the Docker Container

First of all, let's clone this repository

`git clone https://gitlab.com/stretchcloud/API-Exercise`

`cd API-Exercise`

`docker build -t apiapp:latest .`

Your Docker Image is ready. You can either run it in daemon mode or interactive run.

`docker run --name apiapp -p 5000:5000 apiapp:latest` => Run this if you want to debug the output.

`docker run --name apiapp -d -p 5000:5000 apiapp:latest` => Non interactive, daemon mode.

Use `curl` to test the endpoint

`curl -X GET -H "Content-type: application/json" http://127.0.0.1:5000/people`

`curl -X GET -H "Content-type: application/json" http://127.0.0.1:5000/people/{uuid}`

`curl -X DELETE -H "Content-type: application/json" http://127.0.0.1:5000/people/{uuid}`

`curl -X POST -H "Content-type: application/json" -d '{"survived" : "1", "passengerClass" : "3", "name" : "Sandhya Sarkar", "sex" : "Female", "age" : "104", "siblingsOrSpousesAboard" : "0", "parentsOrChildrenAboard" : "0", "fare" : "40"}' http://127.0.0.1:5000/people/`

`curl -X PUT -H "Content-type: application/json" -d '{"survived" : "1", "passengerClass" : "3", "name" : "Sandhya Sarkar", "sex" : "Female", "age" : "104", "siblingsOrSpousesAboard" : "0", "parentsOrChildrenAboard" : "0", "fare" : "100"}' http://127.0.0.1:5000/people/{uuid}`



### 2. Deploy it to Kubernetes

We have already built the Docker Image and pushed it to Docker Registry. Also, we have supplied the APIApp Deployment and Service YML. Create a deployment and a service and you will be good to go.

`kubectl create -f apiapp-deployment.yml`

`kubectl create -f apiapp-service.yml`

`kubectl get deployments` => Check whether the app has been deployed

`kubectl get service` => Check whether the service has been deployed

`kubectl get pods` => Check whether the POD is up and running 

`kubectl port-forward service/apiapp 5000 5000` => Create the port-forward to access the API

At this point, you can use the same curl option to test the API endpoint.

### Note
Due to time constraint, this application has been packaged inside a single docker container and did not use the best practice of App and DB as separate container/POD and then persist the data with statefulset & a PV & PVC.