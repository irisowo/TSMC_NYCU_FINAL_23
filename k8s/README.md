## Setting
```bash=
gcloud config set compute/zone asia-east1-b
gcloud config set compute/region asia-east1
```

## Cluster setting
```bash=
gcloud config set container/cluster project23
gcloud container clusters get-credentials project23 --zone asia-east1 --project nycu-lab-23
```

## Running web application
```bash=
git clone https://github.com/GinnyCosine/TSMC_NYCU_FINAL_23
cd TSMC_NYCU_FINAL_23/k8s
kubectl apply -f  flask_deployment.yaml
kubectl apply -f  flask_service.yaml
kubectl apply -f  react_deployment.yaml
kubectl apply -f  react_service.yaml
```

## Running cron task of crawler
1. Set up PVC
    ```bash=
    cd TSMC_NYCU_FINAL_23/k8s
    kubectl apply -f  crontab_pod.yaml
    kubectl apply -f  pvc-demo.yaml
    ```
2. Run cronJob
    ```bash=
    cd TSMC_NYCU_FINAL_23/k8s
    # execute crawler/crawler_sample_and_trend.py per minute
    kubectl apply -f  cronjob_crawler.yaml
    ```