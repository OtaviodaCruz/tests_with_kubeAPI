import shlex, subprocess

import json

#from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
#config.load_kube_config()

p = subprocess.getoutput('kubectl get --raw /apis/metrics.k8s.io/v1beta1/namespaces/default/pods')
ret_metrics = json.loads(p)
items = ret_metrics['items']

print(ret_metrics)
