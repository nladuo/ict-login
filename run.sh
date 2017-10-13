#!/usr/bin/env bash

while true; do
    ping -c 1 www.baidu.com 1>/dev/null 2>&1
    if [[ $? -ne 0 ]]; then
        echo "retry login"
        python ict_dial.py lichundian01 123456
    fi
    sleep 3600
done
