# 登录计算所网关

适用范围:

* 个人PC长期保持网络连接
* 无GUI的服务器保持网络连接
* openwrt路由器保持网络连接

需要:

* 终端(Terminal)界面
* python3(无需nodejs)


依赖:
```
pip3 install js2py netifaces
```

方法有两种，建议先使用第一种，确认无误后使用第二种保持长期连接:

1. 一次性连接。 `python ict_dial.py <username> <password>`。
2. 保持长期连接。修改run.sh中的username和password，然后执行 `./run.sh`。每隔1小时尝试连接一次。

