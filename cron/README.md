## cron
- Goal
    - Create a pod for pvc
    - Run cron task in another way (that is, using cron instead of cronJob)
        - We use cron instead since we are in autopilot cluster, which may occasional assign cronjob pods to another node.
        - The default storage class autopilot used is rwo(readwriteonly), so the pvc can't be accessed by multiple nodes.
- What does the files under this directory do?
    - After applying crontab_pod.yaml, trend.py and crontab will be executed every day on crawler-pod
- How to retrieve files
    - ```bash=
      cd TSMC_NYCU_FINAL_23/k8s
      ./cpDataToFlask.sh
      ```
-  Note
    - cronjob_crawler.yaml applies deployment, while crontab applies a pod on which PVC is mounted.