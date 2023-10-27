from kubernetes.client.rest import ApiException
from kubernetes import client, config

config.load_kube_config()
pod_name = "ndn-microservice-content-store"
try:
    api_instance = client.CoreV1Api()
    api_response = api_instance.read_namespaced_pod(name=pod_name, namespace='ndn')
    print(api_response)
    print("-------------------------------")
    print(api_response.status.pod_ip)
    
except ApiException as e:
    print('Found exception in reading the logs')
