#!/bin/sh
#Send IP address to GitHub
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
    date | tee ~/cpsc-334/raspi-ip/ip.md
    hostname -I | tee -a ~/cpsc-334/raspi-ip/ip.md
    git -C ~/cpsc-334/raspi-ip/ commit -am "Updated IP"
    git -C ~/cpsc-334/raspi-ip/ push
fi