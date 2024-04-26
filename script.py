import json
import requests
metadata_url="http://169.254.169.254/metadata/scheduledevents"
header={'Metadata':'true'}
query_params={'api-version':'2020-07-01'}
def get_scheduled_events():
    resp=requests.get(metadata_url,headers=header,params=query_params)
    data=resp.json()
    return data
scheduled_events = get_scheduled_events()
print(scheduled_events)
import os
 
from azure.core.exceptions import HttpResponseError
from azure.identity import DefaultAzureCredential
from azure.monitor.ingestion import LogsIngestionClient
 
endpoint = os.environ['https://migrationtestlinux-cn6u.westeurope-1.ingest.monitor.azure.com']
credential = DefaultAzureCredential()
 
client = LogsIngestionClient(endpoint=endpoint, credential=credential, logging_enable=True)
 
rule_id = os.environ['d61c710d283f42dbba4500b589b609ea']
body = scheduled_events
 
try:
    client.upload(rule_id=rule_id, stream_name=os.environ['LOGS_DCR_STREAM_NAME'], logs=body)
except HttpResponseError as e:
    print(f"Upload failed: {e}")
