# ref: https://github.com/kubernetes-client/python/issues/1059
# https://awstip.com/kubernetes-multiple-watches-using-threads-in-python-c213e67fdaca

from kubernetes import client, config, watch

config.load_kube_config()

api_instance = client.CoreV1Api()

w = watch.Watch()
for event in w.stream(api_instance.list_pod_for_all_namespaces, timeout_seconds=0):
    print("Event: %s %s %s" % (event['type'], event['object'].kind, event['object'].metadata.name))
