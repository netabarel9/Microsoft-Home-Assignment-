# Azure AKS Home Assignment
‏
## Description
In this project I created a resource group for the task. 
-In this project I implemented below:
 - Kubernetes Cluser for create services and ingress.
 - Container Registry for push/pull images.
 - DNS zone for connect between the load balencer and ingress(translate the address to the pods)


## AKS with RBAC
- Azure Kubernetes Service (AKS) is a managed container orchestration service provided by Microsoft Azure. It simplifies the deployment, management, and scaling of containerized applications using Kubernetes.
- The purpose of using RBAC in AKS is that you can enforce specific access controls to secure your Kubernetes cluster. RBAC in AKS allows you to define roles and role assignments, granting specific privileges to users, groups, or service administrators.

 For this task I user Azure Kubernetes Service RBAC Admin, AcrPush, AcrPull roles.


```bash
 az aks create -g netRG -n netaKC --enable-aad --enable-azure-rbac
```
## Kubernetes

Kubernetes, is an open-source container orchestration platform for automating the deployment, scaling, and management of containerized applications. 

Main features and concepts  I use of Kubernetes include:
* **Deployments :** Deployments are used to describe the desired state for a set of pods.
* **Container:** Kubernetes automates the deployment, scaling, and operation of application containers. It abstracts away the underlying infrastructure, allowing developers and operators to focus on defining and managing the desired state of their applications.
* **Pods:** The smallest deployable units in Kubernetes are pods. A pod is a group of one or more containers that share the same network namespace, storage, and specifications. Containers within a pod can communicate with each other using localhost.
* **Services:** Kubernetes Services expose a set of pods as a network service. They provide a stable endpoint and allow communication between different parts of an application or between applications within a cluster.
* **Namespaces:** Kubernetes supports the concept of namespaces, which allows you to create isolated environments within a cluster. Namespaces help organize and manage resources. I create ingress namespace.


## Deploynents

I created images for the services and I add readinessProbe and livenessProbe.
* The readinessProbe is a mechanism to determine when a container is ready to accept traffic or requests. It is used by Kubernetes to decide whether a pod should receive network traffic. If the readiness probe fails, the pod is marked as not ready, and it is excluded from the service's load balancer until it becomes ready again.
* The livenessProbe is used to determine if a container is still running and healthy. If the liveness probe fails, Kubernetes restarts the container to attempt to recover it. Liveness probes are useful for detecting and recovering from situations where the application inside the container has entered a state where it cannot recover on its own.


## Services

- Service a: contain python script that use in web framework - flask for creat a routing:
  * /bitcoin_value
  * /average_value
  * /healthz
  * /readyz
 
 - Service b: contain simple html with "Welcome to Azure Container Service (AKS)" message.

## Ingress
![alt text](dash.png)



   
  
  


