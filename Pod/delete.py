from kubernetes import client, config

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True
   
config.load_kube_config()
custom_api = client.CustomObjectsApi()

resource = custom_api.get_namespaced_custom_object(group="metrics.k8s.io", version="v1beta1", namespace="ndn", plural="pods", name="cs1")

print(resource)
len_containers = range(len(resource["containers"]))
CPU_total = 0.0
memory_total = 0.0

for i in len_containers:
	container_CPU = resource["containers"][i]["usage"]["cpu"]
	container_memory = resource["containers"][i]["usage"]["memory"]
	
	try:
		container_CPU = container_CPU[:-1]
		container_memory = container_memory[:-1]
		
		if not isnumber(container_CPU):
			container_CPU = container_CPU[:-1]
		if not isnumber(container_memory):
			container_memory = container_memory[:-1]
			
		container_CPU = int(container_CPU)
		container_memory = int(container_memory)
		
		CPU_total = CPU_total + container_CPU        
		memory_total = memory_total + container_memory
	except ValueError:
		print("Error during convertion")
		
	except TypeError:
		print("Error during operation")
		
print("CPU_total", CPU_total)

