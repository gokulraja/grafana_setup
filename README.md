
# Setup for Node-monitoring and Web-monitoring

**Client-side Setup:**

**Download node-exporter:**
    
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

**Download prometheus, grafana ,blackbox-exporter :**

    wget https://github.com/prometheus/prometheus/releases/download/v2.27.1/prometheus-2.27.1.linux-amd64.tar.gz
    wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.19.0/blackbox_exporter-0.19.0.linux-amd64.tar.gz
    wget https://dl.grafana.com/oss/release/grafana_7.5.7_amd64.deb

Requires file wouldbe downloaded.

**Installation for grafana :**

    sudo apt-get install -y adduser libfontconfig1
    sudo dpkg -i grafana_7.5.7_amd64.deb

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


for pasting the data use shift+insert

for saving use ctrl+o 

for exit use ctrl+x

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

grafana runs on 3000 port.



## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

  