# from jira import JIRA 
import requests
import json
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user="root",
    password="Ujala123@",
    database="tickets_data"
)

URL="https://ujalasaini.atlassian.net/rest/api/2/search#"

Second_url="https://ujalasaini.atlassian.net//rest/api/3/issue/TIC-27/transitions"

headers={
    "Accept":"application/json",
    "Content-Type":"application/json"
}

payload=json.dumps({
    
    "transition": {
        "id": "21"
    }
})
respons1=requests.post(Second_url,headers=headers,data=payload ,auth=("ujala21@navgurukul.org","h6W4HG8bof8A3fN0fUxe2508"))
# print(respons1.text)

response=requests.get(URL,headers=headers,auth=("ujala21@navgurukul.org","h6W4HG8bof8A3fN0fUxe2508"))
data=response.json()
issues=data["issues"]
for k in issues:
    d=k["fields"]
    for j in d["status"]:
        pass
    name=(d["status"]["name"])
    # print(name)
    id=(d["status"]["id"])
    # print(id)
    for i in d["reporter"]:
        pass
    displayName=(d["reporter"]["displayName"]) 
    # print(displayName)
    emailAddress=(d["reporter"]["emailAddress"]) 
    # print(emailAddress)
    description=(d["description"])
    # print(description)
    updated=(d["updated"])
    # print(updated)
    

    cur=mydb.cursor()
    insert="INSERT INTO data1(name,Number,Description,displayname,emailAddress,updated) VALUES(%s,%s,%s,%s,%s,%s)"
    data=(name,id,description,displayName,emailAddress,updated)
    cur.execute(insert,data)
    mydb.commit()