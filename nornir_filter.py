#!/usr/bin/env python

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="nornir.yaml")
at_sbb = nr.filter(idc='AT')
print(nr.inventory.hosts)
print(at_sbb.inventory.hosts)
