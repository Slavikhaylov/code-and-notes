#!/bin/bash

# start vpn service
sudo vpnclient start
sleep 1

# connect to client service, then connect to server, allow time for server
# to wake up
vpncmd localhost /client /CMD remoteenable
vpncmd localhost /client /CMD accountconnect user 
sleep 10

# get vpn server ip
serverip="$(getent hosts vod.splay.uz | cut -d ' ' -f 1)"
echo Server IP is $serverip
sleep 1

# get active hardware adapter name
hwadapter="$(ip route | sed -n '1 p' | cut -d ' ' -f 5)"
echo Adapter name is $hwadapter
sleep 1

# get default gateway of cellphone NIC connection
dgw="$(ip neigh show dev $hwadapter nud reachable | cut -d ' ' -f 1)"
echo Default Gateway is $dgw
sleep 1

# create new route to vpn server via default gateway of active adapter
sudo ip route add $serverip/32 via $dgw dev $hwadapter

# get address assigned to virtual vpn adapter
sudo dhclient vpn_vpn

# set up ip forwarding
sudo sysctl -w net.ipv4.ip_forward=1
