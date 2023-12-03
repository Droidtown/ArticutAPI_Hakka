#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

shiftRule =[
    (re.compile(r"<MODIFIER>([^<])</MODIFIER><MODIFIER>(\1)</MODIFIER><MODIFIER>\2</MODIFIER>"), ("</MODIFIER><MODIFIER>",), ("",),)
]