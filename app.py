from flask import Flask
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from time import sleep 

# You can generate a Token from the "Tokens Tab" in the UI
token = "8TWdi_zdwPcIK-Dzs0ExYth55STiiTSjUmlvGZPWLZq5-_6dsJppWNf5DMJYhjWOgCmozhnWTwmSVg9Pfmb5ZA=="
org = "toor"
bucket = "checking"

client = InfluxDBClient(url="http://152.70.71.114:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

for i in range(1,50):
    point = Point("mem").tag("host", "websites").tag("url","facebook.com").field("used_percent",i+82.00).time(datetime.utcnow(), WritePrecision.NS)
    print(i)
    write_api.write(bucket, org, point)
    sleep(1)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# client = InfluxDBClient(host='152.70.71.114', port=8086, username='root', password='password' )
# client.create_database('flask_web_monitor')
# print(client.get_list_database())
# app.run()