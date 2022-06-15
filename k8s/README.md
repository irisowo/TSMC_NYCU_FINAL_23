## Running web application
```bash=
git clone https://github.com/GinnyCosine/TSMC_NYCU_FINAL_23
cd TSMC_NYCU_FINAL_23/k8s
kubectl apply -f  flask.yaml
kubectl apply -f  react.yaml
```

## Running crawler cronjob
1. Set up NFS and PVC
    ```bash=
    cd TSMC_NYCU_FINAL_23/k8s/nfs
    kubectl apply -f nfs.yaml
    ```

2. Set up base pod to access PVC & Run cronJob
    ```bash=
    cd TSMC_NYCU_FINAL_23/k8s/nfs
    kubectl apply -f nfs-pod.yaml
    ```

## Another way to run crawler cronjob
* Goal
    * Set up PVC
    * assign a base pod
    * assign cronjob pods on the same node with base pod to acces rwo PVC
* ```bash=
  cd TSMC_NYCU_FINAL_23/k8s
  kubectl apply -f pvc-demo.yaml
  kubectl apply -f crontab_pod.yaml
  kubectl apply -f cronjob_nodeSelector.yaml
   ```

## Copy file from nfs-pod to flask-app pod
* ```bash=
   cd TSMC_NYCU_FINAL_23/k8s   
   ./cpDataToFlask.sh
   ```