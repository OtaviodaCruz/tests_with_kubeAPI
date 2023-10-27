from kubernetes import client, config
import time

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

max_attempt = 2

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True
    
pod_default_attrs = {
    "cs": {
    "container_name": "microservice-content-store",
    "container_image": "otaviocruz/ndn_microservice-content_store:1.0",
    "template_labels": {"app": "microservice-content-store"},
    "pod_name": "content-store-deploy",
    "limits":{"cpu": "500m", "memory": "300M"} # 500m -> 0.5 (50%) of 1 core CPU. 300M -> 300 megabytes
    },
    "nr": {
    "container_name": "microservice-name-router",
    "container_image": "otaviocruz/ndn_microservice-name_router:1.0",
    "template_labels": {"app": "microservice-name-router"},
    "pod_name": "name-router-deploy",
    "limits":{"cpu": "500m", "memory": "300M"} # 500m -> 0.5 (50%) of 1 core CPU. 300M -> 300 megabytes
    },
    "br": {
    "container_name": "microservice-backward-router",
    "container_image": "otaviocruz/ndn_microservice-backward_router:1.0",
    "template_labels": {"app": "microservice-backward-router"},
    "pod_name": "name-backward-deploy",
    "limits":{"cpu": "500m", "memory": "300M"} # 500m -> 0.5 (50%) of 1 core CPU. 300M -> 300 megabytes
    }
}

def create_pod_object(tupla_pod, pod_name):
 
    for attempt in range(max_attempt + 1):    
        try:
            # Configureate Pod template container
            container = client.V1Container(
                name=tupla_pod["container_name"],
                image=tupla_pod["container_image"],
                #ports=[client.V1ContainerPort(container_port=80)],
                resources=client.V1ResourceRequirements(
                    #requests={"cpu": "100m", "memory": "200Mi"},
                    limits=tupla_pod["limits"],
                ),
            )
            container1 = client.V1Container(
                name="aa",
                image=tupla_pod["container_image"],
                #ports=[client.V1ContainerPort(container_port=80)],
                resources=client.V1ResourceRequirements(
                    #requests={"cpu": "100m", "memory": "200Mi"},
                    limits={"cpu": "100m", "memory": "200Mi"},
                ),
            )

            # Create the specification of deployment
            spec = client.V1PodSpec(containers=[container, container1])

            # Instantiate the pod object
            pod_obj = client.V1Pod(
                api_version="v1",
                kind="Pod",
                metadata=client.V1ObjectMeta(name=pod_name),
                spec=spec,
            )
            return pod_obj
        
        except ApiException as e:
            if attempt < max_attempt:
                print(bcolors.FAIL + "[Error] create pod object" + " (", e.status, ")" + " ", e.reason, ". Try again" + bcolors.ENDC)
                logger.error("[Error] create pod object" + " (" + e.status + ")" + " " + e.reason + ". Try again")
            else: 
                print(bcolors.FAIL + "[Critical Error] create pod object" + " (", e.status, ")" + " ", e.reason, bcolors.ENDC)
                return False


def create_pod(api, pod_obj, namespace="ndn", field_manager="ndn_manager"):
    for attempt in range(max_attempt + 1):    
        try:
            # Create deployment
            resp = api.create_namespaced_pod(
                body=pod_obj, 
                namespace=namespace, 
                field_manager=field_manager,
            )
            
            print(resp)
            print("aqui")
            
            total_limits_cpu = 0
            total_limits_memory = 0
            for i in pod_obj.spec.containers:
                limits_cpu = i.resources.limits["cpu"]
                limits_cpu = limits_cpu[:-1]
                if not isnumber(limits_cpu):
                    limits_cpu = limits_cpu[:-1]
                print(limits_cpu)
                total_limits_cpu += int(limits_cpu)
                
                limits_memory = i.resources.limits["memory"]
                limits_memory = limits_memory[:-1]
                if not isnumber(limits_memory):
                    limits_memory = limits_memory[:-1]
                print(limits_memory)
                total_limits_memory += int(limits_memory)

            while True:            
                api_response = api.read_namespaced_pod(name=pod_obj.metadata.name, namespace=namespace)           
                if api_response.status.phase != 'Pending':                
                    break            
                time.sleep(1)
            return True

        except ApiException as e:
            if attempt < max_attempt:
                print(bcolors.FAIL + "[Error] create Pod" + " (", e.status, ")" + " ", e.reason, ". Try again" + bcolors.ENDC)
            else: 
                print(bcolors.FAIL + "[Critical Error] create Pod" + " (", e.status, ")" + " ", e.reason, ". Try again" + bcolors.ENDC)
                return False
                

v1 = client.CoreV1Api()

pod_obj1 = create_pod_object(pod_default_attrs["cs"], "cs5")

create_pod(v1, pod_obj1, namespace="ndn", field_manager="ndn_manager")
