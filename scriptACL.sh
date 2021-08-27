#!/bin/bash
echo "Input the suspicious MAC address:"
read MAC
export MAC
iptables -I INPUT -m mac --mac-source $MAC -j LOG
grep -i $MAC /var/log/syslog > logempower
if [ $? == 0 ] 
then
 echo "Connecting to the server to send alert..."
 python3 ./producer.py
else
 echo
 echo "MAC Address not found in the log file"
fi

