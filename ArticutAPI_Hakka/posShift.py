#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

shiftRule =[(re.compile("((?<=</ENTITY_num>)|(?<=</QUANTIFIER>))<ENTITY_noun>身</ENTITY_noun>"),("ENTITY_noun",),("ENTITY_classifier",)),
            (re.compile("<FUNC_inter>無</FUNC_inter>(?=<ACTION_verb>)"),("FUNC_inter",),("FUNC_negation",)),
            (re.compile("(?<=[^<愛]</ACTION_verb>)<ACTION_verb>[好等]</ACTION_verb>"), ("ACTION_verb",), ("ASPECT",)),
            (re.compile("<ACTION_verb>[當蓋]</ACTION_verb><MODIFIER>[^<]+</MODIFIER>"),("<ACTION_verb>", "</ACTION_verb><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),
            (re.compile("<ACTION_verb>感覺</ACTION_verb><ACTION_verb>著</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",),("",)),
            (re.compile("<MODIFIER>緊</MODIFIER>(?=<ACTION_verb>)"),("MODIFIER",),("TIME_justtime",)),
            (re.compile("<FUNC_inter>無</FUNC_inter>$"),("FUNC_inter",),("CLAUSE_Q",)),
            (re.compile("<FUNC_degreeHead>恁</FUNC_degreeHead><MODIFIER>[^<]+</MODIFIER>"),("<FUNC_degreeHead>", "</FUNC_degreeHead><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),
            (re.compile("</MODIFIER_color><MODIFIER_color>"), ("</MODIFIER_color><MODIFIER_color>",), ("",)),
            (re.compile("<FUNC_inner>還</FUNC_inner><MODIFIER>[^<]+</MODIFIER>"),("<FUNC_inner>", "</FUNC_inner><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>[^<]+</ENTITY_classifier>"), ("</ENTITY_num><ENTITY_classifier>", "ENTITY_num"), ("", "ENTITY_classifier")),
            (re.compile("<ACTION_verb>([^<])</ACTION_verb><ACTION_verb>\\1</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>講</ACTION_verb><ACTION_verb>話</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
]