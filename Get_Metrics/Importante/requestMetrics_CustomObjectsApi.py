from kubernetes import client, config

config.load_kube_config()
api = client.CustomObjectsApi()

resource = api.list_namespaced_custom_object(group="metrics.k8s.io",version="v1beta1", namespace="default", plural="pods")
#resource = api.get_namespaced_custom_object(group="metrics.k8s.io", version="v1beta1", namespace=namespace, plural="pods", name=podName)
for pod in resource["items"]:
    print(pod['containers'], "\n")
    
print(resource)

