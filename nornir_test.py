#!/usr/bin/env python

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko import netmiko_send_command

nr = InitNornir(config_file="nornir.yaml")
results = nr.run(task=netmiko_send_command, command_string='dis ver')
print_result(results)
