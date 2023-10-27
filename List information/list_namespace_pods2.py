from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
field_selector = 'metadata.namespace==default'
ret = v1.read_namespaced_pod(name="deploy-manage-dfdc99c7f-26xcr", namespace="default")
print(ret)

#print(ret.spec.containers[0].resources.limits.get('cpu'))
