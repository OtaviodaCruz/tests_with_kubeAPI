from kubernetes.client.rest import ApiException
from kubernetes import client, config

config.load_kube_config()
try:
    k8s_api = client.CoreV1Api()
    print("Getting k8s nodes...")
    response = k8s_api.list_node()
    
    
    print(response)
except ApiException as e:
    print('Found exception in reading the logs')

