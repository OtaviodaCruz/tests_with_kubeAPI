from kubernetes import client, config, watch
from urllib3.exceptions import ProtocolError

config.load_kube_config()
v1 = client.CoreV1Api()
field_selector='involvedObject.name='+'my_pod'
stream = watch.Watch().stream(v1.list_namespaced_event, "default", timeout_seconds=5)
for event in stream:
    print(event['object'].message)
