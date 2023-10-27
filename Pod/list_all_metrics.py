from kubernetes.config import load_kube_config                                  
from kubernetes.client import CustomObjectsApi                                  
load_kube_config()                                                              
cust = CustomObjectsApi()                                                       
a = cust.list_cluster_custom_object('metrics.k8s.io', 'v1beta1', 'nodes') # All node metrics

b = cust.list_cluster_custom_object('metrics.k8s.io', 'v1beta1', 'pods') # All Pod Metrics
print(b)
c = cust.list_namespaced_custom_object('metrics.k8s.io', 'v1beta1', 'default', 'pods') # Just pod metrics for the default namespace

