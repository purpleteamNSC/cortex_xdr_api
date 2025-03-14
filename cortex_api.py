import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key_id = os.getenv("API_Key_ID")
api_key = os.getenv("API_Key")
fqdn = os.getenv("Cortex_XDR_FQDN")




def teste(api_key_id, api_key):
    headers = {"x-xdr-auth-id": str(api_key_id), "Authorization": api_key}
    parameters = {}
    res = requests.post(
        url=f"https://{fqdn}/public_api/v1/incidents/get_incidents",
        headers=headers,
        json=parameters,
    )
    return res

print(teste(api_key_id, api_key).json())