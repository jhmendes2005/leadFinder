import json

#obtém a KEY da API
def get_api_key():
    with open('../slv0.0.2/data/_security/keys.json', 'r') as f:
        key_dict = json.load(f)

    print(key_dict['api_key'])
    return key_dict['api_key']