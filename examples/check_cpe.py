#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libnmap.parser import NmapParser

rep = NmapParser.parse_fromfile("libnmap/test/files/full_sudo6.xml")

print(f"Nmap scan discovered {rep.hosts_up}/{rep.hosts_total} hosts up")
for _host in rep.hosts:
    if _host.is_up():
        print(f"+ Host: {_host.address} {' '.join(_host.hostnames)}")

        # get CPE from service if available
        for s in _host.services:
            print(f"    Service: {s.port}/{s.protocol} ({s.state})")
            # NmapService.cpelist returns an array of CPE objects
            for _serv_cpe in s.cpelist:
                print(f"        CPE: {_serv_cpe.cpestring}")

        if _host.os_fingerprinted:
            print("  OS Fingerprints")
            for osm in _host.os.osmatches:
                print(f"    Found Match:{osm.name} ({osm.accuracy}%)")
                # NmapOSMatch.get_cpe() method return an array of string
                # unlike NmapOSClass.cpelist which returns an array of CPE obj
                for cpe in osm.get_cpe():
                    print(f"\t    CPE: {cpe}")
