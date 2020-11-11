#!/bin/bash
# Author: yousong.xiang
# Date:  2020.11.9
# Version: v1.0.1
# 批量安装zabbix-agent
Hostname=$1
ZABBIX_SERVER=192.168.0.42
ZABBIX_PORT=10050

function check_rpm() {
    rpm_name=$1
    num=`rpm -qa|grep ${rpm_name}|wc -l`
    echo ${num}
}

if [ `check_rpm zabbix-agent` == 1 ]; then
    yum upgrade /tmp/zabbix-ansible/packages/zabbix-agent-5.0.5-1.el7.x86_64.rpm -y
else
    yum localinstall /tmp/zabbix-ansible/packages/zabbix-agent-5.0.5-1.el7.x86_64.rpm -y
fi
cat>/etc/zabbix/zabbix_agentd.conf<<EOF
PidFile=/var/run/zabbix/zabbix_agentd.pid
LogFile=/var/log/zabbix/zabbix_agentd.log
LogFileSize=30
HostMetadataItem=system.uname
Server=$ZABBIX_SERVER
ServerActive=$ZABBIX_SERVER
Include=/etc/zabbix/zabbix_agentd.d/*.conf
Hostname=$Hostname
EOF

if [ -d /tmp/zabbix-ansible/monitor_sh ]; then
    mv -f /tmp/zabbix-ansible/monitor_sh /etc/zabbix
fi

if [ -d /tmp/zabbix-ansible/monitor_bat ]; then
    mv -f /tmp/zabbix-ansible/monitor_bat /etc/zabbix
fi

if [ -d /tmp/zabbix_agentd.d ]; then
    mv -f /tmp/zabbix-ansible/zabbix_agentd.d/* /etc/zabbix/zabbix_agentd.d/
fi

if [ -d /tmp/zabbix-ansible/md_service_maintenance ]; then
    mv -f /tmp/zabbix-ansible/md_service_maintenance /etc/zabbix/monitor_sh
fi

systemctl restart zabbix-agent.service
systemctl enable zabbix-agent.service

firewall-cmd --list-all
if [ $? -eq 0 ]; then
  firewall-cmd --zone=public --add-port=${ZABBIX_PORT}/tcp --permanent
  firewall-cmd --reload
fi

