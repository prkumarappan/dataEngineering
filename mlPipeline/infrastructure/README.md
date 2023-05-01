# Provision infrastructure
This folder containts code to provision infrastructure in Google Cloud Platform using Terraform. 

## Folder Structure
+ setUpEnvironment: this folder contains the code to set up basic infrastructure in Google Cloud Platform. This includes creating a bucket, moving the machine learning model to provisioned bucket and enabling necessary APIs. This folder is a standalone terraform project.
+ development: this folder contains the code to provision the necessary infrastructure to deploy and serve the ternsorflow model in google cloud platform. This project includes creating a Kubernetes cluster, deploying the model as a service and exposing the service to the internet. This is the root folder for the terraform project that also includes modules folder.
+ modules: this folder contains code to provision VPC, subnet and Google Kubernetes Engine cluster. 
+ tf-serving: this folder contains code to deploy the tensorflow model as a service in Google Kubernetes Engine cluster. 
+ tf-serving-test: this folder contains code to test the tensorflow model deployed as a service in Google Kubernetes Engine cluster.  

## Debug kubenetes cluster
+ Run `kubectl get services`
+ Run `kubectl get svc fashion`
+ Run `kubectl get pods -l app=fashion`
+ Run `kubectl describe pod <POD_NAME>`

## Run test model prediction
1. [Finish until step 19 in Project Setup](../README.md)
2. Manually upload the folder tf-serving-test/00000123 to the bucket created in [Project Setup](../README.md)
3. Update the bucket name in tf-serving-test/configmap.yaml
4. Run 
```
gcloud container clusters get-credentials infrastructure-as-code-385010-gke --zone us-central1-c && \
kubectl apply -f tf-serving-test/configmap.yaml && \
kubectl apply -f tf-serving-test/deployment.yaml && \
kubectl autoscale deployment half-plus-two --cpu-percent=60 --min=1 --max=2 && \
kubectl apply -f tf-serving-test/services.yaml
```
1. Run `kubectl get svc half-plus-two`
2. Copy External-IP 
3. Replace External-IP and Run `curl -d '{"instances": [1.0, 2.0, 5.0]}' \
    -X POST http://External-IP:8501/v1/models/half-plus-two:predict`
