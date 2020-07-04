#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libnmap.parser import NmapParser

rep = NmapParser.parse_fromfile("libnmap/test/files/os_scan6.xml")

print(f"{rep.hosts_up}/{rep.hosts_total} hosts up")
for _host in rep.hosts:
    if _host.is_up():
        print(f"{_host.address} {' '.join(_host.hostnames)}")
        if _host.os_fingerprinted:
            print("OS Fingerprint:")
            msg = ""
            for osm in _host.os.osmatches:
                print(f"Found Match:{osm.name} ({osm.accuracy}%)")
                for osc in osm.osclasses:
                    print(f"\tOS Class: {osc.description}")
                    for cpe in osc.cpelist:
                        print(f"\tCPE: {cpe.cpestring}")
        else:
            print("No fingerprint available")
