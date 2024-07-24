#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

shiftRule =[(re.compile("((?<=</ENTITY_num>)|(?<=</QUANTIFIER>))<ENTITY_noun>身</ENTITY_noun>"),("ENTITY_noun",),("ENTITY_classifier",)),
            (re.compile("<FUNC_inter>無</FUNC_inter>((?=<ACTION_verb>)|(?=<MODIFIER>))"),("FUNC_inter",),("FUNC_negation",)),
            (re.compile("(?<=[^<愛知做得]</ACTION_verb>)<ACTION_verb>[好等]</ACTION_verb>"), ("ACTION_verb",), ("ASPECT",)),
            (re.compile("<MODIFIER>緊</MODIFIER>(?=<ACTION_verb>)"),("MODIFIER",),("TIME_justtime",)),
            (re.compile("<FUNC_inter>無</FUNC_inter>$"),("FUNC_inter",),("CLAUSE_Q",)),
            (re.compile("<MODIFIER>大</MODIFIER><ACTION_verb>聲</ACTION_verb>"),("<MODIFIER>大</MODIFIER><ACTION_verb>聲</ACTION_verb>",), ("<MODIFIER>大聲</MODIFIER>",)),
            (re.compile("<FUNC_degreeHead>[恁當蓋]</FUNC_degreeHead><MODIFIER>[^<]+</MODIFIER>"),("<FUNC_degreeHead>", "</FUNC_degreeHead><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),
            (re.compile("</MODIFIER_color><MODIFIER_color>"), ("</MODIFIER_color><MODIFIER_color>",), ("",)),
            (re.compile("<FUNC_inner>還</FUNC_inner><MODIFIER>[^<]+</MODIFIER>"),("<FUNC_inner>", "</FUNC_inner><MODIFIER>", "</MODIFIER>"), ("<DegreeP>", "", "</DegreeP>")),
            (re.compile("(?<=</ENTITY_num>)<ENTITY_noun>個人</ENTITY_noun>"),("<ENTITY_noun>個人</ENTITY_noun>",), ("<ENTITY_classifier>個</ENTITY_classifier><ENTITY_noun>人</ENTITY_noun>",)),
            (re.compile("<ENTITY_num>[^<]+</ENTITY_num><ENTITY_classifier>[^<]+</ENTITY_classifier>"), ("</ENTITY_num><ENTITY_classifier>", "ENTITY_num"), ("", "ENTITY_classifier")),
            (re.compile("<ACTION_verb>([^<])</ACTION_verb><ACTION_verb>\\1</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>講</ACTION_verb><ACTION_verb>話</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("(?<=</FUNC_degreeHead>)<ACTION_verb>好</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<FUNC_degreeHead>[當蓋]</FUNC_degreeHead><ACTION_verb>[^<]+</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<FUNC_degreeHead>[^<]+</FUNC_degreeHead><MODIFIER>[^<]+</MODIFIER>"),("</FUNC_degreeHead><MODIFIER>", "<FUNC_degreeHead>", "</MODIFIER>"), ("", "<DegreeP>", "</DegreeP>")),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>起來</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>[著到]</ACTION_verb>"), ("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ASPECT>忒</ASPECT><MODIFIER>[^<]+</MODIFIER>"),("</ASPECT><MODIFIER>", "ASPECT", "MODIFIER"), ("", "DegreeP", "DegreeP")),
            (re.compile("<ACTION_verb>斷</ACTION_verb><ASPECT>[忒核]</ASPECT>"),("</ACTION_verb><ASPECT>", "ASPECT",), ("", "ACTION_verb")),
            (re.compile("(?<=</ENTITY_num>)<ENTITY_noun>個人</ENTITY_noun>"),("<ENTITY_noun>個人</ENTITY_noun>",), ("<ENTITY_classifier>個</ENTITY_classifier><ENTITY_noun>人</ENTITY_noun>",)),
            (re.compile("(?<=</FUNC_degreeHead>)<ACTION_verb>好</ACTION_verb>"), ("ACTION_verb",), ("MODIFIER",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><MODIFIER>飽</MODIFIER>"),("</ACTION_verb><MODIFIER>","MODIFIER"), ("","ACTION_verb")),
            (re.compile("(?<=</ACTION_verb>)<TIME_day>夜</TIME_day>"),("TIME_day",), ("ENTITY_noun",)),
            (re.compile("<ASPECT>好</ASPECT>(?=<CLAUSE_Q>)"),("ASPECT",), ("ACTION_verb",)),
            (re.compile("<ACTION_verb>[上下]</ACTION_verb><ENTITY_noun>禮拜</ENTITY_noun>"),("</ACTION_verb><ENTITY_noun>","ACTION_verb","ENTITY_noun"), ("","TIME_justtime","TIME_justtime")),
            (re.compile("(<ACTION_verb>好</ACTION_verb>)<QUANTIFIER>歸</QUANTIFIER>"),("QUANTIFIER",), ("ACTION_verb",)),
            (re.compile("(?<=</ENTITY_classifier>)<ACTION_verb>妄想</ACTION_verb>"),("ACTION_verb",), ("ENTITY_noun",)),
            (re.compile("<FUNC_degreeHead>[恁盡過]</FUNC_degreeHead>(?=<ACTION_verb>)"),("FUNC_degreeHead",), ("MODIFIER",)),
            (re.compile("<ACTION_verb>打</ACTION_verb><ACTION_verb>結</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<DegreeP>盡好</DegreeP><ACTION_verb>食</ACTION_verb>"),("DegreeP",), ("ACTION_verb",)),
            (re.compile("(?<=擺</ENTITY_classifier>)<ACTION_verb>旅行</ACTION_verb>"),("ACTION_verb",), ("ENTITY_noun",)),
            (re.compile("<ACTION_verb>包</ACTION_verb>(?=<ENTITY_noun>)"),("ACTION_verb",), ("ENTITY_classifier",)),
            (re.compile("<FUNC_determiner>[^<]+</FUNC_determiner><ENTITY_classifier>[^<]+</ENTITY_classifier>"),("</FUNC_determiner><ENTITY_classifier>","FUNC_determiner","ENTITY_classifier"), ("","ENTITY_DetPhrase","ENTITY_DetPhrase")),
            (re.compile("<ENTITY_pronoun>[^<]+</ENTITY_pronoun>(?=<ENTITY_pronoun>)"),("ENTITY_pronoun",), ("ENTITY_possessive",)),
            (re.compile("<FUNC_inter>無</FUNC_inter><ENTITY_noun>人</ENTITY_noun>"),("FUNC_inter",), ("FUNC_negation",)),
            (re.compile("<ACTION_verb>[^<]+</ACTION_verb><ACTION_verb>[出來下來入]+</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<ENTITY_person>錢放</ENTITY_person>"),("<ENTITY_person>錢放</ENTITY_person>",), ("<ENTITY_noun>錢</ENTITY_noun><ACTION_verb>放</ACTION_verb>",)),
            (re.compile("<ENTITY_noun>[^<]+</ENTITY_noun><ENTITY_classifier>頂</ENTITY_classifier>"),("ENTITY_classifier",), ("RANGE_locality",)),
            (re.compile("<MODIFIER>毋好</MODIFIER>(?=<ACTION_verb>)"),("MODIFIER",), ("FUNC_negation",)),
            (re.compile("<ACTION_verb>晒</ACTION_verb><ENTITY_noun>日頭</ENTITY_noun>"),("</ACTION_verb><ENTITY_noun>","</ENTITY_noun>"), ("","</ACTION_verb>")),
            (re.compile("<ACTION_verb>打開</ACTION_verb><ACTION_verb>來</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",), ("",)),
            (re.compile("<MODIFIER>([^<])</MODIFIER><MODIFIER>\\1</MODIFIER>"), ("</MODIFIER><MODIFIER>",), ("",)),
            (re.compile("<ACTION_verb>關</ACTION_verb><ASPECT>好</ASPECT>"), ("ASPECT",), ("MODIFIER",)),
]