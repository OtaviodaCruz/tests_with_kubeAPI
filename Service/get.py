from kubernetes.client.rest import ApiException
from kubernetes import client, config

config.load_kube_config()
svc_name = "a"
try:
    api_instance = client.CoreV1Api()
    api_response = api_instance.read_namespaced_service(name=svc_name, namespace='default')
    print(api_response)
    print("-------------------------------")
    print(api_response.spec.cluster_ip)
    
except ApiException as e:
    print('Found exception in reading the logs')
