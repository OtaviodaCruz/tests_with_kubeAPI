from kubernetes import client, config
import json


# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

api_client = client.ApiClient()
ret_metrics = api_client.call_api(
            '/apis/metrics.k8s.io/v1beta1/namespaces/' + 'ndn' + '/pods', 'GET',
            auth_settings=['BearerToken'], response_type='json', _preload_content=False)
response = ret_metrics[0].data.decode('utf-8')
#print('RESP', json.loads(response))

print(response)
