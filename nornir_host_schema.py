#!/usr/bin/env python

from nornir.core.inventory import Host
import json
print(json.dumps(Host.schema(), indent=4))
