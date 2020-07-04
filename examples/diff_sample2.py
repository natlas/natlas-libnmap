#!/usr/bin/env python
# -*- coding: utf-8 -*-

from libnmap.parser import NmapParser


def nested_obj(objname):
    splitted = objname.split("::")
    return splitted if len(splitted) == 2 else None


def print_diff_added(obj1, obj2, added):
    for akey in added:
        nested = nested_obj(akey)
        subobj1 = None
        if nested is not None:
            if nested[0] == "NmapHost":
                subobj1 = obj1.get_host_byid(nested[1])
            elif nested[0] == "NmapService":
                subobj1 = obj1.get_service_byid(nested[1])
            if subobj1:
                print(f"+ {subobj1}")
        else:
            print(f"+ {obj1} {akey}: {getattr(obj1, akey)}")


def print_diff_removed(obj1, obj2, removed):
    for rkey in removed:
        nested = nested_obj(rkey)
        subobj2 = None
        if nested is not None:
            if nested[0] == "NmapHost":
                subobj2 = obj2.get_host_byid(nested[1])
            elif nested[0] == "NmapService":
                subobj2 = obj2.get_service_byid(nested[1])
            if subobj2:
                print(f"- {subobj2}")
        else:
            print(f"- {obj2} {rkey}: {getattr(obj2, rkey)}")


def print_diff_changed(obj1, obj2, changes):
    for mkey in changes:
        nested = nested_obj(mkey)
        subobj1 = None
        subobj2 = None
        if nested is not None:
            if nested[0] == "NmapHost":
                subobj1 = obj1.get_host_byid(nested[1])
                subobj2 = obj2.get_host_byid(nested[1])
            elif nested[0] == "NmapService":
                subobj1 = obj1.get_service_byid(nested[1])
                subobj2 = obj2.get_service_byid(nested[1])
            if subobj1 and subobj2:
                print_diff(subobj1, subobj2)
        else:
            print(f"~ {obj1} {mkey}: {getattr(obj2, mkey)} => {getattr(obj1, mkey)}")


def print_diff(obj1, obj2):
    ndiff = obj1.diff(obj2)

    print_diff_changed(obj1, obj2, ndiff.changed())
    print_diff_added(obj1, obj2, ndiff.added())
    print_diff_removed(obj1, obj2, ndiff.removed())


def main():
    newrep = NmapParser.parse_fromfile("libnmap/test/files/2_hosts_achange.xml")
    oldrep = NmapParser.parse_fromfile("libnmap/test/files/1_hosts.xml")

    print_diff(newrep, oldrep)


if __name__ == "__main__":
    main()
