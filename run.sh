#!/usr/bin/env bash
username=xxx
passwd=xxx

while true; do
    ping -c 1 www.baidu.com 1>/dev/null 2>&1
    if [[ $? -ne 0 ]]; then
        echo "Retry login as user:$username and password:$passwd"
        python ict_dial.py $username $passwd
    else
      echo "Connected"
    fi
    echo "Wait 1 hour to beat heart."
    echo "......"
    sleep 3600
done
