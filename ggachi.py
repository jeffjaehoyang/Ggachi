import requests

def fly(spec):
    if spec['method'] == 'GET':
        response = requests.get(spec['api_endpoint'])
        if response.status_code == spec['expected_response_status_code']:
            return {
                'status': 'ok'
            }