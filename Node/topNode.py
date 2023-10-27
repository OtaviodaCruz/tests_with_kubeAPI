from kubernetes.client.rest import ApiException
from kubernetes import client, config

config.load_kube_config()
try:
    k8s_api = client.CoreV1Api()
    print("Getting k8s nodes...")
    response = k8s_api.list_node()
    
    
#node_list = kube_client.list_node(watch=False, pretty=True, limit=1000)
    if len(response.items) > 0:
        print("NODE\t\t\t\t\t\tSTATUS")
        for node in response.items:
            node_name = node.metadata.name
        #node_status = "Not Ready"   # Unknown, not ready, unhealthy, etc.
        #node_scheduling = node.spec.unschedulable
        #for condition in node.status.conditions:
        #    if condition.type == "Ready" and condition.status:
        #        node_status = "Ready"
        #        break
        #if node_scheduling is None or not node_scheduling:
        #    print(f"{node_name} {node_status}")
        #else:
        #    print(f"{node_name} {node_status},SchedulingDisabled")
#else:
#    print("No nodes available in the cluster")



except ApiException as e:
    print('Found exception in reading the logs')










