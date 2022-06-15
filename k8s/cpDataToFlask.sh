#!/bin/bash

src="nfs-pod"
for pod in $(kubectl get pod -o name)
do
    if [[ $pod == *"flask-app"* ]]; then
        stripped_pod="${pod:4}"
        printf "==============================\n $stripped_pod \n==============================\n"
        kubectl cp $src:/sample_crawler/history/data.csv ./data.csv
        kubectl cp ./data.csv $stripped_pod:/server/data.csv
    fi
done
