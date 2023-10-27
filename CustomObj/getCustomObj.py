from kubernetes import client, config

config.load_kube_config()
api = client.CustomObjectsApi()

resource = api.get_namespaced_custom_object(
group="monitoring.coreos.com",
version="v1",
name="prometheus-grafana",
namespace="default",
plural="servicemonitors")

print("Resource details:")
print(resource)


#resource = api.get_namespaced_custom_object("monitoring.coreos.com", "v1beta1", "default", "servicemonitor", "prometheus-grafana")

#for pod in resource["containers"]:
#    print(pod["usage"]["cpu"], "\n")
    
#print(resource)

