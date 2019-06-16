#!/usr/bin/env bash
username=xxx
passwd=xxx

bold=$(tput bold)
normal=$(tput sgr0)

while true; do
    echo "${bold}Connecting... Hold on for a second.${normal}"
    ping -c 1 www.baidu.com 1>/dev/null 2>&1
    if [[ $? -ne 0 ]]; then
        echo "${bold}Retry login as user:${username} and password:${passwd}${normal}"
        python ict_dial.py $username $passwd
    else
      echo "${bold}Connected${normal}"
    fi
    echo "${bold}Wait 1 hour to beat heart."
    echo "......${normal}"
    sleep 3600
done
