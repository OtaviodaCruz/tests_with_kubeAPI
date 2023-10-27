from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.AppsV1Api()

name = 'nginx-deployment'
deployment_manifest = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"labels": {"app": "nginx"}, "name": name},
        "spec": {
            "replicas": 1,
            "selector": {"matchLabels": {"app": "nginx"}},
            "template": {
                "metadata": {"labels": {"app": "nginx"}},
                "spec": {
                    "containers": [
                        {
                            "name": "nginx",
                            "image": "nginx:1.14.2",
                            "ports": [{"containerPort": 80}],
                        }
                    ]
                },
            },
        },
    }


namespace = 'default'
body = deployment_manifest


api_response = v1.patch_namespaced_deployment(name, namespace, body)

print("Feito")

