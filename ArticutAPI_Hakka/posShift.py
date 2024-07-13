#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

shiftRule =[
    (re.compile(r"<MODIFIER>([^<])</MODIFIER><MODIFIER>(\1)</MODIFIER><MODIFIER>\2</MODIFIER>"), ("</MODIFIER><MODIFIER>",), ("",),),
    (re.compile("<ENTITY_classifier>時</ENTITY_classifier><ACTION_eventQuantifier>節</ACTION_eventQuantifier>"),("<ENTITY_classifier>時</ENTITY_classifier><ACTION_eventQuantifier>節</ACTION_eventQuantifier>",),("<TIME_justtime>時節</TIME_justtime>",)),
    (re.compile("<ACTION_verb>歸</ACTION_verb><ENTITY_oov>身汗</ENTITY_oov>"),("<ACTION_verb>歸</ACTION_verb><ENTITY_oov>身汗</ENTITY_oov>",),("<MODIFIER>歸身</MODIFIER><ENTITY_noun>汗</ENTITY_noun>",)),
    (re.compile("<ACTION_verb>附</ACTION_verb><MODIFIER>近</MODIFIER>"),("<ACTION_verb>附</ACTION_verb><MODIFIER>近</MODIFIER>",),("<RANGE_locality>附近</RANGE_locality>",)),
    (re.compile("<ENTITY_classifier>時</ENTITY_classifier><ENTITY_oov>間</ENTITY_oov>"),("<ENTITY_classifier>時</ENTITY_classifier><ENTITY_oov>間</ENTITY_oov>",),("<TIME_justtime>時間</TIME_justtime>",)),
    (re.compile("<MODIFIER>同</MODIFIER>((?=<ENTITY_noun>)|(?=<ENTITY_pronoun>))"), ("MODIFIER",), ("ACTION_lightVerb",)),
    (re.compile("(?<=</ACTION_verb>)<ACTION_verb>[好等]</ACTION_verb>"), ("ACTION_verb",), ("ASPECT",)),
    (re.compile("<ACTION_verb>試</ACTION_verb><ACTION_verb>著</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",),("",)),
    (re.compile("<ACTION_verb>感覺</ACTION_verb><ACTION_verb>著</ACTION_verb>"),("</ACTION_verb><ACTION_verb>",),("",)),
    (re.compile("<ACTION_verb>請</ACTION_verb><MODIFIER>假</MODIFIER>"),("<ACTION_verb>請</ACTION_verb><MODIFIER>假</MODIFIER>",), ("<ACTION_verb>請假</ACTION_verb>",)),
    (re.compile("<MODIFIER>當</MODIFIER><MODIFIER>[^<]+</MODIFIER>"),("</MODIFIER><MODIFIER>","MODIFIER"), ("", "DegreeP")),
    (re.compile("<MODIFIER>蓋</MODIFIER><MODIFIER>[^<]+</MODIFIER>"),("</MODIFIER><MODIFIER>","MODIFIER"), ("", "DegreeP")),
    (re.compile("<ACTION_verb>緊尋</ACTION_verb>"),("<ACTION_verb>緊尋</ACTION_verb>",), ("<TIME_justtime>緊</TIME_justtime><ACTION_verb>尋</ACTION_verb>",)),
    (re.compile("<ENTITY_num>一</ENTITY_num><ENTITY_classifier>下</ENTITY_classifier><ENTITY_oov>仔</ENTITY_oov>"),("<ENTITY_num>一</ENTITY_num><ENTITY_classifier>下</ENTITY_classifier><ENTITY_oov>仔</ENTITY_oov>",),("<TIME_justtime>一下仔</TIME_justtime>",)),
    (re.compile("<FUNC_negation>無</FUNC_negation>$"),("FUNC_negation",),("CLAUSE_Q",)),
    (re.compile("<MODIFIER>恁</MODIFIER><MODIFIER>[^<]+</MODIFIER>"),("</MODIFIER><MODIFIER>","MODIFIER"), ("", "DegreeP")),
    (re.compile("<ENTITY_classifier>日</ENTITY_classifier><ENTITY_oov>仔</ENTITY_oov>"),("<ENTITY_classifier>日</ENTITY_classifier><ENTITY_oov>仔</ENTITY_oov>",),("<ENTITY_noun>日仔</ENTITY_noun>",)),
    (re.compile("</MODIFIER_color><MODIFIER_color>"), ("</MODIFIER_color><MODIFIER_color>",), ("",)),
    (re.compile("<ENTITY_noun>花</ENTITY_noun><ENTITY_noun>花</ENTITY_noun>"),("<ENTITY_noun>花</ENTITY_noun><ENTITY_noun>花</ENTITY_noun>",),("<MODIFIER>花花</MODIFIER>",)),
    (re.compile("<ACTION_verb>緊跌</ACTION_verb>"),("<ACTION_verb>緊跌</ACTION_verb>",), ("<TIME_justtime>緊</TIME_justtime><ACTION_verb>跌</ACTION_verb>",)),
    (re.compile("<ACTION_quantifiedVerb>塞塞</ACTION_quantifiedVerb>"),("<ACTION_quantifiedVerb>塞塞</ACTION_quantifiedVerb>",), ("<MODIFIER>塞塞</MODIFIER>",)),
    (re.compile("<ENTITY_oov>靚</ENTITY_oov>"),("ENTITY_oov",),("MODIFIER",)),
    (re.compile("<MODIFIER>還</MODIFIER><MODIFIER>[^<]+</MODIFIER>"),("</MODIFIER><MODIFIER>","MODIFIER"), ("", "DegreeP")),
    (re.compile("<ACTION_quantifiedVerb>聾聾</ACTION_quantifiedVerb>"),("ACTION_quantifiedVerb",),("MODIFIER",)),
    (re.compile("<MODIFIER>大</MODIFIER><ENTITY_noun>聲</ENTITY_noun>"),("<MODIFIER>大</MODIFIER><ENTITY_noun>聲</ENTITY_noun>",),("<MODIFIER>大聲</MODIFIER>",)),
    (re.compile("<FUNC_degreeHead>較</FUNC_degreeHead><MODIFIER>大聲</MODIFIER>"),("<FUNC_degreeHead>較</FUNC_degreeHead><MODIFIER>大聲</MODIFIER>",),("<DegreeP>較大聲</DegreeP>",)),
    (re.compile("<FUNC_degreeHead>過</FUNC_degreeHead><MODIFIER>大聲</MODIFIER>"),("<FUNC_degreeHead>過</FUNC_degreeHead><MODIFIER>大聲</MODIFIER>",),("<DegreeP>過大聲</DegreeP>",)),
    (re.compile("<ACTION_verb>講</ACTION_verb><ENTITY_oov>話</ENTITY_oov>"),("</ACTION_verb><ENTITY_oov>","</ENTITY_oov>"),("","</ACTION_verb>",)),
    (re.compile("<QUANTIFIER>兜</QUANTIFIER><ENTITY_oov>仔</ENTITY_oov>"),("</QUANTIFIER><ENTITY_oov>","</ENTITY_oov>"),("","</QUANTIFIER>",)),
    (re.compile("<ENTITY_oov>䟘</ENTITY_oov><ACTION_verb>起來</ACTION_verb>"),("<ENTITY_oov>䟘</ENTITY_oov><ACTION_verb>起來</ACTION_verb>",),("<ACTION_verb>䟘起來</ACTION_verb>",)),
    (re.compile("<MODIFIER>([^<])</MODIFIER><MODIFIER>\\1</MODIFIER>"), ("</MODIFIER><MODIFIER>",), ("",)),
]