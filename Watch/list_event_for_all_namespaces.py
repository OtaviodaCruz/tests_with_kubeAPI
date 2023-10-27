# get ADDED/MODIFIED/DELETED events for the v1 Event objects.

from kubernetes import client, config, watch

config.load_kube_config()
    
core_api = client.CoreV1Api()
watcher = watch.Watch()
stream = watcher.stream(core_api.list_event_for_all_namespaces, timeout_seconds=5)
for raw_event in stream:
    print("Kubernetes Event: %s %s" % (raw_event['type'],raw_event['object'].metadata.name))
