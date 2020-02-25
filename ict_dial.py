#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auto login ICT gateway
# Author: Andrew(lichundian@gmail.com)
# Date: 2017.08.31

# modified by: nladuo
# Date: 2020.02.25

import sys
import hashlib
import hmac
import urllib2
from urllib import urlencode
import os
import re
import json
import netifaces
from js_lib import js_lib

# The local server must connect the gateway directly
# without other routers in the middle.
# Get router's ips or a computer's ips
def getips():
    ips = []
    for ifcard in netifaces.interfaces():
        addrs = netifaces.ifaddresses(ifcard)
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                ips.append(addr['addr'])
    return ips


if __name__ == '__main__':
    username = ""
    password = ""
    acid = "1"
    enc_ver = "srun_bx1"
    n_param = "200"
    type_param = "1"

    if len(sys.argv) >= 3:
        username = sys.argv[1]
        password = sys.argv[2]
    else:
        print("Usage: python ict_dial.py username password")
        exit(1)


    for _ip in getips():
        ip = _ip

        try:
            # request token jsonp data
            token_jsonp = urllib2.urlopen("http://gw.ict.ac.cn/cgi-bin/get_challenge?callback=xxx&username=" + username + "&ip=" + ip).read()
            # parse token
            m = re.search("xxx\((.*)\)", token_jsonp)
            if m is None:
                exit()
            token_json = m.group(1)
            token = str(json.loads(token_json)["challenge"])
            # token = "cd64441c10977a0b4ecefd7f1d6add323d8b3e959fef0ef68bca246b4dcb9ac0"
            # print "token:(" + token + ")"

            info_origin_json = '{"username":"%s","password":"%s","ip":"%s","acid":"%s","enc_ver":"%s"}' %(username, password, ip, acid, enc_ver)

            conn_obj = {}
            conn_obj["action"] = "login"
            conn_obj["info"] = "{SRBX1}" + js_lib.base64_encode(js_lib.encap(info_origin_json, token))

            hasher = hmac.new(token)
            hasher.update("")
            pass_md5 = hasher.hexdigest()
            conn_obj["password"] = "{MD5}"+ pass_md5
            hasher = hashlib.sha1()
            hasher.update(token + username + token + pass_md5 + token + acid + token + ip + token + n_param + token + type_param + token + conn_obj["info"])
            conn_obj["chksum"] = hasher.hexdigest()
            conn_obj["n"] = n_param
            conn_obj["type"] = type_param
            conn_obj["ac_id"] = acid
            conn_obj["username"] = username
            conn_obj["ip"] = ip


            # print conn_obj
            conn_url = "http://gw.ict.ac.cn/cgi-bin/srun_portal?callback=xxx&" + urlencode(conn_obj) + "&_=1503984175899"
            conn = urllib2.urlopen(conn_url).read()
            # print conn
        except Exception, e:
            print e
            print ip, "failed"
    status = subprocess.call("ping -c 2 www.baidu.com",shell=True, stdout=FNULL, stderr=FNULL)
    if status == 0:
        print "Connect internet well!!!"
    else:
        print "Login failed"

