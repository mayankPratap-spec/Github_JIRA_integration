from flask import Flask,request,jsonify
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route("/createJIRA",methods = ['POST'])
def CreateJira():
   
    url = "https://mayankpratap.atlassian.net/rest/api/3/issue"

    API_Token = "" #replace with your token from JIRA

    auth = HTTPBasicAuth("mayankpratap578@gmail.com", API_Token)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
    
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "Mayank's JIRA ticket",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },

        "issuetype": {
        "id": "10001"
        },
    
        "project": {
        "key": "MAYAN"
        },
        "summary": "Mayank Pratap's first JIRA ticket",
    

    } })

    webhook = request.json
    response = None
    if webhook['comment'].get('body') == "/jira":
        response = requests.request("POST", url, data=payload, headers=headers, auth=auth)
        return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
    else:
        print('Jira issue will be created if comment includes /jira')
        return "No action taken for this comment", 200
    

app.run('0.0.0.0',port=5000)
