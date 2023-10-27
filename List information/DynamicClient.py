from kubernetes import client, config, dynamic
from kubernetes.client import api_client


 # Creating a dynamic client
client1 = dynamic.DynamicClient(
    api_client.ApiClient(configuration=config.load_kube_config())
)

api = client1.resources.get(api_version="apps/v1", kind="Deployment")
#pod apiVersion: v1

deployment_created = api.get(name="nginx-deployment", namespace="default")
#for i in ret.items:
#    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
print("%s" % (deployment_created))
