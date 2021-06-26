
# Setup for Node-monitoring and Web-monitoring

**Create a new user, switch to the new user and move to the user path**
    
    sudo adduser monitoring
    sudo usermod -aG sudo monitoring
    su monitoring

**Client-side Setup:**

**Single installation file for client side**

    wget https://raw.githubusercontent.com/manofsteel0007/grafana_setup/main/client-setup.sh
    chmod +x client-setup.sh
    ./client-setup.sh

**OR Download node-exporter:**
    
    wget https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-amd64.tar.gz

Node exporter will be downloaded

**Expand node-exporter:**

    tar xvzf node_exporter-1.1.2.linux-amd64.tar.gz

**Run node_exporter:**

move inside the folder and run node_exporter

    cd node_exporter-1.1.2.linux-amd64
    ./node_exporter

node_exporter run on 9100 port and expose 9100 port.

**Server-side Setup:**

**Single installation file for server side**

    wget https://raw.githubusercontent.com/manofsteel0007/grafana_setup/main/server-setup.sh
    chmod +x server-setup.sh
    ./server-setup.sh

**Install influxdb2 for ubuntu amd64**

    sudo mkdir /opt/influxdb
    sudo wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.0.7-arm64.deb -O /opt/influxdb/influxdb2-2.0.7-arm64.deb
    sudo dpkg -i /opt/influxdb/influxdb2-2.0.7-arm64.deb

for adding a new node, open prometheus.yml 

inside job_name: node 

    - targets:
      - http://example:9100
      #add here

pasting your ip address of the client instead of 'example'.

for adding a web target, open prometheus.yml

inside job_name: blackbox and job_name: website-monitoring-icmp 

    - targets:
      - http://example.com
      #add here

paste the target url install 'http://example.com'

**OR Download prometheus, grafana ,blackbox-exporter :**

    wget https://github.com/prometheus/prometheus/releases/download/v2.27.1/prometheus-2.27.1.linux-amd64.tar.gz
    wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.19.0/blackbox_exporter-0.19.0.linux-amd64.tar.gz
    wget https://dl.grafana.com/oss/release/grafana_8.0.3_amd64.deb

Requires file would be downloaded.

**Installation for grafana :**

    sudo apt-get install -y adduser libfontconfig1
    sudo dpkg -i grafana_8.0.3_amd64.deb

grafana will be installed as service.

**Run grafana :**

    sudo systemctl daemon-reload
    sudo systemctl start grafana-server
    sudo systemctl status grafana-server

Grafana run on 3000 port and expose 3000 port.

**Expand Prometheus and blackbox_exporter :**

    tar xvzf prometheus-2.27.1.linux-amd64.tar.gz
    tar xvzf blackbox_exporter-0.19.0.linux-amd64.tar.gz

**Add blackbox as a service:**

Create a file blackbox.service

    sudo nano /etc/systemd/system/blackbox.service

place the data from blackbox.service (github-repo)

*check the user and location of the blackbox_exporter file and save the file.  

**Edit blackbox.yml file and start blackbox:**

    sudo nano blackbox.yml

replace the data from blackbox.yml (blackbox_exporter directory) with the data from blackbox.yml (github-repo)

    sudo systemctl daemon-reload
    sudo systemctl start blackbox.service
    sudo systemctl status blackbox.service

the service should be active now.

blackbox runs on 9115 port.

**Edit prometheus.yml file:**

    sudo nano prometheus.yml

replace the data from prometheus.yml (prometheus directory) with the data from prometheus.yml (github-repo)

for adding a new node, open prometheus.yml 

inside job_name: node 

    - targets:
      - http://example:9100
      #add here

pasting your ip address of the client instead of 'example'.

for adding a web target, open prometheus.yml

inside job_name: blackbox and job_name: website-monitoring-icmp 

    - targets:
      - http://example.com
      #add here

paste the target url install 'http://example.com'

**Grafana Setup**

setting up smtp 

    sudo service grafana-server stop

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/0.png)

    sudo service grafana-server start

grafana runs on 3000 port.

for custom overall Node_monitoring import the grafana_dashboard.json file

**influxdb setup**

influxdb runs on 8086 port.

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/10.png)

after signing in data->token->root's token->token

copy the token and paste inside the app.py

## Screenshots

http://localhost:8086

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/1.png)

http://localhost:3000

user-name: admin and password: admin

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/1.png)

 set new password

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/2.png)

 add a data source

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/3.png)

 click prometheus
 
![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/4.png)

 enter url as shown
 
![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/5.jpeg)
 
 import dashboard

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/9.png)

 for web-monitoring the code is 13041 and for node-monitoring code is 13978
  
![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/6.png)

 select prometheus data-source

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/7.png)

 for node-exporter

![App Screenshot](https://github.com/manofsteel0007/grafana_setup/raw/main/images/8.png)
