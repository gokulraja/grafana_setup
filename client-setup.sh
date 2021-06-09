#!/bin/bash

mkdir /opt/node_exporter

cd /opt/node_exporter

wget https://github.com/prometheus/node_exporter/releases/download/v1.1.2/node_exporter-1.1.2.linux-amd64.tar.gz 

tar xvzf node_exporter-1.1.2.linux-amd64.tar.gz

sudo wget URL --output /etc/systemd/system/node_exporter.service

sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl status node_exporter