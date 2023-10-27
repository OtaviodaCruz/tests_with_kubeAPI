from kubernetes import client, config
import json


# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

api_client = client.ApiClient()
#/api/v1/nodes/
ret_metrics = api_client.call_api(
            '/api/v1/nodes', 'GET',
            auth_settings=['BearerToken'], response_type='json', _preload_content=False)
response = ret_metrics[0].data.decode('utf-8')
print('RESP', json.loads(response)["items"][0]["status"]["allocatable"]["cpu"])

#print(response[0])

