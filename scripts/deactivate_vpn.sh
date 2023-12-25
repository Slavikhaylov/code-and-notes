#!/bin/bash

# disconnect client account from server
vpncmd localhost /client /CMD accountdisconnect user

# stop vpn client service
sudo vpnclient stop

# stop ipv4 forwarding
sudo sysctl -w net.ipv4.ip_forward=0
