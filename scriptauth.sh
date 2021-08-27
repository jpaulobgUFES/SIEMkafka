
#!/bin/bash

echo "Input the suspicious user:"
read user
export user
grep -i "user $user" /var/log/auth.log  > logauth
if  [ $? == 0 ] 
then
 echo "connecting to the server to send alert..."
 python3 producer1.py
else
 echo 
 echo "User not found"
fi
