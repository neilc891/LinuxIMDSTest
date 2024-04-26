import requests
import time
 
metadata_url = "http://169.254.169.254/metadata/scheduledevents"
header = {'Metadata': 'true'}
query_params = {'api-version': '2020-07-01'}
 
def get_scheduled_events():
    resp = requests.get(metadata_url, headers=header, params=query_params)
    data = resp.json()
    return data
 
while True:
    scheduled_events = get_scheduled_events()
    print(scheduled_events)
    time.sleep(10)  # Delay for 10 seconds
