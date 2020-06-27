#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from libnmap.parser import NmapParser, NmapParserException

external_entities_payload = """
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
]>
<lolz><hello>&lol3;</hello></lolz>
"""

baddatalist = [
    "<host>aaa",
    None,
    "",
    123,
    "ports/>>>",
    "<port<>",
    "<port/>",
    "<ports/aaaa>",
    external_entities_payload,
]


class TestNmapParser(unittest.TestCase):
    def test_parse(self):
        for baddata in baddatalist:
            self.assertRaises(NmapParserException, NmapParser.parse, baddata, "zz")
            self.assertRaises(NmapParserException, NmapParser.parse, baddata, "XML")
            self.assertRaises(NmapParserException, NmapParser.parse, baddata, "YAML")


if __name__ == "__main__":
    test_suite = ["test_parse"]

    suite = unittest.TestSuite(map(TestNmapParser, test_suite))
    test_result = unittest.TextTestRunner(verbosity=2).run(suite)
