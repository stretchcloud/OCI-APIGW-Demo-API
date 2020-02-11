# OCI List Instances API


This instruction is to show, how to run the developed List Instances API in either inside a Docker Container or inside a Kubernetes Cluster and then use Oracle Cloud Infrastructure API Gateway to expose it.

This is split in four buckets. Firstly we will see how to build the Docker container to generate the List of Instances, export it to a CSV file & upload it to Object Storage Bucket. Secondly, we will build a Docker Container for the actual Python Flask API and push it to a Docker repository. Third, we will deploy it your OKE Cluster and at the end we will expose it through OCI API Gateway.

We will use OCI Cloud Shell to build everything off, so there is no need to have any intervention on your local machine.

  

### 1. Clone the repository, build & run the Docker Container



Login to your Cloud Shell Console and clone this repository

```bash
$ git clone https://github.com/stretchcloud/OCI-APIGW-Demo-API
$ cd OCI-APIGW-Demo-API/ListInstances
```

You need to edit the config file according to your OCI credentials and also upload the Private Key in PEM format. These files are already in the directory. Just edit and paste your content. If you are unsure, then follow this [link](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm) to get your Keys in there. While editing the config file leave the ***key_file*** parameter as it is in the file.

```bash
Run this to build the Docker container, push it to a repository and run the container to generate & upload the CSV file for the Instances.

$ docker build -t listinstances:latest .
$ docker tag listinstances:latest <docker-hub-handle>/listinstances:latest
$ docker login
$ docker push <docker-hub-handle>/listinstances:latest
$ docker run --name listinstancesapp <docker-hub-handle>/listinstances:latest
```



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



# API

We would like you to implement the below HTTP endpoint.
If you want to, you can expand the capabilities of the API, but please ensure that the following endpoints will work as described below.

| HTTP Verb | Path         | Request Content-Type | Request body | Response Content-Type | Example response body                                        |
| --------- | ------------ | -------------------- | ------------ | --------------------- | ------------------------------------------------------------ |
| GET       | `/instances` | `application/json`   | -            | `application/json`    | `[ { "uuid": "49dc24bd-906d-4497-bcfc-ecc8c309ecfc", survived": true, "passengerClass": 3, "name": "Mr. Owen Harris Braund", "sex": "male", "age": 22, "siblingsOrSpousesAboard": 1, "parentsOrChildrenAboard":0, "fare":7.25}, ... ]` |



