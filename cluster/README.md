## Introduction

Utilizing this assignment to play with K8s locally

## Prerequisites

Make sure you have the following:

- docker
- kind or minikube
- kubectl (kubectx, kubens if possible)

*to forward port in kind cluster*
```bash
kubectl port-forward <pod-name> <local-port>:<remote-port>
```

## Let's go
1. **Step 1: create namespace**
   ```bash
   kubectl create ns cel
   ```
2. **Step 2: apply all yaml file**
   ```bash
   kubectl apply -f configmap.yaml
   kubectl apply -f secret.yaml
   kubectl apply -f database.yaml
   kubectl apply -f api.yaml
   kubectl apply -f dashboard.yaml
   ```
wait api restart (databse is insert the data at the beginning so it has a delay time to response api)