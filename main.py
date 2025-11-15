from uptime_kuma_api import UptimeKumaApi, MonitorType

zidian = {
    "ipadd" : [
    {"hostname" : "test1" , "ip" : "172.16.1.1"},
    {"hostname" : "test2" , "ip" : "172.16.1.2"},
    {"hostname" : "test3" , "ip" : "172.16.1.3"},
    {"hostname" : "test4" , "ip" : "172.16.1.4"},
    {"hostname": "test5", "ip": "172.16.1.5"},
    {"hostname": "test6", "ip": "172.16.1.6"},
    {"hostname": "test7", "ip": "172.16.1.7"},
    {"hostname": "test8", "ip": "172.16.1.8"},
    {"hostname": "test9", "ip": "172.16.1.9"},
    {"hostname": "test10", "ip": "172.16.1.10"},
    {"hostname": "test11", "ip": "172.16.1.11"}
    ]

}
api = UptimeKumaApi('http://1.1.1.1:3001/')
api.login('admin', 'mima')



for key in zidian["ipadd"]:
    result = api.add_monitor(type=MonitorType.PING, name=key["hostname"], hostname=key["ip"])
    print(result)

api.disconnect()
