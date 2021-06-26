#!/bin/bash

sudo mkdir /opt/grafana

sudo wget https://dl.grafana.com/oss/release/grafana_8.0.3_amd64.deb -O /opt/grafana/grafana_8.0.3_amd64.deb

sudo apt-get install -y adduser libfontconfig1

sudo dpkg -i /opt/grafana/grafana_8.0.3_amd64.deb

sudo mkdir /opt/prometheus

sudo wget https://github.com/prometheus/prometheus/releases/download/v2.27.1/prometheus-2.27.1.linux-amd64.tar.gz -O /opt/prometheus/prometheus-2.27.1.linux-amd64.tar.gz

sudo tar xvzf /opt/prometheus/prometheus-2.27.1.linux-amd64.tar.gz -C /opt/prometheus/

sudo mkdir /opt/blackbox

sudo wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.19.0/blackbox_exporter-0.19.0.linux-amd64.tar.gz -O /opt/blackbox/blackbox_exporter-0.19.0.linux-amd64.tar.gz

sudo tar xvzf /opt/blackbox/blackbox_exporter-0.19.0.linux-amd64.tar.gz -C /opt/blackbox/

sudo rm /opt/blackbox/blackbox_exporter-0.19.0.linux-amd64/blackbox.yml

sudo wget https://raw.githubusercontent.com/manofsteel0007/grafana_setup/main/blackbox.yml -O /opt/blackbox/blackbox_exporter-0.19.0.linux-amd64/blackbox.yml

sudo rm /opt/prometheus/prometheus-2.27.1.linux-amd64/prometheus.yml

sudo wget https://raw.githubusercontent.com/manofsteel0007/grafana_setup/main/prometheus.yml -O /opt/prometheus/prometheus-2.27.1.linux-amd64/prometheus.yml

sudo wget https://raw.githubusercontent.com/manofsteel0007/grafana_setup/main/blackbox.service -O /etc/systemd/system/blackbox.service

sudo wget https://raw.githubusercontent.com/manofsteel0007/grafana_setup/main/prometheus.service -O /etc/systemd/system/prometheus.service

sudo rm /opt/prometheus/prometheus-2.27.1.linux-amd64.tar.gz

sudo rm /opt/blackbox/blackbox_exporter-0.19.0.linux-amd64.tar.gz

sudo systemctl daemon-reload

sudo service prometheus start

sudo service blackbox start

sudo systemctl start grafana-server
