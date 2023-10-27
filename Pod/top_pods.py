from kubernetes import client, config

config.load_kube_config()
api = client.CustomObjectsApi()

resource = api.get_namespaced_custom_object("metrics.k8s.io", "v1beta1", "ndn", "pods", "cs1")

for pod in resource["containers"]:
    print(pod["usage"]["cpu"], "\n")
    
print(resource)

