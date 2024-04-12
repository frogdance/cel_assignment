kubectl create ns cel
kubens cel
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml
kubectl apply -f database.yaml
kubectl apply -f api.yaml
kubectl apply -f dashboard.yaml