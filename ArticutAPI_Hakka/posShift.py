#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

shiftRule =[(re.compile("((?<=</ENTITY_num>)|(?<=</QUANTIFIER>))<ENTITY_noun>身</ENTITY_noun>"),("ENTITY_noun",),("ENTITY_classifier",)),
            (re.compile("<FUNC_inter>無</FUNC_inter>((?=<ACTION_verb>)|(?=<MODIFIER>))"),("FUNC_inter",),("FUNC_negation",)),
            (re.compile("(?<=[^<愛]</ACTION_verb>)<ACTION_verb>[好等]</ACTION_verb>"), ("ACTION_verb",), ("ASPECT",)),
            (re.compile("<ACTION_verb>[當蓋]</ACTION_verb><MODIFIER>[^<]+</MODIFIER>"),("<ACTION_verb>", "</ACTION_verb><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),
            (re.compile("<MODIFIER>緊</MODIFIER>(?=<ACTION_verb>)"),("MODIFIER",),("TIME_justtime",)),
            (re.compile("<FUNC_inter>無</FUNC_inter>$"),("FUNC_inter",),("CLAUSE_Q",)),
            (re.compile("<FUNC_degreeHead>恁</FUNC_degreeHead><MODIFIER>[^<]+</MODIFIER>"),("<FUNC_degreeHead>", "</FUNC_degreeHead><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),
            (re.compile("</MODIFIER_color><MODIFIER_color>"), ("</MODIFIER_color><MODIFIER_color>",), ("",)),
            (re.compile("<FUNC_inner>還</FUNC_inner><MODIFIER>[^<]+</MODIFIER>"),("<FUNC_inner>", "</FUNC_inner><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),
            (re.compile("(?<=</ENTITY_num>)<ENTITY_noun>個人</ENTITY_noun>"),("<ENTITY_noun>個人</ENTITY_noun>",), ("<ENTITY_classifier>個</ENTITY_classifier><ENTITY_noun>人</ENTITY_noun>",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>[^<]+</ENTITY_classifier>"), ("</ENTITY_num><ENTITY_classifier>", "ENTITY_num"), ("", "ENTITY_classifier")),
            (re.compile("<ACTION_verb>([^<])</ACTION_verb><ACTION_verb>\\1</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>講</ACTION_verb><ACTION_verb>話</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<MODIFIER>大</MODIFIER><ACTION_verb>聲</ACTION_verb>"),("<MODIFIER>大</MODIFIER><ACTION_verb>聲</ACTION_verb>",), ("<MODIFIER>大聲</MODIFIER>",)),
            (re.compile("(?<=</FUNC_degreeHead>)<ACTION_verb>好</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<FUNC_degreeHead>[^<]+</FUNC_degreeHead><MODIFIER>[^<]+</MODIFIER>"),("</FUNC_degreeHead><MODIFIER>", "<FUNC_degreeHead>", "</MODIFIER>"), ("", "<DegreeP>", "</DegreeP>")),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>起來</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>[著到]</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ASPECT>忒</ASPECT><MODIFIER>[^<]+</MODIFIER>"),("</ASPECT><MODIFIER>", "ASPECT", "MODIFIER"), ("", "DegreeP", "DegreeP")),
            (re.compile("<ACTION_verb>斷</ACTION_verb><ASPECT>[忒核]</ASPECT>"),("</ACTION_verb><ASPECT>", "ASPECT",), ("", "ACTION_verb")),
            (re.compile("(?<=</ENTITY_num>)<ENTITY_noun>個人</ENTITY_noun>"),("<ENTITY_noun>個人</ENTITY_noun>",), ("<ENTITY_classifier>個</ENTITY_classifier><ENTITY_noun>人</ENTITY_noun>",)),
            (re.compile("(?<=</FUNC_degreeHead>)<ACTION_verb>好</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
]