## Setting
```
gcloud config set compute/zone asia-east1-b
gcloud config set compute/region asia-east1
```

## Cluster setting
```
gcloud config set container/cluster project23
gcloud container clusters get-credentials project23 --zone asia-east1 --project nycu-lab-23
```

## Running
```
git clone https://github.com/GinnyCosine/TSMC_NYCU_FINAL_23
cd TSMC_NYCU_FINAL_23/k8s
kubectl apply -f  flask_deployment.yaml
kubectl apply -f  flask_service.yaml
kubectl apply -f  react_deployment.yaml
kubectl apply -f  react_service.yaml
```

