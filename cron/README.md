## cron
* Goal
    * Run cron task in another way (that is, using crontab instead of cronJob)
* What does the files under this directory do?
    * After applying crontab_pod.yaml, trend.py and crontab will be executed every day on crawler-pod
*  Note
    * cronjob_crawler.yaml applies deployment method, while crontab applied on a pod on which PVC is mounted.