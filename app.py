from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from time import sleep
import requests 
import yaml
import json
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content


# You can generate a Token from the "Tokens Tab" in the UI
token = "8TWdi_zdwPcIK-Dzs0ExYth55STiiTSjUmlvGZPWLZq5-_6dsJppWNf5DMJYhjWOgCmozhnWTwmSVg9Pfmb5ZA=="
org = "toor"
bucket = "checking"

client = InfluxDBClient(url="http://127.0.0.1:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

# a_yaml_file = open("./prometheus.yml")
# parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

# x=parsed_yaml_file["a_dictionary"]

# print(x[scrape_configs])

f = open('url.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)

port_dict={}
flag={}

def check_domian(url,val):
    global flag
    try:
        response = requests.get(url)
        if response.status_code==200 and val in response.text:
            flag[url]=0
            return 0
        else:
            return 1
    except Exception as e :
        # print (e)
        if flag[url]==0:
            flag[url]=1
            sg = sendgrid.SendGridAPIClient(api_key='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')
            from_email = Email("18euit009@skcet.ac.in")  # Change to your verified sender
            to_email = To("18eumc071@skcet.ac.in")  # Change to your recipient
            subject = url+" website is down!!!"
            #content = Content(content=url+" website is down kindly check the server",mime_type="plain/text")
            content = "<div>"+url+" website is down kindly check the server"+"</div>"
            mail = Mail(from_email, to_email, subject,html_content=content)
            # Get a JSON-ready representation of the Mail object
            mail_json = mail.get()

            # Send an HTTP POST request to /mail/send
            response = sg.client.mail.send.post(request_body=mail_json)
            print("Sent Mail")
        return 1
    

for i in data:
    flag[i]=0

while True:
    for url in data:
        point = Point("mem").tag("host", "websites").tag("url",url).field("status",check_domian(url,data[url])).time(datetime.utcnow(), WritePrecision.NS)
        # print(i)
        write_api.write(bucket, org, point)
        sleep(1)

