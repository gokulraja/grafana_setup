#!/bin/bash

sudo mkdir /opt/node_exporter

wget https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-amd64.tar.gz -O /opt/node_exporter

sudo tar xvzf node_exporter-1.1.2.linux-amd64.tar.gz

sudo wget https://raw.githubusercontent.com/manofsteel0007/grafana_setup/main/node_exporter.service -O /etc/systemd/system/

subnet=$(ip -o -f inet addr show | awk '/scope global/ {print $4}')

sudo ufw allow from $subnet to any port 9100

sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl status node_exporter