#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  cookie-quick-manager-to-netscape.py
#
#  Copyright 2021 Edward Wang <edward.c.wang@compdigitec.com>

import json
import sys
from typing import List
from urllib.parse import urlparse

def to_cookie_bool(boolvar: bool) -> str:
    return "TRUE" if boolvar else "FALSE"

def cookie_quick_manager_to_netscape(filename: str) -> str:
    """
    Parse a JSON export from Cookie Quick Manager (Firefox extension) into
    Netscape format.

    :return: Output
    """
    output = "# Netscape HTTP Cookie File\n"

    with open(filename, 'r') as f:
        jsonobject: List = json.load(f)
        for cookie in jsonobject:
            # Host raw looks like "https://.docs.google.com/spreadsheets/d/XYZ"
            domain = urlparse(cookie['Host raw']).netloc
            has_leading_dot = to_cookie_bool(domain.startswith('.'))
            path = cookie['Path raw']
            secure = to_cookie_bool('https' in cookie['Host raw'])
            expiration = cookie['Expires raw']
            name = cookie['Name raw']
            value = cookie['Content raw']
            output += f"{domain}\t{has_leading_dot}\t{path}\t{secure}\t{expiration}\t{name}\t{value}\n"

    return output

def main(args: List[str]) -> int:
    if len(args) < 2:
        print(f"Usage: {args[0]} cookies.json", file=sys.stderr)
        print("  cookies.json: JSON export from Cookie Quick Manager", file=sys.stderr)
        print("  Prints output to stdout", file=sys.stderr)
        return 1

    filename = args[1]
    output = cookie_quick_manager_to_netscape(filename)
    print(output)

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
