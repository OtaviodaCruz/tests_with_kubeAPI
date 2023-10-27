from kubernetes.client.rest import ApiException
from kubernetes import client, config

try:
    config.load_kube_config()
    pod_name = "deploy-manage-8485dcd6f7-7lbqh"
    api_instance = client.CoreV1Api()
    api_response = api_instance.read_namespaced_pod(name=pod_name, namespace='default', _preload_content=False)
    print(api_response)
except ApiException as e:
    print('Found exception in reading the logs')
