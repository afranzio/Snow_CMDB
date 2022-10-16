import requests
import pandas as pd
import json


class cmdb_requestor:
    def __init__(self):
        self.url = "https://dev***.service-now.com"
        self.user = '****'
        self.pwd = '****'
        self.headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    def cmdb_get(self):
        tableurl = self.url + '/api/now/table/cmdb/instance'
        filters = '?sysparm_query=active=true&sysparm_display_value=true'
        url = tableurl + filters
        # Set the request parameters
        response=requests.get(url, auth=(self.user, self.pwd), headers=self.headers)
        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
            exit()
        else:
            json_data=response.json()['result']
            cmdb_items=[]
            for each in json_data:
                cmdb_items.append(each)
            data=json.loads(json.dumps(cmdb_items))
            df=pd.json_normalize(data)
            df.to_excel('cmdb.xlsx', index=False)
            print("File Created Successfully")
    
    def cmdb_update(self, record_id, payload):
        url = self.url + '/api/now/cmdb/instance/cmdb_ci_appl/'+str(record_id)
        response = requests.patch(url, auth=(self.user, self.pwd), headers=self.headers, data=json.dumps(payload))
        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
            print("error")
            exit()
        else:
            json_data=response.json()['result']
            cmdb_items=[]
            for each in json_data:
                cmdb_items.append(each)
            data=json.loads(json.dumps(cmdb_items))
            print(data)
    def cmdb_create(self, payload):
        url = self.url + "/api/now/cmdb/instance/cmdb_ci_linux_server"
        response = requests.post(url, auth=(self.user, self.pwd), headers=self.headers, data=json.dumps(payload))
        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:', response.content)
            print("error")
            exit()
        else:
            json_data=response.json()['result']
            cmdb_items=[]
            for each in json_data:
                cmdb_items.append(each)
            data=json.loads(json.dumps(cmdb_items))
            print(data)
